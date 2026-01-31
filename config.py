"""
Configuration file for UKF Basketball Predictor
"""
import os
from typing import Optional, List
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API Configuration
# Set your API key in .env file or as an environment variable
API_KEY: Optional[str] = os.getenv("BASKETBALL_API_KEY", None)
API_BASE_URL: str = os.getenv("API_BASE_URL", "https://api.sportsdata.io/v3/cbb")

# The Odds API Configuration
THE_ODDS_API_KEY: Optional[str] = os.getenv("THE_ODDS_API_KEY", None)
THE_ODDS_API_BASE_URL: str = "https://api.the-odds-api.com/v4"

# ESPN API Configuration (free, no key required)
USE_ESPN_FOR_HISTORICAL: bool = True  # Use ESPN for historical game data instead of SportsDataIO
ESPN_API_BASE_URL: str = "https://site.api.espn.com/apis/site/v2/sports/basketball/mens-college-basketball"

# Season Configuration
# Note: Free trial typically has access to current/future seasons only
# For SportsDataIO free trial, this should be 2026 (or current season year)
CURRENT_SEASON: int = int(os.getenv("CURRENT_SEASON", "2026"))  # Default to 2026 for free trial
SEASON_TYPE: str = "regular"  # "regular" or "postseason"

# UKF Parameters
# Process noise (how much state can change between games)
PROCESS_NOISE = {
    "offensive_rating": 0.5,  # Small changes in offensive strength
    "defensive_rating": 0.5,  # Small changes in defensive strength
    "home_advantage": 0.1,    # Very slow drift for home advantage
    "health_status": 0.2,    # Can change quickly with injuries
    "momentum": 0.3,         # Moderate changes
    "fatigue": 0.4,          # Can change with schedule
    "pace": 0.2              # Relatively stable
}

# Measurement noise (uncertainty in observations)
MEASUREMENT_NOISE = {
    "score_differential": 8.0,  # Points
    "total_points": 10.0,       # Points
    "pace": 2.0                  # Possessions
}

# Feature Calculation Parameters
MOMENTUM_WINDOW: int = 10  # Number of recent games for momentum
MOMENTUM_DECAY: float = 0.85  # Exponential decay factor for momentum
FATIGUE_WINDOW_DAYS: int = 7  # Days to consider for fatigue
FATIGUE_GAME_WEIGHT: float = 0.15  # Fatigue per game
FATIGUE_TRAVEL_WEIGHT: float = 0.1  # Additional fatigue per 100 miles traveled
REST_DECAY: float = 0.2  # Fatigue reduction per rest day

# Data Refresh Intervals
CACHE_EXPIRY_MINUTES: int = 10080  # Cache game data for 7 days (completed games don't change)
DATA_REFRESH_INTERVAL: int = 30  # Refresh predictions every 30 minutes

# Data Storage
DATA_DIR: str = "data"
CACHE_DIR: str = os.path.join(DATA_DIR, "cache")

# Default values for missing data
DEFAULT_HEALTH_STATUS: float = 1.0  # Assume full health if data unavailable
DEFAULT_PACE: float = 70.0  # Average possessions per game
DEFAULT_HOME_ADVANTAGE: float = 3.0  # Default home advantage in points

# KenPom integration
KENPOM_SUMMARY_PATTERN: str = "summary{season}.csv"
KENPOM_DEFAULT_ADJ_EM: float = 0.0
KENPOM_DEFAULT_ADJ_O: float = 100.0
KENPOM_DEFAULT_ADJ_D: float = 100.0
KENPOM_DEFAULT_ADJ_T: float = 70.0
KENPOM_MARGIN_WEIGHT: float = float(os.getenv("KENPOM_MARGIN_WEIGHT", "0.25"))
KENPOM_PACE_WEIGHT: float = float(os.getenv("KENPOM_PACE_WEIGHT", "0.25"))
KENPOM_FUZZY_MATCH_THRESHOLD: float = float(os.getenv("KENPOM_FUZZY_MATCH_THRESHOLD", "0.65"))
KENPOM_RATINGS_WEIGHT: float = float(os.getenv("KENPOM_RATINGS_WEIGHT", "0.25"))

# Database Configuration
DATABASE_URL: Optional[str] = os.getenv("DATABASE_URL", None)
# Default to SQLite for development if PostgreSQL not available
if not DATABASE_URL:
    DATABASE_URL = os.getenv("SQLITE_DB_URL", "sqlite:///./basketball_predictor.db")

# ML Model Configuration
MODEL_PATH: str = os.getenv("MODEL_PATH", os.path.join(DATA_DIR, "models"))
HYBRID_WEIGHT_UKF: float = float(os.getenv("HYBRID_WEIGHT_UKF", "0.5"))
HYBRID_WEIGHT_ML: float = float(os.getenv("HYBRID_WEIGHT_ML", "0.5"))
ML_FEATURE_COUNT: int = int(os.getenv("ML_FEATURE_COUNT", "52"))

# Neural Network Hyperparameters
NN_HIDDEN_LAYERS: List[int] = [256, 128, 64]
NN_DROPOUT_RATE: float = 0.3
NN_LEARNING_RATE: float = 0.001
NN_BATCH_SIZE: int = 32
NN_EPOCHS: int = 100
NN_VALIDATION_SPLIT: float = 0.2

