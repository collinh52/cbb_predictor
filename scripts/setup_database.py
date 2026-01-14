#!/usr/bin/env python3
"""
Script to set up the database and optionally train the initial model.
"""
import os
import sys

# Add parent directory to path so we can import from src
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Force SQLite for development (can be overridden with DATABASE_URL env var)
if 'DATABASE_URL' not in os.environ:
    os.environ['SQLITE_DB_URL'] = 'sqlite:///./basketball_predictor.db'

from src.database import get_database
from src.predictor import get_predictor
from src.hybrid_predictor import HybridPredictor
from src.data_collector import get_collector
from datetime import datetime

def setup_database():
    """Initialize database tables."""
    print("Setting up database...")
    db = get_database()
    db.init_database()
    print("✓ Database tables created successfully")
    return db

def populate_initial_predictions(db, limit=100):
    """Generate predictions for historical games and store results."""
    print(f"\nGenerating predictions for {limit} historical games...")
    
    predictor = get_predictor()
    predictor.initialize()
    collector = get_collector()
    hybrid_predictor = HybridPredictor(predictor)
    
    # Get completed games
    games = collector.get_completed_games()
    games = games[:limit]  # Limit for initial setup
    
    predictions_saved = 0
    results_saved = 0
    
    for game in games:
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
        
        # Generate prediction
        try:
            prediction = hybrid_predictor.predict_game(game)
            home_team_id = prediction.get('home_team_id')
            away_team_id = prediction.get('away_team_id')
            
            if home_team_id and away_team_id:
                # Save prediction
                hybrid_predictor.save_prediction_to_database(
                    game_id, game_date, home_team_id, away_team_id, prediction
                )
                predictions_saved += 1
                
                # Save result
                hybrid_predictor.update_game_result(game_id, home_score, away_score)
                results_saved += 1
        except Exception as e:
            print(f"Error processing game {game_id}: {e}")
            continue
    
    print(f"✓ Saved {predictions_saved} predictions and {results_saved} results")
    return predictions_saved

if __name__ == "__main__":
    try:
        # Setup database
        db = setup_database()
        
        # Optionally populate with initial predictions
        if '--populate' in sys.argv:
            limit = int(sys.argv[sys.argv.index('--populate') + 1]) if '--populate' in sys.argv and len(sys.argv) > sys.argv.index('--populate') + 1 and sys.argv[sys.argv.index('--populate') + 1].isdigit() else 100
            populate_initial_predictions(db, limit=limit)
        
        print("\n✓ Database setup complete!")
        print("\nNext steps:")
        print("1. To train the model, run: python -m src.train_model")
        print("2. Or with initial data: python setup_database.py --populate 200 && python -m src.train_model")
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

