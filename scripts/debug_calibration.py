"""
Debug script to investigate why predictions are producing huge margins (e.g. +800).
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.predictor import get_predictor
from src.feature_calculator import FeatureCalculator
from src.data_collector import DataCollector
from datetime import datetime

def debug_prediction():
    print("Initializing predictor...")
    # This mimics what daily_collect_odds.py does
    predictor = get_predictor()
    
    # Create a mock game that produced a huge margin
    # e.g. Oregon Ducks @ Nebraska Cornhuskers
    mock_game = {
        'GameID': 'debug_game_1',
        'HomeTeam': 'Nebraska',
        'AwayTeam': 'Oregon',
        'HomeTeamID': 12345,
        'AwayTeamID': 67890,
        'DateTime': datetime.now().isoformat(),
        'PointSpread': -5.0,
        'OverUnder': 145.0
    }
    
    print("\n--- Generating Prediction ---")
    prediction = predictor.predict_game(mock_game)
    
    print("\nPrediction Result:")
    print(f"Margin: {prediction['predicted_margin']}")
    print(f"Total: {prediction['predicted_total']}")
    
    # Dig deeper into components if possible
    # We'll need to inspect the predictor's state directly
    print("\n--- Inspecting State ---")
    home_id = predictor._get_team_id(mock_game, 'HomeTeam', 'HomeTeamID')
    away_id = predictor._get_team_id(mock_game, 'AwayTeam', 'AwayTeamID')
    
    home_state = predictor.ukf.get_team_state(home_id)
    away_state = predictor.ukf.get_team_state(away_id)
    
    print(f"Home State ({mock_game['HomeTeam']}): {home_state}")
    print(f"Away State ({mock_game['AwayTeam']}): {away_state}")
    
    # Recalculate features to see if they are the culprit
    print("\n--- recalculating features ---")
    game_date = datetime.now()
    all_games = predictor.collector.get_completed_games()
    
    home_features = predictor.calculator.get_game_features(
        mock_game, home_id, is_home=True,
        all_games=all_games, current_date=game_date
    )
    
    away_features = predictor.calculator.get_game_features(
        mock_game, away_id, is_home=False,
        all_games=all_games, current_date=game_date
    )
    
    print("\nHome Features:")
    for k, v in home_features.items():
        print(f"  {k}: {v}")
        
    print("\nAway Features:")
    for k, v in away_features.items():
        print(f"  {k}: {v}")

    # Calculate impacts manually (from predictor.py)
    health_impact = (home_features['health_status'] - away_features['health_status']) * 5.0
    momentum_impact = (home_features['momentum'] - away_features['momentum']) * 3.0
    fatigue_impact = (away_features['fatigue'] - home_features['fatigue']) * 2.0
    
    print("\nImpacts:")
    print(f"  Health: {health_impact}")
    print(f"  Momentum: {momentum_impact}")
    print(f"  Fatigue: {fatigue_impact}")

if __name__ == "__main__":
    debug_prediction()

