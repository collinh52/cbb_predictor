"""
Display all team ratings sorted from highest to lowest.
Shows offensive rating, defensive rating, and overall rating.
With Phase 1 improvements: Home Court Advantage, Margin of Victory, and Recency Weighting.
"""
import os
import sys

# Add parent directory to path so we can import from src
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.pop('DATABASE_URL', None)

from src.espn_collector import get_espn_collector
from datetime import datetime, timedelta
from collections import defaultdict
import numpy as np

# Phase 1 Enhancement Parameters
HOME_COURT_ADVANTAGE = 3.5  # Points advantage for home team
RECENCY_DECAY = 0.98  # Exponential decay for game weights (98% of previous game)
MOV_DIMINISHING_THRESHOLD = 10  # Full value up to 10 points, then logarithmic

def calculate_adjusted_margin(margin: float) -> float:
    """
    Apply diminishing returns to margin of victory.
    Full value up to 10 points, then logarithmic to prevent running up score.
    Similar to KenPom's approach.
    """
    if abs(margin) <= MOV_DIMINISHING_THRESHOLD:
        return margin
    else:
        sign = 1 if margin > 0 else -1
        return sign * (MOV_DIMINISHING_THRESHOLD + np.log(abs(margin) - MOV_DIMINISHING_THRESHOLD + 1))

def calculate_recency_weights(game_dates: list) -> list:
    """
    Calculate exponential decay weights for recency.
    Most recent game = 1.0, each prior game *= RECENCY_DECAY
    """
    if not game_dates:
        return []
    
    # Sort to ensure chronological order
    sorted_dates = sorted(game_dates)
    n_games = len(sorted_dates)
    
    weights = []
    for i in range(n_games):
        # i=0 is oldest, i=n_games-1 is most recent
        recency_weight = RECENCY_DECAY ** (n_games - 1 - i)
        weights.append(recency_weight)
    
    return weights

def calculate_team_ratings(games: list, min_games: int = 5, use_sos_adjustment: bool = True) -> list:
    """
    Calculate offensive and defensive ratings for all teams with SOS adjustment.
    
    Args:
        games: List of completed games
        min_games: Minimum number of games required to be included (default 5)
        use_sos_adjustment: Whether to adjust ratings based on opponent strength (default True)
    """
    team_stats = defaultdict(lambda: {
        'points_for': [], 
        'points_against': [], 
        'games': 0,
        'wins': 0,
        'losses': 0,
        'team_name': 'Unknown',
        'team_abbr': '',
        'opponents': [],
        'game_dates': []
    })
    
    for game in games:
        home_id = game.get('HomeTeamID')
        away_id = game.get('AwayTeamID')
        home_name = game.get('HomeTeamName', 'Unknown')
        away_name = game.get('AwayTeamName', 'Unknown')
        home_abbr = game.get('HomeTeam', '')
        away_abbr = game.get('AwayTeam', '')
        home_score = game.get('HomeTeamScore')
        away_score = game.get('AwayTeamScore')
        game_date_str = game.get('DateTime', '')
        
        # Parse game date
        try:
            game_date = datetime.fromisoformat(game_date_str.replace('Z', '+00:00'))
        except:
            game_date = datetime.now()  # Fallback
        
        if home_id and away_id and home_score is not None and away_score is not None:
            # Home team stats (is_home = True)
            team_stats[home_id]['points_for'].append(home_score)
            team_stats[home_id]['points_against'].append(away_score)
            team_stats[home_id]['games'] += 1
            team_stats[home_id]['team_name'] = home_name
            team_stats[home_id]['team_abbr'] = home_abbr
            team_stats[home_id]['game_dates'].append(game_date)
            # Store: (opp_id, opp_score, our_score, is_home, game_date)
            team_stats[home_id]['opponents'].append((away_id, away_score, home_score, True, game_date))
            if home_score > away_score:
                team_stats[home_id]['wins'] += 1
            else:
                team_stats[home_id]['losses'] += 1
            
            # Away team stats (is_home = False)
            team_stats[away_id]['points_for'].append(away_score)
            team_stats[away_id]['points_against'].append(home_score)
            team_stats[away_id]['games'] += 1
            team_stats[away_id]['team_name'] = away_name
            team_stats[away_id]['team_abbr'] = away_abbr
            team_stats[away_id]['game_dates'].append(game_date)
            # Store: (opp_id, opp_score, our_score, is_home, game_date)
            team_stats[away_id]['opponents'].append((home_id, home_score, away_score, False, game_date))
            if away_score > home_score:
                team_stats[away_id]['wins'] += 1
            else:
                team_stats[away_id]['losses'] += 1
    
    # Filter teams with enough games
    qualified_teams = {tid: stats for tid, stats in team_stats.items() if stats['games'] >= min_games}
    
    # Initial ratings (simple averages)
    ratings_dict = {}
    for team_id, stats in qualified_teams.items():
        ratings_dict[team_id] = {
            'team_id': team_id,
            'team_name': stats['team_name'],
            'team_abbr': stats['team_abbr'],
            'offensive_rating': np.mean(stats['points_for']),
            'defensive_rating': np.mean(stats['points_against']),
            'wins': stats['wins'],
            'losses': stats['losses'],
            'games': stats['games'],
            'win_pct': stats['wins'] / stats['games'] if stats['games'] > 0 else 0,
            'opponents': stats['opponents']
        }
    
    # Apply SOS adjustment if requested (now includes Phase 1 enhancements)
    if use_sos_adjustment:
        print('  Applying Phase 1 enhancements:')
        print('    ✓ Home Court Advantage (±3.5 points)')
        print('    ✓ Margin of Victory (diminishing returns)')
        print('    ✓ Recency Weighting (98% decay)')
        print('  Running 10 iterations...')
        ratings_dict = _apply_sos_adjustment(ratings_dict, team_stats, iterations=10)
    
    # Calculate overall rating and convert to list
    ratings = []
    for team_id, rating in ratings_dict.items():
        rating['overall_rating'] = rating['offensive_rating'] - rating['defensive_rating']
        
        # Calculate SOS metrics
        opp_ids = [opp[0] for opp in rating['opponents']]
        opp_records = []
        for opp_id in opp_ids:
            if opp_id in ratings_dict:
                opp_records.append(ratings_dict[opp_id]['win_pct'])
        
        rating['sos'] = np.mean(opp_records) if opp_records else 0.5
        rating['sos_rank'] = 0  # Will be filled in after sorting
        
        ratings.append(rating)
    
    return ratings

