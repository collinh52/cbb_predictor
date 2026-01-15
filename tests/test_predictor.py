"""
Unit tests for the Predictor module.
Tests the main prediction engine.
"""
import pytest
import numpy as np
import sys
import os
from datetime import datetime
from unittest.mock import Mock, patch, MagicMock

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.predictor import Predictor
from src.ukf_model import TeamUKF


class TestPredictorInitialization:
    """Test cases for Predictor initialization."""
    
    @pytest.mark.unit
    def test_predictor_creates_components(self):
        """Test that Predictor initializes with required components."""
        with patch('src.predictor.DataCollector') as MockCollector, \
             patch('src.predictor.FeatureCalculator') as MockCalculator:
            
            MockCollector.return_value.get_completed_games.return_value = []
            MockCollector.return_value.get_kenpom_team_rating.return_value = {
                'adj_em': 0.0,
                'adj_o': 100.0,
                'adj_d': 100.0,
                'adj_t': 70.0
            }
            MockCollector.return_value.get_kenpom_team_rating.return_value = {
                'adj_em': 0.0,
                'adj_o': 100.0,
                'adj_d': 100.0,
                'adj_t': 70.0
            }
            
            predictor = Predictor()
            
            assert predictor.collector is not None
            assert predictor.calculator is not None
            assert predictor.ukf is not None
            assert predictor.initialized == False
    
    @pytest.mark.unit
    def test_predictor_not_initialized_by_default(self):
        """Test that Predictor starts uninitialized."""
        with patch('src.predictor.DataCollector') as MockCollector, \
             patch('src.predictor.FeatureCalculator') as MockCalculator:
            
            MockCollector.return_value.get_completed_games.return_value = []
            MockCollector.return_value.get_kenpom_team_rating.return_value = {
                'adj_em': 0.0,
                'adj_o': 100.0,
                'adj_d': 100.0,
                'adj_t': 70.0
            }
            MockCollector.return_value.get_kenpom_team_rating.return_value = {
                'adj_em': 0.0,
                'adj_o': 100.0,
                'adj_d': 100.0,
                'adj_t': 70.0
            }
            
            predictor = Predictor()
            
            assert not predictor.initialized


class TestTeamIdExtraction:
    """Test cases for team ID extraction and normalization."""
    
    @pytest.fixture
    def predictor(self):
        """Create a Predictor with mocked dependencies."""
        with patch('src.predictor.DataCollector') as MockCollector, \
             patch('src.predictor.FeatureCalculator') as MockCalculator:
            
            MockCollector.return_value.get_completed_games.return_value = []
            MockCollector.return_value.get_kenpom_team_rating.return_value = {
                'adj_em': 0.0,
                'adj_o': 100.0,
                'adj_d': 100.0,
                'adj_t': 70.0
            }
            MockCollector.return_value.get_kenpom_team_rating.return_value = {
                'adj_em': 0.0,
                'adj_o': 100.0,
                'adj_d': 100.0,
                'adj_t': 70.0
            }
            pred = Predictor()
            return pred
    
    @pytest.mark.unit
    def test_get_team_id_from_id_field(self, predictor):
        """Test extracting team ID from ID field."""
        game = {'HomeTeamID': 1234, 'HomeTeam': 'DUKE'}
        
        team_id = predictor._get_team_id(game, 'HomeTeam', 'HomeTeamID')
        
        assert team_id == 1234
    
    @pytest.mark.unit
    def test_get_team_id_from_name_fallback(self, predictor):
        """Test fallback to team name hash when ID is missing."""
        game = {'HomeTeamID': None, 'HomeTeam': 'DUKE'}
        
        team_id = predictor._get_team_id(game, 'HomeTeam', 'HomeTeamID')
        
        assert team_id is not None
        assert isinstance(team_id, int)
    
    @pytest.mark.unit
    def test_get_team_id_returns_none_for_missing(self, predictor):
        """Test that missing team data returns None."""
        game = {}
        
        team_id = predictor._get_team_id(game, 'HomeTeam', 'HomeTeamID')
        
        assert team_id is None
    
    @pytest.mark.unit
    def test_normalize_team_id_int(self, predictor):
        """Test normalizing integer team ID."""
        result = predictor._normalize_team_id(1234)
        
        assert result == 1234
    
    @pytest.mark.unit
    def test_normalize_team_id_string_number(self, predictor):
        """Test normalizing string that's a number."""
        result = predictor._normalize_team_id("1234")
        
        assert result == 1234
    
    @pytest.mark.unit
    def test_normalize_team_id_string_name(self, predictor):
        """Test normalizing team name string to hash."""
        result = predictor._normalize_team_id("Duke Blue Devils")
        
        assert result is not None
        assert isinstance(result, int)
        assert result >= 0
    
    @pytest.mark.unit
    def test_normalize_team_id_consistent(self, predictor):
        """Test that same name produces same ID."""
        result1 = predictor._normalize_team_id("Duke Blue Devils")
        result2 = predictor._normalize_team_id("Duke Blue Devils")
        
        assert result1 == result2


