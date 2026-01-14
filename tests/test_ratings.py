"""
Unit tests for the Rating calculations module.
Tests team rating algorithms including SOS adjustment, HCA, MoV, etc.
"""
import pytest
import numpy as np
import sys
import os
from datetime import datetime, timedelta
from unittest.mock import Mock, patch

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'scripts'))

# Import functions to test (note: they're in a script, not a module)
# We'll need to be careful about imports


class TestAdjustedMarginCalculation:
    """Test cases for margin of victory adjustment."""
    
    @pytest.fixture
    def calculate_adjusted_margin(self):
        """Import the function from the script."""
        from show_team_ratings_v3 import calculate_adjusted_margin
        return calculate_adjusted_margin
    
    @pytest.mark.unit
    def test_small_margin_unchanged(self, calculate_adjusted_margin):
        """Test that small margins are returned unchanged."""
        # Margins <= 10 should be returned as-is
        assert calculate_adjusted_margin(5) == 5
        assert calculate_adjusted_margin(-5) == -5
        assert calculate_adjusted_margin(10) == 10
        assert calculate_adjusted_margin(-10) == -10
    
    @pytest.mark.unit
    def test_large_margin_diminished(self, calculate_adjusted_margin):
        """Test that large margins have diminishing returns."""
        # Margins > 10 should be reduced
        adj_20 = calculate_adjusted_margin(20)
        adj_30 = calculate_adjusted_margin(30)
        
        assert adj_20 < 20
        assert adj_30 < 30
        assert adj_20 > 10  # Still bigger than threshold
        assert adj_30 > adj_20  # Bigger margin still bigger
    
    @pytest.mark.unit
    def test_preserves_sign(self, calculate_adjusted_margin):
        """Test that adjusted margin preserves win/loss sign."""
        assert calculate_adjusted_margin(20) > 0
        assert calculate_adjusted_margin(-20) < 0
        assert calculate_adjusted_margin(50) > 0
        assert calculate_adjusted_margin(-50) < 0
    
    @pytest.mark.unit
    def test_zero_margin(self, calculate_adjusted_margin):
        """Test that zero margin returns zero."""
        assert calculate_adjusted_margin(0) == 0


class TestRecencyWeightsCalculation:
    """Test cases for recency weight calculation."""
    
    @pytest.fixture
    def calculate_recency_weights(self):
        """Import the function from the script."""
        from show_team_ratings_v3 import calculate_recency_weights
        return calculate_recency_weights
    
    @pytest.mark.unit
    def test_empty_dates(self, calculate_recency_weights):
        """Test recency weights with empty list."""
        weights = calculate_recency_weights([])
        assert weights == []
    
    @pytest.mark.unit
    def test_single_date(self, calculate_recency_weights):
        """Test recency weights with single date."""
        dates = [datetime(2026, 1, 15)]
        weights = calculate_recency_weights(dates)
        
        assert len(weights) == 1
        assert weights[0] > 0
    
    @pytest.mark.unit
    def test_most_recent_highest(self, calculate_recency_weights):
        """Test that most recent game has highest weight."""
        dates = [
            datetime(2026, 1, 1),
            datetime(2026, 1, 5),
            datetime(2026, 1, 10),
            datetime(2026, 1, 15),
        ]
        weights = calculate_recency_weights(dates)
        
        # Last date should have highest weight
        assert weights[-1] >= max(weights[:-1])
    
    @pytest.mark.unit
    def test_weights_sum_positive(self, calculate_recency_weights):
        """Test that all weights are positive."""
        dates = [datetime(2026, 1, i) for i in range(1, 11)]
        weights = calculate_recency_weights(dates)
        
        assert all(w > 0 for w in weights)


