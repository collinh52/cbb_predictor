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

**Last Updated**: February 08, 2026 at 12:29 PM

![ATS Accuracy](https://img.shields.io/badge/ATS_Record-62.5%25-brightgreen)

#### 🏆 Rolling ATS Performance

| Timeframe | ATS Record | Accuracy |
|-----------|------------|----------|
| **Last 7 Days** | 209-97 | **68.3%** |
| **Last 30 Days** | 280-168 | **62.5%** |
| **All-Time** | 280-168 | **62.5%** |

**Over/Under Accuracy**: 50.4%

#### 🎯 Accuracy by Confidence (ATS)

| Confidence | Record | Accuracy |
|------------|--------|----------|
| **50%+** | 158-105 | **60.1%** |
| **60%+** | 98-73 | **57.3%** |
| **70%+** | 57-43 | **57.0%** |
| **80%+** | 30-20 | **60.0%** |

#### Straight-Up Predictions (Games Without Vegas Lines)

| **7-Day** | 0/0 (0.0%) |
| **30-Day** | 1/3 (33.3%) |
| **All-Time** | 1/3 (33.3%) |

#### Combined Statistics

- **Total Predictions**: 451
- **Overall Winner Accuracy**: 62.3%

#### 📅 Predictions for Today (2026-02-09)

| Matchup | Spread Pick | Total Pick | Confidence |
|---------|-------------|------------|------------|
| UT Rio Grande Valley Vaqueros @ Nicholls St Colonels | **AWAY** (-1.0) | **UNDER** (145.5) | 64% |
| Alabama A&M Bulldogs @ Grambling St Tigers | **AWAY** (+5.5) | **UNDER** (135.0) | 56% |
| Houston Christian Huskies @ McNeese Cowboys | **HOME** (-18.0) | **UNDER** (140.5) | 54% |
| Xavier Musketeers @ St. John's Red Storm | **HOME** (-14.5) | **UNDER** (162.5) | 68% |
| NC State Wolfpack @ Louisville Cardinals | **HOME** (-7.0) | **UNDER** (161.5) | 66% |
| Oregon Ducks @ Indiana Hoosiers | **HOME** (-11.5) | **OVER** (142.0) | 47% |
| East Texas A&M Lions @ Stephen F. Austin Lumberjacks | **HOME** (-15.5) | **UNDER** (141.0) | 89% |
| Northwestern St Demons @ Lamar Cardinals | **HOME** (-9.0) | **UNDER** (136.0) | 85% |
| Delaware St Hornets @ North Carolina Central Eagles | **HOME** (-8.0) | **UNDER** (134.0) | 93% |
| Texas Southern Tigers @ Bethune-Cookman Wildcats | **HOME** (-8.0) | **OVER** (149.5) | 55% |
| Alabama St Hornets @ Southern Jaguars | **HOME** (-7.0) | **UNDER** (151.5) | 42% |
| Valparaiso Beacons @ Drake Bulldogs | **HOME** (-2.5) | **OVER** (143.5) | 45% |
| Northern Iowa Panthers @ Murray St Racers | **HOME** (-5.0) | **UNDER** (143.0) | 39% |
| Navy Midshipmen @ Bucknell Bison | **AWAY** (-6.5) | **OVER** (134.0) | 44% |
| Jackson St Tigers @ Arkansas-Pine Bluff Golden Lions | **HOME** (-6.0) | **OVER** (158.0) | 64% |
| Central Arkansas Bears @ North Alabama Lions | **AWAY** (-8.0) | **OVER** (149.0) | 28% |
| Southern Illinois Salukis @ Indiana St Sycamores | **HOME** (-1.0) | **UNDER** (145.5) | 58% |
| Illinois St Redbirds @ Evansville Purple Aces | **AWAY** (-9.5) | **UNDER** (138.0) | 60% |
| Arizona Wildcats @ Kansas Jayhawks | **AWAY** (-2.5) | **UNDER** (151.5) | 44% |
| Belmont Bruins @ Bradley Braves | **HOME** (+2.5) | **OVER** (155.0) | 20% |
| St. Francis (PA) Red Flash @ Chicago St Cougars | **HOME** (-2.5) | **UNDER** (145.0) | 25% |
| UNC Wilmington Seahawks @ Charleston Cougars | **HOME** (-1.0) | **UNDER** (149.5) | 24% |
| Texas A&M-CC Islanders @ New Orleans Privateers | **HOME** (+1.0) | **OVER** (148.5) | 24% |
| Alcorn St Braves @ Miss Valley St Delta Devils | **HOME** (+6.0) | **OVER** (141.5) | 14% |
| Incarnate Word Cardinals @ SE Louisiana Lions | **HOME** (-1.0) | **UNDER** (139.0) | 18% |
| Prairie View Panthers @ Florida A&M Rattlers | **HOME** (-3.0) | **UNDER** (147.5) | 48% |
| Yale Bulldogs @ Howard Bison | **HOME** (+8.5) | **UNDER** (147.5) | 36% |

> 📈 *ATS = Against The Spread (with Vegas lines). Updated daily via GitHub Actions.*

<!-- ACCURACY_STATS_END -->

<!-- RANKINGS_START -->

### 🏆 Top 25 Team Rankings

*Updated: February 09, 2026*

| Rank | Team | Record | Rating | Off | Def |
|------|------|--------|--------|-----|-----|
| 1 | Michigan Wolverines | 22-1 | +30.9 | 72.0 | 41.2 |
| 2 | Arizona Wildcats | 23-0 | +28.0 | 69.5 | 41.5 |
| 3 | Duke Blue Devils | 21-2 | +26.1 | 64.9 | 38.8 |
| 4 | Iowa State Cyclones | 21-2 | +25.7 | 67.1 | 41.4 |
| 5 | Illinois Fighting Illini | 20-4 | +25.4 | 67.1 | 41.7 |
| 6 | Louisville Cardinals | 17-6 | +25.4 | 68.6 | 43.7 |
| 7 | Florida Gators | 17-6 | +24.5 | 65.6 | 41.5 |
| 8 | Alabama Crimson Tide | 16-7 | +24.2 | 72.7 | 48.5 |
| 9 | Gonzaga Bulldogs | 23-2 | +24.1 | 65.7 | 41.6 |
| 10 | Purdue Boilermakers | 19-4 | +24.0 | 65.8 | 41.8 |
| 11 | Houston Cougars | 21-2 | +23.9 | 61.6 | 37.7 |
| 12 | Vanderbilt Commodores | 19-4 | +23.7 | 68.5 | 44.8 |
| 13 | Arkansas Razorbacks | 17-6 | +23.3 | 70.2 | 46.9 |
| 14 | BYU Cougars | 17-6 | +23.2 | 68.4 | 45.5 |
| 15 | UConn Huskies | 22-2 | +23.0 | 62.8 | 39.8 |
| 16 | St. John's Red Storm | 18-5 | +22.8 | 66.2 | 43.4 |
| 17 | Kansas Jayhawks | 18-5 | +22.5 | 63.0 | 40.5 |
| 18 | NC State Wolfpack | 18-6 | +22.2 | 67.2 | 45.3 |
| 19 | Tennessee Volunteers | 16-7 | +22.1 | 63.6 | 41.9 |
| 20 | Michigan State Spartans | 20-4 | +21.7 | 61.3 | 39.7 |
| 21 | Kentucky Wildcats | 17-7 | +21.7 | 65.0 | 43.6 |
| 22 | Saint Louis Billikens | 23-1 | +21.5 | 67.7 | 46.2 |
| 23 | Georgia Bulldogs | 17-6 | +21.4 | 69.8 | 48.8 |
| 24 | Texas Tech Red Raiders | 17-6 | +21.3 | 64.8 | 43.5 |
| 25 | Nebraska Cornhuskers | 21-2 | +21.1 | 61.5 | 40.8 |

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

