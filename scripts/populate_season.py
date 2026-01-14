#!/usr/bin/env python3
"""
Script to populate database with all games from the 2025-26 season.
"""
import os
import sys
from datetime import datetime

# Add parent directory to path so we can import from src
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Force SQLite for development
if 'DATABASE_URL' not in os.environ or 'postgresql' in os.environ.get('DATABASE_URL', '').lower():
    os.environ.pop('DATABASE_URL', None)
    os.environ['SQLITE_DB_URL'] = 'sqlite:///./basketball_predictor.db'

import config
from src.database import get_database, Prediction, GameResult
from src.predictor import get_predictor
from src.data_collector import get_collector

def populate_season():
    """Process all games from the 2025-26 season."""
    print("="*70)
    print("POPULATING 2025-26 SEASON DATA")
    print("="*70)
    
    # Initialize components
    db = get_database()
    predictor = get_predictor()
    predictor.initialize()
    collector = get_collector()
    
    # Get all completed games
    print("\nLoading all completed games...")
    all_games = collector.get_completed_games()
    print(f"Found {len(all_games)} completed games")
    
    # Check what we already have
    session = db.get_session()
    try:
        existing_preds = session.query(Prediction).count()
        existing_game_ids = {row[0] for row in session.query(Prediction.game_id).all()}
        print(f"Current predictions in database: {existing_preds}")
        print(f"Unique game IDs already processed: {len(existing_game_ids)}")
    finally:
        session.close()
    
    # Filter games we haven't processed
    games_to_process = [g for g in all_games if g.get('GameID') not in existing_game_ids]
    print(f"\nGames to process: {len(games_to_process)}")
    
    if len(games_to_process) == 0:
        print("✓ All games already processed!")
        return
    
    # Process games in batches
    batch_size = 100
    total_processed = 0
    total_saved = 0
    total_errors = 0
    
    print(f"\nProcessing {len(games_to_process)} games in batches of {batch_size}...")
    print("This will take several minutes...\n")
    
    for batch_start in range(0, len(games_to_process), batch_size):
        batch_end = min(batch_start + batch_size, len(games_to_process))
        batch = games_to_process[batch_start:batch_end]
        
        print(f"Processing batch {batch_start//batch_size + 1} ({batch_start+1}-{batch_end} of {len(games_to_process)})...")
        
        batch_saved = 0
        batch_errors = 0
        
        for game in batch:
            game_id = game.get('GameID')
            home_score = game.get('HomeTeamScore')
            away_score = game.get('AwayTeamScore')
            
            if not game_id or home_score is None or away_score is None:
                batch_errors += 1
                continue
            
            game_date_str = game.get('DateTime', '')
            if not game_date_str:
                batch_errors += 1
                continue
            
            try:
                game_date = datetime.fromisoformat(game_date_str.replace('Z', '+00:00'))
            except:
                batch_errors += 1
                continue
            
            # Generate prediction
            try:
                prediction = predictor.predict_game(game)
                home_team_id = prediction.get('home_team_id')
                away_team_id = prediction.get('away_team_id')
                
                if home_team_id and away_team_id:
                    # Prepare prediction data
                    prediction_data = {
                        'pregame_spread': game.get('PointSpread'),
                        'pregame_total': game.get('OverUnder'),
                        'ukf_predicted_margin': prediction.get('predicted_margin'),
                        'ukf_predicted_total': prediction.get('predicted_total'),
                        'hybrid_predicted_margin': prediction.get('predicted_margin'),  # UKF only for now
                        'hybrid_predicted_total': prediction.get('predicted_total'),
                        'home_covers_probability': prediction.get('home_covers_probability'),
                        'over_probability': prediction.get('over_probability'),
                        'prediction_confidence': prediction.get('overall_confidence'),
                        'prediction_source': 'ukf'
                    }
                    
                    # Save prediction and result
                    session = db.get_session()
                    try:
                        db.save_prediction(
                            game_id, game_date, home_team_id, away_team_id, 
                            prediction_data, session=session
                        )
                        db.save_result(
                            game_id, home_score, away_score,
                            pregame_spread=game.get('PointSpread'),
                            pregame_total=game.get('OverUnder'),
                            session=session
                        )
                        session.commit()
                        batch_saved += 1
                    except Exception as e:
                        session.rollback()
                        batch_errors += 1
                    finally:
                        session.close()
                else:
                    batch_errors += 1
            except Exception as e:
                batch_errors += 1
                if total_errors < 5:  # Only print first few errors
                    print(f"    Error processing game {game_id}: {e}")
        
        total_processed += len(batch)
        total_saved += batch_saved
        total_errors += batch_errors
        
        print(f"  Batch complete: {batch_saved} saved, {batch_errors} errors")
        print(f"  Progress: {total_saved}/{len(games_to_process)} games processed ({100*total_saved/len(games_to_process):.1f}%)")
    
    print("\n" + "="*70)
    print("POPULATION COMPLETE")
    print("="*70)
    print(f"Total games processed: {total_processed}")
    print(f"Successfully saved: {total_saved}")
    print(f"Errors: {total_errors}")
    
    # Final stats
    session = db.get_session()
    try:
        final_pred_count = session.query(Prediction).count()
        final_result_count = session.query(GameResult).count()
        final_training_count = session.query(Prediction, GameResult).join(
            GameResult, Prediction.game_id == GameResult.game_id
        ).count()
        
        print(f"\nFinal database stats:")
        print(f"  Predictions: {final_pred_count}")
        print(f"  Results: {final_result_count}")
        print(f"  Training records: {final_training_count}")
    finally:
        session.close()
    
    print("\n✓ Season data population complete!")

if __name__ == "__main__":
    try:
        populate_season()
    except KeyboardInterrupt:
        print("\n\n⚠ Process interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

