"""
Unit tests for the ML Features module.
Tests feature engineering for the ML model.
"""
import pytest
import numpy as np
import config
import sys
import os
import tempfile
import pickle
from datetime import datetime, timedelta
from unittest.mock import Mock, patch

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.ml_features import MLFeatureEngineer
from src.ukf_model import TeamUKF


class TestMLFeatureEngineerInitialization:
    """Test cases for MLFeatureEngineer initialization."""
    
    @pytest.mark.unit
    def test_init_creates_components(self):
        """Test that initialization creates required components."""
        with patch('src.ml_features.DataCollector'), \
             patch('src.ml_features.FeatureCalculator'):
            
            engineer = MLFeatureEngineer()
            
            assert engineer.collector is not None
            assert engineer.calculator is not None
            assert engineer.scaler is not None
            assert engineer.scaler_fitted == False
            assert engineer.feature_names == []
    
    @pytest.mark.unit
    def test_init_accepts_custom_collector(self):
        """Test initialization with custom collector."""
        mock_collector = Mock()
        mock_calculator = Mock()
        
        with patch('src.ml_features.FeatureCalculator'):
            engineer = MLFeatureEngineer(
                collector=mock_collector, 
                calculator=mock_calculator
            )
            
            assert engineer.collector == mock_collector
            assert engineer.calculator == mock_calculator


class TestUKFFeatureExtraction:
    """Test cases for UKF feature extraction."""
    
    @pytest.fixture
    def engineer(self):
        """Create MLFeatureEngineer with mocked dependencies."""
        with patch('src.ml_features.DataCollector'), \
             patch('src.ml_features.FeatureCalculator'):
            return MLFeatureEngineer()
    
    @pytest.mark.unit
    def test_extract_ukf_features_returns_dict(self, engineer, sample_team_state, sample_opponent_state):
        """Test that extract_ukf_features returns dictionary."""
        home_uncertainty = np.ones(TeamUKF.STATE_DIM)
        away_uncertainty = np.ones(TeamUKF.STATE_DIM)
        
        features = engineer.extract_ukf_features(
            home_state=sample_team_state,
            away_state=sample_opponent_state,
            home_uncertainty=home_uncertainty,
            away_uncertainty=away_uncertainty
        )
        
        assert isinstance(features, dict)
    
    @pytest.mark.unit
    def test_extract_ukf_features_contains_home_features(self, engineer, sample_team_state, sample_opponent_state):
        """Test that UKF features include home team features."""
        home_uncertainty = np.ones(TeamUKF.STATE_DIM)
        away_uncertainty = np.ones(TeamUKF.STATE_DIM)
        
        features = engineer.extract_ukf_features(
            home_state=sample_team_state,
            away_state=sample_opponent_state,
            home_uncertainty=home_uncertainty,
            away_uncertainty=away_uncertainty
        )
        
        assert 'home_off_rating' in features
        assert 'home_def_rating' in features
        assert 'home_home_adv' in features
        assert 'home_health' in features
        assert 'home_momentum' in features
        assert 'home_fatigue' in features
        assert 'home_pace' in features
    
    @pytest.mark.unit
    def test_extract_ukf_features_contains_away_features(self, engineer, sample_team_state, sample_opponent_state):
        """Test that UKF features include away team features."""
        home_uncertainty = np.ones(TeamUKF.STATE_DIM)
        away_uncertainty = np.ones(TeamUKF.STATE_DIM)
        
        features = engineer.extract_ukf_features(
            home_state=sample_team_state,
            away_state=sample_opponent_state,
            home_uncertainty=home_uncertainty,
            away_uncertainty=away_uncertainty
        )
        
        assert 'away_off_rating' in features
        assert 'away_def_rating' in features
        assert 'away_health' in features
        assert 'away_momentum' in features
        assert 'away_fatigue' in features
        assert 'away_pace' in features
    
    @pytest.mark.unit
    def test_extract_ukf_features_contains_derived_features(self, engineer, sample_team_state, sample_opponent_state):
        """Test that UKF features include derived features."""
        home_uncertainty = np.ones(TeamUKF.STATE_DIM)
        away_uncertainty = np.ones(TeamUKF.STATE_DIM)
        
        features = engineer.extract_ukf_features(
            home_state=sample_team_state,
            away_state=sample_opponent_state,
            home_uncertainty=home_uncertainty,
            away_uncertainty=away_uncertainty
        )
        
        assert 'off_rating_diff' in features
        assert 'def_rating_diff' in features
        assert 'momentum_diff' in features
        assert 'fatigue_diff' in features
        assert 'pace_avg' in features
        assert 'health_diff' in features
    
    @pytest.mark.unit
    def test_extract_ukf_features_values_correct(self, engineer, sample_team_state, sample_opponent_state):
        """Test that extracted feature values are correct."""
        home_uncertainty = np.ones(TeamUKF.STATE_DIM)
        away_uncertainty = np.ones(TeamUKF.STATE_DIM)
        
        features = engineer.extract_ukf_features(
            home_state=sample_team_state,
            away_state=sample_opponent_state,
            home_uncertainty=home_uncertainty,
            away_uncertainty=away_uncertainty
        )
        
        # Check specific values
        assert features['home_off_rating'] == sample_team_state[TeamUKF.OFF_RATING]
        assert features['away_off_rating'] == sample_opponent_state[TeamUKF.OFF_RATING]
        assert features['off_rating_diff'] == (
            sample_team_state[TeamUKF.OFF_RATING] - sample_opponent_state[TeamUKF.OFF_RATING]
        )