class TestGamePrediction:
    """Test cases for game prediction."""
    
    @pytest.fixture
    def predictor(self):
        """Create a Predictor with mocked dependencies."""
        with patch('src.predictor.DataCollector') as MockCollector, \
             patch('src.predictor.FeatureCalculator') as MockCalculator:
            
            MockCollector.return_value.get_completed_games.return_value = []
            MockCollector.return_value.get_kenpom_team_rating.return_value = {
                'adj_em': 0.0,
                'adj_o': 100.0,
                'adj_d': 100.0,
                'adj_t': 70.0
            }
            MockCalculator.return_value.get_game_features.return_value = {
                'momentum': 0.1,
                'fatigue': 0.1,
                'health_status': 1.0,
                'home_advantage': 3.0,
                'pace': 70.0
            }
            
            pred = Predictor()
            pred.initialized = True
            return pred
    
    @pytest.mark.unit
    def test_predict_game_returns_required_fields(self, predictor, sample_game):
        """Test that predict_game returns all required fields."""
        prediction = predictor.predict_game(sample_game)
        
        required_fields = [
            'predicted_margin',
            'predicted_total',
            'margin_uncertainty',
            'total_uncertainty',
            'predicted_winner',
        ]
        
        for field in required_fields:
            assert field in prediction, f"Missing field: {field}"
    
    @pytest.mark.unit
    def test_predict_game_with_spread(self, predictor, sample_game):
        """Test prediction with spread included."""
        prediction = predictor.predict_game(sample_game)
        
        # Should have spread-related fields
        assert 'spread' in prediction
        assert 'home_covers_probability' in prediction
        assert 'away_covers_probability' in prediction
        assert 'home_covers_confidence' in prediction
    
    @pytest.mark.unit
    def test_predict_game_with_total(self, predictor, sample_game):
        """Test prediction with over/under total."""
        prediction = predictor.predict_game(sample_game)
        
        # Should have total-related fields
        assert 'total_line' in prediction
        assert 'over_probability' in prediction
        assert 'under_probability' in prediction
        assert 'over_confidence' in prediction
    
    @pytest.mark.unit
    def test_predict_game_probabilities_valid(self, predictor, sample_game):
        """Test that probabilities are valid (0-1 range)."""
        prediction = predictor.predict_game(sample_game)
        
        if prediction['home_covers_probability'] is not None:
            assert 0 <= prediction['home_covers_probability'] <= 1
            assert 0 <= prediction['away_covers_probability'] <= 1
            # Should sum to 1
            assert abs(prediction['home_covers_probability'] + 
                      prediction['away_covers_probability'] - 1.0) < 0.001
        
        if prediction['over_probability'] is not None:
            assert 0 <= prediction['over_probability'] <= 1
            assert 0 <= prediction['under_probability'] <= 1
    
    @pytest.mark.unit
    def test_predict_game_winner_matches_margin(self, predictor, sample_game):
        """Test that predicted winner matches margin sign."""
        prediction = predictor.predict_game(sample_game)
        
        if prediction['predicted_margin'] > 0:
            assert prediction['predicted_winner'] == 'home'
        elif prediction['predicted_margin'] < 0:
            assert prediction['predicted_winner'] == 'away'
    
    @pytest.mark.unit
    def test_predict_game_missing_teams(self, predictor):
        """Test prediction with missing team info."""
        bad_game = {'DateTime': '2026-01-15T19:00:00Z'}
        
        prediction = predictor.predict_game(bad_game)
        
        # Should return empty prediction
        assert prediction['predicted_margin'] == 0.0
        assert prediction['overall_confidence'] == 0.0


class TestEmptyPrediction:
    """Test cases for empty prediction structure."""
    
    @pytest.fixture
    def predictor(self):
        """Create a Predictor with mocked dependencies."""
        with patch('src.predictor.DataCollector') as MockCollector, \
             patch('src.predictor.FeatureCalculator') as MockCalculator:
            
            MockCollector.return_value.get_completed_games.return_value = []
            MockCollector.return_value.get_kenpom_team_rating.return_value = {
                'adj_em': 0.0,
                'adj_o': 100.0,
                'adj_d': 100.0,
                'adj_t': 70.0
            }
            pred = Predictor()
            return pred
    
    @pytest.mark.unit
    def test_empty_prediction_structure(self, predictor):
        """Test _empty_prediction returns correct structure."""
        empty = predictor._empty_prediction()
        
        assert empty['predicted_margin'] == 0.0
        assert empty['predicted_total'] == 0.0
        assert empty['margin_uncertainty'] == 0.0
        assert empty['total_uncertainty'] == 0.0
        assert empty['predicted_winner'] is None
        assert empty['spread'] is None
        assert empty['total_line'] is None
        assert empty['overall_confidence'] == 0.0


