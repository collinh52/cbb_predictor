"""
FastAPI backend for UKF Basketball Predictor.
"""
from fastapi import FastAPI, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
from jinja2 import Template
from typing import List, Dict, Optional
from datetime import datetime
import os
import json

from src.predictor import get_predictor, get_hybrid_predictor
from src.data_collector import get_collector
from src.database import get_database

app = FastAPI(title="UKF Basketball Predictor")

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
async def get_todays_games():
    """Get today's games with hybrid predictions."""
    try:
        collector = get_collector()
        hybrid_predictor = get_hybrid_predictor()
        database = get_database()
        
        games = collector.get_todays_games()
        
        # Format response
        results = []
        for game in games:
            game_id = game.get('GameID')
            game_date_str = game.get('DateTime', '')
            
            try:
                game_date = datetime.fromisoformat(game_date_str.replace('Z', '+00:00')) if game_date_str else datetime.now()
            except:
                game_date = datetime.now()
            
            # Generate hybrid prediction
            pred = hybrid_predictor.predict_game(game)
            
            # Save prediction to database
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
                'home_team_id': home_team_id,
                'away_team_id': away_team_id,
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


@app.get("/api/health")
async def health_check():
    """Health check endpoint."""
    return {'status': 'healthy', 'timestamp': datetime.now().isoformat()}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

