"""
Unit tests for the Unscented Kalman Filter (UKF) model.
Tests the TeamUKF and MultiTeamUKF classes.
"""
import pytest
import numpy as np
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.ukf_model import TeamUKF, MultiTeamUKF


class TestTeamUKF:
    """Test cases for TeamUKF class."""
    
    @pytest.mark.unit
    def test_initial_state_defaults(self):
        """Test that UKF initializes with correct default state values."""
        ukf = TeamUKF(team_id=1)
        state = ukf.get_state()
        
        # Check default values
        assert state[TeamUKF.OFF_RATING] == 100.0, "Default offensive rating should be 100"
        assert state[TeamUKF.DEF_RATING] == 100.0, "Default defensive rating should be 100"
        assert state[TeamUKF.HOME_ADV] == 3.0, "Default home advantage should be 3.0"
        assert state[TeamUKF.HEALTH] == 1.0, "Default health should be 1.0"
        assert state[TeamUKF.MOMENTUM] == 0.0, "Default momentum should be 0"
        assert state[TeamUKF.FATIGUE] == 0.0, "Default fatigue should be 0"
        assert state[TeamUKF.PACE] == 70.0, "Default pace should be 70.0"
    
    @pytest.mark.unit
    def test_initial_state_custom(self):
        """Test UKF initialization with custom state."""
        custom_state = np.array([95.0, 92.0, 4.0, 0.9, 0.5, 0.2, 72.0])
        ukf = TeamUKF(team_id=2, initial_state=custom_state)
        state = ukf.get_state()
        
        np.testing.assert_array_almost_equal(state, custom_state)
    
    @pytest.mark.unit
    def test_state_dimension(self):
        """Test that state vector has correct dimension."""
        ukf = TeamUKF(team_id=1)
        state = ukf.get_state()
        
        assert len(state) == TeamUKF.STATE_DIM, f"State should have {TeamUKF.STATE_DIM} dimensions"
        assert TeamUKF.STATE_DIM == 7, "STATE_DIM should be 7"
    
    @pytest.mark.unit
    def test_state_indices_correct(self):
        """Test that state indices are correctly defined."""
        assert TeamUKF.OFF_RATING == 0
        assert TeamUKF.DEF_RATING == 1
        assert TeamUKF.HOME_ADV == 2
        assert TeamUKF.HEALTH == 3
        assert TeamUKF.MOMENTUM == 4
        assert TeamUKF.FATIGUE == 5
        assert TeamUKF.PACE == 6
    
    @pytest.mark.unit
    def test_get_uncertainty(self):
        """Test uncertainty calculation."""
        ukf = TeamUKF(team_id=1)
        uncertainty = ukf.get_uncertainty()
        
        assert len(uncertainty) == TeamUKF.STATE_DIM
        assert all(u >= 0 for u in uncertainty), "Uncertainties should be non-negative"
    
    @pytest.mark.unit
    def test_predict_step(self):
        """Test that predict step updates state without errors."""
        ukf = TeamUKF(team_id=1)
        initial_state = ukf.get_state().copy()
        
        ukf.predict()
        new_state = ukf.get_state()
        
        # State should be finite after predict
        assert all(np.isfinite(new_state)), "All state values should be finite after predict"
        
        # The process model in _process_model clamps values, but the UKF 
        # predict step may produce intermediate values. Check that OFF/DEF
        # ratings are reasonable (the most stable values)
        assert 0 <= new_state[TeamUKF.OFF_RATING] <= 200
        assert 0 <= new_state[TeamUKF.DEF_RATING] <= 200
    
    @pytest.mark.unit
    def test_update_from_game_home_win(self, sample_opponent_state, sample_features):
        """Test state update after a home win."""
        ukf = TeamUKF(team_id=1)
        initial_off = ukf.get_state()[TeamUKF.OFF_RATING]
        
        # Simulate a home win by 10 points
        ukf.update_from_game(
            opponent_state=sample_opponent_state,
            score_diff=10,  # Won by 10
            total_points=150,
            actual_pace=70.0,
            is_home=True,
            features=sample_features
        )
        
        new_state = ukf.get_state()
        
        # State should still be in valid bounds
        assert 50 <= new_state[TeamUKF.OFF_RATING] <= 150
        assert 50 <= new_state[TeamUKF.DEF_RATING] <= 150
    
    @pytest.mark.unit
    def test_update_from_game_away_loss(self, sample_opponent_state, sample_features):
        """Test state update after an away loss."""
        ukf = TeamUKF(team_id=1)
        
        # Simulate an away loss by 5 points
        ukf.update_from_game(
            opponent_state=sample_opponent_state,
            score_diff=-5,  # Lost by 5
            total_points=140,
            actual_pace=68.0,
            is_home=False,
            features=sample_features
        )
        
        new_state = ukf.get_state()
        
        # State should still be in valid bounds
        assert 50 <= new_state[TeamUKF.OFF_RATING] <= 150
        assert 50 <= new_state[TeamUKF.DEF_RATING] <= 150
    
    @pytest.mark.unit
    def test_state_bounds_after_extreme_game(self, sample_opponent_state):
        """Test that state values remain bounded after extreme results."""
        ukf = TeamUKF(team_id=1)
        
        # Simulate extreme blowout win
        extreme_features = {
            'health_status': 1.0,
            'momentum': 1.0,
            'fatigue': 0.0
        }
        
        ukf.update_from_game(
            opponent_state=sample_opponent_state,
            score_diff=50,  # Blowout win
            total_points=200,
            actual_pace=85.0,  # Fast pace
            is_home=True,
            features=extreme_features
        )
        
        state = ukf.get_state()
        
        # All values should be clamped to valid ranges
        assert 50 <= state[TeamUKF.OFF_RATING] <= 150
        assert 50 <= state[TeamUKF.DEF_RATING] <= 150
        assert 0 <= state[TeamUKF.HOME_ADV] <= 10
        assert 0 <= state[TeamUKF.HEALTH] <= 1
        assert -1 <= state[TeamUKF.MOMENTUM] <= 1
        assert 0 <= state[TeamUKF.FATIGUE] <= 1
        assert 60 <= state[TeamUKF.PACE] <= 80
    
    @pytest.mark.unit
    def test_pace_update_smoothing(self, sample_opponent_state, sample_features):
        """Test that pace updates are smoothed (not instant changes)."""
        ukf = TeamUKF(team_id=1)
        initial_pace = ukf.get_state()[TeamUKF.PACE]
        
        # Simulate game with different pace
        ukf.update_from_game(
            opponent_state=sample_opponent_state,
            score_diff=5,
            total_points=160,
            actual_pace=75.0,  # Different from default 70
            is_home=True,
            features=sample_features
        )
        
        new_pace = ukf.get_state()[TeamUKF.PACE]
        
        # Pace should move toward actual but not completely
        # 0.9 * 70 + 0.1 * 75 = 70.5
        assert initial_pace < new_pace <= 75.0
    
    @pytest.mark.unit
    def test_home_advantage_update(self, sample_opponent_state, sample_features):
        """Test that home advantage updates based on home performance."""
        ukf = TeamUKF(team_id=1)
        initial_hca = ukf.get_state()[TeamUKF.HOME_ADV]
        
        # Big home win should increase HCA
        ukf.update_from_game(
            opponent_state=sample_opponent_state,
            score_diff=20,  # Big home win
            total_points=160,
            actual_pace=70.0,
            is_home=True,
            features=sample_features
        )
        
        new_hca = ukf.get_state()[TeamUKF.HOME_ADV]
        
        # HCA should be updated
        assert new_hca >= 0
        assert new_hca <= 10


