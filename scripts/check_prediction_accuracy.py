#!/usr/bin/env python3
"""
Check the accuracy of stored predictions against actual game results.
"""
import os
import sys
from datetime import datetime, timedelta

# Add parent directory to path so we can import from src
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.prediction_tracker import PredictionTracker


def main():
    print()
    print('='*80)
    print('COLLEGE BASKETBALL PREDICTION ACCURACY CHECKER')
    print(datetime.now().strftime('%A, %B %d, %Y'))
    print('='*80)
    print()

    tracker = PredictionTracker()

    # Check for unchecked predictions
    unchecked = tracker.list_unchecked_predictions()

    if unchecked:
        print(f'Found {len(unchecked)} predictions waiting for results:')
        print()

        for pred in unchecked:
            game_info = pred['game_info']
            prediction = pred['prediction']
            print(f"📅 {pred['date']}: {game_info['away_name']} @ {game_info['home_name']}")

            if prediction.get('covers_pick'):
                print(f"   Spread: {prediction['covers_pick']} ({prediction.get('covers_conf', 0):.0f}% confidence)")
            if prediction.get('total_pick'):
                print(f"   Total: {prediction['total_pick']} ({prediction.get('total_conf', 0):.0f}% confidence)")
            print()

        # Ask user which date to check
        if len(unchecked) > 0:
            print('Checking results for all unchecked predictions...')
            print()

            # Check results for each date that has unchecked predictions
            dates_to_check = set(pred['date'] for pred in unchecked)

            for check_date in sorted(dates_to_check):
                print(f'🔍 Checking results for {check_date}...')
                result = tracker.check_results_for_date(check_date)

                if 'error' in result:
                    print(f'   ❌ {result["error"]}')
                else:
                    display_accuracy_results(check_date, result)
                print()

    # Show overall accuracy report
    print('📊 OVERALL ACCURACY REPORT (Last 7 days)')
    print('='*50)

    overall_report = tracker.get_accuracy_report(days_back=7)

    if 'error' in overall_report:
        print(f'❌ {overall_report["error"]}')
    else:
        display_accuracy_results('Last 7 Days', overall_report)


def display_accuracy_results(date_label, results):
    """Display accuracy results in a nice format."""
    total_games = results['total_games']

    if total_games == 0:
        print(f'   No games found for {date_label}')
        return

    spread_acc = results['spread_accuracy'] * 100
    total_acc = results['total_accuracy'] * 100
    spread_weighted = results['spread_weighted_accuracy'] * 100
    total_weighted = results['total_weighted_accuracy'] * 100

    print(f'   📈 {date_label}: {total_games} games analyzed')
    print()
    print('   SPREAD ACCURACY:')
    print(f'   • Raw: {spread_acc:.1f}% ({sum(1 for r in results["results"] if r.get("spread_correct"))}/{total_games})')
    print(f'   • Confidence-weighted: {spread_weighted:.1f}%')
    print()
    print('   TOTAL ACCURACY:')
    print(f'   • Raw: {total_acc:.1f}% ({sum(1 for r in results["results"] if r.get("total_correct"))}/{total_games})')
    print(f'   • Confidence-weighted: {total_weighted:.1f}%')
    print()

    # Show individual results
    print('   INDIVIDUAL RESULTS:')
    for result in results['results']:
        game = result['game']
        spread_correct = result.get('spread_correct', False)
        total_correct = result.get('total_correct', False)

        spread_icon = '✅' if spread_correct else '❌'
        total_icon = '✅' if total_correct else '❌'

        spread_pick = result.get('spread_pick', 'None')
        total_pick = result.get('total_pick', 'None')

        print(f'   {spread_icon} {total_icon} {game}')
        print(f'      Score: {result["actual_score"]} (Total: {result["actual_total"]:.1f})')

        if spread_pick != 'None':
            print(f'      Spread: {spread_pick} vs {result["spread_line"]:+.1f} ({result.get("spread_confidence", 0):.0f}% conf)')
        if total_pick != 'None':
            print(f'      Total: {total_pick} vs {result["total_line"]:.1f} ({result.get("total_confidence", 0):.0f}% conf)')
        print()


if __name__ == '__main__':
    main()
