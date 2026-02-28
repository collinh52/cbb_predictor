# 🏀 College Basketball Predictor (CBB Predictor)

[![Test Status](https://github.com/yourusername/cbb_predictor/actions/workflows/test.yml/badge.svg)](https://github.com/yourusername/cbb_predictor/actions/workflows/test.yml)
[![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A sophisticated college basketball prediction system with **68.96% backtested accuracy** using advanced statistical methods and machine learning techniques.

## ✨ Key Features

### 🎯 Advanced Rating System (Phase 3D)
- **Fixed Home Court Advantage**: 0-4 point realistic range (vs. previous 5.0 cap)
- **Road Warrior Bonus**: Teams performing better away from home get +0-3 points
- **Pace Adjustment**: Tempo-free ratings (points per 100 possessions)
- **Pythagorean Expectation**: Identifies lucky/unlucky teams with regression
- **Enhanced Neutral Court Detection**: 248 games detected (vs. 0 before)

### 📊 Comprehensive Data & APIs
- **5,889+ games** from ESPN API across **372 D1 teams**
- **Real-time predictions** using live ESPN data
- **Betting line integration** via The Odds API
- **Prediction tracking** with accuracy monitoring

### 🔬 Rigorous Validation
- **68.96% backtested accuracy** on 2024-25 season
- **Three validation methods**: Last season, rolling, and cross-validation
- **Statistical significance testing** (p < 0.05 vs. random guessing)
- **Historical accuracy tracking** with confidence intervals

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/yourusername/cbb_predictor.git
cd cbb_predictor

# Install dependencies
pip install -r requirements.txt

# Install Playwright browser binaries (for KenPom login)
python -m playwright install chromium

# Set up environment variables
cp .env.example .env
# Edit .env with your API keys

# View current team ratings
python scripts/show_team_ratings_v3.py

# Generate today's predictions
python scripts/predict_today.py

# Validate accuracy
python validation/run_all_backtests.py
```

## 📈 Performance Metrics

### Backtested Accuracy: **68.96%**
- **Tested on**: 1,849 predictions from 2024-25 season
- **High confidence** (>10 pt margin): **94.7%** accuracy
- **Medium confidence** (5-10 pt margin): **79.9%** accuracy
- **Statistically significant**: p < 0.05 vs. random guessing

<!-- ACCURACY_STATS_START -->

### 🎯 Live ATS Prediction Tracking

**Last Updated**: February 28, 2026 at 04:48 AM

![ATS Accuracy](https://img.shields.io/badge/ATS_Record-50.2%25-yellowgreen)

#### 🏆 Rolling ATS Performance

| Timeframe | ATS Record | Accuracy |
|-----------|------------|----------|
| **Latest** (2026-02-27) | 9-11 | **45.0%** |
| **Last 7 Days** | 156-168 | **48.1%** |
| **Last 30 Days** | 388-385 | **50.2%** |
| **All-Time** | 388-385 | **50.2%** |

**Over/Under Accuracy**: 49.9%

#### 🎯 Accuracy by Confidence (ATS)

| Confidence | Record | Accuracy |
|------------|--------|----------|
| **50%+** | 113-116 | **49.3%** |
| **60%+** | 46-38 | **54.8%** |
| **70%+** | 18-15 | **54.5%** |
| **80%+** | 5-5 | **50.0%** |

#### 🏀 ATS Accuracy by Conference

| Conference | Record | Accuracy |
|------------|--------|----------|
| Western Athletic | 12-4 | **75.0%** |
| Big South | 15-6 | **71.4%** |
| Ivy League | 8-5 | **61.5%** |
| Southeastern | 22-14 | **61.1%** |
| Summit League | 9-6 | **60.0%** |
| Mountain West | 15-10 | **60.0%** |
| Atlantic Coast | 22-16 | **57.9%** |
| Atlantic 10 | 15-11 | **57.7%** |
| Mid-Eastern Athletic | 8-6 | **57.1%** |
| Mid-American | 17-13 | **56.7%** |
| Southern | 14-11 | **56.0%** |
| Ohio Valley | 15-12 | **55.6%** |
| ASUN | 16-14 | **53.3%** |
| Big 12 | 17-16 | **51.5%** |
| Big East | 12-12 | **50.0%** |
| America East | 10-10 | **50.0%** |
| Big Sky | 11-11 | **50.0%** |
| Southwestern Athletic | 11-11 | **50.0%** |
| Missouri Valley | 12-13 | **48.0%** |
| Horizon League | 10-11 | **47.6%** |
| Patriot League | 7-8 | **46.7%** |
| Conference USA | 11-13 | **45.8%** |
| Big Ten | 17-22 | **43.6%** |
| West Coast | 8-12 | **40.0%** |
| Metro Atlantic Athletic | 12-18 | **40.0%** |
| Southland | 8-12 | **40.0%** |
| Coastal Athletic Association | 11-17 | **39.3%** |
| Sun Belt | 16-25 | **39.0%** |
| American | 12-19 | **38.7%** |
| Northeast | 8-13 | **38.1%** |
| Big West | 9-16 | **36.0%** |

> *A game counts for a conference if either team is a member.*

#### Combined Statistics

- **Total Predictions**: 773
- **Overall Winner Accuracy**: 50.2%

#### 📅 Predictions for Today (2026-02-28)

| Matchup | Spread Pick | Total Pick | Confidence |
|---------|-------------|------------|------------|
| Arkansas Razorbacks @ Florida Gators | **HOME** (-8.5) | **UNDER** (167.5) | 56% |
| Gonzaga Bulldogs @ Saint Mary's Gaels | **HOME** (+1.5) | **UNDER** (143.5) | 18% |

> 📈 *ATS = Against The Spread (with Vegas lines). Updated daily via GitHub Actions.*

<!-- ACCURACY_STATS_END -->

<!-- RANKINGS_START -->

### 🏆 Top 25 Team Rankings

*Updated: February 28, 2026*

| Rank | Team | Record | Rating | Off | Def |
|------|------|--------|--------|-----|-----|
| 1 | Michigan Wolverines | 27-2 | +30.7 | 71.8 | 41.1 |
| 2 | Duke Blue Devils | 26-2 | +27.4 | 65.4 | 38.0 |
| 3 | Arizona Wildcats | 26-2 | +27.1 | 68.4 | 41.3 |
| 4 | Illinois Fighting Illini | 22-7 | +26.3 | 67.6 | 41.8 |
| 5 | Louisville Cardinals | 20-8 | +25.8 | 69.2 | 43.8 |
| 6 | Alabama Crimson Tide | 21-7 | +25.0 | 73.5 | 48.7 |
| 7 | Iowa State Cyclones | 24-4 | +24.9 | 65.3 | 40.4 |
| 8 | Gonzaga Bulldogs | 28-2 | +24.6 | 65.6 | 41.0 |
| 9 | Florida Gators | 22-6 | +24.6 | 65.9 | 41.5 |
| 10 | Arkansas Razorbacks | 21-7 | +24.6 | 71.1 | 46.6 |
| 11 | Purdue Boilermakers | 22-6 | +24.4 | 66.1 | 41.7 |
| 12 | Vanderbilt Commodores | 22-6 | +23.3 | 67.6 | 44.3 |
| 13 | BYU Cougars | 20-8 | +23.3 | 69.0 | 45.9 |
| 14 | UConn Huskies | 26-3 | +23.2 | 62.8 | 39.7 |
| 15 | Houston Cougars | 23-5 | +22.9 | 60.4 | 37.5 |
| 16 | Texas Tech Red Raiders | 21-7 | +22.5 | 65.4 | 42.9 |
| 17 | Kansas Jayhawks | 21-7 | +22.4 | 63.0 | 40.6 |
| 18 | Michigan State Spartans | 23-5 | +22.4 | 62.0 | 39.6 |
| 19 | Tennessee Volunteers | 20-8 | +21.9 | 62.8 | 41.2 |
| 20 | St. John's Red Storm | 22-6 | +21.4 | 64.3 | 42.9 |
| 21 | NC State Wolfpack | 19-9 | +21.3 | 66.3 | 45.3 |
| 22 | Virginia Cavaliers | 25-3 | +21.3 | 63.8 | 42.6 |
| 23 | Nebraska Cornhuskers | 24-4 | +21.2 | 61.5 | 40.3 |
| 24 | Georgia Bulldogs | 19-9 | +21.2 | 69.1 | 48.3 |
| 25 | Kentucky Wildcats | 18-10 | +21.2 | 64.3 | 43.5 |

> *Rankings based on tempo-free efficiency ratings with strength of schedule adjustment.*

<!-- RANKINGS_END -->

### Real-World Application
- **Daily predictions** with confidence scores
- **Betting line integration** for spread/total picks
- **Historical tracking** of prediction accuracy
- **Risk management** with variance-based confidence

## 📁 Project Structure

```
cbb_predictor/
├── src/                          # Core source code
│   ├── api.py                   # FastAPI backend
│   ├── predictor.py             # Main prediction engine
│   ├── ukf_model.py             # Unscented Kalman Filter
│   ├── data_collector.py        # API data collection
│   ├── espn_collector.py        # ESPN API integration
│   ├── odds_collector.py        # The Odds API integration
│   ├── feature_calculator.py    # Feature engineering
│   ├── database.py              # Database models (SQLAlchemy)
│   ├── hybrid_predictor.py      # UKF + ML hybrid model
│   ├── ml_model.py              # Neural network model
│   ├── ml_features.py           # ML feature engineering
│   ├── accuracy_tracker.py      # Accuracy tracking
│   └── team_name_mapping.py     # Team name reconciliation
├── scripts/                      # Utility scripts
│   ├── show_team_ratings_v3.py  # Display team ratings
│   ├── predict_today.py         # Today's game predictions
│   ├── populate_season.py       # Populate database with season data
│   ├── setup_and_train.py       # Database setup + training
│   ├── daily_collect_odds.py    # Odds collection (GitHub Actions)
│   ├── daily_check_results.py   # Results checking (GitHub Actions)
│   ├── update_readme_accuracy.py # README accuracy updates
│   └── test_odds_api.py         # Test Odds API integration
├── validation/                   # Backtesting & validation
│   ├── backtest_option1_last_season.py
│   ├── backtest_option2_rolling.py
│   ├── backtest_option3_cross_validation.py
│   └── run_all_backtests.py
├── docs/                         # Documentation
│   ├── ARCHITECTURE.md          # Technical architecture
│   ├── STATUS.md                # Development status
│   ├── DEVELOPMENT_HISTORY.md   # Historical development notes
│   └── backtest_results/        # Historical backtest outputs
├── data/                         # Data storage
│   ├── cache/                   # API response cache
│   └── models/                  # Trained ML models
├── static/                       # Web frontend assets
├── templates/                    # HTML templates
├── config.py                     # Configuration
├── requirements.txt              # Python dependencies
├── basketball_predictor.db       # SQLite database
└── .env                          # API keys (not in git)
```

## Quick Start

### 1. Installation

```bash
# Clone or navigate to project
cd "Cursor Test"

# Install dependencies
pip install -r requirements.txt

# Set up API keys in .env
echo 'BASKETBALL_API_KEY="your_sportsdata_key"' > .env
echo 'THE_ODDS_API_KEY="your_odds_api_key"' >> .env
```

### 2. View Team Ratings

```bash
python scripts/show_team_ratings_v3.py
```

**Output**: All 372 D1 teams ranked with Phase 1 enhanced ratings

### 3. Get Today's Predictions

```bash
python scripts/predict_today.py
```

**Output**: Today's games with predicted scores, spreads, and totals

### 4. Validate System Accuracy

```bash
python validation/run_all_backtests.py
```

**Output**: Comprehensive accuracy report from 3 validation methods

## Rating Algorithm

### Phase 1 Enhancements (Implemented)

1. **Home Court Advantage (±3.5 points)**
   - Road wins valued more than home wins
   - Adjusts opponent strength based on venue

2. **Margin of Victory (diminishing returns)**
   - Blowout wins count more than squeakers
   - Logarithmic scaling prevents running up score
   - 20-point win ≈ 13.5 adjusted points

3. **Recency Weighting (98% decay)**
   - Recent games weighted more heavily
   - Captures momentum and team improvement
   - Most recent game = 1.0x, 10 games ago = 0.82x

### Current Performance

- **Rating Spread**: +73.0 (Michigan) to -56.8 (worst)
- **Estimated Accuracy**: ~57% ATS (validation pending)
- **Comparison**: KenPom ~58-60%, BartTorvik ~57-59%

### Top 5 Teams (Phase 1 Enhanced)

1. Michigan (14-1) - +73.0 🔥
2. Alabama (11-5) - +64.0 🔥 (toughest schedule)
3. Iowa State (16-0) - +62.2 🔥
4. Purdue (15-1) - +61.7 🔥
5. Arizona (16-0) - +61.6 🔥

## API Endpoints

Start the web server:
```bash
uvicorn src.api:app --reload
```

Available endpoints:
- `GET /` - Web interface
- `GET /api/games/today` - Today's games
- `GET /api/predictions/{game_id}` - Game prediction
- `GET /api/predictions/accuracy` - Overall accuracy
- `GET /api/models/versions` - Model versions

## Validation Methods

### Option 1: Last Season Validation
Tests on 2024-25 season (different season = true out-of-sample)

### Option 2: Rolling Validation
Tests on recent 2025-26 games (realistic real-world scenario)

### Option 3: Cross-Validation
5-fold cross-validation with confidence intervals (most rigorous)

**Run all three:**
```bash
python validation/run_all_backtests.py
```

## Configuration

Edit `config.py` for:
- API keys and endpoints
- UKF parameters (process/measurement noise)
- Feature calculation weights
- Database settings
- ML model hyperparameters

## Data Sources

- **ESPN API**: Historical game data (free)
- **The Odds API**: Real-time betting lines (free tier)
- **SportsDataIO**: Alternative data source (free trial)

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Links

- **GitHub Repository**: [https://github.com/yourusername/cbb_predictor](https://github.com/yourusername/cbb_predictor)
- **Issues**: [https://github.com/yourusername/cbb_predictor/issues](https://github.com/yourusername/cbb_predictor/issues)

---

**Built with ❤️ for the basketball analytics community**

## Development Roadmap

### Phase 1 ✅ COMPLETE
- [x] Home court advantage
- [x] Margin of victory
- [x] Recency weighting
- [x] SOS adjustment
- [x] Comprehensive data collection (5,889 games)

### Phase 2 (Future)
- [ ] Pace adjustment (tempo-free stats)
- [ ] Pythagorean expectation
- [ ] Conference strength multipliers
- [ ] Four Factors (requires box score data)
- [ ] Advanced player tracking

### Target: 62-65% ATS accuracy (KenPom level)

## Contributing

This is a personal project for learning and experimentation with sports analytics.

## License

Private project - all rights reserved.

## Acknowledgments

- **KenPom**: Inspiration for rating methodology
- **Dean Oliver**: Four Factors framework
- **ESPN**: Free API access for historical data
- **The Odds API**: Real-time betting line data

---

**Last Updated**: January 12, 2026  
**Current Version**: Phase 1 Complete (v1.0)

