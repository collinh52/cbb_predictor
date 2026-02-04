"""
FastAPI backend for UKF Basketball Predictor.
"""
from fastapi import FastAPI, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
from jinja2 import Template
from typing import List, Dict, Optional
from datetime import datetime
from pydantic import BaseModel
import os
import json

from src.predictor import get_predictor, get_hybrid_predictor
from src.data_collector import get_collector
from src.database import get_database
from src.espn_collector import get_espn_collector
from src.feature_calculator import FeatureCalculator

app = FastAPI(title="UKF Basketball Predictor")

# In-memory cache for rankings (cleared on server restart)
_rankings_cache = {
    'data': None,
    'timestamp': None,
    'ttl_seconds': 300  # 5 minutes
}


# Pydantic models for request/response
class CustomPredictionRequest(BaseModel):
    home_team_id: int
    away_team_id: int
    neutral_court: bool = False


# Mount static files
static_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "static")
templates_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "templates")

if os.path.exists(static_path):
    app.mount("/static", StaticFiles(directory=static_path), name="static")


@app.get("/", response_class=HTMLResponse)
async def root():
    """Serve main dashboard."""
    index_path = os.path.join(templates_path, "index.html")
    if os.path.exists(index_path):
        with open(index_path, 'r') as f:
            return HTMLResponse(f.read())
    else:
        return HTMLResponse("""
        <!DOCTYPE html>
        <html>
        <head>
            <title>UKF Basketball Predictor</title>
            <meta http-equiv="refresh" content="0; url=/static/index.html">
        </head>
        <body>
            <p>Redirecting to <a href="/static/index.html">dashboard</a>...</p>
        </body>
        </html>
        """)