class TestPythagoreanExpectation:
    """Test cases for Pythagorean win expectation."""
    
    @pytest.fixture
    def calculate_pythagorean_expectation(self):
        """Import the function from the script."""
        from show_team_ratings_v3 import calculate_pythagorean_expectation
        return calculate_pythagorean_expectation
    
    @pytest.mark.unit
    def test_equal_scoring(self, calculate_pythagorean_expectation):
        """Test that equal offense and defense gives 50%."""
        result = calculate_pythagorean_expectation(75.0, 75.0)
        assert abs(result - 0.5) < 0.001
    
    @pytest.mark.unit
    def test_better_offense_higher_expectation(self, calculate_pythagorean_expectation):
        """Test that better offense gives higher expectation."""
        result = calculate_pythagorean_expectation(80.0, 70.0)
        assert result > 0.5
    
    @pytest.mark.unit
    def test_worse_offense_lower_expectation(self, calculate_pythagorean_expectation):
        """Test that worse offense gives lower expectation."""
        result = calculate_pythagorean_expectation(70.0, 80.0)
        assert result < 0.5
    
    @pytest.mark.unit
    def test_bounded_output(self, calculate_pythagorean_expectation):
        """Test that output is bounded [0, 1]."""
        # Extreme cases
        result_dominant = calculate_pythagorean_expectation(100.0, 50.0)
        result_weak = calculate_pythagorean_expectation(50.0, 100.0)
        
        assert 0 <= result_dominant <= 1
        assert 0 <= result_weak <= 1
    
    @pytest.mark.unit
    def test_invalid_input(self, calculate_pythagorean_expectation):
        """Test handling of invalid input."""
        result = calculate_pythagorean_expectation(0.0, 75.0)
        assert result == 0.5  # Default for invalid
        
        result = calculate_pythagorean_expectation(-10.0, 75.0)
        assert result == 0.5


class TestLuckFactor:
    """Test cases for luck factor calculation."""
    
    @pytest.fixture
    def calculate_luck_factor(self):
        """Import the function from the script."""
        from show_team_ratings_v3 import calculate_luck_factor
        return calculate_luck_factor
    
    @pytest.mark.unit
    def test_no_luck(self, calculate_luck_factor):
        """Test that same actual and expected gives 0 luck."""
        luck = calculate_luck_factor(0.6, 0.6)
        assert luck == 0.0
    
    @pytest.mark.unit
    def test_lucky_team(self, calculate_luck_factor):
        """Test positive luck when outperforming."""
        luck = calculate_luck_factor(0.7, 0.5)  # Winning 70% but expected 50%
        assert luck > 0
    
    @pytest.mark.unit
    def test_unlucky_team(self, calculate_luck_factor):
        """Test negative luck when underperforming."""
        luck = calculate_luck_factor(0.4, 0.6)  # Winning 40% but expected 60%
        assert luck < 0


class TestRoadWarriorBonus:
    """Test cases for road warrior bonus calculation."""
    
    @pytest.fixture
    def calculate_road_warrior_bonus(self):
        """Import the function from the script."""
        from show_team_ratings_v3 import calculate_road_warrior_bonus
        return calculate_road_warrior_bonus
    
    @pytest.mark.unit
    def test_no_bonus_insufficient_games(self, calculate_road_warrior_bonus):
        """Test no bonus with insufficient games."""
        rating = {'home_record': '1-0', 'away_record': '1-0'}
        bonus = calculate_road_warrior_bonus(rating)
        assert bonus == 0.0
    
    @pytest.mark.unit
    def test_no_bonus_better_home(self, calculate_road_warrior_bonus):
        """Test no bonus when better at home."""
        rating = {'home_record': '8-2', 'away_record': '4-6'}  # Better at home
        bonus = calculate_road_warrior_bonus(rating)
        assert bonus == 0.0
    
    @pytest.mark.unit
    def test_bonus_better_road(self, calculate_road_warrior_bonus):
        """Test bonus when better on road."""
        rating = {'home_record': '4-6', 'away_record': '8-2'}  # Better on road
        bonus = calculate_road_warrior_bonus(rating)
        assert bonus > 0.0
    
    @pytest.mark.unit
    def test_bonus_capped(self, calculate_road_warrior_bonus):
        """Test that bonus is capped at 3."""
        rating = {'home_record': '0-10', 'away_record': '10-0'}  # Extreme case
        bonus = calculate_road_warrior_bonus(rating)
        assert bonus <= 3.0


