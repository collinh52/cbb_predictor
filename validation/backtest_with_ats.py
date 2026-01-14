"""
Enhanced Backtesting with ATS (Against The Spread) Tracking

This module provides backtesting capabilities that separately track:
1. Games WITH Vegas spread data - true ATS accuracy
2. Games WITHOUT spread data - implied spread (model margin) accuracy

Useful for understanding model performance in different contexts.
"""
import os
import sys
from datetime import datetime, timedelta
from collections import defaultdict
from typing import Dict, List, Tuple, Optional
import numpy as np

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.pop('DATABASE_URL', None)

from src.espn_collector import get_espn_collector

# Add scripts directory to path
scripts_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'scripts')
sys.path.insert(0, scripts_dir)
from show_team_ratings_v3 import calculate_team_ratings


class ATSBacktester:
    """
    Backtester that separately tracks ATS accuracy for games
    with and without Vegas spread data.
    """
    
    def __init__(self):
        self.espn = get_espn_collector()
        
        # Results storage
        self.results_with_spread = []
        self.results_without_spread = []
        self.all_predictions = []
    
    def run_backtest(self, season: int = 2025, training_ratio: float = 0.7) -> Dict:
        """
        Run backtest on a season with separate ATS tracking.
        
        Args:
            season: Season year to backtest
            training_ratio: Ratio of games to use for training (default 70%)
        
        Returns:
            Dictionary with comprehensive accuracy metrics
        """
        print("\n" + "=" * 100)
        print("BACKTESTING WITH ATS TRACKING")
        print(f"Season: {season}")
        print("=" * 100 + "\n")
        
        # Fetch season games
        print("Fetching season games from ESPN...")
        all_games = self.espn.get_all_games_via_team_schedules(season=season)
        
        # Filter completed games
        completed_games = [
            g for g in all_games
            if g.get('HomeTeamScore') is not None and g.get('AwayTeamScore') is not None
        ]
        
        # Parse dates
        for game in completed_games:
            try:
                game['date_obj'] = datetime.fromisoformat(game['DateTime'].replace('Z', '+00:00'))
            except:
                game['date_obj'] = datetime.now()
        
        completed_games.sort(key=lambda x: x['date_obj'])
        
        print(f"✓ Found {len(completed_games)} completed games")
        
        # Count games with spread data
        games_with_spread = [g for g in completed_games if g.get('PointSpread') is not None]
        print(f"✓ Games with Vegas spread data: {len(games_with_spread)}")
        print(f"✓ Games without spread data: {len(completed_games) - len(games_with_spread)}")
        
        if len(completed_games) < 100:
            print("⚠️  Warning: Not enough games for reliable backtesting")
            return {"error": "Insufficient games"}
        
        # Split into training and testing
        split_point = int(len(completed_games) * training_ratio)
        training_games = completed_games[:split_point]
        test_games = completed_games[split_point:]
        
        print(f"\n✓ Training set: {len(training_games)} games")
        print(f"✓ Test set: {len(test_games)} games")
        
        # Group test games by week
        weeks = defaultdict(list)
        for game in test_games:
            week_key = game['date_obj'].strftime('%Y-W%U')
            weeks[week_key].append(game)
        
        current_training_games = training_games.copy()
        
        print("\nRunning weekly predictions...")
        print("-" * 100)
        
        for week_num, (week_key, week_games) in enumerate(sorted(weeks.items()), 1):
            # Calculate ratings using games up to this week
            try:
                ratings_result = calculate_team_ratings(
                    current_training_games, min_games=5, use_sos_adjustment=True
                )
                if isinstance(ratings_result, tuple):
                    ratings, _ = ratings_result
                else:
                    ratings = ratings_result
                ratings_dict = {r['team_id']: r for r in ratings}
            except Exception as e:
                print(f"Error calculating ratings for week {week_key}: {e}")
                continue
            
            week_results = {'with_spread': [], 'without_spread': []}
            
            for game in week_games:
                home_id = game.get('HomeTeamID')
                away_id = game.get('AwayTeamID')
                home_score = game.get('HomeTeamScore')
                away_score = game.get('AwayTeamScore')
                vegas_spread = game.get('PointSpread')
                vegas_total = game.get('OverUnder')
                
                if not (home_id and away_id and home_score is not None and away_score is not None):
                    continue
                
                if home_id not in ratings_dict or away_id not in ratings_dict:
                    continue
                
                # Get ratings
                home_rating = ratings_dict[home_id]['overall_rating']
                away_rating = ratings_dict[away_id]['overall_rating']
                
                # Predicted margin (home team perspective)
                predicted_margin = home_rating - away_rating
                actual_margin = home_score - away_score
                actual_total = home_score + away_score
                
                # Create prediction record
                prediction = {
                    'date': game['date_obj'],
                    'home_team': game.get('HomeTeamName', 'Unknown'),
                    'away_team': game.get('AwayTeamName', 'Unknown'),
                    'home_id': home_id,
                    'away_id': away_id,
                    'predicted_margin': predicted_margin,
                    'actual_margin': actual_margin,
                    'actual_total': actual_total,
                    'home_rating': home_rating,
                    'away_rating': away_rating,
                    'vegas_spread': vegas_spread,
                    'vegas_total': vegas_total,
                    'has_vegas_line': vegas_spread is not None
                }
                
                # Determine winner prediction correctness
                predicted_home_wins = predicted_margin > 0
                actual_home_wins = actual_margin > 0
                winner_correct = predicted_home_wins == actual_home_wins
                prediction['winner_correct'] = winner_correct
                
                # Calculate ATS result if spread available
                if vegas_spread is not None:
                    # Home covers if actual margin beats the spread
                    home_covered = actual_margin > vegas_spread
                    
                    # Our pick: if predicted margin > spread, pick home
                    pick_home = predicted_margin > vegas_spread
                    ats_correct = pick_home == home_covered
                    
                    prediction['spread_pick'] = 'HOME' if pick_home else 'AWAY'
                    prediction['ats_correct'] = ats_correct
                    prediction['home_covered'] = home_covered
                    
                    # Over/under if available
                    if vegas_total is not None:
                        went_over = actual_total > vegas_total
                        # Simplified total prediction: use average pace * ratings
                        predicted_total = 140 + (home_rating + away_rating) / 10  # Rough estimate
                        pick_over = predicted_total > vegas_total
                        total_correct = pick_over == went_over
                        prediction['total_correct'] = total_correct
                        prediction['total_pick'] = 'OVER' if pick_over else 'UNDER'
                    
                    self.results_with_spread.append(prediction)
                    week_results['with_spread'].append(prediction)
                else:
                    # No spread - track implied spread (winner prediction)
                    prediction['ats_correct'] = winner_correct
                    self.results_without_spread.append(prediction)
                    week_results['without_spread'].append(prediction)
                
                self.all_predictions.append(prediction)
            
            # Print weekly results
            with_spread_correct = sum(1 for p in week_results['with_spread'] if p.get('ats_correct'))
            without_spread_correct = sum(1 for p in week_results['without_spread'] if p.get('ats_correct'))
            
            with_count = len(week_results['with_spread'])
            without_count = len(week_results['without_spread'])
            
            if with_count + without_count > 0:
                print(f"Week {week_num} ({week_key}):")
                if with_count > 0:
                    print(f"  With Vegas: {with_spread_correct}/{with_count} ATS ({with_spread_correct/with_count*100:.1f}%)")
                if without_count > 0:
                    print(f"  Without Vegas: {without_spread_correct}/{without_count} S/U ({without_spread_correct/without_count*100:.1f}%)")
            
            # Add week's games to training set
            current_training_games.extend(week_games)
        
        # Calculate final statistics
        return self._calculate_final_stats()
    
    def _calculate_final_stats(self) -> Dict:
        """Calculate comprehensive final statistics."""
        print("\n" + "=" * 100)
        print("BACKTESTING RESULTS - COMPREHENSIVE ATS ANALYSIS")
        print("=" * 100 + "\n")
        
        # WITH Vegas Lines (True ATS)
        if self.results_with_spread:
            ats_correct = sum(1 for p in self.results_with_spread if p.get('ats_correct'))
            ats_total = len(self.results_with_spread)
            ats_accuracy = ats_correct / ats_total
            
            total_correct = sum(1 for p in self.results_with_spread if p.get('total_correct'))
            total_count = sum(1 for p in self.results_with_spread if p.get('total_correct') is not None)
            total_accuracy = total_correct / total_count if total_count > 0 else 0
            
            print("📊 WITH VEGAS LINES (True ATS)")
            print("-" * 50)
            print(f"Total Predictions: {ats_total}")
            print(f"ATS Correct: {ats_correct}")
            print(f"**ATS Accuracy: {ats_accuracy*100:.2f}%**")
            if total_count > 0:
                print(f"Over/Under Accuracy: {total_accuracy*100:.2f}% ({total_correct}/{total_count})")
            print()
            
            # Breakdown by confidence
            high_conf = [p for p in self.results_with_spread 
                        if abs(p['predicted_margin'] - p['vegas_spread']) > 5]
            med_conf = [p for p in self.results_with_spread 
                       if 2 < abs(p['predicted_margin'] - p['vegas_spread']) <= 5]
            low_conf = [p for p in self.results_with_spread 
                       if abs(p['predicted_margin'] - p['vegas_spread']) <= 2]
            
            if high_conf:
                high_acc = sum(1 for p in high_conf if p.get('ats_correct')) / len(high_conf) * 100
                print(f"  High Edge (>5 pts vs line): {len(high_conf)} games, {high_acc:.1f}% ATS")
            if med_conf:
                med_acc = sum(1 for p in med_conf if p.get('ats_correct')) / len(med_conf) * 100
                print(f"  Medium Edge (2-5 pts): {len(med_conf)} games, {med_acc:.1f}% ATS")
            if low_conf:
                low_acc = sum(1 for p in low_conf if p.get('ats_correct')) / len(low_conf) * 100
                print(f"  Low Edge (<2 pts): {len(low_conf)} games, {low_acc:.1f}% ATS")
        else:
            ats_accuracy = 0
            print("📊 WITH VEGAS LINES: No games with spread data available")
        
        print()
        
        # WITHOUT Vegas Lines (Implied Spread / Straight-Up)
        if self.results_without_spread:
            su_correct = sum(1 for p in self.results_without_spread if p.get('ats_correct'))
            su_total = len(self.results_without_spread)
            su_accuracy = su_correct / su_total
            
            print("📊 WITHOUT VEGAS LINES (Straight-Up)")
            print("-" * 50)
            print(f"Total Predictions: {su_total}")
            print(f"Correct: {su_correct}")
            print(f"**Accuracy: {su_accuracy*100:.2f}%**")
            print()
            
            # Breakdown by predicted margin
            high_conf = [p for p in self.results_without_spread if abs(p['predicted_margin']) > 10]
            med_conf = [p for p in self.results_without_spread if 5 < abs(p['predicted_margin']) <= 10]
            low_conf = [p for p in self.results_without_spread if abs(p['predicted_margin']) <= 5]
            
            if high_conf:
                high_acc = sum(1 for p in high_conf if p.get('ats_correct')) / len(high_conf) * 100
                print(f"  High Confidence (>10 pts): {len(high_conf)} games, {high_acc:.1f}%")
            if med_conf:
                med_acc = sum(1 for p in med_conf if p.get('ats_correct')) / len(med_conf) * 100
                print(f"  Medium Confidence (5-10 pts): {len(med_conf)} games, {med_acc:.1f}%")
            if low_conf:
                low_acc = sum(1 for p in low_conf if p.get('ats_correct')) / len(low_conf) * 100
                print(f"  Low Confidence (<5 pts): {len(low_conf)} games, {low_acc:.1f}%")
        else:
            su_accuracy = 0
            print("📊 WITHOUT VEGAS LINES: No games without spread data")
        
        print()
        
        # Combined Statistics
        all_correct = sum(1 for p in self.all_predictions if p.get('winner_correct'))
        all_total = len(self.all_predictions)
        combined_accuracy = all_correct / all_total if all_total > 0 else 0
        
        print("📊 COMBINED (All Games - Winner Prediction)")
        print("-" * 50)
        print(f"Total Predictions: {all_total}")
        print(f"Winner Correct: {all_correct}")
        print(f"**Winner Accuracy: {combined_accuracy*100:.2f}%**")
        print()
        
        # Margin error analysis
        margins = [abs(p['predicted_margin'] - p['actual_margin']) for p in self.all_predictions]
        if margins:
            avg_margin_error = np.mean(margins)
            median_margin_error = np.median(margins)
            print(f"Average Margin Error: {avg_margin_error:.2f} points")
            print(f"Median Margin Error: {median_margin_error:.2f} points")
        
        print("\n" + "=" * 100)
        
        # Return comprehensive results
        return {
            "with_vegas_lines": {
                "total": len(self.results_with_spread),
                "ats_correct": sum(1 for p in self.results_with_spread if p.get('ats_correct')),
                "ats_accuracy": ats_accuracy if self.results_with_spread else None,
                "total_correct": sum(1 for p in self.results_with_spread if p.get('total_correct')),
                "results": self.results_with_spread
            },
            "without_vegas_lines": {
                "total": len(self.results_without_spread),
                "correct": sum(1 for p in self.results_without_spread if p.get('ats_correct')),
                "accuracy": su_accuracy if self.results_without_spread else None,
                "results": self.results_without_spread
            },
            "combined": {
                "total": all_total,
                "winner_correct": all_correct,
                "winner_accuracy": combined_accuracy,
                "avg_margin_error": np.mean(margins) if margins else None,
                "median_margin_error": np.median(margins) if margins else None
            }
        }
    
    def save_results(self, filename: str = "backtest_ats_results.txt"):
        """Save detailed results to file."""
        output_dir = os.path.dirname(os.path.abspath(__file__))
        output_path = os.path.join(output_dir, filename)
        
        with open(output_path, 'w') as f:
            f.write("=" * 100 + "\n")
            f.write("BACKTESTING RESULTS WITH ATS TRACKING\n")
            f.write("=" * 100 + "\n\n")
            
            # Summary
            if self.results_with_spread:
                ats_correct = sum(1 for p in self.results_with_spread if p.get('ats_correct'))
                f.write(f"WITH VEGAS LINES: {ats_correct}/{len(self.results_with_spread)} ATS ")
                f.write(f"({ats_correct/len(self.results_with_spread)*100:.1f}%)\n")
            
            if self.results_without_spread:
                su_correct = sum(1 for p in self.results_without_spread if p.get('ats_correct'))
                f.write(f"WITHOUT VEGAS LINES: {su_correct}/{len(self.results_without_spread)} ")
                f.write(f"({su_correct/len(self.results_without_spread)*100:.1f}%)\n")
            
            f.write("\n" + "-" * 100 + "\n")
            f.write("DETAILED PREDICTIONS (WITH VEGAS LINES)\n")
            f.write("-" * 100 + "\n\n")
            
            for i, p in enumerate(self.results_with_spread[:100], 1):  # Limit to first 100
                status = "✓" if p.get('ats_correct') else "✗"
                f.write(f"{i}. {p['date'].strftime('%Y-%m-%d')} - {p['away_team']} @ {p['home_team']}\n")
                f.write(f"   Vegas Spread: {p['vegas_spread']:+.1f}\n")
                f.write(f"   Our Edge: {p['predicted_margin'] - p['vegas_spread']:+.1f}\n")
                f.write(f"   Pick: {p.get('spread_pick', 'N/A')}\n")
                f.write(f"   Actual: {p['actual_margin']:+d}\n")
                f.write(f"   Result: {status}\n\n")
        
        print(f"\n✓ Detailed results saved to {output_path}")


def run_ats_backtest():
    """Main function to run ATS backtest."""
    backtester = ATSBacktester()
    results = backtester.run_backtest(season=2025)
    backtester.save_results()
    return results


if __name__ == "__main__":
    run_ats_backtest()

