#!/usr/bin/env python3
"""
Daily Odds Collection Script

This script is designed to run daily (via GitHub Actions or cron) to:
1. Fetch ALL games with betting odds from The Odds API (primary source)
2. Generate predictions using the hybrid model
3. Store predictions with Vegas lines for ATS tracking

Run this script BEFORE games start to capture pre-game lines.
"""
import os
import sys
from datetime import datetime, timedelta
from typing import Dict

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.odds_collector import get_odds_collector
from src.predictor import get_hybrid_predictor
from src.ats_tracker import get_ats_tracker
from src.data_collector import DataCollector
import config


def collect_odds_and_predictions(target_date: str = None):
    """
    Collect odds and generate predictions for a given date.
    
    Uses The Odds API as the PRIMARY source for games (more comprehensive),
    with ESPN as backup for additional game details.
    
    Args:
        target_date: Date string in YYYY-MM-DD format (defaults to today)
    """
    if target_date is None:
        target_date = datetime.now().strftime('%Y-%m-%d')
    
    print()
    print("=" * 80)
    print("DAILY ODDS COLLECTION & PREDICTION")
    print(f"Date: {target_date}")
    print("=" * 80)
    print()
    
    kenpom_ratings = DataCollector().get_kenpom_ratings()
    if not kenpom_ratings:
        print("⚠️  KenPom summary file not found; predictions will skip KenPom blending")
    
    # Initialize collectors
    odds_collector = get_odds_collector()
    ats_tracker = get_ats_tracker()
    
    # PRIMARY: Fetch all games with odds from The Odds API
    print("🎰 Fetching games from The Odds API (primary source)...")
    all_odds = odds_collector.get_ncaab_odds()
    
    if not all_odds:
        print("⚠️  No odds data available (API key not set or quota exceeded)")
        print("   Falling back to ESPN for game data...")
        return _collect_from_espn_fallback(target_date, ats_tracker)
    
    print(f"✓ Retrieved {len(all_odds)} games with betting lines")
    
    # Filter games for target date that HAVEN'T STARTED yet (pregame lines only)
    target_dt = datetime.strptime(target_date, '%Y-%m-%d')
    target_end = target_dt + timedelta(days=1)
    now = datetime.now()
    
    todays_games = []
    skipped_live = 0
    
    for game in all_odds:
        try:
            commence_time = datetime.fromisoformat(game['commence_time'].replace('Z', '+00:00'))
            game_start = commence_time.replace(tzinfo=None)
            
            # IMPORTANT: Skip games that have already started (would have live lines, not pregame)
            if game_start <= now:
                skipped_live += 1
                continue
            
            # Check if game is on target date
            if target_dt.date() <= game_start.date() <= target_end.date():
                todays_games.append(game)
        except (KeyError, ValueError):
            continue
    
    print(f"✓ Found {len(todays_games)} upcoming games for {target_date} (pregame lines)")
    if skipped_live > 0:
        print(f"  ⚠️  Skipped {skipped_live} games already in progress (live lines)")
    
    if not todays_games:
        print("ℹ️  No games with betting lines for this date")
        return {"success": True, "predictions": 0, "message": "No games for this date"}
    
    # Initialize predictor
    print("\n🤖 Initializing prediction model...")
    try:
        predictor = get_hybrid_predictor()
    except Exception as e:
        print(f"⚠️  Error initializing hybrid predictor: {e}")
        print("   Falling back to UKF-only predictions")
        from src.predictor import get_predictor
        predictor = get_predictor()
    
    # Process each game from Odds API
    predictions_stored = 0
    skipped_existing = 0
    
    print("\n" + "-" * 80)
    print(f"GENERATING PREDICTIONS FOR {len(todays_games)} GAMES")
    print("-" * 80 + "\n")
    
    for game_data in todays_games:
        home_team = game_data.get('home_team', '')
        away_team = game_data.get('away_team', '')
        game_id = game_data.get('id', f"{away_team}_{home_team}_{target_date}")
        commence_time = game_data.get('commence_time', '')
        
        if not home_team or not away_team:
            continue
        
        # Check if we already have a prediction for this game
        existing = ats_tracker.records.get(game_id)
        if existing and existing.has_vegas_line:
            skipped_existing += 1
            continue
        
        # Extract spread and total from odds data
        vegas_spread = None
        vegas_total = None
        
        bookmakers = game_data.get('bookmakers', [])
        if bookmakers:
            # Use first available bookmaker
            for bookmaker in bookmakers:
                markets = bookmaker.get('markets', [])
                for market in markets:
                    if market.get('key') == 'spreads':
                        outcomes = market.get('outcomes', [])
                        for outcome in outcomes:
                            # Find home team spread
                            if home_team.lower() in outcome.get('name', '').lower():
                                vegas_spread = float(outcome.get('point', 0))
                                break
                    elif market.get('key') == 'totals':
                        outcomes = market.get('outcomes', [])
                        for outcome in outcomes:
                            if outcome.get('name') == 'Over':
                                vegas_total = float(outcome.get('point', 0))
                                break
                if vegas_spread is not None:
                    break
        
        # Build a game dict compatible with predictor
        game_for_prediction = {
            'GameID': game_id,
            'HomeTeam': home_team,
            'AwayTeam': away_team,
            'HomeTeamID': abs(hash(home_team)) % 100000,
            'AwayTeamID': abs(hash(away_team)) % 100000,
            'DateTime': commence_time,
            'PointSpread': vegas_spread,
            'OverUnder': vegas_total
        }
        
        # Generate prediction
        try:
            prediction = predictor.predict_game(game_for_prediction)
            
            # Handle both UKF-only and hybrid predictors
            predicted_margin = prediction.get('hybrid_predicted_margin', prediction.get('predicted_margin', 0))
            predicted_total = prediction.get('hybrid_predicted_total', prediction.get('predicted_total', 140))
            confidence = prediction.get('overall_confidence', 50)
        except Exception as e:
            print(f"⚠️  Error predicting {away_team} @ {home_team}: {e}")
            continue
        
        # Store prediction with Vegas lines
        record = ats_tracker.store_prediction(
            game_id=game_id,
            game_date=target_date,
            home_team=home_team,
            away_team=away_team,
            home_team_id=game_for_prediction['HomeTeamID'],
            away_team_id=game_for_prediction['AwayTeamID'],
            predicted_margin=predicted_margin,
            predicted_total=predicted_total,
            prediction_confidence=confidence,
            vegas_spread=vegas_spread,
            vegas_total=vegas_total
        )
        
        predictions_stored += 1
        
        # Print prediction details
        spread_info = f"Line: {vegas_spread:+.1f}" if vegas_spread is not None else "No line"
        total_info = f"O/U: {vegas_total:.1f}" if vegas_total is not None else ""
        
        pick_emoji = "🏠" if record.spread_pick == "HOME" else "✈️"
        total_emoji = "📈" if record.total_pick == "OVER" else "📉" if record.total_pick == "UNDER" else ""
        
        edge = predicted_margin - (vegas_spread or 0)
        edge_str = f"Edge: {edge:+.1f}" if vegas_spread is not None else ""
        
        print(f"{pick_emoji} {away_team} @ {home_team}")
        print(f"   {spread_info} | {total_info}")
        print(f"   Model: {home_team} by {predicted_margin:+.1f} | {edge_str}")
        print(f"   Pick: {record.spread_pick} {total_emoji}{record.total_pick}")
        print()
    
    # Summary
    print("\n" + "=" * 80)
    print("COLLECTION SUMMARY")
    print("=" * 80)
    print(f"✓ Games available: {len(todays_games)}")
    print(f"✓ Predictions stored: {predictions_stored}")
    if skipped_existing > 0:
        print(f"✓ Skipped (already tracked): {skipped_existing}")
    
    # Count how many have Vegas lines
    games_with_lines = sum(1 for r in ats_tracker.records.values() 
                          if r.game_date == target_date and r.has_vegas_line)
    print(f"✓ Games with Vegas lines: {games_with_lines}")
    
    # Show current accuracy stats
    print("\n📊 CURRENT ACCURACY STATS:")
    summary = ats_tracker.get_accuracy_summary()
    all_time = summary["all_time"]
    
    if all_time["with_vegas_predictions"] > 0:
        print(f"   ATS (with Vegas): {all_time['with_vegas_spread_accuracy']*100:.1f}% ({all_time['with_vegas_predictions']} predictions)")
    if all_time["without_vegas_predictions"] > 0:
        print(f"   Straight-up: {all_time['without_vegas_accuracy']*100:.1f}% ({all_time['without_vegas_predictions']} predictions)")
    if all_time["combined_predictions"] > 0:
        print(f"   Combined: {all_time['combined_straight_up']*100:.1f}% ({all_time['combined_predictions']} total)")
    
    # Update README with new predictions
    try:
        from scripts.update_readme_accuracy import update_readme
        print("📝 Updating README with new predictions...")
        update_readme()
    except ImportError:
        # Fallback if running from scripts dir directly
        try:
            from update_readme_accuracy import update_readme
            print("📝 Updating README with new predictions...")
            update_readme()
        except ImportError as e:
            print(f"⚠️  Could not update README: {e}")
    
    print()
    
    return {
        "success": True,
        "predictions": predictions_stored,
        "games_available": len(todays_games),
        "with_vegas_lines": games_with_lines,
        "date": target_date
    }