class TestNeutralCourtDetection:
    """Test cases for neutral court game detection."""
    
    @pytest.fixture
    def is_neutral_court_game(self):
        """Import the function from the script."""
        from show_team_ratings_v3 import is_neutral_court_game
        return is_neutral_court_game
    
    @pytest.mark.unit
    def test_regular_season_game(self, is_neutral_court_game):
        """Test that regular season game is not neutral."""
        game = {
            'date': '2026-01-15',
            'HomeTeamScore': 75,
            'AwayTeamScore': 70,
            'HomeTeam': 'Duke',
            'AwayTeam': 'Wake Forest'
        }
        assert is_neutral_court_game(game) == False
    
    @pytest.mark.unit
    def test_march_madness_game(self, is_neutral_court_game):
        """Test that March Madness game is detected as neutral."""
        game = {
            'date': '2026-03-20',  # March Madness time
            'HomeTeamScore': 75,
            'AwayTeamScore': 70,
            'HomeTeam': 'Duke',
            'AwayTeam': 'UNC'
        }
        # During tournament season, should be detected as neutral
        result = is_neutral_court_game(game)
        assert result == True
    
    @pytest.mark.unit
    def test_neutral_flag(self, is_neutral_court_game):
        """Test explicit neutral site flag."""
        game = {
            'date': '2026-01-15',
            'HomeTeamScore': 75,
            'AwayTeamScore': 70,
            'neutral_site': True
        }
        assert is_neutral_court_game(game) == True


class TestPaceAdjustment:
    """Test cases for pace adjustment."""
    
    @pytest.fixture
    def apply_pace_adjustment(self):
        """Import the function from the script."""
        from show_team_ratings_v3 import apply_pace_adjustment
        return apply_pace_adjustment
    
    @pytest.mark.unit
    def test_pace_adjustment_output(self, apply_pace_adjustment):
        """Test that pace adjustment returns two values."""
        off_rating, def_rating = apply_pace_adjustment(75.0, 70.0)
        
        assert isinstance(off_rating, float)
        assert isinstance(def_rating, float)
    
    @pytest.mark.unit
    def test_pace_adjustment_reasonable_values(self, apply_pace_adjustment):
        """Test that pace adjusted values are reasonable."""
        # Typical college basketball: 70-80 PPG
        off_rating, def_rating = apply_pace_adjustment(75.0, 70.0)
        
        # Pace adjusted values should be positive and finite
        assert off_rating > 0 and np.isfinite(off_rating)
        assert def_rating > 0 and np.isfinite(def_rating)
        # Efficiency typically ranges from 40-120 per 100 possessions
        assert 40 < off_rating < 150
        assert 40 < def_rating < 150


