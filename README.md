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

**Last Updated**: March 03, 2026 at 05:10 AM

![ATS Accuracy](https://img.shields.io/badge/ATS_Record-51.0%25-yellowgreen)

#### 🏆 Rolling ATS Performance

| Timeframe | ATS Record | Accuracy |
|-----------|------------|----------|
| **Latest** (2026-03-02) | 7-9 | **43.8%** |
| **Last 7 Days** | 173-162 | **51.6%** |
| **Last 30 Days** | 482-464 | **51.0%** |
| **All-Time** | 482-464 | **51.0%** |

**Over/Under Accuracy**: 51.2%

#### 🎯 Accuracy by Confidence (ATS)

| Confidence | Record | Accuracy |
|------------|--------|----------|
| **50%+** | 135-143 | **48.6%** |
| **60%+** | 56-53 | **51.4%** |
| **70%+** | 19-18 | **51.4%** |
| **80%+** | 5-5 | **50.0%** |

#### 🏀 ATS Accuracy by Conference

| Conference | Record | Accuracy |
|------------|--------|----------|
| Big South | 19-6 | **76.0%** |
| Western Athletic | 14-5 | **73.7%** |
| Southern | 19-11 | **63.3%** |
| Mountain West | 19-12 | **61.3%** |
| Summit League | 11-7 | **61.1%** |
| Ivy League | 10-7 | **58.8%** |
| Southeastern | 25-19 | **56.8%** |
| Atlantic 10 | 18-14 | **56.2%** |
| Atlantic Coast | 27-21 | **56.2%** |
| Mid-American | 19-15 | **55.9%** |
| Mid-Eastern Athletic | 12-10 | **54.5%** |
| America East | 13-11 | **54.2%** |
| ASUN | 19-17 | **52.8%** |
| Southwestern Athletic | 14-13 | **51.9%** |
| Missouri Valley | 16-15 | **51.6%** |
| Patriot League | 9-9 | **50.0%** |
| Ohio Valley | 16-16 | **50.0%** |
| Southland | 15-15 | **50.0%** |
| Conference USA | 14-15 | **48.3%** |
| Big East | 14-15 | **48.3%** |
| Big 12 | 20-22 | **47.6%** |
| Coastal Athletic Association | 16-18 | **47.1%** |
| Metro Atlantic Athletic | 16-20 | **44.4%** |
| West Coast | 11-14 | **44.0%** |
| Horizon League | 11-14 | **44.0%** |
| Big West | 13-17 | **43.3%** |
| Big Ten | 20-27 | **42.6%** |
| Big Sky | 13-19 | **40.6%** |
| American | 15-22 | **40.5%** |
| Northeast | 10-15 | **40.0%** |
| Sun Belt | 16-25 | **39.0%** |

> *A game counts for a conference if either team is a member.*

#### Combined Statistics

- **Total Predictions**: 946
- **Overall Winner Accuracy**: 51.0%

#### 📅 Recent Predictions (2026-03-02)

| Matchup | Spread Pick | Total Pick | Confidence |
|---------|-------------|------------|------------|
| McNeese Cowboys @ Nicholls St Colonels | **AWAY** (-11.0) | **UNDER** (145.0) | 67% |
| IUPUI Jaguars @ Cleveland St Vikings | **HOME** (-1.5) | **UNDER** (170.0) | 88% |
| Coppin St Eagles @ Howard Bison | **AWAY** (+19.5) | **OVER** (136.5) | 49% |
| Northwestern St Demons @ UT Rio Grande Valley Vaqueros | **AWAY** (+10.5) | **UNDER** (137.5) | 72% |
| Iowa State Cyclones @ Arizona Wildcats | **AWAY** (+8.5) | **UNDER** (147.5) | 60% |
| East Texas A&M Lions @ Texas A&M-CC Islanders | **AWAY** (+8.0) | **UNDER** (137.0) | 66% |
| SE Louisiana Lions @ New Orleans Privateers | **AWAY** (+7.5) | **UNDER** (144.0) | 33% |
| Duke Blue Devils @ NC State Wolfpack | **HOME** (+9.5) | **UNDER** (148.5) | 39% |
| Montana Grizzlies @ N Colorado Bears | **AWAY** (+6.5) | **UNDER** (153.5) | 53% |
| Idaho Vandals @ Eastern Washington Eagles | **HOME** (-3.0) | **UNDER** (153.0) | 40% |
| Norfolk St Spartans @ Morgan St Bears | **HOME** (+2.5) | **OVER** (154.5) | 38% |
| Weber State Wildcats @ Portland St Vikings | **AWAY** (+4.5) | **UNDER** (146.0) | 35% |
| Idaho State Bengals @ Sacramento St Hornets | **HOME** (-1.5) | **UNDER** (159.5) | 19% |
| Stephen F. Austin Lumberjacks @ Incarnate Word Cardinals | **HOME** (+8.5) | **UNDER** (145.5) | 24% |
| Montana St Bobcats @ Northern Arizona Lumberjacks | **HOME** (+5.5) | **UNDER** (142.5) | 23% |
| North Carolina Central Eagles @ Maryland-Eastern Shore Hawks | **AWAY** (+1.0) | **UNDER** (133.5) | 13% |
| South Carolina St Bulldogs @ Delaware St Hornets | **AWAY** (+1.5) | **UNDER** (138.0) | 51% |
| Lamar Cardinals @ Houston Christian Huskies | **HOME** (+1.0) | **UNDER** (132.5) | 32% |

> 📈 *ATS = Against The Spread (with Vegas lines). Updated daily via GitHub Actions.*

<!-- ACCURACY_STATS_END -->

<!-- RANKINGS_START -->

### 🏆 Top 25 Team Rankings

*Updated: March 03, 2026*

| Rank | Team | Record | Rating | Off | Def |
|------|------|--------|--------|-----|-----|
| 1 | Michigan Wolverines | 27-2 | +30.8 | 71.8 | 41.1 |
| 2 | Duke Blue Devils | 28-2 | +28.2 | 65.6 | 37.4 |
| 3 | Arizona Wildcats | 28-2 | +28.2 | 68.8 | 40.7 |
| 4 | Illinois Fighting Illini | 22-7 | +26.4 | 67.7 | 41.8 |
| 5 | Florida Gators | 23-6 | +25.6 | 66.9 | 41.6 |
| 6 | Louisville Cardinals | 20-9 | +25.6 | 69.1 | 44.0 |
| 7 | Alabama Crimson Tide | 22-7 | +25.0 | 72.9 | 48.2 |
| 8 | Iowa State Cyclones | 24-6 | +24.7 | 64.9 | 40.6 |
| 9 | Purdue Boilermakers | 22-7 | +24.7 | 66.2 | 41.8 |
| 10 | Gonzaga Bulldogs | 28-3 | +24.2 | 65.1 | 40.9 |
| 11 | Arkansas Razorbacks | 21-8 | +23.9 | 71.0 | 47.1 |
| 12 | Houston Cougars | 24-5 | +23.6 | 61.0 | 37.4 |
| 13 | UConn Huskies | 27-3 | +23.3 | 63.1 | 39.9 |
| 14 | Vanderbilt Commodores | 22-7 | +23.2 | 67.5 | 44.3 |
| 15 | BYU Cougars | 20-9 | +23.0 | 68.7 | 45.9 |
| 16 | Texas Tech Red Raiders | 22-7 | +22.9 | 65.5 | 42.7 |
| 17 | St. John's Red Storm | 23-6 | +22.5 | 65.1 | 42.6 |
| 18 | Michigan State Spartans | 24-5 | +22.5 | 61.9 | 39.4 |
| 19 | Kansas Jayhawks | 21-8 | +22.2 | 62.8 | 40.6 |
| 20 | Tennessee Volunteers | 20-9 | +22.0 | 62.7 | 41.1 |
| 21 | Kentucky Wildcats | 19-10 | +21.9 | 65.0 | 43.4 |
| 22 | Georgia Bulldogs | 20-9 | +21.6 | 69.2 | 47.9 |
| 23 | Nebraska Cornhuskers | 25-4 | +21.3 | 61.4 | 40.2 |
| 24 | Saint Louis Billikens | 26-3 | +21.1 | 67.2 | 46.1 |
| 25 | Virginia Cavaliers | 25-4 | +20.9 | 63.4 | 42.4 |

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

