# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A college basketball prediction system that combines Unscented Kalman Filtering (UKF) with neural networks to predict game outcomes, spreads, and totals. Currently achieving **68.96% backtested accuracy** with live ATS (Against The Spread) tracking via GitHub Actions.

## Common Commands

### Installation
```bash
pip install -r requirements.txt
python -m playwright install chromium  # For KenPom data collection
```

### Environment Setup
Create a `.env` file with:
```
THE_ODDS_API_KEY=your_key
BASKETBALL_API_KEY=your_key
KENPOM_USERNAME=your_username
KENPOM_PASSWORD=your_password
```

### Core Operations
```bash
# View current team ratings
python scripts/show_team_ratings_v3.py

# Generate today's predictions
python scripts/predict_today.py

# Collect odds for upcoming games
python scripts/daily_collect_odds.py

# Setup database and train ML model
python scripts/setup_and_train.py --populate 200 --train

# Populate database with historical games
python scripts/populate_season.py
```

### Validation and Testing
```bash
# Run all backtests
python validation/run_all_backtests.py

# Individual backtest methods
python validation/backtest_option1_last_season.py
python validation/backtest_option2_rolling.py
python validation/backtest_option3_cross_validation.py

# Run tests
pytest
pytest tests/test_predictor.py  # Single test file
pytest -v  # Verbose output
pytest --cov=src  # With coverage
```

### Web Server
```bash
uvicorn src.api:app --reload
```

## Architecture

### Prediction Pipeline

The system uses a **hybrid approach** combining two complementary models:

1. **UKF (Unscented Kalman Filter)**: Physics-based state estimation
   - Tracks 7-dimensional team state: offensive rating, defensive rating, home advantage, health, momentum, fatigue, pace
   - Updates beliefs incrementally as games occur
   - Provides uncertainty estimates via covariance matrices
   - Handles non-linear game dynamics

2. **Neural Network**: Pattern recognition
   - 52-feature input combining UKF states, uncertainties, and contextual data
   - Architecture: [256, 128, 64] hidden layers with 30% dropout
   - Trained on historical game outcomes
   - Learns complex interactions UKF can't model

3. **Hybrid Predictor** (`src/hybrid_predictor.py`):
   - Combines UKF and ML predictions with configurable weights (default: 0.5/0.5)
   - Falls back to UKF-only when ML model unavailable
   - Produces final spread/total predictions with confidence scores

### Data Flow

```
ESPN API → DataCollector → FeatureCalculator → UKF State Updates
                                                      ↓
                                        MLFeatureEngineer (52 features)
                                                      ↓
                                            Neural Network Model
                                                      ↓
                                            HybridPredictor
                                                      ↓
                                         Predictions + Confidence
```

### Key Components

**`src/predictor.py`**: Core UKF-based prediction engine
- Initializes by processing all historical games chronologically
- Updates team states via `_process_completed_game()`
- Generates predictions via `predict_game()`

**`src/hybrid_predictor.py`**: Combines UKF + ML
- Loads active model from database or latest from filesystem
- Extracts 52 features for ML input
- Blends predictions based on configured weights

**`src/ukf_model.py`**: Kalman filter implementation
- `TeamUKF`: Single team state tracker (7D state vector)
- `MultiTeamUKF`: Manages all teams, handles initialization
- Uses `filterpy` library for UKF math

**`src/ml_features.py`**: Feature engineering
- `extract_ukf_features()`: 24 UKF state + uncertainty features
- `extract_contextual_features()`: 28 game context features (rest, form, lines, KenPom)
- `fit_scaler()` / `transform_features()`: Standardization for neural network

**`src/ml_model.py`**: Neural network
- `SpreadPredictionModel`: Keras Sequential model
- Predicts both spread and total simultaneously (2 outputs)
- Includes training, evaluation, and save/load methods

**`src/data_collector.py`**: Historical game data
- Abstracts ESPN API and SportsDataIO
- Caches responses to reduce API calls
- `get_completed_games()`: Retrieves season history

**`src/odds_collector.py`**: Live betting lines
- Integrates with The Odds API
- Fetches current spreads and totals
- Used for ATS tracking and predictions

**`src/database.py`**: SQLAlchemy models
- `Prediction`: Stores UKF, ML, and hybrid predictions
- `GameResult`: Actual outcomes for accuracy tracking
- `ModelAccuracy`: Daily accuracy metrics
- `ModelVersion`: ML model versioning and metadata

**`src/ats_tracker.py`**: Against-the-spread accuracy
- Tracks predictions vs Vegas lines
- Calculates rolling accuracy (7-day, 30-day, all-time)
- Confidence-based stratification
- Updates README.md via `scripts/update_readme_accuracy.py`

**`src/team_name_mapping.py`**: Name reconciliation
- Maps team names across ESPN, KenPom, and The Odds API
- Uses fuzzy matching when exact match fails
- Critical for joining data from multiple sources

