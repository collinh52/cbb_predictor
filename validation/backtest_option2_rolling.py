"""
OPTION 2: Rolling Validation on Current Season (2025-26)
Uses time-based train/test split - more realistic for real-world usage.
"""
import os
import sys

# Add parent directory to path so we can import from src and scripts
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.pop('DATABASE_URL', None)

from src.espn_collector import get_espn_collector
from datetime import datetime, timedelta
from collections import defaultdict
import numpy as np

# Add scripts directory to path
scripts_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'scripts')
sys.path.insert(0, scripts_dir)
from show_team_ratings_v3 import calculate_team_ratings

def backtest_rolling_current_season():
    """
    Rolling validation on 2025-26 season:
    - Split: First 80% for training, last 20% for testing
    - More realistic: simulates using ratings built on past to predict future
    """
    print("\n" + "="*100)
    print("OPTION 2: ROLLING VALIDATION ON CURRENT SEASON (2025-26)")
    print("="*100 + "\n")
    
    espn = get_espn_collector()
    
    # Fetch current season games
    print("Fetching 2025-26 season games from ESPN...")
    all_games = espn.get_all_games_via_team_schedules(season=2026)
    
    # Filter completed games with scores
    completed_games = [
        g for g in all_games 
        if g.get('HomeTeamScore') is not None and g.get('AwayTeamScore') is not None
    ]
    
    # Sort by date
    for game in completed_games:
        try:
            game['date_obj'] = datetime.fromisoformat(game['DateTime'].replace('Z', '+00:00'))
        except:
            game['date_obj'] = datetime.now()
    
    completed_games.sort(key=lambda x: x['date_obj'])
    
    print(f"✓ Found {len(completed_games)} completed games from 2025-26 season")
    
    if len(completed_games) < 100:
        print("⚠️  Warning: Not enough games for reliable rolling validation")
        return
    
    # Time-based split (80/20)
    split_point = int(len(completed_games) * 0.8)
    training_games = completed_games[:split_point]
    test_games = completed_games[split_point:]
    
    split_date = training_games[-1]['date_obj'] if training_games else datetime.now()
    
    print(f"✓ Training period: {len(training_games)} games (up to {split_date.strftime('%Y-%m-%d')})")
    print(f"✓ Testing period: {len(test_games)} games (from {split_date.strftime('%Y-%m-%d')} onwards)")
    print()
    
    # Build ratings on training data
    print("Building ratings on training data...")
    try:
        ratings_result = calculate_team_ratings(training_games, min_games=5, use_sos_adjustment=True)
        # Handle both old format (list) and new format (tuple)
        if isinstance(ratings_result, tuple):
            ratings, neutral_stats = ratings_result
        else:
            ratings = ratings_result
        ratings_dict = {r['team_id']: r for r in ratings}
        print(f"✓ Built ratings for {len(ratings)} teams")
    except Exception as e:
        print(f"Error calculating ratings: {e}")
        return
    
    print()
    
    # Test on hold-out data
    print("Testing on hold-out data...")
    print("-" * 100)
    
    predictions = []
    correct_predictions = 0
    total_predictions = 0
    
    # Predict each test game
    for game in test_games:
        home_id = game.get('HomeTeamID')
        away_id = game.get('AwayTeamID')
        home_score = game.get('HomeTeamScore')
        away_score = game.get('AwayTeamScore')
        
        if not (home_id and away_id and home_score is not None and away_score is not None):
            continue
        
        if home_id not in ratings_dict or away_id not in ratings_dict:
            continue  # Skip if teams don't have ratings
        
        # Get ratings
        home_rating = ratings_dict[home_id]['overall_rating']
        away_rating = ratings_dict[away_id]['overall_rating']
        
        # Predict margin
        predicted_margin = home_rating - away_rating
        
        # Actual margin
        actual_margin = home_score - away_score
        
        # Check if prediction was correct
        predicted_winner = "HOME" if predicted_margin > 0 else "AWAY"
        actual_winner = "HOME" if actual_margin > 0 else "AWAY"
        
        is_correct = predicted_winner == actual_winner
        
        if is_correct:
            correct_predictions += 1
        
        total_predictions += 1
        
        # Store prediction
        predictions.append({
            'date': game['date_obj'],
            'home_team': game.get('HomeTeamName', 'Unknown'),
            'away_team': game.get('AwayTeamName', 'Unknown'),
            'predicted_margin': predicted_margin,
            'actual_margin': actual_margin,
            'predicted_winner': predicted_winner,
            'actual_winner': actual_winner,
            'correct': is_correct,
            'home_rating': home_rating,
            'away_rating': away_rating,
            'home_sos': ratings_dict[home_id].get('sos', 0.5),
            'away_sos': ratings_dict[away_id].get('sos', 0.5)
        })
        
        # Print every 20th prediction
        if total_predictions % 20 == 0:
            running_acc = (correct_predictions / total_predictions) * 100
            print(f"Predictions: {total_predictions}, Running accuracy: {running_acc:.1f}%")
    
    print("-" * 100)
    print()
    
    # Calculate statistics
    if total_predictions > 0:
        overall_accuracy = (correct_predictions / total_predictions) * 100
        
        print("="*100)
        print("ROLLING VALIDATION RESULTS - 2025-26 SEASON")
        print("="*100)
        print()
        print(f"Training Games: {len(training_games)}")
        print(f"Test Games: {total_predictions}")
        print(f"Correct Predictions: {correct_predictions}")
        print(f"**Overall Accuracy: {overall_accuracy:.2f}%**")
        print()
        
        # Margin analysis
        margins = [abs(p['predicted_margin'] - p['actual_margin']) for p in predictions]
        avg_margin_error = np.mean(margins)
        median_margin_error = np.median(margins)
        std_margin_error = np.std(margins)
        
        print(f"Average Margin Error: {avg_margin_error:.2f} points")
        print(f"Median Margin Error: {median_margin_error:.2f} points")
        print(f"Std Dev Margin Error: {std_margin_error:.2f} points")
        print()
        
        # Confidence breakdown
        print("ACCURACY BY PREDICTED MARGIN:")
        confidence_buckets = [
            (">15 pts", lambda p: abs(p['predicted_margin']) > 15),
            ("10-15 pts", lambda p: 10 < abs(p['predicted_margin']) <= 15),
            ("5-10 pts", lambda p: 5 < abs(p['predicted_margin']) <= 10),
            ("<5 pts (toss-up)", lambda p: abs(p['predicted_margin']) <= 5)
        ]
        
        for label, condition in confidence_buckets:
            bucket_preds = [p for p in predictions if condition(p)]
            if bucket_preds:
                bucket_acc = sum(1 for p in bucket_preds if p['correct']) / len(bucket_preds) * 100
                print(f"  {label}: {len(bucket_preds)} games, {bucket_acc:.1f}% accuracy")
        
        print()
        
        # Best and worst predictions
        predictions.sort(key=lambda p: abs(p['predicted_margin'] - p['actual_margin']))
        
        print("BEST PREDICTIONS (smallest margin error):")
        for i, p in enumerate(predictions[:5], 1):
            error = abs(p['predicted_margin'] - p['actual_margin'])
            status = "✓" if p['correct'] else "✗"
            print(f"  {i}. {p['home_team']} vs {p['away_team']}")
            print(f"     Predicted: {p['predicted_margin']:+.1f}, Actual: {p['actual_margin']:+.1f}, Error: {error:.1f} {status}")
        
        print()
        print("WORST PREDICTIONS (largest margin error):")
        for i, p in enumerate(predictions[-5:][::-1], 1):
            error = abs(p['predicted_margin'] - p['actual_margin'])
            status = "✓" if p['correct'] else "✗"
            print(f"  {i}. {p['home_team']} vs {p['away_team']}")
            print(f"     Predicted: {p['predicted_margin']:+.1f}, Actual: {p['actual_margin']:+.1f}, Error: {error:.1f} {status}")
        
        print()
        print("="*100)
        
        # Save results
        save_results(predictions, overall_accuracy, split_date, "option2_rolling")
        
    else:
        print("⚠️  No predictions made - insufficient data")