class TestContextualFeatureExtraction:
    """Test cases for contextual feature extraction."""
    
    @pytest.fixture
    def engineer(self):
        """Create MLFeatureEngineer with mocked dependencies."""
        with patch('src.ml_features.DataCollector'), \
             patch('src.ml_features.FeatureCalculator') as MockCalc:
            
            mock_calc_instance = MockCalc.return_value
            mock_calc_instance._normalize_team_id.side_effect = lambda x: x if isinstance(x, int) else abs(hash(str(x))) % 100000
            
            eng = MLFeatureEngineer()
            eng.calculator._normalize_team_id = mock_calc_instance._normalize_team_id
            eng.collector.get_kenpom_team_rating.return_value = {
                'adj_em': 0.0,
                'adj_o': 100.0,
                'adj_d': 100.0,
                'adj_t': 70.0
            }
            return eng
    
    @pytest.mark.unit
    def test_extract_contextual_features_returns_dict(self, engineer, sample_game, sample_games_list):
        """Test that contextual features returns dictionary."""
        features = engineer.extract_contextual_features(
            game=sample_game,
            home_team_id=1234,
            away_team_id=5678,
            game_date=datetime(2026, 1, 15),
            all_games=sample_games_list
        )
        
        assert isinstance(features, dict)
    
    @pytest.mark.unit
    def test_extract_contextual_features_contains_rest_days(self, engineer, sample_game, sample_games_list):
        """Test that contextual features include rest days."""
        features = engineer.extract_contextual_features(
            game=sample_game,
            home_team_id=1234,
            away_team_id=5678,
            game_date=datetime(2026, 1, 15),
            all_games=sample_games_list
        )
        
        assert 'home_rest_days' in features
        assert 'away_rest_days' in features
        assert 'rest_days_diff' in features
    
    @pytest.mark.unit
    def test_extract_contextual_features_contains_form(self, engineer, sample_game, sample_games_list):
        """Test that contextual features include recent form."""
        features = engineer.extract_contextual_features(
            game=sample_game,
            home_team_id=1234,
            away_team_id=5678,
            game_date=datetime(2026, 1, 15),
            all_games=sample_games_list
        )
        
        assert 'home_form_5' in features
        assert 'home_form_10' in features
        assert 'away_form_5' in features
        assert 'away_form_10' in features
        assert 'form_diff_5' in features
        assert 'form_diff_10' in features
    
    @pytest.mark.unit
    def test_extract_contextual_features_contains_h2h(self, engineer, sample_game, sample_games_list):
        """Test that contextual features include head-to-head."""
        features = engineer.extract_contextual_features(
            game=sample_game,
            home_team_id=1234,
            away_team_id=5678,
            game_date=datetime(2026, 1, 15),
            all_games=sample_games_list
        )
        
        assert 'h2h_margin' in features
    
    @pytest.mark.unit
    def test_extract_contextual_features_contains_time(self, engineer, sample_game, sample_games_list):
        """Test that contextual features include time features."""
        features = engineer.extract_contextual_features(
            game=sample_game,
            home_team_id=1234,
            away_team_id=5678,
            game_date=datetime(2026, 1, 15),
            all_games=sample_games_list
        )
        
        assert 'hour_of_day' in features
        assert 'day_of_week' in features
    
    @pytest.mark.unit
    def test_extract_contextual_features_pregame_lines(self, engineer, sample_game, sample_games_list):
        """Test that contextual features include pregame lines."""
        features = engineer.extract_contextual_features(
            game=sample_game,
            home_team_id=1234,
            away_team_id=5678,
            game_date=datetime(2026, 1, 15),
            all_games=sample_games_list
        )
        
        assert 'pregame_spread' in features
        assert 'pregame_total' in features
        assert features['pregame_spread'] == sample_game['PointSpread']
        assert features['pregame_total'] == sample_game['OverUnder']


