# Project Structure - College Basketball Predictor

## Directory Organization

```
Cursor Test/
│
├── 📁 src/                          # Core Source Code
│   ├── api.py                      # FastAPI backend server
│   ├── predictor.py                # Main prediction engine
│   ├── ukf_model.py                # Unscented Kalman Filter implementation
│   ├── espn_collector.py           # ESPN API integration
│   ├── odds_collector.py           # The Odds API integration
│   ├── data_collector.py           # Multi-source data collection
│   ├── feature_calculator.py       # Feature engineering (momentum, fatigue, etc)
│   ├── database.py                 # SQLAlchemy models and DB operations
│   ├── hybrid_predictor.py         # UKF + ML hybrid model
│   ├── ml_model.py                 # Neural network model
│   ├── ml_features.py              # ML feature engineering
│   ├── train_model.py              # Model training pipeline
│   ├── accuracy_tracker.py         # Accuracy tracking and metrics
│   ├── team_name_mapping.py        # Team name reconciliation across APIs
│   └── __init__.py                 # Package initialization
│
├── 📁 scripts/                      # User-Facing Scripts
│   ├── show_team_ratings.py        # Display all team ratings (Phase 1 enhanced)
│   ├── predict_today.py            # Generate today's game predictions
│   ├── populate_season.py          # Populate database with season data
│   ├── update_accuracy.py          # Update accuracy metrics
│   ├── test_odds_api.py            # Test Odds API connection
│   ├── setup_database.py           # Initialize database
│   └── setup_and_train.py          # Setup + train initial model
│
├── 📁 validation/                   # Backtesting & Validation
│   ├── backtest_option1_last_season.py      # Test on 2024-25 season
│   ├── backtest_option2_rolling.py          # Rolling validation (80/20 split)
│   ├── backtest_option3_cross_validation.py # K-fold cross-validation
│   ├── run_all_backtests.py                 # Run all three methods
│   └── README.md                            # Validation documentation
│
├── 📁 docs/                         # Documentation
│   ├── PHASE1_COMPLETE.md          # Phase 1 implementation details
│   ├── RATING_IMPROVEMENTS.md      # Roadmap for future improvements
│   ├── ESPN_INTEGRATION_COMPLETE.md # ESPN API integration
│   ├── DATA_COLLECTION_FIX.md      # Data collection improvements
│   ├── SOS_ADJUSTMENT_SUMMARY.md   # SOS methodology
│   ├── ALTERNATIVE_APIS.md         # API recommendations
│   ├── HYBRID_MODEL_README.md      # Hybrid UKF+ML model
│   ├── README.md                   # Old main README
│   └── ukf_basketball_predictor_d863926c.plan.md # Original plan
│
├── 📁 data/                         # Data Storage
│   ├── cache/                      # API response cache (1796 files)
│   ├── models/                     # Trained ML models
│   │   ├── model_v1_20260112_102041.keras
│   │   ├── model_v1_20260112_102041_metadata.json
│   │   └── scaler_v1_20260112_102041.pkl
│   └── team_names_comparison.json  # Team name mappings
│
├── 📁 static/                       # Web Frontend Assets
│   ├── app.js                      # Frontend JavaScript
│   └── style.css                   # Styling
│
├── 📁 templates/                    # HTML Templates
│   └── index.html                  # Main web interface
│
├── 📄 README.md                     # Main project documentation
├── 📄 config.py                     # Configuration settings
├── 📄 requirements.txt              # Python dependencies
├── 📄 .env                          # API keys (git ignored)
├── 📄 .gitignore                    # Git ignore rules
└── 📄 basketball_predictor.db       # SQLite database
```

## File Counts

- **Core Modules**: 15 files in `src/`
- **User Scripts**: 7 files in `scripts/`
- **Validation**: 5 files in `validation/`
- **Documentation**: 9 files in `docs/`
- **Cached Data**: 1,796 files in `data/cache/`
- **Total Python Files**: ~30 files

## Import Path Resolution

All scripts in `scripts/` and `validation/` include:

```python
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
```

This allows them to import from `src/` regardless of current working directory.

## Quick Reference

