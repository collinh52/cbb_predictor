"""
Generate predictions for today's games using ESPN historical data and The Odds API betting lines.
Uses Phase 2.5 enhancements: Fixed HCA + Consistency-adjusted confidence
"""
import os
import sys

# Add parent directory to path so we can import from src
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.pop('DATABASE_URL', None)

import config
import numpy as np
from src.espn_collector import get_espn_collector
from src.odds_collector import get_odds_collector
from src.team_name_mapping import get_odds_api_name
from src.prediction_tracker import PredictionTracker
from datetime import datetime, timedelta
from collections import defaultdict

# Import Phase 3A rating calculation (with Road Warrior Bonus)
from show_team_ratings_v3 import calculate_team_ratings as calculate_ratings_v3

def calculate_team_ratings(games: list, min_games: int = 5) -> dict:
    """
    Calculate simple team ratings from recent games.
    
    Args:
        games: List of completed games
        min_games: Minimum games required (filters out non-D1 teams)
    """
    team_stats = defaultdict(lambda: {'points_for': [], 'points_against': [], 'games': 0})
    
    for game in games:
        home_id = game.get('HomeTeamID')
        away_id = game.get('AwayTeamID')
        home_score = game.get('HomeTeamScore')
        away_score = game.get('AwayTeamScore')
        
        if home_id and away_id and home_score is not None and away_score is not None:
            team_stats[home_id]['points_for'].append(home_score)
            team_stats[home_id]['points_against'].append(away_score)
            team_stats[home_id]['games'] += 1
            
            team_stats[away_id]['points_for'].append(away_score)
            team_stats[away_id]['points_against'].append(home_score)
            team_stats[away_id]['games'] += 1
    
    # Calculate ratings (only include teams with enough games)
    ratings = {}
    for team_id, stats in team_stats.items():
        if stats['games'] >= min_games:
            off_rating = sum(stats['points_for']) / stats['games']
            def_rating = sum(stats['points_against']) / stats['games']
            ratings[team_id] = {
                'offensive': off_rating,
                'defensive': def_rating,
                'games': stats['games']
            }
    
    return ratings

