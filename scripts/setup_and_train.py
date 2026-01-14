#!/usr/bin/env python3
"""
Script to set up the database and train the initial model.
Uses SQLite for development by default.
"""
import os
import sys

# Add parent directory to path so we can import from src
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Force SQLite for development (override DATABASE_URL if set)
if 'DATABASE_URL' not in os.environ or 'postgresql' in os.environ.get('DATABASE_URL', '').lower():
    os.environ.pop('DATABASE_URL', None)
    os.environ['SQLITE_DB_URL'] = 'sqlite:///./basketball_predictor.db'
    print("Using SQLite database for development (basketball_predictor.db)")

# Reload config after setting environment
import importlib
import config
importlib.reload(config)

from src.database import get_database, Database
from src.predictor import get_predictor
from src.hybrid_predictor import HybridPredictor
from src.data_collector import get_collector
from datetime import datetime

def setup_database():
    """Initialize database tables."""
    print("Setting up database...")
    # Create a fresh database instance to avoid cached connection
    db = Database(config.DATABASE_URL)
    db.init_database()
    print("✓ Database tables created successfully")
    return db

def populate_initial_predictions_and_results(db, limit=100):
    """Generate predictions for historical games and store results."""
    print(f"\nGenerating predictions and results for {limit} historical games...")
    
    predictor = get_predictor()
    predictor.initialize()
    collector = get_collector()
    
    # Get completed games
    games = collector.get_completed_games()
    if len(games) == 0:
        print("No completed games found. Cannot populate database.")
        return 0, 0
    
    games = games[:limit]  # Limit for initial setup
    
    predictions_saved = 0
    results_saved = 0
    
    # Use UKF predictor only (ML model won't be available yet)
    for i, game in enumerate(games):
        if (i + 1) % 10 == 0:
            print(f"  Processing game {i+1}/{len(games)}...")
        
        game_id = game.get('GameID')
        home_score = game.get('HomeTeamScore')
        away_score = game.get('AwayTeamScore')
        
        if not game_id or home_score is None or away_score is None:
            continue
        
        game_date_str = game.get('DateTime', '')
        if not game_date_str:
            continue
        
        try:
            game_date = datetime.fromisoformat(game_date_str.replace('Z', '+00:00'))
        except:
            continue
        
        # Generate UKF prediction (no ML yet)
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
                    'hybrid_predicted_margin': prediction.get('predicted_margin'),  # Use UKF for now
                    'hybrid_predicted_total': prediction.get('predicted_total'),
                    'home_covers_probability': prediction.get('home_covers_probability'),
                    'over_probability': prediction.get('over_probability'),
                    'prediction_confidence': prediction.get('overall_confidence'),
                    'prediction_source': 'ukf'
                }
                
                # Save prediction
                db.save_prediction(
                    game_id, game_date, home_team_id, away_team_id, prediction_data
                )
                predictions_saved += 1
                
                # Save result
                db.save_result(
                    game_id, home_score, away_score,
                    pregame_spread=game.get('PointSpread'),
                    pregame_total=game.get('OverUnder')
                )
                results_saved += 1
        except Exception as e:
            print(f"  Error processing game {game_id}: {e}")
            continue
    
    print(f"✓ Saved {predictions_saved} predictions and {results_saved} results")
    return predictions_saved, results_saved

def train_model(db):
    """Train the neural network model."""
    print("\nTraining neural network model...")
    
    # Check if we have enough training data
    training_data = db.get_training_data(limit=5)
    if len(training_data) < 50:
        print(f"⚠ Warning: Only {len(training_data)} training records found. Need at least 50.")
        print("You may want to populate more predictions first with: python setup_and_train.py --populate 200")
        return False
    
    try:
        from src.train_model import train_model
        results = train_model()
        print(f"\n✓ Model training completed!")
        print(f"  Version: {results['version_number']}")
        print(f"  Training examples: {results['training_examples']}")
        print(f"  Validation RMSE (margin): {results['validation_metrics']['margin_rmse']:.2f}")
        print(f"  Validation RMSE (total): {results['validation_metrics']['total_rmse']:.2f}")
        return True
    except Exception as e:
        print(f"✗ Model training failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Set up database and train model")
    parser.add_argument("--populate", type=int, default=100, 
                       help="Number of games to populate (default: 100)")
    parser.add_argument("--train", action="store_true", 
                       help="Train the model after setup")
    parser.add_argument("--skip-populate", action="store_true",
                       help="Skip populating predictions (assume database already has data)")
    
    args = parser.parse_args()
    
    try:
        # Setup database
        db = setup_database()
        
        # Populate initial predictions and results
        if not args.skip_populate:
            predictions, results = populate_initial_predictions_and_results(db, limit=args.populate)
            if predictions == 0:
                print("\n⚠ No predictions were saved. Cannot train model.")
                sys.exit(1)
        else:
            print("Skipping population (assuming database already has data)")
            training_data = db.get_training_data(limit=5)
            print(f"Found {len(training_data)} training records in database")
        
        # Train model if requested
        if args.train:
            train_model(db)
        else:
            print("\n✓ Database setup complete!")
            print("\nTo train the model, run:")
            print("  python setup_and_train.py --skip-populate --train")
            print("  OR")
            print("  python -m src.train_model")
        
    except Exception as e:
        print(f"\n✗ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