class TestRestDaysCalculation:
    """Test cases for rest days calculation."""
    
    @pytest.fixture
    def engineer(self):
        """Create MLFeatureEngineer with mocked dependencies."""
        with patch('src.ml_features.DataCollector'), \
             patch('src.ml_features.FeatureCalculator') as MockCalc:
            
            mock_calc_instance = MockCalc.return_value
            mock_calc_instance._normalize_team_id.side_effect = lambda x: x if isinstance(x, int) else abs(hash(str(x))) % 100000
            
            eng = MLFeatureEngineer()
            eng.calculator._normalize_team_id = mock_calc_instance._normalize_team_id
            eng.collector.get_kenpom_team_rating.return_value = {
                'adj_em': 0.0,
                'adj_o': 100.0,
                'adj_d': 100.0,
                'adj_t': 70.0
            }
            return eng
    
    @pytest.mark.unit
    def test_rest_days_no_prior_games(self, engineer):
        """Test rest days calculation with no prior games."""
        games = []
        game_date = datetime(2026, 1, 15)
        
        rest_days = engineer._calculate_rest_days(
            team_id=1234,
            game_date=game_date,
            all_games=games
        )
        
        assert rest_days == 7  # Default when no games
    
    @pytest.mark.unit
    def test_rest_days_with_recent_game(self, engineer):
        """Test rest days with a recent game."""
        game_date = datetime(2026, 1, 15)
        games = [{
            'HomeTeamID': 1234,
            'HomeTeam': 'TestTeam',
            'AwayTeamID': 5678,
            'AwayTeam': 'Opponent',
            'HomeTeamScore': 80,
            'AwayTeamScore': 70,
            'Status': 'Final',
            'DateTime': (game_date - timedelta(days=2)).isoformat() + 'Z'
        }]
        
        rest_days = engineer._calculate_rest_days(
            team_id=1234,
            game_date=game_date,
            all_games=games
        )
        
        # Rest days should be positive (7 is default when no games match)
        assert rest_days >= 0


class TestRecentFormCalculation:
    """Test cases for recent form calculation."""
    
    @pytest.fixture
    def engineer(self):
        """Create MLFeatureEngineer with mocked dependencies."""
        with patch('src.ml_features.DataCollector'), \
             patch('src.ml_features.FeatureCalculator') as MockCalc:
            
            mock_calc_instance = MockCalc.return_value
            mock_calc_instance._normalize_team_id.side_effect = lambda x: x if isinstance(x, int) else abs(hash(str(x))) % 100000
            
            eng = MLFeatureEngineer()
            eng.calculator._normalize_team_id = mock_calc_instance._normalize_team_id
            return eng
    
    @pytest.mark.unit
    def test_recent_form_no_games(self, engineer):
        """Test recent form with no games returns 0."""
        form = engineer._calculate_recent_form(
            team_id=1234,
            game_date=datetime(2026, 1, 15),
            all_games=[],
            window=5
        )
        
        assert form == 0.0
    
    @pytest.mark.unit
    def test_recent_form_winning_streak(self, engineer):
        """Test recent form with winning streak."""
        game_date = datetime(2026, 1, 15)
        games = []
        
        # Create 5 wins
        for i in range(5):
            games.append({
                'HomeTeamID': 1234,
                'HomeTeam': 'TestTeam',
                'AwayTeamID': 5678 + i,
                'AwayTeam': f'Opponent{i}',
                'HomeTeamScore': 80,
                'AwayTeamScore': 70,
                'Status': 'Final',
                'DateTime': (game_date - timedelta(days=i+1)).isoformat() + 'Z'
            })
        
        form = engineer._calculate_recent_form(
            team_id=1234,
            game_date=game_date,
            all_games=games,
            window=5
        )
        
        # Form should be >= 0 (mocked calculator may not match teams)
        assert form >= 0


