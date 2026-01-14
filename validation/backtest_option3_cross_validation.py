"""
OPTION 3: K-Fold Cross-Validation (Most Rigorous)
Multiple train/test splits with confidence intervals.
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

def backtest_cross_validation(k_folds=5):
    """
    K-fold cross-validation:
    - Split games into K folds chronologically
    - For each fold: train on other K-1 folds, test on that fold
    - Average accuracy across all folds
    - Provides confidence intervals
    """
    print("\n" + "="*100)
    print(f"OPTION 3: {k_folds}-FOLD CROSS-VALIDATION (MOST RIGOROUS)")
    print("="*100 + "\n")
    
    espn = get_espn_collector()
    
    # Fetch current season games (can also use last season)
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
    
    if len(completed_games) < 500:
        print(f"⚠️  Warning: Only {len(completed_games)} games available")
        print("   Cross-validation works best with 500+ games")
        print("   Results may have high variance")
    
    print()
    
    # Split into K folds (chronologically)
    fold_size = len(completed_games) // k_folds
    folds = []
    
    for i in range(k_folds):
        start_idx = i * fold_size
        end_idx = start_idx + fold_size if i < k_folds - 1 else len(completed_games)
        folds.append(completed_games[start_idx:end_idx])
        
        fold_start = completed_games[start_idx]['date_obj'].strftime('%Y-%m-%d')
        fold_end = completed_games[end_idx-1]['date_obj'].strftime('%Y-%m-%d')
        print(f"Fold {i+1}: {len(folds[i])} games ({fold_start} to {fold_end})")
    
    print()
    
    # Run cross-validation
    fold_accuracies = []
    fold_predictions = []
    
    for fold_num in range(k_folds):
        print(f"\n{'='*100}")
        print(f"FOLD {fold_num + 1}/{k_folds}")
        print('='*100)
        
        # Create train/test split
        test_fold = folds[fold_num]
        train_folds = [game for i, fold in enumerate(folds) if i != fold_num for game in fold]
        
        print(f"Training games: {len(train_folds)}")
        print(f"Test games: {len(test_fold)}")
        
        # Build ratings on training data
        try:
            ratings_result = calculate_team_ratings(train_folds, min_games=5, use_sos_adjustment=True)
            # Handle both old format (list) and new format (tuple)
            if isinstance(ratings_result, tuple):
                ratings, neutral_stats = ratings_result
            else:
                ratings = ratings_result
            ratings_dict = {r['team_id']: r for r in ratings}
            print(f"✓ Built ratings for {len(ratings)} teams")
        except Exception as e:
            print(f"✗ Error calculating ratings: {e}")
            continue
        
        # Test on this fold
        correct = 0
        total = 0
        predictions = []
        
        for game in test_fold:
            home_id = game.get('HomeTeamID')
            away_id = game.get('AwayTeamID')
            home_score = game.get('HomeTeamScore')
            away_score = game.get('AwayTeamScore')
            
            if not (home_id and away_id and home_score is not None and away_score is not None):
                continue
            
            if home_id not in ratings_dict or away_id not in ratings_dict:
                continue
            
            # Predict
            home_rating = ratings_dict[home_id]['overall_rating']
            away_rating = ratings_dict[away_id]['overall_rating']
            predicted_margin = home_rating - away_rating
            actual_margin = home_score - away_score
            
            predicted_winner = "HOME" if predicted_margin > 0 else "AWAY"
            actual_winner = "HOME" if actual_margin > 0 else "AWAY"
            is_correct = predicted_winner == actual_winner
            
            if is_correct:
                correct += 1
            total += 1
            
            predictions.append({
                'fold': fold_num + 1,
                'date': game['date_obj'],
                'home_team': game.get('HomeTeamName', 'Unknown'),
                'away_team': game.get('AwayTeamName', 'Unknown'),
                'predicted_margin': predicted_margin,
                'actual_margin': actual_margin,
                'correct': is_correct
            })
        
        if total > 0:
            fold_accuracy = (correct / total) * 100
            fold_accuracies.append(fold_accuracy)
            fold_predictions.extend(predictions)
            
            print(f"\nFold {fold_num + 1} Results:")
            print(f"  Correct: {correct}/{total}")
            print(f"  Accuracy: {fold_accuracy:.2f}%")
        else:
            print(f"\nFold {fold_num + 1}: No valid predictions")
    
    # Calculate overall statistics
    print("\n" + "="*100)
    print("CROSS-VALIDATION SUMMARY")
    print("="*100 + "\n")
    
    if fold_accuracies:
        mean_accuracy = np.mean(fold_accuracies)
        std_accuracy = np.std(fold_accuracies)
        min_accuracy = np.min(fold_accuracies)
        max_accuracy = np.max(fold_accuracies)
        
        # 95% confidence interval
        confidence_interval = 1.96 * (std_accuracy / np.sqrt(len(fold_accuracies)))
        
        print(f"Accuracies across {len(fold_accuracies)} folds:")
        for i, acc in enumerate(fold_accuracies, 1):
            print(f"  Fold {i}: {acc:.2f}%")
        
        print()
        print(f"**Mean Accuracy: {mean_accuracy:.2f}%**")
        print(f"Standard Deviation: {std_accuracy:.2f}%")
        print(f"95% Confidence Interval: [{mean_accuracy - confidence_interval:.2f}%, {mean_accuracy + confidence_interval:.2f}%]")
        print(f"Min Accuracy: {min_accuracy:.2f}%")
        print(f"Max Accuracy: {max_accuracy:.2f}%")
        print()
        
        # Overall statistics across all folds
        all_correct = sum(1 for p in fold_predictions if p['correct'])
        all_total = len(fold_predictions)
        overall_accuracy = (all_correct / all_total) * 100 if all_total > 0 else 0
        
        print(f"Overall Results (all folds combined):")
        print(f"  Total Predictions: {all_total}")
        print(f"  Correct: {all_correct}")
        print(f"  Accuracy: {overall_accuracy:.2f}%")
        print()
        
        # Margin analysis
        margins = [abs(p['predicted_margin'] - p['actual_margin']) for p in fold_predictions]
        print(f"Margin Error Statistics:")
        print(f"  Mean Absolute Error: {np.mean(margins):.2f} points")
        print(f"  Median Absolute Error: {np.median(margins):.2f} points")
        print(f"  Std Dev: {np.std(margins):.2f} points")
        print()
        
        # Statistical significance test
        print("STATISTICAL ANALYSIS:")
        print(f"  Null Hypothesis: Accuracy = 50% (random guessing)")
        
        # Simple z-test
        p_null = 0.50
        p_observed = overall_accuracy / 100
        n = all_total
        z_score = (p_observed - p_null) / np.sqrt(p_null * (1 - p_null) / n)
        
        print(f"  Z-score: {z_score:.2f}")
        if z_score > 1.96:
            print(f"  Result: ✓ Significantly better than random (p < 0.05)")
        elif z_score > 1.645:
            print(f"  Result: ~ Marginally better than random (p < 0.10)")
        else:
            print(f"  Result: ✗ Not significantly different from random")
        
        print()
        print("="*100)
        
        # Save results
        save_results(fold_predictions, fold_accuracies, mean_accuracy, std_accuracy, confidence_interval)
        
    else:
        print("⚠️  No fold produced valid predictions")

def save_results(predictions, fold_accuracies, mean_acc, std_acc, ci):
    """Save detailed cross-validation results."""
    output_file = "backtest_results_option3_cross_validation.txt"
    
    with open(output_file, 'w') as f:
        f.write("="*100 + "\n")
        f.write("CROSS-VALIDATION RESULTS\n")
        f.write("="*100 + "\n\n")
        
        f.write(f"Number of Folds: {len(fold_accuracies)}\n")
        f.write(f"Mean Accuracy: {mean_acc:.2f}%\n")
        f.write(f"Standard Deviation: {std_acc:.2f}%\n")
        f.write(f"95% Confidence Interval: [{mean_acc - ci:.2f}%, {mean_acc + ci:.2f}%]\n\n")
        
        f.write("FOLD ACCURACIES:\n")
        for i, acc in enumerate(fold_accuracies, 1):
            f.write(f"  Fold {i}: {acc:.2f}%\n")
        
        f.write("\n" + "="*100 + "\n")
        f.write("DETAILED PREDICTIONS (all folds):\n")
        f.write("-"*100 + "\n\n")
        
        # Sort by date
        predictions.sort(key=lambda p: p['date'])
        
        for i, p in enumerate(predictions, 1):
            status = "✓" if p['correct'] else "✗"
            f.write(f"{i}. [Fold {p['fold']}] {p['date'].strftime('%Y-%m-%d')} - ")
            f.write(f"{p['away_team']} @ {p['home_team']}\n")
            f.write(f"   Predicted margin: {p['predicted_margin']:+.1f}\n")
            f.write(f"   Actual margin: {p['actual_margin']:+.1f}\n")
            f.write(f"   Error: {abs(p['predicted_margin'] - p['actual_margin']):.1f} pts\n")
            f.write(f"   {status} {'CORRECT' if p['correct'] else 'INCORRECT'}\n\n")
    
    print(f"✓ Detailed results saved to {output_file}")

if __name__ == "__main__":
    backtest_cross_validation(k_folds=5)

