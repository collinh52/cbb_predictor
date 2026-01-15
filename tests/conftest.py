"""
Pytest configuration and shared fixtures for CBB Predictor tests.
"""
import pytest
import sys
import os
from datetime import datetime, timedelta
from typing import Dict, List
import numpy as np
import config

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


@pytest.fixture
def sample_game() -> Dict:
    """Create a sample game dictionary for testing."""
    return {
        'GameID': 12345,
        'DateTime': '2026-01-15T19:00:00Z',
        'Season': 2026,
        'SeasonType': 1,
        'Status': 'Final',
        'HomeTeamID': 1234,
        'AwayTeamID': 5678,
        'HomeTeam': 'DUKE',
        'AwayTeam': 'UNC',
        'HomeTeamName': 'Duke Blue Devils',
        'AwayTeamName': 'North Carolina Tar Heels',
        'HomeTeamScore': 78,
        'AwayTeamScore': 72,
        'PointSpread': -5.5,
        'OverUnder': 145.0,
        'IsClosed': True,
    }


@pytest.fixture
def sample_game_no_score() -> Dict:
    """Create a sample game without scores (upcoming game)."""
    return {
        'GameID': 12346,
        'DateTime': '2026-01-20T19:00:00Z',
        'Season': 2026,
        'SeasonType': 1,
        'Status': 'Scheduled',
        'HomeTeamID': 1234,
        'AwayTeamID': 5678,
        'HomeTeam': 'DUKE',
        'AwayTeam': 'UNC',
        'HomeTeamName': 'Duke Blue Devils',
        'AwayTeamName': 'North Carolina Tar Heels',
        'HomeTeamScore': None,
        'AwayTeamScore': None,
        'PointSpread': -3.5,
        'OverUnder': 142.0,
        'IsClosed': False,
    }


@pytest.fixture
def sample_games_list() -> List[Dict]:
    """Create a list of sample games for testing."""
    base_date = datetime(2026, 1, 1)
    games = []
    
    # Create 20 games for testing
    teams = [
        (1001, 'Duke', 'DUKE'),
        (1002, 'UNC', 'UNC'),
        (1003, 'Kentucky', 'UK'),
        (1004, 'Kansas', 'KU'),
        (1005, 'Gonzaga', 'GONZ'),
    ]
    
    game_id = 10000
    for i in range(20):
        home_idx = i % len(teams)
        away_idx = (i + 1) % len(teams)
        
        home_team = teams[home_idx]
        away_team = teams[away_idx]
        
        # Vary scores to create interesting data
        home_score = 70 + (i * 3) % 20
        away_score = 65 + (i * 5) % 25
        
        games.append({
            'GameID': game_id + i,
            'DateTime': (base_date + timedelta(days=i)).isoformat() + 'Z',
            'Season': 2026,
            'SeasonType': 1,
            'Status': 'Final',
            'HomeTeamID': home_team[0],
            'AwayTeamID': away_team[0],
            'HomeTeam': home_team[2],
            'AwayTeam': away_team[2],
            'HomeTeamName': home_team[1],
            'AwayTeamName': away_team[1],
            'HomeTeamScore': home_score,
            'AwayTeamScore': away_score,
            'PointSpread': -3.5 + (i % 7),
            'OverUnder': 140.0 + (i % 10),
            'IsClosed': True,
        })
    
    return games


@pytest.fixture
def sample_team_state() -> np.ndarray:
    """Create a sample team state vector."""
    return np.array([
        95.0,   # offensive_rating
        92.0,   # defensive_rating
        3.5,    # home_advantage
        1.0,    # health_status
        0.2,    # momentum
        0.1,    # fatigue
        70.0    # pace
    ])


@pytest.fixture
def sample_opponent_state() -> np.ndarray:
    """Create a sample opponent state vector."""
    return np.array([
        90.0,   # offensive_rating
        95.0,   # defensive_rating
        3.0,    # home_advantage
        0.95,   # health_status
        -0.1,   # momentum
        0.2,    # fatigue
        68.0    # pace
    ])


@pytest.fixture
def sample_features() -> Dict:
    """Create sample game features."""
    return {
        'momentum': 0.3,
        'fatigue': 0.1,
        'health_status': 1.0,
        'home_advantage': 3.5,
        'pace': 70.0
    }


@pytest.fixture
def sample_ml_features() -> np.ndarray:
    """Create sample ML feature array."""
    return np.random.randn(config.ML_FEATURE_COUNT).astype(np.float32)


@pytest.fixture
def sample_training_data():
    """Create sample training data for ML model."""
    n_samples = 100
    n_features = config.ML_FEATURE_COUNT
    
    X = np.random.randn(n_samples, n_features).astype(np.float32)
    # Target: [margin, total]
    y = np.column_stack([
        np.random.randn(n_samples) * 10,  # margins around 0
        np.random.randn(n_samples) * 10 + 145  # totals around 145
    ]).astype(np.float32)
    
    return X, y

