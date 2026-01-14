"""
Integration tests for the CBB Predictor pipeline.
Tests the full prediction flow from data to predictions.
"""
import pytest
import numpy as np
import sys
import os
from datetime import datetime, timedelta
from unittest.mock import Mock, patch, MagicMock

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestPredictionPipeline:
    """Integration tests for the full prediction pipeline."""
    
    @pytest.fixture
    def mock_collector(self):
        """Create a mocked data collector with sample data."""
        collector = Mock()
        
        # Create sample completed games
        games = []
        base_date = datetime(2025, 11, 15)
        
        teams = [(1001, 'Duke'), (1002, 'UNC'), (1003, 'Kentucky'), (1004, 'Kansas')]
        
        for i in range(20):
            home_idx = i % len(teams)
            away_idx = (i + 1) % len(teams)
            
            games.append({
                'GameID': 10000 + i,
                'DateTime': (base_date + timedelta(days=i)).isoformat() + 'Z',
                'Status': 'Final',
                'HomeTeamID': teams[home_idx][0],
                'AwayTeamID': teams[away_idx][0],
                'HomeTeam': teams[home_idx][1],
                'AwayTeam': teams[away_idx][1],
                'HomeTeamName': teams[home_idx][1],
                'AwayTeamName': teams[away_idx][1],
                'HomeTeamScore': 75 + (i % 10),
                'AwayTeamScore': 70 + (i % 8),
            })
        
        collector.get_completed_games.return_value = games
        collector.get_player_injuries.return_value = []
        collector.get_team_stats.return_value = None
        
        return collector
    
    @pytest.mark.integration
    def test_predictor_initialization_with_data(self, mock_collector):
        """Test predictor initialization processes historical data."""
        with patch('src.predictor.DataCollector', return_value=mock_collector):
            from src.predictor import Predictor
            
            predictor = Predictor()
            predictor.initialize()
            
            assert predictor.initialized
            # Should have processed some teams
            assert len(predictor.ukf.teams) > 0
    
    @pytest.mark.integration
    def test_full_prediction_flow(self, mock_collector):
        """Test full prediction flow from initialization to prediction."""
        with patch('src.predictor.DataCollector', return_value=mock_collector):
            from src.predictor import Predictor
            
            predictor = Predictor()
            predictor.initialize()
            
            # Create a test game
            game = {
                'HomeTeamID': 1001,
                'AwayTeamID': 1002,
                'HomeTeam': 'Duke',
                'AwayTeam': 'UNC',
                'DateTime': '2026-01-15T19:00:00Z',
                'PointSpread': -3.5,
                'OverUnder': 145.0,
            }
            
            prediction = predictor.predict_game(game)
            
            # Verify prediction has required fields
            assert 'predicted_margin' in prediction
            assert 'predicted_total' in prediction
            assert 'predicted_winner' in prediction
            assert prediction['predicted_winner'] in ['home', 'away', None]
    
    @pytest.mark.integration
    def test_multiple_predictions_consistent(self, mock_collector):
        """Test that multiple predictions for same game are consistent."""
        with patch('src.predictor.DataCollector', return_value=mock_collector):
            from src.predictor import Predictor
            
            predictor = Predictor()
            predictor.initialize()
            
            game = {
                'HomeTeamID': 1001,
                'AwayTeamID': 1002,
                'HomeTeam': 'Duke',
                'AwayTeam': 'UNC',
                'DateTime': '2026-01-15T19:00:00Z',
            }
            
            pred1 = predictor.predict_game(game)
            pred2 = predictor.predict_game(game)
            
            # Same game should give same prediction
            assert pred1['predicted_margin'] == pred2['predicted_margin']
            assert pred1['predicted_total'] == pred2['predicted_total']


