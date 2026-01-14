"""
Display all team ratings sorted from highest to lowest.
Phase 2 Improvements:
1. Team-specific home court advantage
2. Neutral court game handling
3. Venue performance tracking (home/away/neutral)
4. Variance/consistency metrics
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

# Phase 2 Enhancement Parameters
DEFAULT_HOME_COURT_ADVANTAGE = 3.5  # Default if insufficient data
RECENCY_DECAY = 0.98  # Exponential decay for game weights
MOV_DIMINISHING_THRESHOLD = 10  # Full value up to 10 points, then logarithmic
NEUTRAL_COURT_KEYWORDS = ['neutral', 'championship', 'tournament', 'classic', 'showcase']

def is_neutral_court_game(game: dict) -> bool:
    """
    Detect if a game is played on a neutral court.
    Checks for tournament/neutral site indicators.
    """
    # ESPN API might have a neutral site indicator
    if game.get('neutral_site') or game.get('neutral'):
        return True
    
    # Check location/notes for neutral keywords
    location = str(game.get('location', '')).lower()
    notes = str(game.get('notes', '')).lower()
    
    for keyword in NEUTRAL_COURT_KEYWORDS:
        if keyword in location or keyword in notes:
            return True
    
    return False

def calculate_team_specific_hca(team_id: int, games: list) -> dict:
    """
    Calculate team-specific home court advantage.
    
    Returns:
        {
            'hca': float,  # Home court advantage in points
            'home_record': str,
            'away_record': str,
            'neutral_record': str,
            'home_margin': float,  # Average margin at home
            'away_margin': float,  # Average margin away
            'neutral_margin': float  # Average margin neutral
        }
    """
    home_games = []
    away_games = []
    neutral_games = []
    
    for game in games:
        home_id = game.get('HomeTeamID')
        away_id = game.get('AwayTeamID')
        home_score = game.get('HomeTeamScore')
        away_score = game.get('AwayTeamScore')
        
        if home_score is None or away_score is None:
            continue
        
        is_neutral = is_neutral_court_game(game)
        
        if home_id == team_id:
            margin = home_score - away_score
            if is_neutral:
                neutral_games.append(margin)
            else:
                home_games.append(margin)
        elif away_id == team_id:
            margin = away_score - home_score
            if is_neutral:
                neutral_games.append(margin)
            else:
                away_games.append(margin)
    
    # Calculate average margins
    home_margin = np.mean(home_games) if home_games else 0
    away_margin = np.mean(away_games) if away_games else 0
    neutral_margin = np.mean(neutral_games) if neutral_games else 0
    
    # Calculate team-specific HCA
    # HCA = difference between home performance and away performance
    if home_games and away_games:
        team_hca = home_margin - away_margin
    else:
        team_hca = DEFAULT_HOME_COURT_ADVANTAGE
    
    # Clamp to reasonable range (0 to 8 points)
    team_hca = max(0, min(8, team_hca))
    
    # Calculate records
    home_wins = sum(1 for m in home_games if m > 0)
    away_wins = sum(1 for m in away_games if m > 0)
    neutral_wins = sum(1 for m in neutral_games if m > 0)
    
    return {
        'hca': team_hca,
        'home_record': f"{home_wins}-{len(home_games) - home_wins}",
        'away_record': f"{away_wins}-{len(away_games) - away_wins}",
        'neutral_record': f"{neutral_wins}-{len(neutral_games) - neutral_wins}" if neutral_games else "0-0",
        'home_margin': home_margin,
        'away_margin': away_margin,
        'neutral_margin': neutral_margin,
        'home_games': len(home_games),
        'away_games': len(away_games),
        'neutral_games': len(neutral_games)
    }

def calculate_variance_metrics(team_id: int, games: list) -> dict:
    """
    Calculate team consistency/variance metrics.
    High variance = unpredictable, low variance = consistent
    """
    margins = []
    
    for game in games:
        home_id = game.get('HomeTeamID')
        away_id = game.get('AwayTeamID')
        home_score = game.get('HomeTeamScore')
        away_score = game.get('AwayTeamScore')
        
        if home_score is None or away_score is None:
            continue
        
        if home_id == team_id:
            margin = home_score - away_score
            margins.append(margin)
        elif away_id == team_id:
            margin = away_score - home_score
            margins.append(margin)
    
    if not margins:
        return {'variance': 0, 'std_dev': 0, 'consistency_score': 0}
    
    variance = np.var(margins)
    std_dev = np.std(margins)
    
    # Consistency score: lower std_dev = more consistent (0-100 scale)
    # Typical std_dev is 10-15 points, so we'll use that as baseline
    consistency_score = max(0, 100 - (std_dev * 5))
    
    return {
        'variance': variance,
        'std_dev': std_dev,
        'consistency_score': consistency_score
    }

def calculate_adjusted_margin(margin: float) -> float:
    """Apply diminishing returns to margin of victory."""
    if abs(margin) <= MOV_DIMINISHING_THRESHOLD:
        return margin
    else:
        sign = 1 if margin > 0 else -1
        return sign * (MOV_DIMINISHING_THRESHOLD + np.log(abs(margin) - MOV_DIMINISHING_THRESHOLD + 1))

def calculate_recency_weights(game_dates: list) -> list:
    """Calculate exponential decay weights for recency."""
    if not game_dates:
        return []
    
    sorted_dates = sorted(game_dates)
    weights = []
    for i in range(len(sorted_dates)):
        days_ago = len(sorted_dates) - 1 - i
        weight = RECENCY_DECAY ** days_ago
        weights.append(weight)
    
    return weights

def calculate_team_ratings(games: list, min_games: int = 5, use_sos_adjustment: bool = True) -> list:
    """
    Calculate team ratings with Phase 2 enhancements:
    1. Team-specific home court advantage
    2. Neutral court handling
    3. Venue performance tracking
    4. Variance metrics
    """
    print('\nCalculating team ratings with Phase 2 enhancements...')
    print('(Filtering teams with <5 games to exclude non-D1 opponents)')
    
    # Gather basic stats
    team_stats = defaultdict(lambda: {
        'points_for': [],
        'points_against': [],
        'games': 0,
        'wins': 0,
        'losses': 0,
        'team_name': 'Unknown',
        'team_abbr': '',
        'opponents': []
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
        
        if not all([home_id, away_id, home_score is not None, away_score is not None, game_date_str]):
            continue
        
        try:
            game_date = datetime.fromisoformat(game_date_str.replace('Z', '+00:00'))
        except:
            continue
        
        is_neutral = is_neutral_court_game(game)
        
        # Home team stats
        team_stats[home_id]['points_for'].append(home_score)
        team_stats[home_id]['points_against'].append(away_score)
        team_stats[home_id]['games'] += 1
        team_stats[home_id]['team_name'] = home_name
        team_stats[home_id]['team_abbr'] = home_abbr
        team_stats[home_id]['opponents'].append((away_id, away_score, home_score, not is_neutral, game_date))  # is_home=True unless neutral
        
        if home_score > away_score:
            team_stats[home_id]['wins'] += 1
        else:
            team_stats[home_id]['losses'] += 1
        
        # Away team stats
        team_stats[away_id]['points_for'].append(away_score)
        team_stats[away_id]['points_against'].append(home_score)
        team_stats[away_id]['games'] += 1
        team_stats[away_id]['team_name'] = away_name
        team_stats[away_id]['team_abbr'] = away_abbr
        team_stats[away_id]['opponents'].append((home_id, home_score, away_score, False, game_date))  # is_home=False always
        
        if away_score > home_score:
            team_stats[away_id]['wins'] += 1
        else:
            team_stats[away_id]['losses'] += 1
    
    # Filter qualified teams
    qualified_teams = {team_id: stats for team_id, stats in team_stats.items() 
                       if stats['games'] >= min_games}
    
    # Calculate enhanced metrics for each team
    print(f'  Calculating enhanced metrics for {len(qualified_teams)} teams...')
    ratings_dict = {}
    
    for team_id, stats in qualified_teams.items():
        # Basic ratings
        offensive_rating = np.mean(stats['points_for'])
        defensive_rating = np.mean(stats['points_against'])
        
        # Phase 2: Team-specific home court advantage
        hca_data = calculate_team_specific_hca(team_id, games)
        
        # Phase 2: Variance metrics
        variance_data = calculate_variance_metrics(team_id, games)
        
        ratings_dict[team_id] = {
            'team_id': team_id,
            'team_name': stats['team_name'],
            'team_abbr': stats['team_abbr'],
            'offensive_rating': offensive_rating,
            'defensive_rating': defensive_rating,
            'wins': stats['wins'],
            'losses': stats['losses'],
            'games': stats['games'],
            'win_pct': stats['wins'] / stats['games'] if stats['games'] > 0 else 0,
            'opponents': stats['opponents'],
            # Phase 2 additions
            'hca': hca_data['hca'],
            'home_record': hca_data['home_record'],
            'away_record': hca_data['away_record'],
            'neutral_record': hca_data['neutral_record'],
            'home_margin': hca_data['home_margin'],
            'away_margin': hca_data['away_margin'],
            'neutral_margin': hca_data['neutral_margin'],
            'std_dev': variance_data['std_dev'],
            'consistency_score': variance_data['consistency_score']
        }
    
    # Apply SOS adjustment with Phase 2 enhancements
    if use_sos_adjustment:
        print('  Applying Phase 2 enhancements:')
        print('    ✓ Team-specific Home Court Advantage')
        print('    ✓ Neutral court game handling')
        print('    ✓ Venue performance tracking')
        print('    ✓ Variance/consistency metrics')
        print('    ✓ Margin of Victory (diminishing returns)')
        print('    ✓ Recency Weighting (98% decay)')
        print('  Running 10 iterations...')
        ratings_dict = _apply_sos_adjustment_v2(ratings_dict, team_stats, iterations=10)
    
    # Calculate overall rating and finalize
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
        rating['sos_rank'] = 0
        
        ratings.append(rating)
    
    return sorted(ratings, key=lambda x: x['overall_rating'], reverse=True)

def _apply_sos_adjustment_v2(ratings_dict: dict, team_stats: dict, iterations: int = 10) -> dict:
    """
    SOS adjustment with Phase 2 enhancements:
    - Team-specific HCA
    - Neutral court handling
    - MoV and recency
    """
    # Start with raw ratings
    for team_id in ratings_dict:
        ratings_dict[team_id]['raw_off'] = ratings_dict[team_id]['offensive_rating']
        ratings_dict[team_id]['raw_def'] = ratings_dict[team_id]['defensive_rating']
    
    # Calculate recency weights for each team
    recency_weights_by_team = {}
    for team_id, rating in ratings_dict.items():
        opponents = rating['opponents']
        game_dates = [opp[4] for opp in opponents]
        recency_weights_by_team[team_id] = calculate_recency_weights(game_dates)
    
    # Iteratively adjust ratings
    for iteration in range(iterations):
        new_ratings = {}
        
        for team_id, rating in ratings_dict.items():
            opponents = rating['opponents']
            recency_weights = recency_weights_by_team[team_id]
            team_hca = rating['hca']  # Use team-specific HCA
            
            # Adjust offensive rating
            adj_off_values = []
            weights = []
            
            for idx, (opp_id, opp_score, our_score, is_home, game_date) in enumerate(opponents):
                if opp_id in ratings_dict:
                    league_avg_def = 75.0
                    opp_def = ratings_dict[opp_id]['defensive_rating']
                    opp_hca = ratings_dict[opp_id]['hca']  # Opponent's HCA
                    
                    # Phase 2: Use team-specific HCA for both teams
                    if is_home:
                        # We had home advantage
                        effective_opp_def = opp_def - team_hca
                    else:
                        # Opponent had home advantage (or neutral)
                        effective_opp_def = opp_def + opp_hca
                    
                    effective_opp_def = max(effective_opp_def, 30.0)
                    
                    adjustment = league_avg_def / effective_opp_def
                    
                    # Margin of Victory
                    margin = our_score - opp_score
                    adjusted_margin = calculate_adjusted_margin(margin)
                    mov_weight = 1.0 + (adjusted_margin / 100.0)
                    mov_weight = max(0.8, min(1.3, mov_weight))
                    
                    # Recency Weight
                    recency_weight = recency_weights[idx] if idx < len(recency_weights) else 1.0
                    
                    # Combined weight
                    total_weight = mov_weight * recency_weight
                    
                    adj_off_values.append(our_score * adjustment)
                    weights.append(total_weight)
            
            # Weighted average
            if adj_off_values and sum(weights) > 0:
                new_ratings[team_id] = {
                    'offensive_rating': np.average(adj_off_values, weights=weights)
                }
            else:
                new_ratings[team_id] = {
                    'offensive_rating': rating['offensive_rating']
                }
            
            # Adjust defensive rating (similar logic)
            adj_def_values = []
            weights = []
            
            for idx, (opp_id, opp_score, our_score, is_home, game_date) in enumerate(opponents):
                if opp_id in ratings_dict:
                    league_avg_off = 75.0
                    opp_off = ratings_dict[opp_id]['offensive_rating']
                    opp_hca = ratings_dict[opp_id]['hca']
                    
                    # Adjust opponent's offense for venue
                    if is_home:
                        # Opponent was away, we had home advantage
                        effective_opp_off = opp_off - opp_hca
                    else:
                        # Opponent was home, they had advantage
                        effective_opp_off = opp_off + opp_hca
                    
                    effective_opp_off = max(effective_opp_off, 30.0)
                    
                    adjustment = league_avg_off / effective_opp_off
                    
                    margin = opp_score - our_score  # Reversed for defense
                    adjusted_margin = calculate_adjusted_margin(margin)
                    mov_weight = 1.0 - (adjusted_margin / 100.0)  # Lower is better for defense
                    mov_weight = max(0.8, min(1.3, mov_weight))
                    
                    recency_weight = recency_weights[idx] if idx < len(recency_weights) else 1.0
                    total_weight = mov_weight * recency_weight
                    
                    adj_def_values.append(opp_score * adjustment)
                    weights.append(total_weight)
            
            if adj_def_values and sum(weights) > 0:
                new_ratings[team_id]['defensive_rating'] = np.average(adj_def_values, weights=weights)
            else:
                new_ratings[team_id]['defensive_rating'] = rating['defensive_rating']
        
        # Update ratings
        for team_id in ratings_dict:
            if team_id in new_ratings:
                ratings_dict[team_id]['offensive_rating'] = new_ratings[team_id]['offensive_rating']
                ratings_dict[team_id]['defensive_rating'] = new_ratings[team_id]['defensive_rating']
    
    return ratings_dict

def print_ratings_table(ratings: list, title: str):
    """Print formatted ratings table with Phase 2 metrics."""
    print("\n" + "="*130)
    print(title.center(130))
    print("="*130 + "\n")
    
    header = f"{'Rank':<5} {'Team':<35} {'Off':<7} {'Def':<7} {'Net':<7} {'Record':<10} {'HCA':<6} {'Consistency':<12} {'Home':<8} {'Away':<8} {'Neutral':<8}"
    print(header)
    print("-" * 130)
    
    for i, team in enumerate(ratings[:50], 1):  # Top 50
        # Rating tier emoji
        net = team['overall_rating']
        if net > 50:
            tier = "🔥"
        elif net > 30:
            tier = "⭐"
        elif net > 10:
            tier = "✓"
        elif net > 0:
            tier = "→"
        else:
            tier = "↓"
        
        # Consistency tier
        consistency = team['consistency_score']
        if consistency > 80:
            cons_str = f"{consistency:.0f} 🎯"  # Consistent
        elif consistency > 60:
            cons_str = f"{consistency:.0f} ✓"
        else:
            cons_str = f"{consistency:.0f} ⚠️"  # High variance
        
        off_str = f"{team['offensive_rating']:.1f}"
        def_str = f"{team['defensive_rating']:.1f}"
        net_str = f"{net:+.1f}"
        hca_str = f"{team['hca']:.1f}"
        
        print(f"{i:<5} {team['team_name'][:34]:<35} {off_str:<7} {def_str:<7} "
              f"{tier} {net_str:<6} {team['wins']}-{team['losses']:<8} {hca_str:<6} {cons_str:<12} "
              f"{team['home_record']:<8} {team['away_record']:<8} {team['neutral_record']:<8}")

def main():
    print("\n" + "="*130)
    print("COLLEGE BASKETBALL TEAM RATINGS - 2025-26 SEASON (Phase 2 Enhanced)".center(130))
    print("="*130 + "\n")

    espn = get_espn_collector()
    
    print("Fetching ALL games from ESPN for the 2025-26 season...")
    print("(Using team schedules for comprehensive data - this will take 1-2 minutes)")
    historical_games = espn.get_all_games_via_team_schedules(2026)
    
    completed_games = [g for g in historical_games if g.get('HomeTeamScore') is not None and g.get('AwayTeamScore') is not None]
    print(f"✓ Found {len(completed_games)} completed games")

    ratings = calculate_team_ratings(completed_games, min_games=5, use_sos_adjustment=True)
    print(f"✓ Calculated ratings for {len(ratings)} teams")

    print_ratings_table(ratings, "TEAM RATINGS - Phase 2 Enhanced")

    print("\n" + "="*130)
    print("PHASE 2 ENHANCEMENTS".center(130))
    print("="*130 + "\n")
    print("  ✓ Team-specific Home Court Advantage (not fixed 3.5)")
    print("  ✓ Neutral court game detection and handling")
    print("  ✓ Venue performance tracking (home/away/neutral records)")
    print("  ✓ Variance/consistency metrics (identifies volatile teams)")
    print("  ✓ Alabama's high variance should now be visible (⚠️ indicator)")
    print("\n  Legend:")
    print("    HCA: Team-specific home court advantage (0-8 points)")
    print("    Consistency: 80+ 🎯 = Reliable, <60 ⚠️ = High variance")
    print("    Home/Away/Neutral: Records by venue type")

    print("\n" + "="*130)
    print(f"Based on {len(completed_games)} games through {datetime.now().strftime('%B %d, %Y')}".center(130))
    print("="*130 + "\n")

if __name__ == "__main__":
    main()

