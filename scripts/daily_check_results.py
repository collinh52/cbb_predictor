#!/usr/bin/env python3
"""
Daily Results Checker Script

This script is designed to run daily (via GitHub Actions or cron) to:
1. Find predictions that haven't been checked yet
2. Fetch actual game results from ESPN
3. Calculate ATS accuracy for each prediction
4. Update accuracy statistics

Run this script AFTER games have completed.
"""
import os
import sys
from datetime import datetime, timedelta

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.espn_collector import get_espn_collector
from src.ats_tracker import get_ats_tracker


def check_results(days_back: int = 3):
    """
    Check results for unchecked predictions from recent days.
    
    Args:
        days_back: Number of days back to check (default: 3)
    """
    print()
    print("=" * 80)
    print("DAILY RESULTS CHECKER")
    print(f"Checking predictions from the last {days_back} days")
    print("=" * 80)
    print()
    
    espn = get_espn_collector()
    ats_tracker = get_ats_tracker()
    
    # Get unchecked predictions
    cutoff_date = datetime.now().strftime('%Y-%m-%d')
    unchecked = ats_tracker.get_unchecked_predictions(before_date=cutoff_date)
    
    if not unchecked:
        print("✓ No unchecked predictions found")
        return {"success": True, "checked": 0, "message": "No predictions to check"}
    
    print(f"📋 Found {len(unchecked)} unchecked predictions")
    
    # Group by date for efficient fetching
    predictions_by_date = {}
    for record in unchecked:
        date = record.game_date
        if date not in predictions_by_date:
            predictions_by_date[date] = []
        predictions_by_date[date].append(record)
    
    # Fetch ALL completed games (more comprehensive than scoreboard)
    print("\n" + "-" * 80)
    print("FETCHING ALL GAMES")
    print("-" * 80 + "\n")

    try:
        import config
        all_games = espn.get_all_games_via_team_schedules(config.CURRENT_SEASON)
        # Filter for completed games (have scores)
        completed_games = [g for g in all_games if
                        g.get('HomeTeamScore') is not None and
                        g.get('AwayTeamScore') is not None]
        print(f"✓ Found {len(completed_games)} completed games this season")
    except Exception as e:
        print(f"⚠️  Error fetching games: {e}")
        print("   Falling back to scoreboard method...")
        completed_games = []
        for date in sorted(predictions_by_date.keys()):
            try:
                date_dt = datetime.strptime(date, '%Y-%m-%d')
                games = espn.get_games_for_date(date_dt)
                completed_games.extend([g for g in games if
                                    g.get('HomeTeamScore') is not None and
                                    g.get('AwayTeamScore') is not None])
            except:
                continue

    # Create lookup by game ID and team IDs
    games_by_id = {str(g.get('GameID', '')): g for g in completed_games}
    games_by_teams = {}
    for g in completed_games:
        key = (g.get('HomeTeamID'), g.get('AwayTeamID'))
        games_by_teams[key] = g

    # Check results for each date
    results_checked = 0
    spread_correct = 0
    total_correct = 0

    print("\n" + "-" * 80)
    print("CHECKING RESULTS")
    print("-" * 80 + "\n")

    for date in sorted(predictions_by_date.keys()):
        predictions = predictions_by_date[date]
        print(f"📅 {date}: {len(predictions)} predictions to check")
        
        for record in predictions:
            game_id = record.game_id

            # Try to find matching game by ID first
            game = games_by_id.get(game_id)

            # Then try team IDs (works for games from Odds API)
            if not game:
                team_key = (record.home_team_id, record.away_team_id)
                game = games_by_teams.get(team_key)

            if not game:
                continue
            
            home_score = game.get('HomeTeamScore')
            away_score = game.get('AwayTeamScore')
            
            if home_score is None or away_score is None:
                continue
            
            # Record the result
            updated_record = ats_tracker.record_result(
                game_id=game_id,
                home_score=home_score,
                away_score=away_score
            )
            
            if updated_record:
                results_checked += 1
                
                # Determine correct/incorrect
                spread_icon = "✅" if updated_record.spread_correct else "❌"
                total_icon = ""
                if updated_record.total_correct is not None:
                    total_icon = "✅" if updated_record.total_correct else "❌"
                
                if updated_record.spread_correct:
                    spread_correct += 1
                if updated_record.total_correct:
                    total_correct += 1
                
                # Print result
                actual_margin = updated_record.actual_margin
                actual_total = updated_record.actual_total
                
                if updated_record.has_vegas_line:
                    line_info = f"Line: {updated_record.vegas_spread:+.1f}"
                    home_covered = updated_record.actual_margin + updated_record.vegas_spread > 0
                    covered = "COVERED" if ((home_covered and updated_record.spread_pick == "HOME") or
                                          (not home_covered and updated_record.spread_pick == "AWAY")) else "MISSED"
                else:
                    line_info = "No line"
                    covered = "CORRECT" if updated_record.spread_correct else "WRONG"
                
                print(f"   {spread_icon} {total_icon} {record.away_team} @ {record.home_team}")
                print(f"      Final: {away_score}-{home_score} (Margin: {actual_margin:+d}, Total: {actual_total})")
                print(f"      Predicted: {record.home_team} by {record.predicted_margin:+.1f}")
                print(f"      Pick: {record.spread_pick} - {covered} | {line_info}")
                print()
    
    # Print summary
    print("\n" + "=" * 80)
    print("RESULTS SUMMARY")
    print("=" * 80)
    
    if results_checked > 0:
        spread_accuracy = spread_correct / results_checked * 100
        print(f"✓ Results checked: {results_checked}")
        print(f"✓ Spread accuracy: {spread_accuracy:.1f}% ({spread_correct}/{results_checked})")
        
        if total_correct > 0:
            # Count predictions with total lines
            with_total = sum(1 for r in unchecked if r.has_vegas_line and r.vegas_total is not None)
            if with_total > 0:
                total_accuracy = total_correct / with_total * 100
                print(f"✓ Total accuracy: {total_accuracy:.1f}% ({total_correct}/{with_total})")
    else:
        print("ℹ️  No results checked (games may not be completed yet)")
    
    # Show updated overall accuracy
    print("\n📊 UPDATED ACCURACY STATS:")
    summary = ats_tracker.get_accuracy_summary()
    all_time = summary["all_time"]
    r7 = summary["rolling_7_day"]
    
    if all_time["with_vegas_predictions"] > 0:
        print(f"\n   WITH VEGAS LINES:")
        print(f"   • All-time ATS: {all_time['with_vegas_spread_accuracy']*100:.1f}%")
        print(f"   • 7-day ATS: {r7['with_vegas']['accuracy']*100:.1f}% ({r7['with_vegas']['spread_correct']}/{r7['with_vegas']['predictions']})")
    
    if all_time["without_vegas_predictions"] > 0:
        print(f"\n   WITHOUT VEGAS LINES (Straight-Up):")
        print(f"   • All-time: {all_time['without_vegas_accuracy']*100:.1f}%")
        print(f"   • 7-day: {r7['without_vegas']['accuracy']*100:.1f}% ({r7['without_vegas']['correct']}/{r7['without_vegas']['predictions']})")
    
    if all_time["combined_predictions"] > 0:
        print(f"\n   COMBINED:")
        print(f"   • Total predictions: {all_time['combined_predictions']}")
        print(f"   • Overall accuracy: {all_time['combined_straight_up']*100:.1f}%")
    
    print()
    
    return {
        "success": True,
        "checked": results_checked,
        "spread_correct": spread_correct,
        "spread_accuracy": spread_correct / results_checked if results_checked > 0 else 0,
        "summary": summary
    }


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Check results for predictions")
    parser.add_argument("--days", type=int, default=3, help="Days back to check (default: 3)")
    
    args = parser.parse_args()
    
    check_results(days_back=args.days)