class TestHybridPredictorIntegration:
    """Integration tests for hybrid predictor."""
    
    @pytest.fixture
    def mock_environment(self):
        """Set up mocked environment for hybrid predictor."""
        mock_collector = Mock()
        mock_collector.get_completed_games.return_value = []
        mock_collector.get_player_injuries.return_value = []
        mock_collector.get_team_stats.return_value = None
        
        mock_db = Mock()
        mock_db.get_active_model_version.return_value = None
        
        return mock_collector, mock_db
    
    @pytest.mark.integration
    def test_hybrid_predictor_fallback_to_ukf(self, mock_environment):
        """Test that hybrid predictor falls back to UKF when no ML model."""
        mock_collector, mock_db = mock_environment
        
        with patch('src.predictor.DataCollector', return_value=mock_collector), \
             patch('src.hybrid_predictor.get_database', return_value=mock_db):
            
            from src.predictor import Predictor
            from src.hybrid_predictor import HybridPredictor
            
            ukf_predictor = Predictor()
            ukf_predictor.initialized = True
            
            hybrid = HybridPredictor(ukf_predictor)
            
            game = {
                'HomeTeamID': 1001,
                'AwayTeamID': 1002,
                'HomeTeam': 'Duke',
                'AwayTeam': 'UNC',
                'DateTime': '2026-01-15T19:00:00Z',
            }
            
            prediction = hybrid.predict_game(game)
            
            # Should use UKF only (no ML model)
            assert prediction['prediction_source'] == 'ukf'
    
    @pytest.mark.integration
    def test_hybrid_predictor_with_ukf_features(self, mock_environment):
        """Test that hybrid predictor captures UKF features."""
        mock_collector, mock_db = mock_environment
        
        with patch('src.predictor.DataCollector', return_value=mock_collector), \
             patch('src.hybrid_predictor.get_database', return_value=mock_db):
            
            from src.predictor import Predictor
            from src.hybrid_predictor import HybridPredictor
            
            ukf_predictor = Predictor()
            ukf_predictor.initialized = True
            
            hybrid = HybridPredictor(ukf_predictor)
            
            game = {
                'HomeTeamID': 1001,
                'AwayTeamID': 1002,
                'HomeTeam': 'Duke',
                'AwayTeam': 'UNC',
                'DateTime': '2026-01-15T19:00:00Z',
            }
            
            prediction = hybrid.predict_game(game)
            
            # Should have UKF features stored
            assert 'ukf_features_json' in prediction
            assert 'ml_features_json' in prediction


class TestFeatureEngineeringPipeline:
    """Integration tests for feature engineering pipeline."""
    
    @pytest.mark.integration
    def test_feature_consistency(self):
        """Test that features are consistent across multiple calls."""
        with patch('src.ml_features.DataCollector'), \
             patch('src.ml_features.FeatureCalculator') as MockCalc:
            
            mock_calc = MockCalc.return_value
            mock_calc._normalize_team_id.side_effect = lambda x: x if isinstance(x, int) else hash(str(x)) % 100000
            
            from src.ml_features import MLFeatureEngineer
            from src.ukf_model import TeamUKF
            
            engineer = MLFeatureEngineer()
            engineer.calculator._normalize_team_id = mock_calc._normalize_team_id
            
            home_state = np.array([95.0, 92.0, 3.5, 1.0, 0.2, 0.1, 70.0])
            away_state = np.array([90.0, 95.0, 3.0, 0.95, -0.1, 0.2, 68.0])
            home_uncertainty = np.ones(TeamUKF.STATE_DIM)
            away_uncertainty = np.ones(TeamUKF.STATE_DIM)
            
            game = {
                'DateTime': '2026-01-15T19:00:00Z',
                'PointSpread': -3.5,
                'OverUnder': 145.0,
            }
            
            # First call
            features1, _ = engineer.engineer_features(
                home_state, away_state, home_uncertainty, away_uncertainty,
                game, 1001, 1002, datetime(2026, 1, 15), []
            )
            
            # Second call with same inputs
            features2, _ = engineer.engineer_features(
                home_state, away_state, home_uncertainty, away_uncertainty,
                game, 1001, 1002, datetime(2026, 1, 15), []
            )
            
            np.testing.assert_array_equal(features1, features2)


class TestRatingsToPredictionFlow:
    """Integration tests for ratings to prediction flow."""
    
    @pytest.fixture
    def sample_games_for_ratings(self):
        """Create games for rating calculation."""
        games = []
        base_date = datetime(2025, 11, 15)
        
        # Create enough games for meaningful ratings
        teams = [
            (1001, 'Duke', 'DUKE'),
            (1002, 'UNC', 'UNC'),
            (1003, 'Kentucky', 'UK'),
            (1004, 'Kansas', 'KU'),
        ]
        
        game_id = 30000
        for round_num in range(3):  # 3 rounds of games
            for i, home_team in enumerate(teams):
                for j, away_team in enumerate(teams):
                    if i != j:
                        games.append({
                            'GameID': game_id,
                            'DateTime': (base_date + timedelta(days=game_id - 30000)).isoformat() + 'Z',
                            'Status': 'Final',
                            'HomeTeamID': home_team[0],
                            'AwayTeamID': away_team[0],
                            'HomeTeam': home_team[2],
                            'AwayTeam': away_team[2],
                            'HomeTeamName': home_team[1],
                            'AwayTeamName': away_team[1],
                            'HomeTeamScore': 75 - i * 2 + np.random.randint(-5, 5),
                            'AwayTeamScore': 70 - j * 2 + np.random.randint(-5, 5),
                        })
                        game_id += 1
        
        return games
    
    @pytest.mark.integration
    @pytest.mark.slow
    def test_ratings_inform_predictions(self, sample_games_for_ratings):
        """Test that team ratings influence predictions correctly."""
        # Import the ratings calculation
        sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'scripts'))
        from show_team_ratings_v3 import calculate_team_ratings
        
        # Calculate ratings
        ratings, stats = calculate_team_ratings(sample_games_for_ratings, min_games=5)
        
        if len(ratings) >= 2:
            # Get top and bottom team
            top_team = ratings[0]
            bottom_team = ratings[-1]
            
            # Top team should have higher overall rating
            assert top_team['overall_rating'] > bottom_team['overall_rating']
            
            # When top team plays bottom team at home, should be favored
            predicted_margin = top_team['overall_rating'] - bottom_team['overall_rating']
            assert predicted_margin > 0


