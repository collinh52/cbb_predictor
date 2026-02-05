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

**Last Updated**: February 05, 2026 at 05:13 AM

![ATS Accuracy](https://img.shields.io/badge/ATS_Record-50.4%25-yellowgreen)

#### 🏆 Rolling ATS Performance

| Timeframe | ATS Record | Accuracy |
|-----------|------------|----------|
| **Last 7 Days** | 119-118 | **50.2%** |
| **Last 30 Days** | 120-118 | **50.4%** |
| **All-Time** | 120-118 | **50.4%** |

**Over/Under Accuracy**: 48.3%

#### 🎯 Accuracy by Confidence (ATS)

| Confidence | Record | Accuracy |
|------------|--------|----------|
| **50%+** | 92-94 | **49.5%** |
| **60%+** | 66-72 | **47.8%** |
| **70%+** | 42-43 | **49.4%** |
| **80%+** | 25-20 | **55.6%** |

#### Straight-Up Predictions (Games Without Vegas Lines)

| **7-Day** | 0/0 (0.0%) |
| **30-Day** | 1/3 (33.3%) |
| **All-Time** | 1/3 (33.3%) |

#### Combined Statistics

- **Total Predictions**: 241
- **Overall Winner Accuracy**: 50.2%

#### 📅 Predictions for Today (2026-02-05)

| Matchup | Spread Pick | Total Pick | Confidence |
|---------|-------------|------------|------------|
| Penn State Nittany Lions @ Michigan Wolverines | **HOME** (-25.0) | **UNDER** (162.0) | 70% |
| Abilene Christian Wildcats @ Utah Valley Wolverines | **HOME** (-13.5) | **UNDER** (146.0) | 89% |
| New Haven Chargers @ LIU Sharks | **AWAY** (+9.5) | **UNDER** (150.5) | 95% |
| CSU Bakersfield Roadrunners @ UC Irvine Anteaters | **HOME** (-16.5) | **UNDER** (146.0) | 56% |
| Rider Broncs @ Marist Red Foxes | **HOME** (-14.5) | **OVER** (135.5) | 53% |
| Southern Indiana Screaming Eagles @ Tenn-Martin Skyhawks | **HOME** (-10.5) | **UNDER** (132.5) | 62% |
| Denver Pioneers @ North Dakota St Bison | **HOME** (-12.0) | **OVER** (159.0) | 53% |
| Drexel Dragons @ Campbell Fighting Camels | **HOME** (-4.5) | **UNDER** (143.0) | 50% |
| Binghamton Bearcats @ UMBC Retrievers | **HOME** (-12.5) | **OVER** (138.5) | 65% |
| Canisius Golden Griffins @ Quinnipiac Bobcats | **HOME** (-14.0) | **OVER** (141.5) | 54% |
| Eastern Washington Eagles @ Montana Grizzlies | **HOME** (-6.0) | **UNDER** (151.5) | 55% |
| North Carolina A&T Aggies @ Charleston Cougars | **HOME** (-11.5) | **OVER** (154.5) | 49% |
| Western Illinois Leathernecks @ Tennessee Tech Golden Eagles | **HOME** (-8.5) | **UNDER** (142.0) | 56% |
| Jacksonville Dolphins @ Queens University Royals | **HOME** (-9.0) | **OVER** (147.0) | 54% |
| Northeastern Huskies @ Hofstra Pride | **HOME** (-10.0) | **OVER** (155.5) | 45% |
| Morehead St Eagles @ SE Missouri St Redhawks | **HOME** (-8.0) | **OVER** (145.0) | 48% |
| The Citadel Bulldogs @ Samford Bulldogs | **HOME** (-12.5) | **OVER** (143.0) | 51% |
| UC Riverside Highlanders @ CSU Fullerton Titans | **HOME** (-6.0) | **UNDER** (156.5) | 59% |
| St. Francis (PA) Red Flash @ Mercyhurst Lakers | **HOME** (-9.5) | **UNDER** (135.5) | 66% |
| Chicago St Cougars @ Central Connecticut St Blue Devils | **HOME** (-10.0) | **OVER** (138.5) | 39% |
| Omaha Mavericks @ North Dakota Fighting Hawks | **HOME** (-2.0) | **OVER** (150.0) | 39% |
| Jacksonville St Gamecocks @ Western Kentucky Hilltoppers | **HOME** (-4.5) | **UNDER** (141.0) | 57% |
| Eastern Illinois Panthers @ Tennessee St Tigers | **HOME** (-10.5) | **UNDER** (145.5) | 36% |
| Stonehill Skyhawks @ Fairleigh Dickinson Knights | **HOME** (-2.0) | **UNDER** (128.5) | 36% |
| Long Beach St 49ers @ UC San Diego Tritons | **HOME** (-9.0) | **UNDER** (143.5) | 43% |
| William & Mary Tribe @ UNC Wilmington Seahawks | **HOME** (-5.0) | **UNDER** (159.0) | 59% |
| Loyola (Chi) Ramblers @ Davidson Wildcats | **HOME** (-9.5) | **UNDER** (139.5) | 50% |
| Tarleton State Texans @ Cal Baptist Lancers | **HOME** (-10.0) | **UNDER** (141.5) | 60% |
| Iona Gaels @ Siena Saints | **HOME** (-7.5) | **UNDER** (141.0) | 52% |
| Monmouth Hawks @ Stony Brook Seawolves | **HOME** (-3.5) | **OVER** (135.5) | 46% |
| UMass Lowell River Hawks @ NJIT Highlanders | **HOME** (-2.5) | **UNDER** (148.5) | 40% |
| Idaho Vandals @ Montana St Bobcats | **HOME** (-4.0) | **OVER** (147.5) | 29% |
| UT-Arlington Mavericks @ Utah Tech Trailblazers | **HOME** (-1.0) | **UNDER** (139.5) | 41% |
| N Colorado Bears @ Weber State Wildcats | **HOME** (+1.5) | **UNDER** (162.0) | 35% |
| North Florida Ospreys @ West Georgia Wolves | **HOME** (-7.0) | **UNDER** (169.0) | 39% |
| Stetson Hatters @ Bellarmine Knights | **HOME** (-6.0) | **OVER** (150.0) | 47% |
| Northern Arizona Lumberjacks @ Idaho State Bengals | **HOME** (-8.0) | **OVER** (142.0) | 37% |
| Le Moyne Dolphins @ Wagner Seahawks | **AWAY** (-2.5) | **UNDER** (141.0) | 50% |
| West Virginia Mountaineers @ Cincinnati Bearcats | **HOME** (-5.5) | **UNDER** (128.5) | 47% |
| Ohio State Buckeyes @ Maryland Terrapins | **HOME** (+7.5) | **UNDER** (151.5) | 33% |
| Memphis Tigers @ UAB Blazers | **HOME** (-1.5) | **UNDER** (153.0) | 44% |
| Lindenwood Lions @ Arkansas-Little Rock Trojans | **HOME** (+0.0) | **OVER** (151.5) | 21% |
| Fairfield Stags @ Sacred Heart Pioneers | **HOME** (-1.0) | **OVER** (154.5) | 28% |
| Merrimack Warriors @ Mt. St. Mary's Mountaineers | **HOME** (+3.5) | **UNDER** (136.5) | 33% |
| Florida Gulf Coast Eagles @ Eastern Kentucky Colonels | **HOME** (-1.0) | **OVER** (154.0) | 26% |
| Elon Phoenix @ Hampton Pirates | **HOME** (+2.0) | **OVER** (142.5) | 15% |
| Saint Peter's Peacocks @ Manhattan Jaspers | **HOME** (+4.5) | **OVER** (146.5) | 14% |
| Vermont Catamounts @ Maine Black Bears | **AWAY** (-7.5) | **UNDER** (129.5) | 17% |
| Mercer Bears @ Chattanooga Mocs | **AWAY** (-4.5) | **UNDER** (155.5) | 16% |
| Albany Great Danes @ Bryant Bulldogs | **HOME** (+1.5) | **UNDER** (134.5) | 15% |
| CSU Northridge Matadors @ Cal Poly Mustangs | **HOME** (+2.0) | **UNDER** (176.0) | 29% |
| UC Santa Barbara Gauchos @ UC Davis Aggies | **AWAY** (-2.5) | **OVER** (147.0) | 9% |

> 📈 *ATS = Against The Spread (with Vegas lines). Updated daily via GitHub Actions.*

<!-- ACCURACY_STATS_END -->

<!-- RANKINGS_START -->

### 🏆 Top 25 Team Rankings

*Updated: February 05, 2026*

| Rank | Team | Record | Rating | Off | Def |
|------|------|--------|--------|-----|-----|
| 1 | Michigan Wolverines | 20-1 | +30.2 | 71.7 | 41.5 |
| 2 | Arizona Wildcats | 22-0 | +27.3 | 69.6 | 42.4 |
| 3 | Duke Blue Devils | 21-1 | +26.0 | 64.8 | 38.8 |
| 4 | Iowa State Cyclones | 20-2 | +25.8 | 67.2 | 41.4 |
| 5 | Louisville Cardinals | 16-6 | +25.6 | 68.7 | 43.6 |
| 6 | Illinois Fighting Illini | 20-3 | +25.4 | 66.8 | 41.3 |
| 7 | Florida Gators | 16-6 | +24.4 | 65.9 | 41.9 |
| 8 | Purdue Boilermakers | 18-4 | +24.3 | 66.0 | 41.7 |
| 9 | Gonzaga Bulldogs | 22-2 | +24.0 | 65.7 | 41.6 |
| 10 | Alabama Crimson Tide | 15-7 | +24.0 | 72.3 | 48.3 |
| 11 | Vanderbilt Commodores | 19-3 | +23.9 | 68.5 | 44.6 |
| 12 | Houston Cougars | 20-2 | +23.9 | 61.7 | 37.8 |
| 13 | UConn Huskies | 22-1 | +23.5 | 62.9 | 39.7 |
| 14 | BYU Cougars | 17-5 | +23.1 | 68.1 | 45.3 |
| 15 | Arkansas Razorbacks | 16-6 | +23.0 | 70.3 | 47.3 |
| 16 | Kansas Jayhawks | 17-5 | +22.7 | 63.4 | 40.7 |
| 17 | Tennessee Volunteers | 16-6 | +22.1 | 63.5 | 41.8 |
| 18 | St. John's Red Storm | 17-5 | +22.0 | 65.4 | 43.3 |
| 19 | NC State Wolfpack | 17-6 | +21.9 | 67.0 | 45.4 |
| 20 | Kentucky Wildcats | 16-7 | +21.5 | 65.2 | 44.0 |
| 21 | Saint Louis Billikens | 22-1 | +21.4 | 67.7 | 46.3 |
| 22 | Texas Tech Red Raiders | 16-6 | +21.4 | 65.0 | 43.6 |
| 23 | Michigan State Spartans | 19-4 | +21.2 | 60.6 | 39.5 |
| 24 | Georgia Bulldogs | 16-6 | +21.1 | 70.1 | 49.4 |
| 25 | Nebraska Cornhuskers | 20-2 | +20.7 | 61.0 | 40.6 |

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