@app.get("/api/games/today")
async def get_todays_games(force_refresh: bool = False):
    """
    Get today's games with hybrid predictions.

    Args:
        force_refresh: If True, regenerate predictions even if cached. Default False.
    """
    try:
        collector = get_collector()
        hybrid_predictor = get_hybrid_predictor()
        database = get_database()

        games = collector.get_todays_games()

        # Format response
        results = []
        predictions_generated = 0
        predictions_from_cache = 0

        for game in games:
            game_id = game.get('GameID')
            game_date_str = game.get('DateTime', '')

            try:
                game_date = datetime.fromisoformat(game_date_str.replace('Z', '+00:00')) if game_date_str else datetime.now()
            except:
                game_date = datetime.now()

            # Try to get prediction from database first (much faster)
            cached_pred = None
            if game_id and not force_refresh:
                cached_pred = database.get_prediction_by_game_id(game_id)

            # Use cached prediction if available and recent (within 24 hours)
            if cached_pred and not force_refresh:
                pred_date = cached_pred.get('game_date')
                if isinstance(pred_date, datetime):
                    age_hours = (datetime.now() - pred_date).total_seconds() / 3600
                    if age_hours < 24:
                        predictions_from_cache += 1
                        # Build prediction dict from cached data
                        home_covers_prob = cached_pred.get('home_covers_probability')
                        over_prob = cached_pred.get('over_probability')

                        pred = {
                            'home_team_id': cached_pred.get('home_team_id') or game.get('HomeTeamID'),
                            'away_team_id': cached_pred.get('away_team_id') or game.get('AwayTeamID'),
                            'spread': cached_pred.get('pregame_spread'),
                            'total_line': cached_pred.get('pregame_total'),
                            'ukf_predicted_margin': cached_pred.get('ukf_predicted_margin'),
                            'ukf_predicted_total': cached_pred.get('ukf_predicted_total'),
                            'ml_predicted_margin': cached_pred.get('ml_predicted_margin'),
                            'ml_predicted_total': cached_pred.get('ml_predicted_total'),
                            'hybrid_predicted_margin': cached_pred.get('hybrid_predicted_margin'),
                            'hybrid_predicted_total': cached_pred.get('hybrid_predicted_total'),
                            'predicted_winner': 'home' if (cached_pred.get('hybrid_predicted_margin') or 0) > 0 else 'away',
                            'prediction_source': cached_pred.get('prediction_source', 'hybrid'),
                            'home_covers_probability': home_covers_prob,
                            'away_covers_probability': 1.0 - home_covers_prob if home_covers_prob is not None else None,
                            'over_probability': over_prob,
                            'under_probability': 1.0 - over_prob if over_prob is not None else None,
                            'home_covers_confidence': abs((home_covers_prob or 0.5) - 0.5) * 200 if home_covers_prob is not None else None,
                            'over_confidence': abs((over_prob or 0.5) - 0.5) * 200 if over_prob is not None else None,
                            'overall_confidence': cached_pred.get('prediction_confidence', 50.0)
                        }
                    else:
                        # Prediction is stale, regenerate
                        cached_pred = None

            # Generate new prediction if not cached or stale
            if not cached_pred or force_refresh:
                predictions_generated += 1
                pred = hybrid_predictor.predict_game(game)

                # Save prediction to database for future requests
                home_team_id = pred.get('home_team_id')
                away_team_id = pred.get('away_team_id')
                if game_id and home_team_id and away_team_id:
                    hybrid_predictor.save_prediction_to_database(
                        game_id, game_date, home_team_id, away_team_id, pred
                    )

            results.append({
                'game_id': game_id,
                'date': game_date_str,
                'home_team': game.get('HomeTeam'),
                'away_team': game.get('AwayTeam'),
                'home_team_id': pred.get('home_team_id'),
                'away_team_id': pred.get('away_team_id'),
                'spread': pred.get('spread'),
                'total_line': pred.get('total_line'),
                'prediction': {
                    'predicted_margin': pred.get('hybrid_predicted_margin'),
                    'predicted_total': pred.get('hybrid_predicted_total'),
                    'ukf_predicted_margin': pred.get('ukf_predicted_margin'),
                    'ukf_predicted_total': pred.get('ukf_predicted_total'),
                    'ml_predicted_margin': pred.get('ml_predicted_margin'),
                    'ml_predicted_total': pred.get('ml_predicted_total'),
                    'predicted_winner': pred.get('predicted_winner'),
                    'prediction_source': pred.get('prediction_source'),
                    'home_covers_probability': pred.get('home_covers_probability'),
                    'away_covers_probability': pred.get('away_covers_probability'),
                    'over_probability': pred.get('over_probability'),
                    'under_probability': pred.get('under_probability'),
                    'home_covers_confidence': pred.get('home_covers_confidence'),
                    'over_confidence': pred.get('over_confidence'),
                    'overall_confidence': pred.get('overall_confidence')
                }
            })

        print(f"Performance: {predictions_from_cache} cached, {predictions_generated} generated")
        return {'games': results, 'count': len(results)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/games/upcoming")
async def get_upcoming_games(days: int = 7):
    """Get upcoming games."""
    try:
        collector = get_collector()
        games = collector.get_upcoming_games(days_ahead=days)
        
        results = []
        for game in games:
            results.append({
                'game_id': game.get('GameID'),
                'date': game.get('DateTime'),
                'home_team': game.get('HomeTeam'),
                'away_team': game.get('AwayTeam'),
                'spread': game.get('PointSpread'),
                'total_line': game.get('OverUnder'),
                'status': game.get('Status')
            })
        
        return {'games': results, 'count': len(results)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/predictions/{game_id}")
async def get_prediction(game_id: int):
    """Get detailed hybrid predictions for a specific game."""
    try:
        collector = get_collector()
        hybrid_predictor = get_hybrid_predictor()
        
        game = collector.get_game_details(game_id)
        if not game:
            raise HTTPException(status_code=404, detail="Game not found")
        
        prediction = hybrid_predictor.predict_game(game)
        
        # Save to database
        game_date_str = game.get('DateTime', '')
        try:
            game_date = datetime.fromisoformat(game_date_str.replace('Z', '+00:00')) if game_date_str else datetime.now()
        except:
            game_date = datetime.now()
        
        home_team_id = prediction.get('home_team_id')
        away_team_id = prediction.get('away_team_id')
        if home_team_id and away_team_id:
            hybrid_predictor.save_prediction_to_database(
                game_id, game_date, home_team_id, away_team_id, prediction
            )
        
        return {
            'game_id': game_id,
            'game': {
                'home_team': game.get('HomeTeam'),
                'away_team': game.get('AwayTeam'),
                'date': game.get('DateTime'),
                'spread': game.get('PointSpread'),
                'total_line': game.get('OverUnder')
            },
            'prediction': prediction
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/teams/ratings")
async def get_team_ratings():
    """Get current team ratings."""
    try:
        predictor = get_predictor()
        ratings = predictor.get_team_ratings()

        return {'ratings': ratings, 'count': len(ratings)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/teams/rankings")
async def get_team_rankings(force_refresh: bool = False):
    """Get comprehensive team rankings with all stats (similar to KenPom homepage)."""
    try:
        # Check cache first
        if not force_refresh and _rankings_cache['data'] is not None and _rankings_cache['timestamp'] is not None:
            age = (datetime.now() - _rankings_cache['timestamp']).total_seconds()
            if age < _rankings_cache['ttl_seconds']:
                print(f"Returning cached rankings (age: {age:.1f}s)")
                return _rankings_cache['data']

        print("Generating fresh rankings...")
        predictor = get_predictor()
        espn_collector = get_espn_collector()
        collector = get_collector()

        # Get all teams
        all_teams = espn_collector.get_all_teams()

        # Get UKF ratings for all teams
        ukf_ratings = predictor.get_team_ratings()

        # Get completed games for record calculation
        completed_games = collector.get_completed_games()

        # Build comprehensive rankings
        rankings = []
        for team in all_teams:
            team_id = team.get('id')
            team_name = team.get('name', 'Unknown')

            if not team_id:
                continue

            # Get UKF ratings
            ukf_rating = ukf_ratings.get(team_id, {})
            offensive_rating = ukf_rating.get('offensive_rating', 100.0)
            defensive_rating = ukf_rating.get('defensive_rating', 100.0)
            pace = ukf_rating.get('pace', 70.0)
            momentum = ukf_rating.get('momentum', 0.0)

            # Calculate efficiency margin (offensive - defensive)
            efficiency_margin = offensive_rating - defensive_rating

            # Get KenPom ratings
            kenpom = collector.get_kenpom_team_rating(team_name)

            # Calculate record
            wins = 0
            losses = 0
            for game in completed_games:
                home_id = game.get('HomeTeamID')
                away_id = game.get('AwayTeamID')
                home_score = game.get('HomeTeamScore')
                away_score = game.get('AwayTeamScore')

                if home_score is None or away_score is None:
                    continue

                if home_id == team_id:
                    if home_score > away_score:
                        wins += 1
                    else:
                        losses += 1
                elif away_id == team_id:
                    if away_score > home_score:
                        wins += 1
                    else:
                        losses += 1

            rankings.append({
                'team_id': team_id,
                'team_name': team_name,
                'abbreviation': team.get('abbreviation', ''),
                'conference': team.get('conference', ''),
                'wins': wins,
                'losses': losses,
                'record': f"{wins}-{losses}",
                # Efficiency metrics
                'adj_em': kenpom.get('adj_em', 0.0),
                'adj_o': kenpom.get('adj_o', 100.0),
                'adj_d': kenpom.get('adj_d', 100.0),
                'adj_t': kenpom.get('adj_t', 70.0),
                # UKF ratings
                'offensive_rating': offensive_rating,
                'defensive_rating': defensive_rating,
                'efficiency_margin': efficiency_margin,
                'pace': pace,
                'momentum': momentum,
                # Four Factors
                'efg_o': kenpom.get('efg_o', 50.0),
                'efg_d': kenpom.get('efg_d', 50.0),
                'tov_o': kenpom.get('tov_o', 20.0),
                'tov_d': kenpom.get('tov_d', 20.0),
                'oreb_pct': kenpom.get('oreb_pct', 30.0),
                'ft_rate': kenpom.get('ft_rate', 35.0)
            })

        # Sort by adjusted efficiency margin by default (best to worst)
        rankings.sort(key=lambda x: x['adj_em'], reverse=True)

        # Add rank numbers
        for i, team in enumerate(rankings, 1):
            team['rank'] = i

        result = {'teams': rankings, 'count': len(rankings)}

        # Cache the result
        _rankings_cache['data'] = result
        _rankings_cache['timestamp'] = datetime.now()

        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/predictions/accuracy")
async def get_prediction_accuracy(start_date: Optional[str] = None, end_date: Optional[str] = None):
    """Get model accuracy statistics."""
    try:
        hybrid_predictor = get_hybrid_predictor()
        
        start = datetime.fromisoformat(start_date).date() if start_date else None
        end = datetime.fromisoformat(end_date).date() if end_date else None
        
        accuracy = hybrid_predictor.get_prediction_accuracy(start_date=start, end_date=end)
        return accuracy
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/predictions/{game_id}/result")
async def submit_game_result(game_id: int, home_score: int, away_score: int):
    """Submit game result for accuracy tracking."""
    try:
        hybrid_predictor = get_hybrid_predictor()
        hybrid_predictor.update_game_result(game_id, home_score, away_score)
        
        return {
            'game_id': game_id,
            'home_score': home_score,
            'away_score': away_score,
            'status': 'result_saved'
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/models/versions")
async def get_model_versions():
    """List all model versions."""
    try:
        database = get_database()
        session = database.get_session()
        
        try:
            from src.database import ModelVersion
            models = session.query(ModelVersion).order_by(
                ModelVersion.version_number.desc()
            ).all()
            
            versions = []
            for model in models:
                versions.append({
                    'version_id': model.version_id,
                    'version_number': model.version_number,
                    'model_type': model.model_type,
                    'trained_on_date': model.trained_on_date.isoformat(),
                    'training_games_count': model.training_games_count,
                    'validation_accuracy': model.validation_accuracy,
                    'is_active': model.is_active,
                    'hyperparameters': json.loads(model.hyperparameters_json) if model.hyperparameters_json else {}
                })
            
            return {'versions': versions, 'count': len(versions)}
        finally:
            session.close()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/models/train")
async def trigger_training(season: Optional[int] = None, limit: Optional[int] = None):
    """Trigger model retraining (admin endpoint)."""
    try:
        from src.train_model import train_model
        
        results = train_model(season=season, limit=limit)
        
        return {
            'status': 'training_completed',
            'version_number': results['version_number'],
            'validation_metrics': results['validation_metrics'],
            'training_examples': results['training_examples']
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/predictions/history")
async def get_prediction_history(start_date: Optional[str] = None, end_date: Optional[str] = None, limit: int = 100):
    """Get historical predictions."""
    try:
        database = get_database()
        session = database.get_session()
        
        try:
            from src.database import Prediction, GameResult
            
            query = session.query(Prediction)
            
            if start_date:
                start = datetime.fromisoformat(start_date)
                query = query.filter(Prediction.game_date >= start)
            if end_date:
                end = datetime.fromisoformat(end_date)
                query = query.filter(Prediction.game_date <= end)
            
            predictions = query.order_by(Prediction.game_date.desc()).limit(limit).all()
            
            results = []
            for pred in predictions:
                result_data = None
                result = session.query(GameResult).filter_by(game_id=pred.game_id).first()
                if result:
                    result_data = {
                        'home_score': result.home_score,
                        'away_score': result.away_score,
                        'actual_margin': result.actual_margin,
                        'actual_total': result.actual_total,
                        'home_covered': result.home_covered,
                        'over_hit': result.over_hit
                    }
                
                results.append({
                    'prediction_id': pred.prediction_id,
                    'game_id': pred.game_id,
                    'game_date': pred.game_date.isoformat(),
                    'home_team_id': pred.home_team_id,
                    'away_team_id': pred.away_team_id,
                    'pregame_spread': pred.pregame_spread,
                    'pregame_total': pred.pregame_total,
                    'hybrid_predicted_margin': pred.hybrid_predicted_margin,
                    'hybrid_predicted_total': pred.hybrid_predicted_total,
                    'prediction_source': pred.prediction_source,
                    'prediction_confidence': pred.prediction_confidence,
                    'result': result_data
                })
            
            return {'predictions': results, 'count': len(results)}
        finally:
            session.close()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/teams/list")
async def get_teams_list():
    """Get list of all teams for dropdowns."""
    try:
        espn_collector = get_espn_collector()
        teams = espn_collector.get_all_teams()

        # Sort teams alphabetically by name
        sorted_teams = sorted(teams, key=lambda t: t.get('name', ''))

        # Format for frontend
        teams_list = [
            {
                'id': team.get('id'),
                'name': team.get('name'),
                'abbreviation': team.get('abbreviation', '')
            }
            for team in sorted_teams
            if team.get('id') and team.get('name')
        ]

        return {'teams': teams_list}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/predictions/custom")
async def generate_custom_prediction(request: CustomPredictionRequest):
    """Generate a custom prediction for any two teams."""
    try:
        espn_collector = get_espn_collector()
        hybrid_predictor = get_hybrid_predictor()
        collector = get_collector()

        # Get team names
        teams = espn_collector.get_all_teams()
        home_team_info = next((t for t in teams if t.get('id') == request.home_team_id), None)
        away_team_info = next((t for t in teams if t.get('id') == request.away_team_id), None)

        if not home_team_info or not away_team_info:
            raise HTTPException(status_code=404, detail="Team not found")

        home_team_name = home_team_info.get('name', 'Home Team')
        away_team_name = away_team_info.get('name', 'Away Team')

        # Create a synthetic game object
        game = {
            'HomeTeam': home_team_name,
            'AwayTeam': away_team_name,
            'HomeTeamID': request.home_team_id,
            'AwayTeamID': request.away_team_id,
            'NeutralSite': request.neutral_court,
            'DateTime': datetime.now().isoformat()
        }

        # Generate prediction
        pred = hybrid_predictor.predict_game(game)

        # Extract team features from prediction result
        # The prediction already contains calculated features in ml_features_json
        ml_features = pred.get('ml_features_json', {})

        # Extract home and away features from the ML features dict
        # These are generated by MLFeatureEngineer.engineer_features()
        # Features come from both UKF state and contextual data
        home_features = {
            'offensive_rating': ml_features.get('home_off_rating', 100),
            'defensive_rating': ml_features.get('home_def_rating', 100),
            'pace': ml_features.get('home_pace', 70),
            'kenpom_adj_em': ml_features.get('home_kp_adj_em', 0),
            'kenpom_adj_o': ml_features.get('home_kp_adj_o', 100),
            'kenpom_adj_d': ml_features.get('home_kp_adj_d', 100),
            'kenpom_adj_t': ml_features.get('home_kp_adj_t', 70),
            'momentum': ml_features.get('home_momentum', 0),
            'fatigue': ml_features.get('home_fatigue', 0),
            'health_status': ml_features.get('home_health', 1.0),
            'sos': 0  # SOS not included in ML features, would require team_ratings dict
        }

        away_features = {
            'offensive_rating': ml_features.get('away_off_rating', 100),
            'defensive_rating': ml_features.get('away_def_rating', 100),
            'pace': ml_features.get('away_pace', 70),
            'kenpom_adj_em': ml_features.get('away_kp_adj_em', 0),
            'kenpom_adj_o': ml_features.get('away_kp_adj_o', 100),
            'kenpom_adj_d': ml_features.get('away_kp_adj_d', 100),
            'kenpom_adj_t': ml_features.get('away_kp_adj_t', 70),
            'momentum': ml_features.get('away_momentum', 0),
            'fatigue': ml_features.get('away_fatigue', 0),
            'health_status': ml_features.get('away_health', 1.0),
            'sos': 0  # SOS not included in ML features, would require team_ratings dict
        }

        # Format response with full stats
        return {
            'home_team': home_team_name,
            'away_team': away_team_name,
            'home_team_id': request.home_team_id,
            'away_team_id': request.away_team_id,
            'neutral_court': request.neutral_court,
            'prediction': {
                'predicted_margin': pred.get('hybrid_predicted_margin'),
                'predicted_total': pred.get('hybrid_predicted_total'),
                'ukf_predicted_margin': pred.get('ukf_predicted_margin'),
                'ukf_predicted_total': pred.get('ukf_predicted_total'),
                'ml_predicted_margin': pred.get('ml_predicted_margin'),
                'ml_predicted_total': pred.get('ml_predicted_total'),
                'predicted_winner': pred.get('predicted_winner'),
                'prediction_source': pred.get('prediction_source'),
                'overall_confidence': pred.get('overall_confidence', 0)
            },
            'home_team_stats': {
                'offensive_rating': home_features.get('offensive_rating', 100),
                'defensive_rating': home_features.get('defensive_rating', 100),
                'pace': home_features.get('pace', 70),
                'kenpom_adj_em': home_features.get('kenpom_adj_em', 0),
                'kenpom_adj_o': home_features.get('kenpom_adj_o', 100),
                'kenpom_adj_d': home_features.get('kenpom_adj_d', 100),
                'kenpom_adj_t': home_features.get('kenpom_adj_t', 70),
                'momentum': home_features.get('momentum', 0),
                'fatigue': home_features.get('fatigue', 0),
                'health_status': home_features.get('health_status', 1.0),
                'sos': home_features.get('sos', 0)
            },
            'away_team_stats': {
                'offensive_rating': away_features.get('offensive_rating', 100),
                'defensive_rating': away_features.get('defensive_rating', 100),
                'pace': away_features.get('pace', 70),
                'kenpom_adj_em': away_features.get('kenpom_adj_em', 0),
                'kenpom_adj_o': away_features.get('kenpom_adj_o', 100),
                'kenpom_adj_d': away_features.get('kenpom_adj_d', 100),
                'kenpom_adj_t': away_features.get('kenpom_adj_t', 70),
                'momentum': away_features.get('momentum', 0),
                'fatigue': away_features.get('fatigue', 0),
                'health_status': away_features.get('health_status', 1.0),
                'sos': away_features.get('sos', 0)
            }
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating prediction: {str(e)}")


@app.get("/api/health")
async def health_check():
    """Health check endpoint."""
    return {'status': 'healthy', 'timestamp': datetime.now().isoformat()}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