def _apply_sos_adjustment(ratings_dict: dict, team_stats: dict, iterations: int = 10) -> dict:
    """
    Iteratively adjust ratings based on opponent strength.
    
    NOW WITH PHASE 1 ENHANCEMENTS:
    1. Home Court Advantage: Road wins count more than home wins
    2. Margin of Victory: Dominant wins > close wins (with diminishing returns)
    3. Recency Weighting: Recent games weighted more heavily
    
    This implements a version similar to KenPom with additional improvements.
    """
    # Start with raw ratings
    for team_id in ratings_dict:
        ratings_dict[team_id]['raw_off'] = ratings_dict[team_id]['offensive_rating']
        ratings_dict[team_id]['raw_def'] = ratings_dict[team_id]['defensive_rating']
    
    # Calculate recency weights for each team
    recency_weights_by_team = {}
    for team_id, rating in ratings_dict.items():
        opponents = rating['opponents']
        game_dates = [opp[4] for opp in opponents]  # Extract dates
        recency_weights_by_team[team_id] = calculate_recency_weights(game_dates)
    
    # Iteratively adjust ratings
    for iteration in range(iterations):
        new_ratings = {}
        
        for team_id, rating in ratings_dict.items():
            opponents = rating['opponents']
            recency_weights = recency_weights_by_team[team_id]
            
            # Adjust offensive rating based on opponent defensive strength
            adj_off_values = []
            weights = []
            
            for idx, (opp_id, opp_score, our_score, is_home, game_date) in enumerate(opponents):
                if opp_id in ratings_dict:
                    # PHASE 1 ENHANCEMENT 1: Home Court Advantage
                    # Adjust opponent strength for home court
                    league_avg_def = 75.0
                    opp_def = ratings_dict[opp_id]['defensive_rating']
                    
                    if is_home:
                        # We had home advantage - opponent's defense was effectively harder
                        effective_opp_def = opp_def - HOME_COURT_ADVANTAGE
                    else:
                        # We played away - opponent's defense was effectively easier for them
                        effective_opp_def = opp_def + HOME_COURT_ADVANTAGE
                    
                    # Prevent division by zero
                    effective_opp_def = max(effective_opp_def, 30.0)
                    
                    # Base SOS adjustment
                    adjustment = league_avg_def / effective_opp_def
                    
                    # PHASE 1 ENHANCEMENT 2: Margin of Victory
                    margin = our_score - opp_score
                    adjusted_margin = calculate_adjusted_margin(margin)
                    
                    # Convert margin to weight (1.0 = close game, up to 1.3 for blowout)
                    # Normalize so a 20-point win is ~1.2x weight
                    mov_weight = 1.0 + (adjusted_margin / 100.0)
                    mov_weight = max(0.8, min(1.3, mov_weight))  # Clamp to reasonable range
                    
                    # PHASE 1 ENHANCEMENT 3: Recency Weighting
                    recency_weight = recency_weights[idx] if idx < len(recency_weights) else 1.0
                    
                    # Combined adjustment
                    final_value = our_score * adjustment
                    final_weight = mov_weight * recency_weight
                    
                    adj_off_values.append(final_value)
                    weights.append(final_weight)
                else:
                    adj_off_values.append(our_score)
                    weights.append(1.0)
            
            # Adjust defensive rating based on opponent offensive strength
            adj_def_values = []
            def_weights = []
            
            for idx, (opp_id, opp_score, our_score, is_home, game_date) in enumerate(opponents):
                if opp_id in ratings_dict:
                    # PHASE 1 ENHANCEMENT 1: Home Court Advantage
                    league_avg_off = 75.0
                    opp_off = ratings_dict[opp_id]['offensive_rating']
                    
                    if is_home:
                        # We had home advantage - opponent's offense was effectively weaker
                        effective_opp_off = opp_off - HOME_COURT_ADVANTAGE
                    else:
                        # We played away - opponent's offense was effectively stronger
                        effective_opp_off = opp_off + HOME_COURT_ADVANTAGE
                    
                    # Prevent division by zero
                    effective_opp_off = max(effective_opp_off, 30.0)
                    
                    # Base SOS adjustment
                    adjustment = league_avg_off / effective_opp_off
                    
                    # PHASE 1 ENHANCEMENT 2: Margin of Victory (inverse for defense)
                    margin = our_score - opp_score
                    adjusted_margin = calculate_adjusted_margin(margin)
                    
                    # For defense, winning big means good defense, so similar weight
                    mov_weight = 1.0 + (adjusted_margin / 100.0)
                    mov_weight = max(0.8, min(1.3, mov_weight))
                    
                    # PHASE 1 ENHANCEMENT 3: Recency Weighting
                    recency_weight = recency_weights[idx] if idx < len(recency_weights) else 1.0
                    
                    # Combined adjustment
                    final_value = opp_score * adjustment
                    final_weight = mov_weight * recency_weight
                    
                    adj_def_values.append(final_value)
                    def_weights.append(final_weight)
                else:
                    adj_def_values.append(opp_score)
                    def_weights.append(1.0)
            
            # Calculate weighted averages
            if adj_off_values and sum(weights) > 0:
                weighted_off = sum(v * w for v, w in zip(adj_off_values, weights)) / sum(weights)
            else:
                weighted_off = rating['offensive_rating']
            
            if adj_def_values and sum(def_weights) > 0:
                weighted_def = sum(v * w for v, w in zip(adj_def_values, def_weights)) / sum(def_weights)
            else:
                weighted_def = rating['defensive_rating']
            
            new_ratings[team_id] = {
                **rating,
                'offensive_rating': weighted_off,
                'defensive_rating': weighted_def
            }
        
        ratings_dict = new_ratings
    
    return ratings_dict