### Configuration

**`config.py`**: Centralized settings
- UKF process/measurement noise parameters
- ML model hyperparameters (hidden layers, dropout, learning rate)
- Hybrid blending weights (`HYBRID_WEIGHT_UKF`, `HYBRID_WEIGHT_ML`)
- KenPom integration weights (`KENPOM_RATINGS_WEIGHT`, `KENPOM_MARGIN_WEIGHT`, `KENPOM_PACE_WEIGHT`)
- Database URL, API keys (loaded from `.env`)

### KenPom Integration

KenPom data provides elite-level tempo-free ratings (AdjEM, AdjO, AdjD, AdjT):

1. **Data Collection**:
   - GitHub Actions logs into KenPom using Playwright
   - Downloads `summary{season}.csv` from KenPom data exports
   - Exports cookie to environment for authenticated requests

2. **Feature Integration** (`src/ml_features.py`):
   - Loads KenPom ratings via `load_kenpom_data()`
   - Fuzzy matches team names (threshold: 0.65)
   - Adds to ML feature vector with configurable weight (default: 0.25)

3. **Weighting**: Controlled via `KENPOM_RATINGS_WEIGHT` in config

### GitHub Actions Automation

**`.github/workflows/daily_predictions.yml`**: Automated prediction pipeline

**Collect Odds Job** (runs 10 AM ET):
- Logs into KenPom, downloads ratings
- Collects Vegas lines from The Odds API
- Generates predictions for next 2 days
- Updates README.md with new predictions
- Commits to repo

**Check Results Job** (runs 11 PM ET):
- Fetches completed game scores
- Updates ATS tracking accuracy
- Retrains ML model on latest data
- Updates README.md accuracy stats
- Commits results

**Artifacts**: ATS tracking JSON cached between runs

## Development Notes

### Team State Initialization

Teams start with neutral ratings (100.0 offensive/defensive) and converge to true strength as games accumulate. Early season predictions have higher uncertainty.

### Database vs File Storage

- **Database** (`basketball_predictor.db`): Predictions, results, model versions, daily accuracy
- **JSON Files** (`data/*.json`): ATS tracking for GitHub Actions persistence
- **Model Files** (`data/models/*.keras`): Trained neural networks
- **CSV Files** (`data/summary*.csv`): KenPom ratings

### Feature Engineering Details

The 52 ML features include:
- **UKF States** (14): Home/away offensive rating, defensive rating, home advantage, health, momentum, fatigue, pace
- **UKF Uncertainties** (10): Covariance diagonal elements for key states
- **Derived UKF** (6): Rating differences, pace average, momentum/fatigue/health differentials
- **Game Context** (22): Pregame spread/total, rest days, recent form (W/L streaks), home/away records, KenPom ratings, conference indicators, etc.

### Prediction Confidence

Confidence calculated from:
1. UKF uncertainty (covariance magnitude)
2. Margin magnitude (larger margins = more confident)
3. Home advantage factor

Used to stratify ATS accuracy reporting (50%+, 60%+, 70%+ confidence buckets).

### Testing Strategy

- **Unit Tests** (`tests/test_*.py`): Individual components
- **Integration Tests** (`tests/test_integration.py`): End-to-end prediction flow
- **Backtesting** (`validation/`): Historical accuracy validation
  - Option 1: Last season (out-of-sample)
  - Option 2: Rolling window (realistic)
  - Option 3: Cross-validation (rigorous)

### Common Issues

**Team name mismatches**: Use `team_name_mapping.py` to add mappings. Check fuzzy match threshold if names similar but not matching.

**Missing KenPom data**: Predictor falls back to UKF-only features. Ensure `summary{season}.csv` in `data/` directory.

**Model not loading**: Check `data/models/` for `.keras` files. Verify database has `model_versions` entry with correct path. Use `scripts/setup_and_train.py` to retrain.

**Stale predictions**: GitHub Actions runs twice daily. Manual trigger via workflow dispatch if needed.

**API rate limits**: ESPN is free but may throttle. The Odds API has monthly request limits (free tier: 500/month).

## Database Schema

Key tables and relationships:
- `predictions` ← `game_results` (1:1, FK on game_id)
- `predictions` → `prediction_source` (enum: ukf, ml, hybrid)
- `model_versions` ← `model_accuracy` (1:many, FK on version_id)

Use `Database.get_active_model_version()` to retrieve currently deployed model.
Use `Database.log_prediction()` and `Database.log_result()` for tracking.

## Performance Targets

- **Backtested**: 68.96% overall (69.86% high confidence)
- **Live ATS**: Tracked in README.md (updated daily)
- **Baseline**: ~50% random, ~52-55% basic rating systems
- **Target**: 62-65% (KenPom/BartTorvik level)

The system is in active development with ongoing improvements to feature engineering, model architecture, and KenPom integration.