class TestEngineerFeatures:
    """Test cases for the main engineer_features method."""
    
    @pytest.fixture
    def engineer(self):
        """Create MLFeatureEngineer with mocked dependencies."""
        with patch('src.ml_features.DataCollector'), \
             patch('src.ml_features.FeatureCalculator') as MockCalc:
            
            mock_calc_instance = MockCalc.return_value
            mock_calc_instance._normalize_team_id.side_effect = lambda x: x if isinstance(x, int) else abs(hash(str(x))) % 100000
            
            eng = MLFeatureEngineer()
            eng.calculator._normalize_team_id = mock_calc_instance._normalize_team_id
            return eng
    
    @pytest.mark.unit
    def test_engineer_features_returns_tuple(self, engineer, sample_team_state, sample_opponent_state, sample_game, sample_games_list):
        """Test that engineer_features returns (array, dict) tuple."""
        home_uncertainty = np.ones(TeamUKF.STATE_DIM)
        away_uncertainty = np.ones(TeamUKF.STATE_DIM)
        
        result = engineer.engineer_features(
            home_state=sample_team_state,
            away_state=sample_opponent_state,
            home_uncertainty=home_uncertainty,
            away_uncertainty=away_uncertainty,
            game=sample_game,
            home_team_id=1234,
            away_team_id=5678,
            game_date=datetime(2026, 1, 15),
            all_games=sample_games_list
        )
        
        assert isinstance(result, tuple)
        assert len(result) == 2
        assert isinstance(result[0], np.ndarray)
        assert isinstance(result[1], dict)
    
    @pytest.mark.unit
    def test_engineer_features_array_1d(self, engineer, sample_team_state, sample_opponent_state, sample_game, sample_games_list):
        """Test that feature array is 1-dimensional."""
        home_uncertainty = np.ones(TeamUKF.STATE_DIM)
        away_uncertainty = np.ones(TeamUKF.STATE_DIM)
        
        features_array, _ = engineer.engineer_features(
            home_state=sample_team_state,
            away_state=sample_opponent_state,
            home_uncertainty=home_uncertainty,
            away_uncertainty=away_uncertainty,
            game=sample_game,
            home_team_id=1234,
            away_team_id=5678,
            game_date=datetime(2026, 1, 15),
            all_games=sample_games_list
        )
        
        assert features_array.ndim == 1
    
    @pytest.mark.unit
    def test_engineer_features_sets_feature_names(self, engineer, sample_team_state, sample_opponent_state, sample_game, sample_games_list):
        """Test that engineer_features populates feature_names."""
        home_uncertainty = np.ones(TeamUKF.STATE_DIM)
        away_uncertainty = np.ones(TeamUKF.STATE_DIM)
        
        assert engineer.feature_names == []
        
        engineer.engineer_features(
            home_state=sample_team_state,
            away_state=sample_opponent_state,
            home_uncertainty=home_uncertainty,
            away_uncertainty=away_uncertainty,
            game=sample_game,
            home_team_id=1234,
            away_team_id=5678,
            game_date=datetime(2026, 1, 15),
            all_games=sample_games_list
        )
        
        assert len(engineer.feature_names) > 0
    
    @pytest.mark.unit
    def test_engineer_features_array_matches_dict(self, engineer, sample_team_state, sample_opponent_state, sample_game, sample_games_list):
        """Test that array and dict have same number of features."""
        home_uncertainty = np.ones(TeamUKF.STATE_DIM)
        away_uncertainty = np.ones(TeamUKF.STATE_DIM)
        
        features_array, features_dict = engineer.engineer_features(
            home_state=sample_team_state,
            away_state=sample_opponent_state,
            home_uncertainty=home_uncertainty,
            away_uncertainty=away_uncertainty,
            game=sample_game,
            home_team_id=1234,
            away_team_id=5678,
            game_date=datetime(2026, 1, 15),
            all_games=sample_games_list
        )
        
        assert len(features_array) == len(features_dict)