def predict_game(home_id, away_id, home_abbr, away_abbr, spread, total, ratings):
    """
    Generate prediction with Phase 2.5 enhancements:
    - Uses opponent-adjusted HCA
    - Adjusts confidence based on team consistency
    - Properly converts tempo-free efficiency ratings to expected scores
    """
    # Get Phase 2.5 ratings (with offensive_rating, defensive_rating, hca, consistency_score)
    # Note: offensive_rating and defensive_rating are PER-100-POSSESSION efficiency ratings
    default_rating = {
        'offensive_rating': 52.5,  # League average efficiency
        'defensive_rating': 52.5, 
        'games': 0, 
        'consistency_score': 50,
        'hca': 3.5
    }
    home_rating = ratings.get(home_id, default_rating)
    away_rating = ratings.get(away_id, default_rating)
    
    # Get efficiency ratings (per 100 possessions)
    home_off_eff = home_rating.get('offensive_rating', 52.5)
    home_def_eff = home_rating.get('defensive_rating', 52.5)
    away_off_eff = away_rating.get('offensive_rating', 52.5)
    away_def_eff = away_rating.get('defensive_rating', 52.5)
    
    # Use team-specific HCA
    home_hca = home_rating.get('hca', 3.5)
    
    # Calculate matchup pace (Total Possessions per Game)
    # Average pace is ~144 total possessions
    home_pace = home_rating.get('pace', 144.0)
    away_pace = away_rating.get('pace', 144.0)
    matchup_pace = (home_pace + away_pace) / 2
    
    # Calculate expected efficiency for each team in this matchup (Points per 100 Total Possessions)
    # Home offense vs Away defense: blend the two efficiencies
    home_expected_eff = (home_off_eff + away_def_eff) / 2
    away_expected_eff = (away_off_eff + home_def_eff) / 2
    
    # Convert efficiency to expected points based on matchup pace
    pred_home = (home_expected_eff / 100) * matchup_pace + home_hca
    pred_away = (away_expected_eff / 100) * matchup_pace
    
    pred_margin = pred_home - pred_away
    pred_total = pred_home + pred_away
    
    # Compare to spread
    # IMPORTANT: Spread is always from HOME team's perspective
    # If spread = -7.0, home is favorite (needs to win by >7 to cover)
    # If spread = +6.0, home is underdog (covers if they lose by <6 or win)
    covers_pick = None
    covers_conf = 50
    if spread is not None:
        # pred_margin > 0 means home wins, < 0 means away wins
        # spread < 0 means home is favorite, > 0 means home is underdog
        
        # The key insight: 
        # Home covers if: (pred_margin + spread) > 0
        # This accounts for the spread adjustment
        
        # Example 1: MSU -7.0, pred_margin = +10
        #   → 10 + (-7) = +3 > 0, MSU covers ✓
        # Example 2: MSU -7.0, pred_margin = +3
        #   → 3 + (-7) = -4 < 0, IU covers ✓
        # Example 3: MSST +6.0, pred_margin = -2.8 (ALA wins by 2.8)
        #   → -2.8 + 6 = +3.2 > 0, MSST covers ✓
        
        # Calculate if home covers: (actual_margin + spread) > 0
        # This gives us the "effective margin" after applying the spread
        home_covers_by = pred_margin + spread
        
        diff = abs(home_covers_by)
        base_conf = min(100, 50 + diff * 5)  # Base confidence from margin
        
        # PHASE 2.5: Adjust confidence based on team consistency
        # Average the consistency of both teams
        home_consistency = home_rating.get('consistency_score', 50)
        away_consistency = away_rating.get('consistency_score', 50)
        avg_consistency = (home_consistency + away_consistency) / 2
        
        # Scale confidence: High consistency (80+) = full confidence
        #                   Medium consistency (50) = 85% of base confidence
        #                   Low consistency (20) = 70% of base confidence
        consistency_multiplier = 0.7 + (avg_consistency / 100) * 0.3
        covers_conf = base_conf * consistency_multiplier
        
        # Determine who covers (with 1pt buffer for pushes)
        if home_covers_by > 1:
            # Home team covers the spread
            covers_pick = f'{home_abbr} to COVER ({home_abbr} {spread:+.1f})'
        elif home_covers_by < -1:
            # Away team covers the spread  
            covers_pick = f'{away_abbr} to COVER ({home_abbr} {spread:+.1f})'
        else:
            covers_pick = 'No strong pick (too close to spread)'
            covers_conf = 50 * consistency_multiplier  # Low confidence on close calls
    
    # Compare to total
    total_pick = None
    total_conf = 50
    if total is not None:
        diff = abs(pred_total - total)
        base_total_conf = min(100, 50 + diff * 2)  # Base confidence from difference
        
        # PHASE 2.5: Adjust total confidence based on consistency too
        home_consistency = home_rating.get('consistency_score', 50)
        away_consistency = away_rating.get('consistency_score', 50)
        avg_consistency = (home_consistency + away_consistency) / 2
        consistency_multiplier = 0.7 + (avg_consistency / 100) * 0.3
        total_conf = base_total_conf * consistency_multiplier
        
        if pred_total > total + 3:
            total_pick = f'OVER {total:.1f}'
        elif pred_total < total - 3:
            total_pick = f'UNDER {total:.1f}'
        else:
            total_pick = 'No strong pick (too close)'
            total_conf = 50 * consistency_multiplier
    
    return {
        'pred_home': pred_home,
        'pred_away': pred_away,
        'pred_margin': pred_margin,
        'pred_total': pred_total,
        'covers_pick': covers_pick,
        'covers_conf': covers_conf,
        'total_pick': total_pick,
        'total_conf': total_conf,
        'home_games': home_rating.get('games', 0),
        'away_games': away_rating.get('games', 0),
        'home_consistency': home_rating.get('consistency_score', 50),
        'away_consistency': away_rating.get('consistency_score', 50),
        'avg_consistency': avg_consistency,
        'home_hca': home_rating.get('hca', 3.5)
    }

