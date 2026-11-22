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

**Last Updated**: November 22, 2026 at 06:54 PM

![ATS Accuracy](https://img.shields.io/badge/ATS_Record-50.7%25-yellowgreen)

#### 🏆 Rolling ATS Performance

| Timeframe | ATS Record | Accuracy |
|-----------|------------|----------|
| **Latest** (2026-11-21) | 1-0 | **100.0%** |
| **Last 7 Days** | 16-7 | **69.6%** |
| **Last 30 Days** | 32-25 | **56.1%** |
| **All-Time** | 796-774 | **50.7%** |

**Over/Under Accuracy**: 51.0%

#### 🎯 Accuracy by Confidence (ATS)

| Confidence | Record | Accuracy |
|------------|--------|----------|
| **50%+** | 263-255 | **50.8%** |
| **60%+** | 122-107 | **53.3%** |
| **70%+** | 42-40 | **51.2%** |
| **80%+** | 13-14 | **48.1%** |

#### 🏀 ATS Accuracy by Conference

| Conference | Record | Accuracy |
|------------|--------|----------|
| Big South | 27-8 | **77.1%** |
| Southern | 25-15 | **62.5%** |
| Mountain West | 43-26 | **62.3%** |
| United Athletic | 21-13 | **61.8%** |
| Patriot League | 17-12 | **58.6%** |
| Atlantic Coast | 59-44 | **57.3%** |
| Summit League | 16-12 | **57.1%** |
| West Coast | 24-18 | **57.1%** |
| Mid-Eastern Athletic | 21-17 | **55.3%** |
| Missouri Valley | 27-23 | **54.0%** |
| Atlantic 10 | 41-35 | **53.9%** |
| Southwestern Athletic | 26-23 | **53.1%** |
| Ohio Valley | 23-21 | **52.3%** |
| Big 12 | 55-52 | **51.4%** |
| America East | 19-18 | **51.4%** |
| Mid-American | 31-31 | **50.0%** |
| Big East | 32-32 | **50.0%** |
| Conference USA | 26-27 | **49.1%** |
| Big West | 25-26 | **49.0%** |
| Southland | 20-21 | **48.8%** |
| Southeastern | 58-61 | **48.7%** |
| Metro | 23-26 | **46.9%** |
| Northeast | 14-17 | **45.2%** |
| Sun Belt | 26-32 | **44.8%** |
| Big Ten | 54-67 | **44.6%** |
| Atlantic Sun | 24-31 | **43.6%** |
| Coastal Athletic Association | 23-33 | **41.1%** |
| Horizon League | 16-23 | **41.0%** |
| Big Sky | 19-29 | **39.6%** |
| Ivy League | 10-16 | **38.5%** |
| American | 25-42 | **37.3%** |

> *A game counts for a conference if either team is a member.*

#### Combined Statistics

- **Total Predictions**: 1570
- **Overall Winner Accuracy**: 50.7%

#### 📅 Predictions for Today (2026-11-22)

| Matchup | Spread Pick | Total Pick | Confidence |
|---------|-------------|------------|------------|
| Nicholls St Colonels @ Troy Trojans | **HOME** (-5.5) | **OVER** (135.5) | 62% |
| West Florida Argonauts @ South Alabama Jaguars | **HOME** (-5.5) | **OVER** (138.0) | 59% |
| Southern Indiana Screaming Eagles @ Texas Longhorns | **AWAY** (+37.5) | **UNDER** (150.5) | 71% |
| Seattle Redhawks @ UC San Diego Tritons | **HOME** (+0.0) | **UNDER** (148.5) | 91% |
| Delaware Blue Hens @ UCLA Bruins | **AWAY** (+28.0) | **UNDER** (145.0) | 50% |
| Louisiana Ragin' Cajuns @ USC Trojans | **AWAY** (+31.5) | **UNDER** (145.5) | 53% |
| UMass Lowell River Hawks @ Cincinnati Bearcats | **AWAY** (+29.0) | **UNDER** (150.5) | 78% |
| Maryland-Eastern Shore Hawks @ IUPUI Jaguars | **AWAY** (+10.0) | **UNDER** (140.5) | 53% |
| Evansville Purple Aces @ Memphis Tigers | **AWAY** (+20.0) | **UNDER** (156.5) | 78% |
| NJIT Highlanders @ Boston College Eagles | **AWAY** (+23.0) | **UNDER** (136.0) | 64% |
| Cal Baptist Lancers @ Portland Pilots | **HOME** (-7.5) | **UNDER** (146.5) | 78% |
| UNC Asheville Bulldogs @ Samford Bulldogs | **AWAY** (+10.5) | **UNDER** (154.5) | 73% |
| Utah Utes @ Minnesota Golden Gophers | **AWAY** (+9.5) | **OVER** (131.5) | 43% |
| Tenn-Martin Skyhawks @ Utah Valley Wolverines | **AWAY** (+7.0) | **UNDER** (144.5) | 81% |
| Duquesne Dukes @ Wyoming Cowboys | **HOME** (-4.0) | **OVER** (137.0) | 56% |
| Virginia Tech Hokies @ Oklahoma St Cowboys | **HOME** (+1.0) | **OVER** (158.5) | 55% |
| Temple Owls @ Stephen F. Austin Lumberjacks | **HOME** (+2.0) | **UNDER** (144.5) | 63% |
| Mercyhurst Lakers @ Albany Great Danes | **HOME** (+1.5) | **OVER** (131.5) | 60% |
| Western Kentucky Hilltoppers @ GW Revolutionaries | **HOME** (-3.0) | **OVER** (148.5) | 57% |
| UAB Blazers @ Rhode Island Rams | **HOME** (-2.0) | **UNDER** (153.0) | 73% |
| CSU Fullerton Titans @ Portland St Vikings | **AWAY** (+4.5) | **UNDER** (163.5) | 66% |
| Liberty Flames @ Richmond Spiders | **HOME** (-1.0) | **OVER** (141.0) | 33% |
| William & Mary Tribe @ Youngstown St Penguins | **HOME** (+3.0) | **UNDER** (163.0) | 49% |
| McNeese Cowboys @ Texas State Bobcats | **AWAY** (+2.5) | **UNDER** (142.5) | 17% |
| UC Irvine Anteaters @ Loyola Marymount Lions | **HOME** (+1.5) | **UNDER** (136.5) | 14% |
| Robert Morris Colonials @ New Mexico St Aggies | **AWAY** (+1.5) | **OVER** (134.5) | 23% |
| Lamar Cardinals @ Rice Owls | **HOME** (+2.0) | **UNDER** (164.0) | 55% |
| Valparaiso Beacons @ Southern Miss Golden Eagles | **HOME** (+9.0) | **OVER** (143.5) | 16% |
| San Diego Toreros @ Fordham Rams | **AWAY** (+1.5) | **UNDER** (142.5) | 27% |
| San José St Spartans @ Loyola (Chi) Ramblers | **AWAY** (+4.0) | **UNDER** (146.5) | 10% |
| Utah Tech Trailblazers @ South Dakota Coyotes | **HOME** (+1.5) | **OVER** (153.0) | 16% |

> 📈 *ATS = Against The Spread (with Vegas lines). Updated daily via GitHub Actions.*

<!-- ACCURACY_STATS_END -->

<!-- RANKINGS_START -->

### 🏆 Top 25 Team Rankings

*Updated: November 22, 2026*

| Rank | Team | Record | Rating | Off | Def |
|------|------|--------|--------|-----|-----|
| 1 | Michigan Wolverines | 31-3 | +29.0 | 70.3 | 41.4 |
| 2 | Arizona Wildcats | 32-2 | +27.6 | 68.6 | 40.9 |
| 3 | Duke Blue Devils | 32-2 | +26.5 | 64.6 | 38.0 |
| 4 | Illinois Fighting Illini | 24-8 | +25.4 | 67.0 | 42.1 |
| 5 | Iowa State Cyclones | 27-7 | +25.3 | 64.9 | 39.9 |
| 6 | Florida Gators | 26-7 | +24.8 | 66.6 | 42.2 |
| 7 | Louisville Cardinals | 23-10 | +24.0 | 67.3 | 43.7 |
| 8 | Alabama Crimson Tide | 23-9 | +23.7 | 72.5 | 48.8 |
| 9 | Gonzaga Bulldogs | 30-3 | +23.5 | 64.4 | 40.9 |
| 10 | Houston Cougars | 28-6 | +23.4 | 60.7 | 37.2 |
| 11 | Arkansas Razorbacks | 26-8 | +23.4 | 71.0 | 47.6 |
| 12 | Purdue Boilermakers | 27-8 | +23.3 | 65.1 | 41.8 |
| 13 | Vanderbilt Commodores | 26-8 | +22.8 | 67.5 | 44.7 |
| 14 | St. John's Red Storm | 28-6 | +22.5 | 65.0 | 42.5 |
| 15 | UConn Huskies | 29-5 | +22.1 | 62.0 | 39.9 |
| 16 | BYU Cougars | 23-11 | +22.1 | 67.9 | 45.8 |
| 17 | Michigan State Spartans | 25-7 | +21.6 | 62.7 | 41.1 |
| 18 | Tennessee Volunteers | 22-11 | +21.5 | 62.2 | 41.1 |
| 19 | Texas Tech Red Raiders | 22-10 | +21.4 | 64.5 | 43.1 |
| 20 | Kansas Jayhawks | 23-10 | +21.4 | 62.8 | 41.4 |
| 21 | Wisconsin Badgers | 24-10 | +21.0 | 67.3 | 46.3 |
| 22 | Virginia Cavaliers | 29-5 | +20.8 | 63.3 | 42.5 |
| 23 | Georgia Bulldogs | 22-10 | +20.7 | 69.0 | 48.6 |
| 24 | Kentucky Wildcats | 21-13 | +20.6 | 64.3 | 43.9 |
| 25 | Nebraska Cornhuskers | 26-6 | +20.5 | 61.2 | 40.7 |

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

