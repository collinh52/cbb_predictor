# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Workflow Orchestration

### 1. Plan Mode Default
- Enter plan mode for ANY non-trivial task (3+ steps or architectural decisions)
- If something goes sideways, STOP and re-plan immediately - don't keep pushing
- Use plan mode for verification steps, not just building
- Write detailed specs upfront to reduce ambiguity

### 2. Subagent Strategy
- Use subagents liberally to keep main context window clean
- Offload research, exploration, and parallel analysis to subagents
- For complex problems, throw more compute at it via subagents
- One task per subagent for focused execution

### 3. Self-Improvement Loop
- After ANY correction from the user: update `tasks/lessons.md` with the pattern
- Write rules for yourself that prevent the same mistake
- Ruthlessly iterate on these lessons until mistake rate drops
- Review lessons at session start for relevant project

### 4. Verification Before Done
- Never mark a task complete without proving it works
- Diff behavior between main and your changes when relevant
- Ask yourself: "Would a staff engineer approve this?"
- Run tests, check logs, demonstrate correctness

### 5. Demand Elegance (Balanced)
- For non-trivial changes: pause and ask "is there a more elegant way?"
- If a fix feels hacky: "Knowing everything I know now, implement the elegant solution"
- Skip this for simple, obvious fixes - don't over-engineer
- Challenge your own work before presenting it

### 6. Autonomous Bug Fixing
- When given a bug report: just fix it. Don't ask for hand-holding
- Point at logs, errors, failing tests - then resolve them
- Zero context switching required from the user
- Go fix failing CI tests without being told how

## Task Management

- **Plan First**: Write plan to `tasks/todo.md` with checkable items
- **Verify Plan**: Check in before starting implementation
- **Track Progress**: Mark items complete as you go
- **Explain Changes**: High-level summary at each step
- **Document Results**: Add review section to `tasks/todo.md`
- **Capture Lessons**: Update `tasks/lessons.md` after corrections

## Core Principles

- **Simplicity First**: Make every change as simple as possible. Impact minimal code.
- **No Laziness**: Find root causes. No temporary fixes. Senior developer standards.
- **Minimal Impact**: Changes should only touch what's necessary. Avoid introducing bugs.

## Sports Betting Concepts (Critical Domain Knowledge)

### Vegas Spread Notation

**ALWAYS use standard Vegas convention for spread notation:**

#### How Spreads Work
- **Negative spread** = Team is **favored** (must win by more than the spread to "cover")
  - Example: `Baylor -8.0` means Baylor must win by MORE than 8 points
  - If you bet Baylor -8.0 and they win by 10, you WIN
  - If you bet Baylor -8.0 and they win by 6, you LOSE

- **Positive spread** = Team is **underdog** (gets points added to their score)
  - Example: `Colorado +8.0` means Colorado gets 8 points added
  - If you bet Colorado +8.0 and they lose by 6, you WIN (6 < 8)
  - If you bet Colorado +8.0 and they lose by 10, you LOSE (10 > 8)

#### Storage Convention
- Store spreads from **home team perspective**:
  - `vegas_spread = -8.0` means home team favored by 8
  - `vegas_spread = +8.0` means home team underdog by 8
- **NEVER negate spreads** when collecting from The Odds API - they're already in correct format

#### Display Convention
- When showing a pick, always display the spread **from the picked team's perspective**:
  - Pick HOME at -8.0 → Show `HOME (-8.0)`
  - Pick AWAY at +8.0 → Show `AWAY (+8.0)`
  - If picking AWAY when home is -8.0, flip the sign → Show `AWAY (+8.0)`

#### Common Mistakes to Avoid
1. ❌ **Never show "HOME (+8.0)" when home is favored** - this is impossible (favorites always have negative spreads)
2. ❌ **Don't negate spreads from The Odds API** - they're already in standard format
3. ❌ **Don't confuse spread direction with predicted margin** - they're independent values
4. ✅ **Always verify spread logic**: If team is favored, spread must be negative

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

# Update README with accuracy stats and Top 25 rankings
python scripts/update_readme_accuracy.py
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

# Access at http://localhost:8000
# Web UI includes:
# - Team rankings page (sortable stats table)
# - Custom game predictor (searchable/filterable team dropdowns)
# - Today's predictions
# - Model accuracy dashboard
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

**`scripts/update_readme_accuracy.py`**: README updater
- Updates three dynamic README sections: accuracy stats, predictions, and Top 25 rankings
- Uses markers: `<!-- ACCURACY_STATS_START/END -->` and `<!-- RANKINGS_START/END -->`
- Generates Top 25 rankings table using `calculate_team_ratings()` from `show_team_ratings_v3.py`
- Called by both morning and evening GitHub Actions jobs

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

**Collect Odds Job** (runs 7 AM ET / 12 PM UTC):
- Logs into KenPom using Playwright (anti-detection measures)
- Downloads KenPom summary CSV (`summary{season}.csv`)
- Collects Vegas lines from The Odds API
- Generates predictions for next 2 days (`scripts/predict_today.py --days 2`)
- Updates README.md (predictions table, Top 25 rankings)
- Commits ATS tracking data and README

**Check Results Job** (runs 11 PM ET / 4 AM UTC):
- Fetches completed game scores (last 7 days: `scripts/daily_check_results.py --days 7`)
- Updates ATS tracking accuracy
- Retrains ML model on latest 200 games (`scripts/setup_and_train.py --populate 200 --train`)
- Updates README.md (accuracy stats, Top 25 rankings) via `scripts/update_readme_accuracy.py`
- Commits results and updated models

