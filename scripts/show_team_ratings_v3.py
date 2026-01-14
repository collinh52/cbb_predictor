"""
Display all team ratings sorted from highest to lowest.
Phase 3D Improvements:
1. FIXED: Opponent-adjusted team-specific home court advantage (0-4 range, scaled for realism)
2. ENHANCED NEUTRAL COURT DETECTION: Multi-method detection system
3. PACE ADJUSTMENT: Tempo-free ratings (points per 100 possessions)
4. PYTHAGOREAN EXPECTATION: Identifies lucky/unlucky teams with regression adjustment
5. Venue performance tracking (home/away/neutral)
6. Variance/consistency metrics (affects prediction confidence, not rankings)
7. ROAD WARRIOR BONUS: Teams that perform better on road get rating boost (0-3 points)
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

# Phase 3C Enhancement Parameters
DEFAULT_HOME_COURT_ADVANTAGE = 3.5  # Default if insufficient data
RECENCY_DECAY = 0.98  # Exponential decay for game weights
MOV_DIMINISHING_THRESHOLD = 10  # Full value up to 10 points, then logarithmic

# Pace adjustment parameters
PACE_ESTIMATE_FACTOR = 1.5  # Rough estimate: possessions ≈ total_points / 1.5
PACE_NORMALIZATION = 100  # Convert to per-100 possessions

# Enhanced neutral court detection
NEUTRAL_COURT_KEYWORDS = [
    'neutral', 'championship', 'tournament', 'classic', 'showcase', 'invitational',
    'challenge', 'classic', 'crossover', 'fest', 'all-star', 'exhibition'
]

# Known neutral venues (arenas that frequently host tournaments)
NEUTRAL_VENUES = [
    'madison square garden', 'barclays center', 'united center', 'td garden',
    'wells fargo center', 'spectrum center', 'capital one arena', 'crypto.com arena',
    'golden one center', 'moda center', 'ball arena', 'target center',
    'little caesars arena', 'rocket mortgage fieldhouse', 'kia center',
    'fedex forum', 'smoothie king center', 'toyota center', 'at&t center',
    'oracle park', 'oracle arena', 'chase center', 'sap center',
    # College-specific venues
    'bridgestone arena', 'prudential center', 'ppg paints arena',
    'amway center', 'kfc yum! center', 'bankers life fieldhouse',
    'scotiabank arena', 'air canada centre', 'rogers arena',
    'bell centre', 'rexall place', 'canadian tire centre'
]

# Conference tournament locations (these are typically neutral)
CONFERENCE_TOURNAMENT_VENUES = [
    'indianapolis', 'atlanta', 'phoenix', 'anaheim', 'dallas', 'chicago',
    'st. louis', 'cleveland', 'pittsburgh', 'milwaukee', 'cincinnati',
    'columbus', 'detroit', 'minneapolis', 'nashville', 'new orleans',
    'san antonio', 'salt lake city', 'denver', 'portland', 'seattle'
]

def is_neutral_court_game(game: dict) -> bool:
    """
    Practical neutral court detection for college basketball.

    Since ESPN API doesn't provide location data for most games, we use:
    1. Tournament season detection (March/April)
    2. Conference tournament patterns
    3. Known tournament teams/dates
    """
    try:
        # Method 1: Tournament season (March/April) - high likelihood of neutral courts
        game_date = game.get('date', '')
        if game_date:
            from datetime import datetime
            if isinstance(game_date, str):
                try:
                    parsed_date = datetime.fromisoformat(game_date.replace('Z', '+00:00'))
                except:
                    parsed_date = None
            else:
                parsed_date = game_date

            # March Madness and conference tournaments happen in March/April
            if parsed_date and parsed_date.month in [3, 4] and parsed_date.day > 10:
                # During tournament season, many games are on neutral courts
                # This is a broad brush, but better than nothing
                return True

        # Method 2: Score-based heuristic - very close games might be tournament games
        # Tournament games often have closer margins due to better competition
        home_score = game.get('HomeTeamScore')
        away_score = game.get('AwayTeamScore')

        if home_score is not None and away_score is not None:
            total_score = home_score + away_score
            margin = abs(home_score - away_score)

            # Games with very close scores AND high total points might be tournaments
            # (tournaments often have better offenses leading to higher scores)
            if margin <= 3 and total_score >= 140:
                return True

        # Method 3: Known conference tournament teams
        # During tournament time, certain team combinations suggest neutral courts
        home_team = str(game.get('HomeTeam', '')).strip()
        away_team = str(game.get('AwayTeam', '')).strip()

        # Conference tournament patterns (same conference teams)
        conference_rivals = [
            # Big Ten tournament style matchups
            ('michigan', 'ohio state'), ('michigan', 'purdue'), ('purdue', 'indiana'),
            ('illinois', 'northwestern'), ('wisconsin', 'minnesota'),
            # Big 12 tournament style
            ('kansas', 'texas'), ('kansas', 'oklahoma'), ('houston', 'cincinnati'),
            # ACC tournament style
            ('duke', 'north carolina'), ('clemson', 'florida state'),
            # SEC tournament style
            ('alabama', 'tennessee'), ('florida', 'georgia'), ('auburn', 'lsu')
        ]

        home_lower = home_team.lower()
        away_lower = away_team.lower()

        for team1, team2 in conference_rivals:
            if ((team1 in home_lower and team2 in away_lower) or
                (team1 in away_lower and team2 in home_lower)):
                # If it's tournament season, this is likely a neutral court game
                if parsed_date and parsed_date.month in [3, 4]:
                    return True

        # Method 4: Any API flags (if they exist)
        if game.get('neutral_site') or game.get('neutral'):
            return True

        # Method 5: Check for any location/venue keywords that might exist
        location = str(game.get('location', '')).lower()
        notes = str(game.get('notes', '')).lower()

        for keyword in NEUTRAL_COURT_KEYWORDS:
            if keyword in location or keyword in notes:
                return True

    except Exception as e:
        # If anything goes wrong, default to not neutral
        pass

    return False

def calculate_team_specific_hca_v2(team_id: int, games: list, initial_ratings: dict) -> dict:
    """
    Calculate OPPONENT-ADJUSTED team-specific home court advantage.
    
    This fixes the Phase 2 issue where all teams had HCA = 8.0
    
    The key insight: We need to compare performance vs EXPECTED performance
    based on opponent strength, not just raw margins.
    
    Returns:
        {
            'hca': float,  # Home court advantage in points (0-4 range, scaled for realism)
            'home_record': str,
            'away_record': str,
            'neutral_record': str,
            'home_margin': float,
            'away_margin': float,
            'neutral_margin': float
        }
    """
    home_games = []  # (opponent_id, margin, expected_margin)
    away_games = []  # (opponent_id, margin, expected_margin)
    neutral_games = []
    
    # Get team's baseline rating
    team_rating = initial_ratings.get(team_id, {}).get('overall_rating', 0)
    
    for game in games:
        home_id = game.get('HomeTeamID')
        away_id = game.get('AwayTeamID')
        home_score = game.get('HomeTeamScore')
        away_score = game.get('AwayTeamScore')
        
        if home_score is None or away_score is None:
            continue
        
        is_neutral = is_neutral_court_game(game)
        
        if home_id == team_id:
            opponent_id = away_id
            margin = home_score - away_score

            # Expected margin = our rating - opponent rating
            opp_rating = initial_ratings.get(opponent_id, {}).get('overall_rating', 0)
            expected_margin = team_rating - opp_rating

            if is_neutral:
                neutral_games.append(margin)
            else:
                home_games.append((opponent_id, margin, expected_margin))
                
        elif away_id == team_id:
            opponent_id = home_id
            margin = away_score - home_score
            
            opp_rating = initial_ratings.get(opponent_id, {}).get('overall_rating', 0)
            expected_margin = team_rating - opp_rating
            
            if is_neutral:
                neutral_games.append(margin)
            else:
                away_games.append((opponent_id, margin, expected_margin))
    
    # Calculate opponent-adjusted performance
    home_performance = []  # actual - expected
    away_performance = []  # actual - expected
    
    for opp_id, actual_margin, expected_margin in home_games:
        performance = actual_margin - expected_margin
        home_performance.append(performance)
    
    for opp_id, actual_margin, expected_margin in away_games:
        performance = actual_margin - expected_margin
        away_performance.append(performance)
    
    # HCA = average home performance vs expected - average away performance vs expected
    if home_performance and away_performance:
        avg_home_perf = np.mean(home_performance)
        avg_away_perf = np.mean(away_performance)
        raw_hca = avg_home_perf - avg_away_perf

        # Scale down to realistic college basketball HCA range (typically 2-4 points)
        # The current calculation produces inflated values, so we scale them down
        team_hca = raw_hca * 0.6  # Scale factor to bring 5.0 cap down to ~3.0

    else:
        team_hca = DEFAULT_HOME_COURT_ADVANTAGE

    # Clamp to realistic range for college basketball (0 to 4 points)
    # College HCA is typically 2-4 points, not 5+
    team_hca = max(0, min(4, team_hca))
    
    # Calculate records and raw margins for display
    home_margins = [m for _, m, _ in home_games]
    away_margins = [m for _, m, _ in away_games]
    
    home_wins = sum(1 for m in home_margins if m > 0)
    away_wins = sum(1 for m in away_margins if m > 0)
    neutral_wins = sum(1 for m in neutral_games if m > 0)
    
    return {
        'hca': team_hca,
        'home_record': f"{home_wins}-{len(home_margins) - home_wins}",
        'away_record': f"{away_wins}-{len(away_margins) - away_wins}",
        'neutral_record': f"{neutral_wins}-{len(neutral_games) - neutral_wins}" if neutral_games else "0-0",
        'home_margin': np.mean(home_margins) if home_margins else 0,
        'away_margin': np.mean(away_margins) if away_margins else 0,
        'neutral_margin': np.mean(neutral_games) if neutral_games else 0,
        'home_games': len(home_margins),
        'away_games': len(away_margins),
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

def convert_to_pace_adjusted(ppg_scored: float, ppg_allowed: float) -> tuple:
    """
    Convert raw PPG to pace-adjusted ratings (points per 100 possessions).

    This normalizes for tempo differences between teams:
    - Fast teams score more due to more possessions (not necessarily better)
    - Slow teams score less due to fewer possessions (not necessarily worse)

    Args:
        ppg_scored: Points per game scored by team
        ppg_allowed: Points per game allowed by team

    Returns:
        tuple: (pace_adjusted_offensive, pace_adjusted_defensive)
    """
    # Estimate possessions per game: rough approximation
    # Typical college basketball: 1.0-1.2 points per possession
    # So possessions ≈ total_points / 1.5 gives ~65-75 possessions per game
    estimated_possessions = (ppg_scored + ppg_allowed) / PACE_ESTIMATE_FACTOR

    # Convert to points per 100 possessions
    # This gives a standardized efficiency metric
    pace_adj_offensive = (ppg_scored / estimated_possessions) * PACE_NORMALIZATION
    pace_adj_defensive = (ppg_allowed / estimated_possessions) * PACE_NORMALIZATION

    return pace_adj_offensive, pace_adj_defensive

def calculate_pythagorean_expectation(points_for: float, points_against: float, exponent: float = 11.5) -> float:
    """
    Calculate expected win percentage using Pythagorean formula.

    The Pythagorean expectation estimates a team's true talent based on point differential,
    helping identify "lucky" teams (winning close games unsustainably) vs "unlucky" teams.

    Formula: Expected Win% = (PF^exp) / (PF^exp + PA^exp)
    College basketball exponent ≈ 11.5 (empirically determined)

    Args:
        points_for: Points per game scored
        points_against: Points per game allowed
        exponent: Pythagorean exponent (11.5 for college basketball)

    Returns:
        float: Expected win percentage (0.0 to 1.0)
    """
    if points_for <= 0 or points_against <= 0:
        return 0.5  # Default for invalid data

    # Pythagorean formula
    expected_win_pct = (points_for ** exponent) / (
        points_for ** exponent + points_against ** exponent
    )

    return expected_win_pct

def calculate_luck_factor(actual_win_pct: float, pythagorean_win_pct: float) -> float:
    """
    Calculate how much a team is over/under-performing their Pythagorean expectation.

    Positive luck factor = "lucky" (winning more than expected)
    Negative luck factor = "unlucky" (winning less than expected)

    Args:
        actual_win_pct: Team's actual winning percentage
        pythagorean_win_pct: Expected winning percentage from Pythagorean formula

    Returns:
        float: Luck factor (can be positive or negative)
    """
    return actual_win_pct - pythagorean_win_pct

def calculate_road_warrior_bonus(team_rating: dict) -> float:
    """
    Calculate road warrior bonus for teams that perform better on the road.

    Teams that win a higher percentage of games away than home get rewarded,
    as road wins are harder to achieve and indicate stronger teams.

    Returns bonus in rating points (0-3 range).
    """
    home_record = team_rating.get('home_record', '0-0')
    away_record = team_rating.get('away_record', '0-0')

    # Parse records: "wins-losses"
    try:
        home_wins, home_losses = map(int, home_record.split('-'))
        away_wins, away_losses = map(int, away_record.split('-'))
    except (ValueError, AttributeError):
        return 0.0

    home_games = home_wins + home_losses
    away_games = away_wins + away_losses

    # Need minimum games at each venue
    if home_games < 3 or away_games < 3:
        return 0.0

    home_win_pct = home_wins / home_games if home_games > 0 else 0
    away_win_pct = away_wins / away_games if away_games > 0 else 0

    # Calculate difference: positive means better on road
    road_advantage = away_win_pct - home_win_pct

    # Convert to bonus: 0-3 points based on road advantage
    if road_advantage > 0:
        bonus = min(3.0, road_advantage * 5)  # Scale factor of 5 gives 3.0 max
        return bonus

    return 0.0

def apply_pace_adjustment(points_per_game: float, opponent_points_per_game: float) -> tuple:
    """
    Apply pace adjustment to convert PPG to tempo-free ratings.

    College basketball averages ~1.05 points per possession, so we estimate:
    possessions_per_game = total_points / 1.05

    Then convert to points per 100 possessions for fair comparison.

    Args:
        points_per_game: Team's PPG
        opponent_points_per_game: Opponent's PPG

    Returns:
        tuple: (pace_adjusted_offensive_rating, pace_adjusted_defensive_rating)
    """
    # Estimate possessions per game
    # College basketball: ~1.05 points per possession on average
    estimated_possessions_per_game = (points_per_game + opponent_points_per_game) / 1.05

    # Convert to per-100-possessions rating
    # This gives tempo-free efficiency ratings
    offensive_rating_per_100 = (points_per_game / estimated_possessions_per_game) * 100
    defensive_rating_per_100 = (opponent_points_per_game / estimated_possessions_per_game) * 100

    return offensive_rating_per_100, defensive_rating_per_100

def calculate_team_ratings(games: list, min_games: int = 5, use_sos_adjustment: bool = True) -> list:
    """
    Calculate team ratings with Phase 2.5 enhancements:
    1. FIXED: Opponent-adjusted team-specific HCA (0-5 range)
    2. Neutral court handling
    3. Venue performance tracking
    4. Variance metrics (for confidence, not rankings)
    """
    print('\nCalculating team ratings with Phase 2.5 enhancements...')
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
    
    # Track neutral games for debugging
    neutral_games_count = 0
    neutral_game_examples = []
    all_game_locations = set()  # Track all unique locations for analysis

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

        # Track location data for analysis
        location = str(game.get('location', '')).strip()
        notes = str(game.get('notes', '')).strip()
        matchup = str(game.get('matchup', '')).strip()

        # Collect any non-empty location data
        if location:
            all_game_locations.add(f"location: {location.lower()}")
        if notes:
            all_game_locations.add(f"notes: {notes.lower()}")
        if matchup:
            all_game_locations.add(f"matchup: {matchup.lower()}")

        # Track neutral games
        if is_neutral:
            neutral_games_count += 1
            if len(neutral_game_examples) < 5:  # Keep first 5 examples
                neutral_game_examples.append(f"{away_name} vs {home_name} ({game.get('location', 'Unknown')})")
        
        # Home team stats
        team_stats[home_id]['points_for'].append(home_score)
        team_stats[home_id]['points_against'].append(away_score)
        team_stats[home_id]['games'] += 1
        team_stats[home_id]['team_name'] = home_name
        team_stats[home_id]['team_abbr'] = home_abbr
        team_stats[home_id]['opponents'].append((away_id, away_score, home_score, not is_neutral, game_date))
        
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
        team_stats[away_id]['opponents'].append((home_id, home_score, away_score, False, game_date))
        
        if away_score > home_score:
            team_stats[away_id]['wins'] += 1
        else:
            team_stats[away_id]['losses'] += 1
    
    # Filter qualified teams
    qualified_teams = {team_id: stats for team_id, stats in team_stats.items() 
                       if stats['games'] >= min_games}
    
    # Calculate INITIAL ratings (needed for opponent-adjusted HCA)
    print(f'  Calculating initial ratings for {len(qualified_teams)} teams...')
    initial_ratings = {}
    for team_id, stats in qualified_teams.items():
        raw_offensive = np.mean(stats['points_for'])
        raw_defensive = np.mean(stats['points_against'])

        # Apply pace adjustment for tempo-free ratings
        offensive_rating, defensive_rating = apply_pace_adjustment(raw_offensive, raw_defensive)

        initial_ratings[team_id] = {
            'offensive_rating': offensive_rating,
            'defensive_rating': defensive_rating,
            'overall_rating': offensive_rating - defensive_rating
        }
    
    # Calculate enhanced metrics with opponent-adjusted HCA
    print(f'  Calculating enhanced metrics with FIXED HCA calculation...')
    ratings_dict = {}
    
    for team_id, stats in qualified_teams.items():
        raw_offensive = np.mean(stats['points_for'])
        raw_defensive = np.mean(stats['points_against'])

        # Apply pace adjustment for tempo-free ratings
        offensive_rating, defensive_rating = apply_pace_adjustment(raw_offensive, raw_defensive)

        # Phase 3D: Pythagorean expectation and luck analysis
        actual_win_pct = stats['wins'] / stats['games'] if stats['games'] > 0 else 0
        pythagorean_win_pct = calculate_pythagorean_expectation(raw_offensive, raw_defensive)
        luck_factor = calculate_luck_factor(actual_win_pct, pythagorean_win_pct)

        # Phase 2.5: FIXED opponent-adjusted HCA
        hca_data = calculate_team_specific_hca_v2(team_id, games, initial_ratings)
        
        # Variance metrics
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
            # Phase 2.5 additions
            'hca': hca_data['hca'],
            'home_record': hca_data['home_record'],
            'away_record': hca_data['away_record'],
            'neutral_record': hca_data['neutral_record'],
            'home_margin': hca_data['home_margin'],
            'away_margin': hca_data['away_margin'],
            'neutral_margin': hca_data['neutral_margin'],
            'std_dev': variance_data['std_dev'],
            'consistency_score': variance_data['consistency_score'],
            # Phase 3D: Pythagorean expectation
            'pythagorean_win_pct': pythagorean_win_pct,
            'luck_factor': luck_factor
        }
    
    # Apply SOS adjustment with Phase 2.5 enhancements
    if use_sos_adjustment:
        print('  Applying Phase 2.5 enhancements:')
        print('    ✅ FIXED: Opponent-adjusted Home Court Advantage (0-5 range)')
        print('    ✓ Neutral court game handling')
        print('    ✓ Venue performance tracking')
        print('    ✓ Variance/consistency metrics (for confidence adjustment)')
        print('    ✓ Margin of Victory (diminishing returns)')
        print('    ✓ Recency Weighting (98% decay)')
        print('  Running 10 iterations...')
        ratings_dict = _apply_sos_adjustment_v3(ratings_dict, team_stats, iterations=10)
    
    # Calculate overall rating and finalize
    ratings = []
    for team_id, rating in ratings_dict.items():
        base_rating = rating['offensive_rating'] - rating['defensive_rating']

        # Phase 3A: ROAD WARRIOR BONUS
        # Teams that perform better on the road get a bonus
        road_warrior_bonus = calculate_road_warrior_bonus(rating)
        rating['road_warrior_bonus'] = road_warrior_bonus

        # Phase 3D: LUCK ADJUSTMENT
        # Conservative adjustment for teams significantly over/under-performing Pythagorean expectation
        # Only adjust if luck factor is > 0.10 (10+ win% difference) to avoid overcorrection
        luck_adjustment = 0
        if abs(rating['luck_factor']) > 0.10:
            # Partial regression: adjust by 25% of the luck factor (converted to rating points)
            luck_adjustment = -rating['luck_factor'] * 0.25 * 10  # Convert win% to rating points
            luck_adjustment = max(-3, min(3, luck_adjustment))  # Cap at ±3 points
        rating['luck_adjustment'] = luck_adjustment

        rating['overall_rating'] = base_rating + road_warrior_bonus + luck_adjustment

        # Calculate SOS metrics
        opp_ids = [opp[0] for opp in rating['opponents']]
        opp_records = []
        for opp_id in opp_ids:
            if opp_id in ratings_dict:
                opp_records.append(ratings_dict[opp_id]['win_pct'])

        rating['sos'] = np.mean(opp_records) if opp_records else 0.5
        rating['sos_rank'] = 0

        ratings.append(rating)

    sorted_ratings = sorted(ratings, key=lambda x: x['overall_rating'], reverse=True)

    # Return both ratings and neutral game statistics
    return sorted_ratings, {
        'neutral_games_count': neutral_games_count,
        'neutral_game_examples': neutral_game_examples,
        'all_game_locations': sorted(list(all_game_locations))[:20]  # Top 20 locations for debugging
    }

def _apply_sos_adjustment_v3(ratings_dict: dict, team_stats: dict, iterations: int = 10) -> dict:
    """
    SOS adjustment with Phase 2.5: Using FIXED opponent-adjusted HCA
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
            team_hca = rating['hca']  # Use FIXED team-specific HCA
            
            # Adjust offensive rating
            adj_off_values = []
            weights = []
            
            for idx, (opp_id, opp_score, our_score, is_home, game_date) in enumerate(opponents):
                if opp_id in ratings_dict:
                    league_avg_def = 75.0
                    opp_def = ratings_dict[opp_id]['defensive_rating']
                    opp_hca = ratings_dict[opp_id]['hca']  # Opponent's FIXED HCA
                    
                    # Use team-specific HCA for both teams
                    if is_home:
                        effective_opp_def = opp_def - team_hca
                    else:
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
                    
                    if is_home:
                        effective_opp_off = opp_off - opp_hca
                    else:
                        effective_opp_off = opp_off + opp_hca
                    
                    effective_opp_off = max(effective_opp_off, 30.0)
                    
                    adjustment = league_avg_off / effective_opp_off
                    
                    margin = opp_score - our_score
                    adjusted_margin = calculate_adjusted_margin(margin)
                    mov_weight = 1.0 - (adjusted_margin / 100.0)
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
    """Print formatted ratings table with Phase 2.5 metrics."""
    print("\n" + "="*136)
    print(title.center(136))
    print("="*136 + "\n")
    
    header = f"{'Rank':<5} {'Team':<35} {'Off':<7} {'Def':<7} {'Net':<7} {'Record':<10} {'HCA':<6} {'Road':<6} {'Consistency':<12} {'Home':<8} {'Away':<8} {'Neutral':<8}"
    print(header)
    print("-" * 136)
    
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

        # Luck indicator
        luck_factor = team.get('luck_factor', 0)
        if luck_factor > 0.10:
            luck_symbol = " 🍀"  # Lucky (overperforming)
        elif luck_factor < -0.10:
            luck_symbol = " 😰"  # Unlucky (underperforming)
        else:
            luck_symbol = ""

        off_str = f"{team['offensive_rating']:.1f}"
        def_str = f"{team['defensive_rating']:.1f}"
        net_str = f"{net:+.1f}"
        hca_str = f"{team['hca']:.1f}"
        road_bonus = team.get('road_warrior_bonus', 0)
        road_str = f"{road_bonus:+.1f}" if road_bonus != 0 else "0.0"

        team_name_display = f"{team['team_name'][:32]}{luck_symbol}"

        print(f"{i:<5} {team_name_display:<35} {off_str:<7} {def_str:<7} "
              f"{tier} {net_str:<6} {team['wins']}-{team['losses']:<8} {hca_str:<6} {road_str:<6} {cons_str:<12} "
              f"{team['home_record']:<8} {team['away_record']:<8} {team['neutral_record']:<8}")