### View Team Ratings
```bash
python scripts/show_team_ratings.py
```
**Output**: 372 D1 teams with Phase 1 enhanced ratings

### Get Today's Predictions
```bash
python scripts/predict_today.py
```
**Output**: Today's games with predicted scores and betting recommendations

### Validate System
```bash
python validation/run_all_backtests.py
```
**Output**: Comprehensive accuracy report from 3 validation methods

### Start Web Server
```bash
uvicorn src.api:app --reload
```
**Access**: http://localhost:8000

### Setup Database
```bash
python scripts/setup_database.py
python scripts/setup_and_train.py
```

### Populate Season Data
```bash
python scripts/populate_season.py
```

## Data Flow

```
ESPN API → espn_collector.py → 5,889 games → show_team_ratings.py → Phase 1 Enhanced Ratings
                                                                    ↓
The Odds API → odds_collector.py → Real betting lines → predict_today.py → Predictions
                                                                          ↓
                                                        validation/ → Accuracy Metrics
```

## Key Features by Directory

### src/ (Core)
- **Data Collection**: Multi-API integration (ESPN, The Odds API, SportsDataIO)
- **Rating System**: Phase 1 enhanced (HCA, MoV, Recency)
- **Prediction Engine**: UKF + ML hybrid model
- **Database**: SQLAlchemy ORM with SQLite/PostgreSQL support
- **API Server**: FastAPI with REST endpoints

### scripts/ (User Tools)
- **show_team_ratings.py**: Most important - view all team rankings
- **predict_today.py**: Get predictions for today's games
- **populate_season.py**: One-time setup to load historical data
- **setup_and_train.py**: Initial database and model setup

### validation/ (Testing)
- **Option 1**: Test on different season (2024-25)
- **Option 2**: Test on recent games (rolling validation)
- **Option 3**: K-fold cross-validation with confidence intervals
- **run_all_backtests.py**: Run all three for comprehensive validation

### docs/ (Documentation)
- **PHASE1_COMPLETE.md**: Current implementation details
- **RATING_IMPROVEMENTS.md**: Future enhancement roadmap
- **validation/README.md**: How to validate the system

## Development Workflow

1. **Initial Setup**:
   ```bash
   pip install -r requirements.txt
   python scripts/setup_database.py
   ```

2. **Daily Usage**:
   ```bash
   python scripts/show_team_ratings.py  # View rankings
   python scripts/predict_today.py      # Get predictions
   ```

3. **Validation** (periodic):
   ```bash
   python validation/run_all_backtests.py
   ```

4. **Updates** (as needed):
   ```bash
   python scripts/populate_season.py    # Refresh data
   python scripts/update_accuracy.py    # Update metrics
   ```

## Configuration

All settings in `config.py`:
- API keys (loaded from `.env`)
- UKF parameters
- Feature calculation weights
- Database connection
- ML model hyperparameters
- Phase 1 enhancement parameters

## Dependencies

See `requirements.txt`:
- **Data Science**: numpy, scipy, scikit-learn
- **Web**: fastapi, uvicorn, jinja2
- **Database**: sqlalchemy, psycopg2-binary
- **ML**: tensorflow, filterpy
- **Utilities**: requests, python-dateutil, python-dotenv

## Git Organization

Ignored files (`.gitignore`):
- `.env` (API keys)
- `__pycache__/`
- `*.pyc`
- `data/cache/` (API cache)
- `basketball_predictor.db` (local database)

Tracked files:
- All source code (`src/`, `scripts/`, `validation/`)
- Documentation (`docs/`, `README.md`)
- Configuration (`config.py`, `requirements.txt`)
- Web assets (`static/`, `templates/`)

## Best Practices

1. **Always run from project root**: `cd "Cursor Test"`
2. **Use relative imports**: Scripts handle path resolution
3. **Check documentation**: Start with `README.md`
4. **Validate before betting**: Run backtests first
5. **Keep .env secure**: Never commit API keys

## Next Steps

1. ✅ Project organized and paths fixed
2. ⏳ Run validation to get real accuracy
3. ⏳ Use system for daily predictions
4. ⏳ Implement Phase 2 enhancements (optional)

---

**Last Updated**: January 12, 2026  
**Version**: Phase 1 Complete (v1.0)