def save_results(predictions, accuracy, split_date, filename):
    """Save detailed results to file."""
    output_file = f"backtest_results_{filename}.txt"
    
    with open(output_file, 'w') as f:
        f.write("="*100 + "\n")
        f.write(f"ROLLING VALIDATION RESULTS\n")
        f.write("="*100 + "\n\n")
        f.write(f"Split Date: {split_date.strftime('%Y-%m-%d')}\n")
        f.write(f"Overall Accuracy: {accuracy:.2f}%\n")
        f.write(f"Total Predictions: {len(predictions)}\n\n")
        
        f.write("DETAILED PREDICTIONS:\n")
        f.write("-"*100 + "\n")
        
        # Sort by date
        predictions.sort(key=lambda p: p['date'])
        
        for i, p in enumerate(predictions, 1):
            status = "✓" if p['correct'] else "✗"
            f.write(f"{i}. {p['date'].strftime('%Y-%m-%d')} - {p['away_team']} @ {p['home_team']}\n")
            f.write(f"   Ratings: Home {p['home_rating']:+.1f} (SOS: {p['home_sos']:.3f}) vs ")
            f.write(f"Away {p['away_rating']:+.1f} (SOS: {p['away_sos']:.3f})\n")
            f.write(f"   Predicted: {p['predicted_winner']} by {abs(p['predicted_margin']):.1f}\n")
            f.write(f"   Actual: {p['actual_winner']} by {abs(p['actual_margin']):.1f}\n")
            f.write(f"   Error: {abs(p['predicted_margin'] - p['actual_margin']):.1f} pts\n")
            f.write(f"   Result: {status} {'CORRECT' if p['correct'] else 'INCORRECT'}\n\n")
    
    print(f"✓ Detailed results saved to {output_file}")

if __name__ == "__main__":
    backtest_rolling_current_season()