def main():
    print("\n" + "="*136)
    print("COLLEGE BASKETBALL TEAM RATINGS - 2025-26 SEASON (Phase 3D Enhanced)".center(136))
    print("="*136 + "\n")

    espn = get_espn_collector()
    
    print("Fetching ALL games from ESPN for the 2025-26 season...")
    print("(Using team schedules for comprehensive data - this will take 1-2 minutes)")
    historical_games = espn.get_all_games_via_team_schedules(2026)
    
    completed_games = [g for g in historical_games if g.get('HomeTeamScore') is not None and g.get('AwayTeamScore') is not None]
    print(f"✓ Found {len(completed_games)} completed games")

    ratings, neutral_stats = calculate_team_ratings(completed_games, min_games=5, use_sos_adjustment=True)
    print(f"✓ Calculated ratings for {len(ratings)} teams")

    print_ratings_table(ratings, "TEAM RATINGS - Phase 3D Enhanced (PYTHAGOREAN + PACE + HCA + ROAD WARRIOR + NEUTRAL)")

    print("\n" + "="*136)
    print("PHASE 3D ENHANCEMENTS".center(136))
    print("="*136 + "\n")
    print("  ✅ FIXED HCA: Opponent-adjusted Home Court Advantage (0-4 range, scaled for realism)")
    print("  ✅ ROAD WARRIOR BONUS: Teams with better road performance get 0-3 point rating boost")
    print("  ✅ ENHANCED NEUTRAL COURT DETECTION: Multi-method detection system")
    print("  ✅ PACE ADJUSTMENT: Tempo-free ratings (points per 100 possessions)")
    print("  ✅ PYTHAGOREAN EXPECTATION: Identifies lucky 🍀 vs unlucky 😰 teams with regression")
    print("  ✓ Venue performance tracking (home/away/neutral records)")
    print("  ✓ Variance/consistency metrics (affects prediction CONFIDENCE, not ranking)")
    print()
    print(f"  📍 Neutral Games Detected: {neutral_stats['neutral_games_count']} games")
    if neutral_stats['neutral_game_examples']:
        print("  Examples:")
        for example in neutral_stats['neutral_game_examples']:
            print(f"    • {example}")
    else:
        print("  Examples: None found (may indicate detection needs tuning)")

    # Show sample locations for debugging
    if neutral_stats['all_game_locations']:
        print(f"\n  🏟️ Sample Game Locations ({len(neutral_stats['all_game_locations'])} unique):")
        for loc in neutral_stats['all_game_locations'][:10]:  # Show first 10
            print(f"    • {loc}")
        if len(neutral_stats['all_game_locations']) > 10:
            print(f"    ... and {len(neutral_stats['all_game_locations']) - 10} more")
    print("\n  Legend:")
    print("    HCA: Team-specific home court advantage (0-4 points, opponent-adjusted, scaled for realism)")
    print("    Road: Road Warrior bonus (0-3 points for road success)")
    print("    Consistency: 80+ 🎯 = Reliable, <60 ⚠️ = High variance")
    print("    🍀 = Lucky (overperforming Pythagorean expectation)")
    print("    😰 = Unlucky (underperforming Pythagorean expectation)")
    print("    Home/Away/Neutral: Records by venue type")
    print("\n  Next step: Pace adjustment and Pythagorean expectation for even better accuracy!")

    print("\n" + "="*130)
    print(f"Based on {len(completed_games)} games through {datetime.now().strftime('%B %d, %Y')}".center(130))
    print("="*130 + "\n")

if __name__ == "__main__":
    main()