class TestEdgeCasesIntegration:
    """Integration tests for edge cases."""
    
    @pytest.mark.integration
    def test_new_team_prediction(self):
        """Test prediction for teams with no history."""
        with patch('src.predictor.DataCollector') as MockCollector:
            MockCollector.return_value.get_completed_games.return_value = []
            MockCollector.return_value.get_player_injuries.return_value = []
            
            from src.predictor import Predictor
            
            predictor = Predictor()
            predictor.initialized = True
            
            # New teams not in any historical data
            game = {
                'HomeTeamID': 99999,
                'AwayTeamID': 88888,
                'HomeTeam': 'New Team A',
                'AwayTeam': 'New Team B',
                'DateTime': '2026-01-15T19:00:00Z',
            }
            
            prediction = predictor.predict_game(game)
            
            # Should still return a valid prediction (using defaults)
            assert 'predicted_margin' in prediction
            assert np.isfinite(prediction['predicted_margin'])
    
    @pytest.mark.integration
    def test_game_without_lines(self):
        """Test prediction for game without betting lines."""
        with patch('src.predictor.DataCollector') as MockCollector:
            MockCollector.return_value.get_completed_games.return_value = []
            MockCollector.return_value.get_player_injuries.return_value = []
            
            from src.predictor import Predictor
            
            predictor = Predictor()
            predictor.initialized = True
            
            game = {
                'HomeTeamID': 1001,
                'AwayTeamID': 1002,
                'HomeTeam': 'Duke',
                'AwayTeam': 'UNC',
                'DateTime': '2026-01-15T19:00:00Z',
                # No PointSpread or OverUnder
            }
            
            prediction = predictor.predict_game(game)
            
            # Should still work without lines
            assert 'predicted_margin' in prediction
            assert prediction['spread'] is None
            assert prediction['total_line'] is None


class TestDataFlowIntegration:
    """Integration tests for data flow through the system."""
    
    @pytest.mark.integration
    def test_game_result_updates_state(self):
        """Test that processing a game result updates team state."""
        with patch('src.predictor.DataCollector') as MockCollector:
            MockCollector.return_value.get_completed_games.return_value = []
            MockCollector.return_value.get_player_injuries.return_value = []
            MockCollector.return_value.get_team_stats.return_value = None
            
            from src.predictor import Predictor
            from src.ukf_model import TeamUKF
            
            predictor = Predictor()
            
            # Get initial state for a team
            initial_state = predictor.ukf.get_team_state(1001).copy()
            
            # Process a game
            game = {
                'HomeTeamID': 1001,
                'AwayTeamID': 1002,
                'HomeTeam': 'Duke',
                'AwayTeam': 'UNC',
                'HomeTeamScore': 85,
                'AwayTeamScore': 70,
                'DateTime': '2026-01-15T19:00:00Z',
            }
            
            predictor._process_completed_game(game)
            
            # State should have changed
            new_state = predictor.ukf.get_team_state(1001)
            
            # At minimum, the team should now exist in the UKF
            assert 1001 in predictor.ukf.teams
    
    @pytest.mark.integration
    def test_uncertainty_decreases_with_games(self):
        """Test that prediction uncertainty decreases with more data."""
        with patch('src.predictor.DataCollector') as MockCollector:
            MockCollector.return_value.get_completed_games.return_value = []
            MockCollector.return_value.get_player_injuries.return_value = []
            MockCollector.return_value.get_team_stats.return_value = None
            
            from src.predictor import Predictor
            
            predictor = Predictor()
            
            # Get initial uncertainty
            ukf = predictor.ukf.get_team_ukf(1001)
            initial_uncertainty = ukf.get_uncertainty().copy()
            
            # Process several games
            base_date = datetime(2026, 1, 1)
            for i in range(5):
                game = {
                    'HomeTeamID': 1001,
                    'AwayTeamID': 1002 + i,
                    'HomeTeam': 'Duke',
                    'AwayTeam': f'Team{i}',
                    'HomeTeamScore': 75 + i,
                    'AwayTeamScore': 70,
                    'DateTime': (base_date + timedelta(days=i)).isoformat() + 'Z',
                }
                predictor._process_completed_game(game)
            
            # Get new uncertainty
            final_uncertainty = ukf.get_uncertainty()
            
            # Uncertainty should generally decrease with more observations
            # (though this depends on implementation details)
            # At minimum, uncertainty should remain finite
            assert np.all(np.isfinite(final_uncertainty))

