"""
OPTION 1: Quick Validation on 2024-25 Season
Validates rating system on last season's completed games.
"""
import os
import sys

# Add parent directory to path so we can import from src and scripts
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.pop('DATABASE_URL', None)

from src.espn_collector import get_espn_collector
from datetime import datetime
from collections import defaultdict
import numpy as np

# Add scripts directory to path
scripts_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'scripts')
sys.path.insert(0, scripts_dir)
from show_team_ratings_v3 import calculate_team_ratings

def backtest_last_season():
    """
    Backtest on 2024-25 season:
    1. Get all games from 2024-25 season
    2. For each week, calculate ratings using only prior games
    3. Predict outcomes for that week
    4. Compare to actual results
    """
    print("\n" + "="*100)
    print("OPTION 1: BACKTESTING ON 2024-25 SEASON")
    print("="*100 + "\n")
    
    espn = get_espn_collector()
    
    # Fetch 2024-25 season games
    print("Fetching 2024-25 season games from ESPN...")
    all_games = espn.get_all_games_via_team_schedules(season=2025)
    
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
    
    print(f"✓ Found {len(completed_games)} completed games from 2024-25 season")
    
    if len(completed_games) < 100:
        print("⚠️  Warning: Not enough historical games for reliable backtesting")
        print("   Need at least 100 games, preferably 500+")
        return
    
    # Split into training period and testing weeks
    # Use first 70% for initial ratings, test on remaining 30%
    split_point = int(len(completed_games) * 0.7)
    training_games = completed_games[:split_point]
    test_games = completed_games[split_point:]
    
    print(f"✓ Training period: {len(training_games)} games")
    print(f"✓ Testing period: {len(test_games)} games")
    print()
    
    # Track predictions
    predictions = []
    correct_predictions = 0
    total_predictions = 0
    
    # Weekly backtesting
    print("Running weekly predictions...")
    print("-" * 100)
    
    # Group test games by week
    weeks = defaultdict(list)
    for game in test_games:
        week_key = game['date_obj'].strftime('%Y-W%U')  # Year-Week format
        weeks[week_key].append(game)
    
    current_training_games = training_games.copy()
    
    for week_num, (week_key, week_games) in enumerate(sorted(weeks.items()), 1):
        # Calculate ratings using all games up to this week
        try:
            ratings_result = calculate_team_ratings(current_training_games, min_games=5, use_sos_adjustment=True)
            # Handle both old format (list) and new format (tuple)
            if isinstance(ratings_result, tuple):
                ratings, neutral_stats = ratings_result
            else:
                ratings = ratings_result
            ratings_dict = {r['team_id']: r for r in ratings}
        except Exception as e:
            print(f"Error calculating ratings for week {week_key}: {e}")
            continue
        
        # Predict each game in this week
        week_correct = 0
        week_total = 0
        
        for game in week_games:
            home_id = game.get('HomeTeamID')
            away_id = game.get('AwayTeamID')
            home_score = game.get('HomeTeamScore')
            away_score = game.get('AwayTeamScore')
            
            if not (home_id and away_id and home_score is not None and away_score is not None):
                continue
            
            if home_id not in ratings_dict or away_id not in ratings_dict:
                continue  # Skip if teams don't have enough games
            
            # Get ratings
            home_rating = ratings_dict[home_id]['overall_rating']
            away_rating = ratings_dict[away_id]['overall_rating']
            
            # Predict margin (home team perspective)
            predicted_margin = home_rating - away_rating
            
            # Actual margin
            actual_margin = home_score - away_score
            
            # Check if prediction was correct (same sign = correct direction)
            predicted_winner = "HOME" if predicted_margin > 0 else "AWAY"
            actual_winner = "HOME" if actual_margin > 0 else "AWAY"
            
            is_correct = predicted_winner == actual_winner
            
            if is_correct:
                week_correct += 1
                correct_predictions += 1
            
            week_total += 1
            total_predictions += 1
            
            # Store prediction details
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
                'away_rating': away_rating
            })
        
        # Print weekly results
        if week_total > 0:
            week_accuracy = (week_correct / week_total) * 100
            print(f"Week {week_num} ({week_key}): {week_correct}/{week_total} correct ({week_accuracy:.1f}%)")
        
        # Add this week's games to training set for next week
        current_training_games.extend(week_games)
    
    print("-" * 100)
    print()
    
    # Calculate overall statistics
    if total_predictions > 0:
        overall_accuracy = (correct_predictions / total_predictions) * 100
        
        print("="*100)
        print("BACKTESTING RESULTS - 2024-25 SEASON")
        print("="*100)
        print()
        print(f"Total Predictions: {total_predictions}")
        print(f"Correct Predictions: {correct_predictions}")
        print(f"**Overall Accuracy: {overall_accuracy:.2f}%**")
        print()
        
        # Calculate additional statistics
        margins = [abs(p['predicted_margin'] - p['actual_margin']) for p in predictions]
        avg_margin_error = np.mean(margins)
        median_margin_error = np.median(margins)
        
        print(f"Average Margin Error: {avg_margin_error:.2f} points")
        print(f"Median Margin Error: {median_margin_error:.2f} points")
        print()
        
        # Breakdown by confidence
        high_conf = [p for p in predictions if abs(p['predicted_margin']) > 10]
        med_conf = [p for p in predictions if 5 < abs(p['predicted_margin']) <= 10]
        low_conf = [p for p in predictions if abs(p['predicted_margin']) <= 5]
        
        if high_conf:
            high_acc = sum(1 for p in high_conf if p['correct']) / len(high_conf) * 100
            print(f"High Confidence (>10 pt margin): {len(high_conf)} games, {high_acc:.1f}% accuracy")
        
        if med_conf:
            med_acc = sum(1 for p in med_conf if p['correct']) / len(med_conf) * 100
            print(f"Medium Confidence (5-10 pt margin): {len(med_conf)} games, {med_acc:.1f}% accuracy")
        
        if low_conf:
            low_acc = sum(1 for p in low_conf if p['correct']) / len(low_conf) * 100
            print(f"Low Confidence (<5 pt margin): {len(low_conf)} games, {low_acc:.1f}% accuracy")
        
        print()
        print("="*100)
        
        # Save detailed results
        save_results(predictions, overall_accuracy, "option1_last_season")
        
    else:
        print("⚠️  No predictions made - insufficient data")

def save_results(predictions, accuracy, filename):
    """Save detailed results to file."""
    output_file = f"backtest_results_{filename}.txt"
    
    with open(output_file, 'w') as f:
        f.write("="*100 + "\n")
        f.write(f"BACKTESTING RESULTS - {filename.upper()}\n")
        f.write("="*100 + "\n\n")
        f.write(f"Overall Accuracy: {accuracy:.2f}%\n")
        f.write(f"Total Predictions: {len(predictions)}\n\n")
        
        f.write("DETAILED PREDICTIONS:\n")
        f.write("-"*100 + "\n")
        
        for i, p in enumerate(predictions, 1):
            status = "✓" if p['correct'] else "✗"
            f.write(f"{i}. {p['date'].strftime('%Y-%m-%d')} - {p['away_team']} @ {p['home_team']}\n")
            f.write(f"   Predicted: {p['predicted_winner']} by {abs(p['predicted_margin']):.1f}\n")
            f.write(f"   Actual: {p['actual_winner']} by {abs(p['actual_margin']):.1f}\n")
            f.write(f"   Result: {status} {'CORRECT' if p['correct'] else 'INCORRECT'}\n\n")
    
    print(f"✓ Detailed results saved to {output_file}")

if __name__ == "__main__":
    backtest_last_season()