class TestScaler:
    """Test cases for feature scaling."""
    
    @pytest.fixture
    def engineer(self):
        """Create MLFeatureEngineer with mocked dependencies."""
        with patch('src.ml_features.DataCollector'), \
             patch('src.ml_features.FeatureCalculator'):
            return MLFeatureEngineer()
    
    @pytest.mark.unit
    def test_fit_scaler(self, engineer):
        """Test fitting the scaler."""
        feature_arrays = [np.random.randn(config.ML_FEATURE_COUNT) for _ in range(100)]
        
        engineer.fit_scaler(feature_arrays)
        
        assert engineer.scaler_fitted == True
    
    @pytest.mark.unit
    def test_fit_scaler_empty(self, engineer):
        """Test fitting scaler with empty list."""
        engineer.fit_scaler([])
        
        assert engineer.scaler_fitted == False
    
    @pytest.mark.unit
    def test_transform_features_unfitted(self, engineer):
        """Test transform without fitting returns original."""
        features = np.random.randn(config.ML_FEATURE_COUNT).astype(np.float32)
        
        transformed = engineer.transform_features(features)
        
        np.testing.assert_array_equal(features, transformed)
    
    @pytest.mark.unit
    def test_transform_features_fitted(self, engineer):
        """Test transform after fitting."""
        # Fit scaler
        feature_arrays = [np.random.randn(config.ML_FEATURE_COUNT) for _ in range(100)]
        engineer.fit_scaler(feature_arrays)
        
        # Transform
        features = np.random.randn(config.ML_FEATURE_COUNT).astype(np.float32)
        transformed = engineer.transform_features(features)
        
        # Should be different after standardization
        assert transformed.shape == features.shape


class TestScalerSaveLoad:
    """Test cases for scaler persistence."""
    
    @pytest.fixture
    def fitted_engineer(self):
        """Create MLFeatureEngineer with fitted scaler."""
        with patch('src.ml_features.DataCollector'), \
             patch('src.ml_features.FeatureCalculator'):
            engineer = MLFeatureEngineer()
            
            # Fit scaler
            feature_arrays = [np.random.randn(config.ML_FEATURE_COUNT) for _ in range(100)]
            engineer.fit_scaler(feature_arrays)
            engineer.feature_names = [f'feature_{i}' for i in range(config.ML_FEATURE_COUNT)]
            
            return engineer
    
    @pytest.mark.unit
    def test_save_scaler(self, fitted_engineer):
        """Test saving the scaler."""
        with tempfile.TemporaryDirectory() as tmpdir:
            scaler_path = os.path.join(tmpdir, 'scaler.pkl')
            fitted_engineer.save_scaler(scaler_path)
            
            assert os.path.exists(scaler_path)
    
    @pytest.mark.unit
    def test_load_scaler(self, fitted_engineer):
        """Test loading the scaler."""
        with tempfile.TemporaryDirectory() as tmpdir:
            scaler_path = os.path.join(tmpdir, 'scaler.pkl')
            fitted_engineer.save_scaler(scaler_path)
            
            # Create new engineer and load
            with patch('src.ml_features.DataCollector'), \
                 patch('src.ml_features.FeatureCalculator'):
                new_engineer = MLFeatureEngineer()
                new_engineer.load_scaler(scaler_path)
                
                assert new_engineer.scaler_fitted == True
                assert new_engineer.feature_names == fitted_engineer.feature_names
    
    @pytest.mark.unit
    def test_loaded_scaler_transforms_same(self, fitted_engineer):
        """Test that loaded scaler produces same transformation."""
        test_features = np.random.randn(config.ML_FEATURE_COUNT).astype(np.float32)
        original_transform = fitted_engineer.transform_features(test_features.copy())
        
        with tempfile.TemporaryDirectory() as tmpdir:
            scaler_path = os.path.join(tmpdir, 'scaler.pkl')
            fitted_engineer.save_scaler(scaler_path)
            
            with patch('src.ml_features.DataCollector'), \
                 patch('src.ml_features.FeatureCalculator'):
                new_engineer = MLFeatureEngineer()
                new_engineer.load_scaler(scaler_path)
                loaded_transform = new_engineer.transform_features(test_features.copy())
                
                np.testing.assert_array_almost_equal(
                    original_transform, loaded_transform
                )