def main():
    print()
    print('='*110)
    print('COLLEGE BASKETBALL TEAM RATINGS - 2025-26 SEASON')
    print('='*110)
    print()
    
    # Get full season data from ESPN (using team schedules for complete coverage)
    print('Fetching ALL games from ESPN for the 2025-26 season...')
    print('(Using team schedules for comprehensive data - this will take 1-2 minutes)')
    espn = get_espn_collector()
    
    historical_games = espn.get_all_games_via_team_schedules(season=2026)
    
    # Filter to completed games
    historical_games = [g for g in historical_games if g.get('HomeTeamScore') is not None]
    
    print(f'✓ Found {len(historical_games)} completed games')
    print()
    
    # Calculate ratings (only teams with 5+ games to filter out non-D1)
    print('Calculating team ratings...')
    print('(Filtering out teams with <5 games - likely non-D1 or exhibition opponents)')
    ratings = calculate_team_ratings(historical_games, min_games=5, use_sos_adjustment=True)
    
    # Sort by overall rating (highest to lowest)
    ratings.sort(key=lambda x: x['overall_rating'], reverse=True)
    
    print(f'✓ Calculated ratings for {len(ratings)} teams')
    print()
    
    # Calculate and assign SOS ranks
    ratings_by_sos = sorted(ratings, key=lambda x: x['sos'], reverse=True)
    for i, team in enumerate(ratings_by_sos, 1):
        team['sos_rank'] = i
    
    # Display ratings
    print('='*110)
    print('TEAM RATINGS - Phase 1 Enhanced (HCA + MoV + Recency)')
    print('='*110)
    print()
    print(f'{"Rank":<5} {"Team":<30} {"Record":<10} {"Off":<6} {"Def":<6} {"Overall":<8} {"SOS":<7} {"Games":<6}')
    print('-'*110)
    
    for i, team in enumerate(ratings, 1):
        team_name = team['team_name'][:28]  # Truncate long names
        record = f"{team['wins']}-{team['losses']}"
        off_rating = team['offensive_rating']
        def_rating = team['defensive_rating']
        overall = team['overall_rating']
        sos = team['sos']
        sos_rank = team['sos_rank']
        games = team['games']
        
        # Color coding for overall rating
        if overall > 10:
            indicator = '🔥'  # Elite
        elif overall > 5:
            indicator = '⭐'  # Great
        elif overall > 0:
            indicator = '✓'   # Good
        elif overall > -5:
            indicator = '→'   # Average
        else:
            indicator = '↓'   # Below average
        
        # Format SOS with rank
        sos_display = f'{sos:.3f}'
        
        print(f'{i:<5} {team_name:<30} {record:<10} {off_rating:>5.1f} {def_rating:>5.1f} {overall:>+7.1f} {indicator} {sos_display:<7} {games:<6}')
        
        # Add separator every 25 teams
        if i % 25 == 0 and i < len(ratings):
            print('-'*110)
    
    print()
    print('='*110)
    print('RATING DEFINITIONS')
    print('='*110)
    print()
    print('  Offensive Rating (Off):  SOS-adjusted points scored per game')
    print('  Defensive Rating (Def):  SOS-adjusted points allowed per game')
    print('  Overall Rating:          Off - Def (higher is better)')
    print('  SOS:                     Strength of Schedule (opponent win %)')
    print()
    print('  PHASE 1 ENHANCEMENTS APPLIED:')
    print('    ✓ Home Court Advantage: Road wins > home wins (±3.5 pts)')
    print('    ✓ Margin of Victory: Blowouts > close wins (diminishing returns)')
    print('    ✓ Recency Weighting: Recent games weighted more (98% decay)')
    print()
    print('  🔥 Elite      (Overall > +10)')
    print('  ⭐ Great      (Overall > +5)')
    print('  ✓  Good       (Overall > 0)')
    print('  →  Average    (Overall > -5)')
    print('  ↓  Below Avg  (Overall ≤ -5)')
    print()
    
    # Show top 10 offensive and defensive teams
    print('='*110)
    print('TOP 10 OFFENSIVE TEAMS')
    print('='*110)
    print()
    
    offensive_leaders = sorted(ratings, key=lambda x: x['offensive_rating'], reverse=True)[:10]
    print(f'{"Rank":<5} {"Team":<35} {"PPG":<8} {"Record":<10}')
    print('-'*110)
    for i, team in enumerate(offensive_leaders, 1):
        print(f'{i:<5} {team["team_name"][:33]:<35} {team["offensive_rating"]:>6.1f}  {team["wins"]}-{team["losses"]:<10}')
    
    print()
    print('='*110)
    print('TOP 10 DEFENSIVE TEAMS')
    print('='*110)
    print()
    
    defensive_leaders = sorted(ratings, key=lambda x: x['defensive_rating'])[:10]
    print(f'{"Rank":<5} {"Team":<35} {"PAPG":<8} {"Record":<10}')
    print('-'*110)
    for i, team in enumerate(defensive_leaders, 1):
        print(f'{i:<5} {team["team_name"][:33]:<35} {team["defensive_rating"]:>6.1f}  {team["wins"]}-{team["losses"]:<10}')
    
    print()
    print('='*110)
    print(f'Based on {len(historical_games)} games through {datetime.now().strftime("%B %d, %Y")}')
    print('='*110)
    print()

if __name__ == '__main__':
    main()