class TestTeamRatings:
    """Test cases for team ratings retrieval."""
    
    @pytest.fixture
    def predictor(self):
        """Create a Predictor with some team data."""
        with patch('src.predictor.DataCollector') as MockCollector, \
             patch('src.predictor.FeatureCalculator') as MockCalculator:
            
            MockCollector.return_value.get_completed_games.return_value = []
            pred = Predictor()
            
            # Add some teams to the UKF
            pred.ukf.get_team_ukf(1234)
            pred.ukf.get_team_ukf(5678)
            
            return pred
    
    @pytest.mark.unit
    def test_get_team_ratings_returns_dict(self, predictor):
        """Test that get_team_ratings returns a dictionary."""
        ratings = predictor.get_team_ratings()
        
        assert isinstance(ratings, dict)
    
    @pytest.mark.unit
    def test_get_team_ratings_contains_teams(self, predictor):
        """Test that ratings contain expected teams."""
        ratings = predictor.get_team_ratings()
        
        assert 1234 in ratings
        assert 5678 in ratings
    
    @pytest.mark.unit
    def test_get_team_ratings_structure(self, predictor):
        """Test that each team rating has correct structure."""
        ratings = predictor.get_team_ratings()
        
        for team_id, rating in ratings.items():
            assert 'offensive_rating' in rating
            assert 'defensive_rating' in rating
            assert 'home_advantage' in rating
            assert 'health_status' in rating
            assert 'momentum' in rating
            assert 'fatigue' in rating
            assert 'pace' in rating


class TestPredictGames:
    """Test cases for batch game prediction."""
    
    @pytest.fixture
    def predictor(self):
        """Create a Predictor with mocked dependencies."""
        with patch('src.predictor.DataCollector') as MockCollector, \
             patch('src.predictor.FeatureCalculator') as MockCalculator:
            
            MockCollector.return_value.get_completed_games.return_value = []
            MockCalculator.return_value.get_game_features.return_value = {
                'momentum': 0.1,
                'fatigue': 0.1,
                'health_status': 1.0,
                'home_advantage': 3.0,
                'pace': 70.0
            }
            
            pred = Predictor()
            return pred
    
    @pytest.mark.unit
    def test_predict_games_returns_list(self, predictor, sample_games_list):
        """Test that predict_games returns a list."""
        results = predictor.predict_games(sample_games_list[:3])
        
        assert isinstance(results, list)
        assert len(results) == 3
    
    @pytest.mark.unit
    def test_predict_games_structure(self, predictor, sample_games_list):
        """Test that each result has game and prediction."""
        results = predictor.predict_games(sample_games_list[:2])
        
        for result in results:
            assert 'game' in result
            assert 'prediction' in result
    
    @pytest.mark.unit
    def test_predict_games_empty_list(self, predictor):
        """Test prediction with empty game list."""
        results = predictor.predict_games([])
        
        assert results == []


class TestPredictorEdgeCases:
    """Edge case tests for Predictor."""
    
    @pytest.fixture
    def predictor(self):
        """Create a Predictor with mocked dependencies."""
        with patch('src.predictor.DataCollector') as MockCollector, \
             patch('src.predictor.FeatureCalculator') as MockCalculator:
            
            MockCollector.return_value.get_completed_games.return_value = []
            MockCalculator.return_value.get_game_features.return_value = {
                'momentum': 0.0,
                'fatigue': 0.0,
                'health_status': 1.0,
                'home_advantage': 3.0,
                'pace': 70.0
            }
            
            pred = Predictor()
            pred.initialized = True
            return pred
    
    @pytest.mark.unit
    def test_predict_game_no_spread(self, predictor):
        """Test prediction when spread is not available."""
        game = {
            'HomeTeamID': 1234,
            'AwayTeamID': 5678,
            'HomeTeam': 'DUKE',
            'AwayTeam': 'UNC',
            'DateTime': '2026-01-15T19:00:00Z',
            'PointSpread': None,
            'OverUnder': 145.0,
        }
        
        prediction = predictor.predict_game(game)
        
        assert prediction['spread'] is None
        assert prediction['home_covers_probability'] is None
    
    @pytest.mark.unit
    def test_predict_game_no_total_line(self, predictor):
        """Test prediction when total line is not available."""
        game = {
            'HomeTeamID': 1234,
            'AwayTeamID': 5678,
            'HomeTeam': 'DUKE',
            'AwayTeam': 'UNC',
            'DateTime': '2026-01-15T19:00:00Z',
            'PointSpread': -5.5,
            'OverUnder': None,
        }
        
        prediction = predictor.predict_game(game)
        
        assert prediction['total_line'] is None
        assert prediction['over_probability'] is None
    
    @pytest.mark.unit
    def test_uncertainty_is_positive(self, predictor, sample_game):
        """Test that uncertainties are always positive."""
        prediction = predictor.predict_game(sample_game)
        
        assert prediction['margin_uncertainty'] >= 0
        assert prediction['total_uncertainty'] >= 0
    
    @pytest.mark.unit
    def test_confidence_in_valid_range(self, predictor, sample_game):
        """Test that confidence is in 0-100 range."""
        prediction = predictor.predict_game(sample_game)
        
        if prediction['home_covers_confidence'] is not None:
            assert 0 <= prediction['home_covers_confidence'] <= 100
        
        if prediction['over_confidence'] is not None:
            assert 0 <= prediction['over_confidence'] <= 100
        
        assert 0 <= prediction['overall_confidence'] <= 100