def _collect_from_espn_fallback(target_date: str, ats_tracker) -> Dict:
    """
    Fallback to ESPN when Odds API is unavailable.
    Games collected this way won't have Vegas lines (straight-up only).
    """
    from src.espn_collector import get_espn_collector
    
    espn = get_espn_collector()
    target_datetime = datetime.strptime(target_date, '%Y-%m-%d')
    
    print(f"📅 Fetching games from ESPN for {target_date}...")
    games = espn.get_games_for_date(target_datetime)
    
    if not games:
        print("❌ No games found")
        return {"success": False, "error": "No games found", "predictions": 0}
    
    upcoming_games = [g for g in games if not g.get('IsClosed', False)]
    print(f"✓ Found {len(upcoming_games)} upcoming games (ESPN)")
    
    if not upcoming_games:
        return {"success": True, "predictions": 0, "message": "All games completed"}
    
    # Initialize predictor
    try:
        predictor = get_hybrid_predictor()
    except Exception as e:
        from src.predictor import get_predictor
        predictor = get_predictor()
    
    predictions_stored = 0
    
    for game in upcoming_games:
        game_id = str(game.get('GameID', ''))
        home_team = game.get('HomeTeam', '')
        away_team = game.get('AwayTeam', '')
        
        if not game_id or not home_team or not away_team:
            continue
        
        existing = ats_tracker.records.get(game_id)
        if existing:
            continue
        
        try:
            prediction = predictor.predict_game(game)
            predicted_margin = prediction.get('predicted_margin', 0)
            predicted_total = prediction.get('predicted_total', 140)
            confidence = prediction.get('overall_confidence', 50)
        except Exception as e:
            continue
        
        ats_tracker.store_prediction(
            game_id=game_id,
            game_date=target_date,
            home_team=home_team,
            away_team=away_team,
            home_team_id=game.get('HomeTeamID', 0),
            away_team_id=game.get('AwayTeamID', 0),
            predicted_margin=predicted_margin,
            predicted_total=predicted_total,
            prediction_confidence=confidence,
            vegas_spread=None,  # No Vegas line from ESPN fallback
            vegas_total=None
        )
        predictions_stored += 1
        print(f"✈️ {away_team} @ {home_team} - Predicted: {home_team} by {predicted_margin:+.1f} (no line)")
    
    print(f"\n✓ Stored {predictions_stored} predictions (without Vegas lines)")
    return {"success": True, "predictions": predictions_stored, "with_vegas_lines": 0}


def collect_upcoming_days(days: int = 3):
    """
    Collect odds for upcoming days.
    Useful for getting lines early when available.
    """
    results = []
    for i in range(days):
        target_date = (datetime.now() + timedelta(days=i)).strftime('%Y-%m-%d')
        result = collect_odds_and_predictions(target_date)
        results.append(result)
    return results


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Collect odds and generate predictions")
    parser.add_argument("--date", type=str, help="Target date (YYYY-MM-DD), defaults to today")
    parser.add_argument("--days", type=int, default=1, help="Number of days to collect (default: 1)")
    
    args = parser.parse_args()
    
    if args.days > 1:
        collect_upcoming_days(args.days)
    else:
        collect_odds_and_predictions(args.date)