def main():
    print()
    print('='*80)
    print('COLLEGE BASKETBALL PREDICTIONS FOR TODAY (Phase 3D)')
    print(datetime.now().strftime('%A, %B %d, %Y'))
    print('='*80)
    print()
    
    # Get historical games from ESPN for the full season (using team schedules)
    print('Fetching ALL games from ESPN for the 2025-26 season...')
    print('(Using team schedules for comprehensive data - this will take 1-2 minutes)')
    espn = get_espn_collector()
    
    # Fetch full season data via team schedules
    all_games = espn.get_all_games_via_team_schedules(season=config.CURRENT_SEASON)
    historical_games = [g for g in all_games if g.get('HomeTeamScore') is not None and g.get('AwayTeamScore') is not None]
    
    print(f'✓ Found {len(historical_games)} completed games for 2025-26 season')
    print()

    # Initialize prediction tracker
    tracker = PredictionTracker()
    print('✓ Initialized prediction tracking system')
    print()

    # Calculate team ratings using Phase 3D (all enhancements)
    print('Calculating team ratings with Phase 3D enhancements...')
    print('  ✓ FIXED HCA: Opponent-adjusted Home Court Advantage (0-4 range, scaled for realism)')
    print('  ✓ ROAD WARRIOR BONUS: Teams with better road performance get 0-3 point rating boost')
    print('  ✓ ENHANCED NEUTRAL COURT DETECTION: Multi-method detection system')
    print('  ✓ PACE ADJUSTMENT: Tempo-free ratings (points per 100 possessions)')
    print('  ✓ PYTHAGOREAN EXPECTATION: Identifies lucky 🍀 vs unlucky 😰 teams with regression')
    print('  ✓ Variance/consistency metrics (affects prediction CONFIDENCE, not ranking)')
    ratings_result = calculate_ratings_v3(historical_games, min_games=5, use_sos_adjustment=True)
    
    # Handle tuple return (ratings_list, neutral_stats)
    if isinstance(ratings_result, tuple):
        ratings_list, neutral_stats = ratings_result
    else:
        ratings_list = ratings_result
    
    # Convert list to dict for easy lookup (by ID and by name)
    ratings = {team['team_id']: team for team in ratings_list}
    
    # Also create name-based lookup for matching Odds API teams
    # Multiple lookup methods: full name, first word, abbreviation
    ratings_by_name = {}
    for team in ratings_list:
        name = team.get('team_name', '').lower()
        abbr = team.get('team_abbr', '').lower()
        
        # Store by full name
        ratings_by_name[name] = team
        # Store by abbreviation
        if abbr:
            ratings_by_name[abbr] = team
        # Store by first word of name (e.g., "syracuse" from "Syracuse Orange")
        if name:
            first_word = name.split()[0]
            if first_word not in ratings_by_name:  # Don't overwrite more specific matches
                ratings_by_name[first_word] = team
    
    print(f'✓ Calculated Phase 3D ratings for {len(ratings)} teams')
    print()
    
    # Get ALL upcoming games from The Odds API (primary source - more comprehensive)
    print("Fetching ALL upcoming games from The Odds API (primary source)...")
    odds_collector = get_odds_collector()
    all_odds = odds_collector.get_ncaab_odds()
    print(f'✓ Found {len(all_odds)} games with betting lines')
    print()
    
    # Filter to UPCOMING games only (not started yet) - avoids live betting lines
    now = datetime.now()
    tomorrow_end = now + timedelta(days=2)
    
    upcoming_games = []
    skipped_live = 0
    
    for odds_game in all_odds:
        try:
            commence_time = datetime.fromisoformat(odds_game['commence_time'].replace('Z', '+00:00'))
            game_start = commence_time.replace(tzinfo=None)
            
            # IMPORTANT: Only include games that HAVEN'T STARTED YET
            # This ensures we get pregame lines, not live betting lines
            if game_start <= now:
                skipped_live += 1
                continue  # Skip games that have already started
            
            # Only include games within the next 2 days
            if game_start > tomorrow_end:
                continue
            
            # Convert Odds API format to our standard game format
            home_team = odds_game.get('home_team', '')
            away_team = odds_game.get('away_team', '')
            
            # Extract spread and total from bookmakers
            spread = None
            total = None
            bookmakers = odds_game.get('bookmakers', [])
            for bookmaker in bookmakers:
                markets = bookmaker.get('markets', [])
                for market in markets:
                    if market['key'] == 'spreads':
                        for outcome in market.get('outcomes', []):
                            if outcome['name'] == home_team:
                                spread = outcome.get('point')
                    elif market['key'] == 'totals':
                        for outcome in market.get('outcomes', []):
                            if outcome['name'] == 'Over':
                                total = outcome.get('point')
                if spread is not None:
                    break
            
            # Create game dict compatible with our system
            game = {
                'GameID': odds_game.get('id', f"{away_team}_{home_team}"),
                'HomeTeam': home_team.split()[-1] if home_team else '',  # Last word as abbr
                'AwayTeam': away_team.split()[-1] if away_team else '',
                'HomeTeamName': home_team,
                'AwayTeamName': away_team,
                'HomeTeamID': abs(hash(home_team)) % 100000,
                'AwayTeamID': abs(hash(away_team)) % 100000,
                'DateTime': odds_game.get('commence_time'),
                'date': odds_game.get('commence_time', ''),
                'PointSpread': spread,
                'OverUnder': total
            }
            upcoming_games.append(game)
        except (KeyError, ValueError):
            continue
    
    print(f'✓ Found {len(upcoming_games)} upcoming games (pregame lines only)')
    if skipped_live > 0:
        print(f'  ⚠️  Skipped {skipped_live} games already in progress (live lines)')
    print()
    
    # Helper function to find team rating by name
    def find_rating_by_name(team_name: str) -> dict:
        """Find team rating using various name matching strategies."""
        if not team_name:
            return None
        
        name_lower = team_name.lower()
        
        # Try exact match first
        if name_lower in ratings_by_name:
            return ratings_by_name[name_lower]
        
        # Try first word (e.g., "Syracuse" from "Syracuse Orange")
        first_word = name_lower.split()[0]
        if first_word in ratings_by_name:
            return ratings_by_name[first_word]
        
        # Try last word (e.g., "Orange" from "Syracuse Orange")
        last_word = name_lower.split()[-1]
        if last_word in ratings_by_name:
            return ratings_by_name[last_word]
        
        # Try partial matching - find any key that contains the first word
        for key, rating in ratings_by_name.items():
            if first_word in key or key in name_lower:
                return rating
        
        return None
    
    # Generate predictions (all games from Odds API have lines)
    print('\n' + '='*80)
    print('PREDICTIONS')
    print('='*80)
    print()
    
    games_with_odds = [g for g in upcoming_games if g.get('PointSpread') is not None]
    teams_matched = 0
    teams_unmatched = 0
    
    for i, game in enumerate(games_with_odds, 1):
        home_name = game.get('HomeTeamName', 'Unknown')
        away_name = game.get('AwayTeamName', 'Unknown')
        
        # Look up ratings by team name instead of ID
        home_rating_data = find_rating_by_name(home_name)
        away_rating_data = find_rating_by_name(away_name)
        
        # Get team IDs from the matched ratings (or use hash if not found)
        if home_rating_data:
            home_id = home_rating_data['team_id']
            teams_matched += 1
        else:
            home_id = abs(hash(home_name)) % 100000
            teams_unmatched += 1
            
        if away_rating_data:
            away_id = away_rating_data['team_id']
            teams_matched += 1
        else:
            away_id = abs(hash(away_name)) % 100000
            teams_unmatched += 1
        home_abbr = game.get('HomeTeam', '')
        away_abbr = game.get('AwayTeam', '')
        spread = game.get('PointSpread')
        total = game.get('OverUnder')
        
        pred = predict_game(home_id, away_id, home_abbr, away_abbr, spread, total, ratings)

        # Store prediction for tracking
        game_info = {
            'home_team': home_abbr,
            'away_team': away_abbr,
            'home_name': home_name,
            'away_name': away_name,
            'date': game.get('date', datetime.now().strftime('%Y-%m-%d')),
            'spread': spread,
            'total': total
        }
        tracker.store_prediction(game_info, pred)

        print(f'{i}. {away_name} @ {home_name}')
        game_time = game.get('date', 'TBD')
        print(f'   Time: {game_time[:16] if len(game_time) > 16 else game_time}')
        print()
        print(f'   BETTING LINES:')
        if spread is not None:
            print(f'   Spread: {home_abbr} {spread:+.1f}')
        if total is not None:
            print(f'   Total: {total:.1f}')
        print()
        home_games = pred['home_games']
        away_games = pred['away_games']
        pred_away_score = pred['pred_away']
        pred_home_score = pred['pred_home']
        pred_margin_val = pred['pred_margin']
        pred_total_val = pred['pred_total']
        
        print(f'   MODEL PREDICTIONS (Phase 3C, based on {home_games}/{away_games} games):')
        print(f'   Predicted Score: {away_abbr} {pred_away_score:.1f}, {home_abbr} {pred_home_score:.1f}')
        print(f'   Predicted Margin: {home_abbr} {pred_margin_val:+.1f}')
        print(f'   Predicted Total: {pred_total_val:.1f}')
        print(f'   Team HCA: {home_abbr} +{pred.get("home_hca", 3.5):.1f} pts (opponent-adjusted)')
        print(f'   Consistency: {home_abbr} {pred.get("home_consistency", 50):.0f}/100, '
              f'{away_abbr} {pred.get("away_consistency", 50):.0f}/100')
        print()
        
        if pred['covers_pick']:
            covers_pick_str = pred['covers_pick']
            covers_conf_val = pred['covers_conf']
            print(f'   SPREAD PICK: {covers_pick_str} (Confidence: {covers_conf_val:.0f}%)')
        if pred['total_pick']:
            total_pick_str = pred['total_pick']
            total_conf_val = pred['total_conf']
            print(f'   TOTAL PICK: {total_pick_str} (Confidence: {total_conf_val:.0f}%)')
        
        print()
        print('-'*80)
        print()
    
    if not games_with_odds:
        print('No games with betting lines available.')
    
    print(f'Showing all {len(games_with_odds)} games with betting lines')
    print()
    print('='*80)
    print('PREDICTION SUMMARY')
    print('='*80)
    print()
    print(f'✓ Analyzed {len(historical_games)} completed games from 2025-26 season')
    print(f'✓ Calculated ratings for {len(ratings)} teams')
    print(f'✓ Generated predictions for {len(games_with_odds)} games with betting lines')
    print(f'✓ Team matching: {teams_matched} matched, {teams_unmatched} unmatched')
    print(f'✓ Stored predictions for accuracy tracking')
    print()

    # Show recent accuracy if available
    print('📊 RECENT ACCURACY (Last 7 days):')
    try:
        recent_accuracy = tracker.get_accuracy_report(days_back=7)
        if 'error' not in recent_accuracy and recent_accuracy['total_games'] > 0:
            spread_acc = recent_accuracy['spread_accuracy'] * 100
            total_acc = recent_accuracy['total_accuracy'] * 100
            print(f'   Spread: {spread_acc:.1f}% ({recent_accuracy["total_games"]} games)')
            print(f'   Total:  {total_acc:.1f}% ({recent_accuracy["total_games"]} games)')
        else:
            print('   No recent results to analyze')
    except Exception as e:
        print(f'   Error loading accuracy data: {e}')
    print()

    print('Note: Predictions based on season-long averages. Actual totals in recent')
    print('      games average 147.9 points with home teams scoring 76.4 ppg.')
    print()
    print('💡 To check accuracy: python scripts/check_prediction_accuracy.py')

if __name__ == '__main__':
    main()