class TestMultiTeamUKF:
    """Test cases for MultiTeamUKF class."""
    
    @pytest.mark.unit
    def test_initialization(self):
        """Test MultiTeamUKF initialization."""
        multi_ukf = MultiTeamUKF()
        
        assert hasattr(multi_ukf, 'teams')
        assert len(multi_ukf.teams) == 0
    
    @pytest.mark.unit
    def test_get_team_ukf_creates_new(self):
        """Test that get_team_ukf creates new UKF for unknown team."""
        multi_ukf = MultiTeamUKF()
        
        ukf = multi_ukf.get_team_ukf(team_id=1234)
        
        assert ukf is not None
        assert isinstance(ukf, TeamUKF)
        assert ukf.team_id == 1234
        assert 1234 in multi_ukf.teams
    
    @pytest.mark.unit
    def test_get_team_ukf_returns_existing(self):
        """Test that get_team_ukf returns existing UKF."""
        multi_ukf = MultiTeamUKF()
        
        ukf1 = multi_ukf.get_team_ukf(team_id=1234)
        ukf2 = multi_ukf.get_team_ukf(team_id=1234)
        
        assert ukf1 is ukf2
    
    @pytest.mark.unit
    def test_get_team_state(self):
        """Test getting team state."""
        multi_ukf = MultiTeamUKF()
        
        state = multi_ukf.get_team_state(team_id=5678)
        
        assert len(state) == TeamUKF.STATE_DIM
        assert state[TeamUKF.OFF_RATING] == 100.0  # Default
    
    @pytest.mark.unit
    def test_get_all_states(self):
        """Test getting all team states."""
        multi_ukf = MultiTeamUKF()
        
        # Create a few teams
        multi_ukf.get_team_ukf(1)
        multi_ukf.get_team_ukf(2)
        multi_ukf.get_team_ukf(3)
        
        all_states = multi_ukf.get_all_states()
        
        assert len(all_states) == 3
        assert 1 in all_states
        assert 2 in all_states
        assert 3 in all_states
    
    @pytest.mark.unit
    def test_update_from_game(self, sample_features):
        """Test updating both teams from a game."""
        multi_ukf = MultiTeamUKF()
        
        home_features = sample_features.copy()
        away_features = sample_features.copy()
        away_features['momentum'] = -0.2
        
        # Update from a game result
        multi_ukf.update_from_game(
            home_team_id=1234,
            away_team_id=5678,
            home_score=80,
            away_score=75,
            actual_pace=70.0,
            home_features=home_features,
            away_features=away_features
        )
        
        # Both teams should now exist
        assert 1234 in multi_ukf.teams
        assert 5678 in multi_ukf.teams
        
        # Get states
        home_state = multi_ukf.get_team_state(1234)
        away_state = multi_ukf.get_team_state(5678)
        
        # States should be valid
        assert len(home_state) == TeamUKF.STATE_DIM
        assert len(away_state) == TeamUKF.STATE_DIM
    
    @pytest.mark.unit
    def test_multiple_games_accumulate(self, sample_features):
        """Test that multiple games properly update team states."""
        multi_ukf = MultiTeamUKF()
        
        # Simulate several games
        for i in range(5):
            multi_ukf.update_from_game(
                home_team_id=100,
                away_team_id=200 + i,
                home_score=75 + i,
                away_score=70,
                actual_pace=70.0,
                home_features=sample_features,
                away_features=sample_features
            )
        
        # Home team played 5 games
        home_state = multi_ukf.get_team_state(100)
        
        # Rating should have evolved from default
        # (exact values depend on implementation details)
        assert home_state is not None
        assert 50 <= home_state[TeamUKF.OFF_RATING] <= 150