class TestTeamRatingsIntegration:
    """Integration tests for the full rating calculation pipeline."""
    
    @pytest.fixture
    def calculate_team_ratings(self):
        """Import the function from the script."""
        from show_team_ratings_v3 import calculate_team_ratings
        return calculate_team_ratings
    
    @pytest.fixture
    def sample_season_games(self):
        """Create a set of games for testing ratings."""
        teams = [
            (1001, 'Duke', 'DUKE'),
            (1002, 'UNC', 'UNC'),
            (1003, 'Kentucky', 'UK'),
            (1004, 'Kansas', 'KU'),
            (1005, 'Gonzaga', 'GONZ'),
            (1006, 'Michigan', 'MICH'),
            (1007, 'Villanova', 'NOVA'),
            (1008, 'Arizona', 'ARIZ'),
        ]
        
        games = []
        base_date = datetime(2025, 11, 15)
        game_id = 20000
        
        # Create round-robin games
        for i, home_team in enumerate(teams):
            for j, away_team in enumerate(teams):
                if i != j:
                    # Vary scores - higher-ranked teams (lower index) generally win
                    home_base = 75 - i * 2  # Better teams score more
                    away_base = 75 - j * 2
                    
                    # Add home advantage
                    home_score = home_base + 3 + np.random.randint(-5, 10)
                    away_score = away_base + np.random.randint(-5, 10)
                    
                    games.append({
                        'GameID': game_id,
                        'DateTime': (base_date + timedelta(days=len(games))).isoformat() + 'Z',
                        'Status': 'Final',
                        'HomeTeamID': home_team[0],
                        'AwayTeamID': away_team[0],
                        'HomeTeam': home_team[2],
                        'AwayTeam': away_team[2],
                        'HomeTeamName': home_team[1],
                        'AwayTeamName': away_team[1],
                        'HomeTeamScore': max(45, home_score),  # Minimum score
                        'AwayTeamScore': max(45, away_score),
                    })
                    game_id += 1
        
        return games
    
    @pytest.mark.unit
    @pytest.mark.slow
    def test_calculate_team_ratings_returns_list(self, calculate_team_ratings, sample_season_games):
        """Test that calculate_team_ratings returns a list."""
        ratings, stats = calculate_team_ratings(sample_season_games, min_games=5)
        
        assert isinstance(ratings, list)
    
    @pytest.mark.unit
    @pytest.mark.slow
    def test_ratings_sorted_by_overall(self, calculate_team_ratings, sample_season_games):
        """Test that ratings are sorted by overall rating (descending)."""
        ratings, stats = calculate_team_ratings(sample_season_games, min_games=5)
        
        overall_ratings = [r['overall_rating'] for r in ratings]
        assert overall_ratings == sorted(overall_ratings, reverse=True)
    
    @pytest.mark.unit
    @pytest.mark.slow
    def test_ratings_contain_required_fields(self, calculate_team_ratings, sample_season_games):
        """Test that each rating contains required fields."""
        ratings, stats = calculate_team_ratings(sample_season_games, min_games=5)
        
        if len(ratings) > 0:
            required_fields = [
                'team_id', 'team_name', 'offensive_rating', 'defensive_rating',
                'overall_rating', 'wins', 'losses', 'games', 'hca'
            ]
            
            for field in required_fields:
                assert field in ratings[0], f"Missing field: {field}"
    
    @pytest.mark.unit
    @pytest.mark.slow
    def test_ratings_respects_min_games(self, calculate_team_ratings, sample_season_games):
        """Test that ratings filter by minimum games."""
        ratings, stats = calculate_team_ratings(sample_season_games, min_games=10)
        
        for rating in ratings:
            assert rating['games'] >= 10


class TestVarianceMetrics:
    """Test cases for variance/consistency metrics."""
    
    @pytest.fixture
    def calculate_variance_metrics(self):
        """Import the function from the script."""
        from show_team_ratings_v3 import calculate_variance_metrics
        return calculate_variance_metrics
    
    @pytest.mark.unit
    def test_variance_no_games(self, calculate_variance_metrics):
        """Test variance calculation with no games."""
        result = calculate_variance_metrics(team_id=1234, games=[])
        
        assert result['variance'] == 0
        assert result['std_dev'] == 0
        assert result['consistency_score'] == 0
    
    @pytest.mark.unit
    def test_consistent_team(self, calculate_variance_metrics):
        """Test variance for consistent team (low variance)."""
        games = [
            {'HomeTeamID': 1234, 'AwayTeamID': 5678, 'HomeTeamScore': 75, 'AwayTeamScore': 70},
            {'HomeTeamID': 1234, 'AwayTeamID': 5679, 'HomeTeamScore': 76, 'AwayTeamScore': 71},
            {'HomeTeamID': 1234, 'AwayTeamID': 5680, 'HomeTeamScore': 74, 'AwayTeamScore': 69},
        ]
        
        result = calculate_variance_metrics(team_id=1234, games=games)
        
        assert result['std_dev'] < 5  # Low standard deviation
        assert result['consistency_score'] > 50  # High consistency
    
    @pytest.mark.unit
    def test_inconsistent_team(self, calculate_variance_metrics):
        """Test variance for inconsistent team (high variance)."""
        games = [
            {'HomeTeamID': 1234, 'AwayTeamID': 5678, 'HomeTeamScore': 95, 'AwayTeamScore': 60},  # +35
            {'HomeTeamID': 1234, 'AwayTeamID': 5679, 'HomeTeamScore': 55, 'AwayTeamScore': 80},  # -25
            {'HomeTeamID': 1234, 'AwayTeamID': 5680, 'HomeTeamScore': 80, 'AwayTeamScore': 70},  # +10
        ]
        
        result = calculate_variance_metrics(team_id=1234, games=games)
        
        assert result['std_dev'] > 10  # High standard deviation