**README Dynamic Sections** (updated daily):
| Section | Morning Job | Evening Job | Markers |
|---------|-------------|-------------|---------|
| Today's Predictions | ✅ | - | Within `ACCURACY_STATS` |
| Accuracy Stats | - | ✅ | `<!-- ACCURACY_STATS_START/END -->` |
| Top 25 Rankings | ✅ | ✅ | `<!-- RANKINGS_START/END -->` |

**Caching Strategy**:
- Game cache: Weekly refresh (key: `game-cache-{YEAR}-W{WEEK}`)
- ATS data: Per-run cache with fallback (`ats_tracking.json`, `ats_accuracy.json`)
- ML models: Per-run cache with fallback (`data/models/*.keras`)
- Retention: 90 days for ATS artifacts

**Manual Triggers**: Use workflow_dispatch with options:
- `collect_odds`: Generate predictions only
- `check_results`: Update accuracy only
- `both`: Full pipeline
- `update_readme`: Refresh README stats

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

**Team name mismatches**:
- Use `src/team_name_mapping.py` to add mappings
- Fuzzy match threshold: 0.65 (configurable via `KENPOM_FUZZY_MATCH_THRESHOLD`)
- Recent fix (commit 998fdb1): Improved fuzzy matching to prevent incorrect team rating assignments
- Debug with `scripts/show_team_ratings_v3.py` to see which teams lack KenPom data

**Missing KenPom data**:
- Predictor falls back to UKF-only features (default ratings: AdjO=100.0, AdjD=100.0, AdjT=70.0)
- Ensure `summary{season}.csv` in `data/` directory
- KenPom login may fail due to anti-bot detection - check GitHub Actions logs
- If login fails, predictions continue with default ratings (warning shown)

**Model not loading**:
- Check `data/models/` for `.keras` files
- Verify database has `model_versions` entry with `is_active=True`
- Use `Database.get_active_model_version()` to debug
- Retrain with `scripts/setup_and_train.py --populate 200 --train`
- Falls back to UKF-only predictions if ML model unavailable

**Stale predictions**:
- GitHub Actions runs twice daily (7 AM, 11 PM ET)
- Manual trigger via workflow_dispatch in Actions tab
- Select action: collect_odds, check_results, both, or update_readme

**API rate limits**:
- ESPN: Free, but may throttle - uses HTTP response caching (7-day cache for completed games)
- The Odds API: 500 requests/month on free tier - minimize calls with `--days` parameter
- Cache key includes week number for automatic weekly refresh

**Database binding errors**:
- Recent fix (commit fa77098): Fixed database binding error in custom prediction feature extraction
- Ensure SQLAlchemy models match database schema
- Recreate database if schema changed: `rm basketball_predictor.db && python scripts/setup_and_train.py`

**Performance/caching issues**:
- Recent addition (commit a170bca): Prediction caching for dramatic performance improvement
- Clear cache if stale: `rm -rf data/cache/` or use `scripts/check_cache.py` to inspect

## Web Interface

The FastAPI web application (`src/api.py`) provides:

### Pages
- **Home** (`/`): Overview with today's predictions
- **Team Rankings** (`/rankings`): Sortable table with UKF states, KenPom ratings, and records
- **Custom Predictor** (`/predict`): Matchup builder with searchable/filterable team dropdowns
- **Accuracy Dashboard**: Historical prediction performance

### API Endpoints
- `GET /api/games/today`: Today's scheduled games with predictions
- `GET /api/predictions/{game_id}`: Detailed prediction for specific game
- `POST /api/predict/custom`: Generate prediction for custom matchup
- `GET /api/predictions/accuracy`: Overall accuracy metrics
- `GET /api/models/versions`: ML model version history
- `GET /api/teams/rankings`: Team rankings with full state vectors

### Frontend Features
- **Searchable dropdowns**: Fuzzy search for team selection in custom predictor
- **Sortable tables**: Click column headers to sort by any metric
- **Real-time predictions**: Live updates when new odds are fetched
- **Confidence indicators**: Color-coded by prediction confidence level

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

## Debugging Workflow

### Investigating Prediction Issues

1. **Check UKF state**: `python scripts/show_team_ratings_v3.py` shows current ratings for all teams
2. **Inspect features**: Use `scripts/debug_calibration.py` to examine feature extraction
3. **Verify data quality**: `scripts/check_cache.py` shows cache status and game counts
4. **Test specific matchup**: Web UI custom predictor or `src/hybrid_predictor.py` directly

### Validating Model Performance

1. **Quick check**: `python validation/backtest_option2_rolling.py` (fastest, realistic scenario)
2. **Comprehensive**: `python validation/run_all_backtests.py` (runs all three methods)
3. **Live accuracy**: Check README.md for current ATS tracking stats and Top 25 rankings (updated daily via GitHub Actions)

### Updating After Code Changes

1. **Retrain model**: `python scripts/setup_and_train.py --populate 200 --train`
2. **Clear cache**: `rm -rf data/cache/` if prediction logic changed
3. **Run tests**: `pytest -v` for unit tests, `pytest tests/test_integration.py` for end-to-end
4. **Validate accuracy**: Run backtests to ensure no regression

### KenPom Integration Issues

1. **Test login**: `python scripts/kenpom_login_improved.py` (requires credentials in `.env`)
2. **Manual download**: Place `summary{season}.csv` in `data/` directory
3. **Verify parsing**: Check logs for fuzzy match warnings
4. **Fallback behavior**: System works without KenPom (uses default ratings)