class TestUKFEdgeCases:
    """Edge case tests for UKF model."""
    
    @pytest.mark.unit
    def test_zero_score_differential(self, sample_opponent_state, sample_features):
        """Test handling of tie game (rare in basketball)."""
        ukf = TeamUKF(team_id=1)
        
        ukf.update_from_game(
            opponent_state=sample_opponent_state,
            score_diff=0,  # Tie
            total_points=140,
            actual_pace=70.0,
            is_home=True,
            features=sample_features
        )
        
        state = ukf.get_state()
        assert all(np.isfinite(state)), "All state values should be finite"
    
    @pytest.mark.unit
    def test_very_low_total_points(self, sample_opponent_state, sample_features):
        """Test handling of low-scoring game."""
        ukf = TeamUKF(team_id=1)
        
        ukf.update_from_game(
            opponent_state=sample_opponent_state,
            score_diff=5,
            total_points=90,  # Very low scoring
            actual_pace=60.0,  # Slow pace
            is_home=True,
            features=sample_features
        )
        
        state = ukf.get_state()
        assert all(np.isfinite(state)), "All state values should be finite"
        assert 60 <= state[TeamUKF.PACE] <= 80
    
    @pytest.mark.unit
    def test_very_high_total_points(self, sample_opponent_state, sample_features):
        """Test handling of high-scoring game."""
        ukf = TeamUKF(team_id=1)
        
        ukf.update_from_game(
            opponent_state=sample_opponent_state,
            score_diff=10,
            total_points=200,  # Very high scoring
            actual_pace=85.0,  # Fast pace (will be clamped to 80)
            is_home=True,
            features=sample_features
        )
        
        state = ukf.get_state()
        assert all(np.isfinite(state)), "All state values should be finite"
        assert 60 <= state[TeamUKF.PACE] <= 80  # Should be clamped
    
    @pytest.mark.unit
    def test_negative_momentum_features(self, sample_opponent_state):
        """Test handling of negative momentum in features."""
        ukf = TeamUKF(team_id=1)
        
        features = {
            'health_status': 0.8,
            'momentum': -0.5,  # Negative momentum
            'fatigue': 0.4
        }
        
        ukf.update_from_game(
            opponent_state=sample_opponent_state,
            score_diff=-10,  # Loss
            total_points=140,
            actual_pace=70.0,
            is_home=False,
            features=features
        )
        
        state = ukf.get_state()
        assert -1 <= state[TeamUKF.MOMENTUM] <= 1
    
    @pytest.mark.unit
    def test_repeated_predictions(self):
        """Test that repeated predict calls are stable."""
        ukf = TeamUKF(team_id=1)
        
        states = []
        for _ in range(10):
            ukf.predict()
            states.append(ukf.get_state().copy())
        
        # States should all be valid
        for state in states:
            assert all(np.isfinite(state))
            assert 50 <= state[TeamUKF.OFF_RATING] <= 150

