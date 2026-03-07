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

**Last Updated**: March 07, 2026 at 04:55 AM

![ATS Accuracy](https://img.shields.io/badge/ATS_Record-50.9%25-yellowgreen)

#### 🏆 Rolling ATS Performance

| Timeframe | ATS Record | Accuracy |
|-----------|------------|----------|
| **Latest** (2026-03-06) | 19-16 | **54.3%** |
| **Last 7 Days** | 177-160 | **52.5%** |
| **Last 30 Days** | 567-546 | **50.9%** |
| **All-Time** | 567-546 | **50.9%** |

**Over/Under Accuracy**: 52.6%

#### 🎯 Accuracy by Confidence (ATS)

| Confidence | Record | Accuracy |
|------------|--------|----------|
| **50%+** | 160-158 | **50.3%** |
| **60%+** | 68-62 | **52.3%** |
| **70%+** | 24-21 | **53.3%** |
| **80%+** | 6-6 | **50.0%** |

#### 🏀 ATS Accuracy by Conference

| Conference | Record | Accuracy |
|------------|--------|----------|
| Big South | 23-7 | **76.7%** |
| Western Athletic | 15-7 | **68.2%** |
| Southern | 20-12 | **62.5%** |
| Mountain West | 23-14 | **62.2%** |
| Summit League | 13-9 | **59.1%** |
| Missouri Valley | 22-16 | **57.9%** |
| Southeastern | 30-22 | **57.7%** |
| Mid-Eastern Athletic | 15-11 | **57.7%** |
| Atlantic Coast | 32-24 | **57.1%** |
| Big 12 | 28-22 | **56.0%** |
| Ohio Valley | 21-17 | **55.3%** |
| Atlantic 10 | 22-18 | **55.0%** |
| Patriot League | 12-10 | **54.5%** |
| America East | 15-13 | **53.6%** |
| Ivy League | 10-9 | **52.6%** |
| Southwestern Athletic | 18-17 | **51.4%** |
| ASUN | 22-22 | **50.0%** |
| Southland | 15-15 | **50.0%** |
| Mid-American | 22-24 | **47.8%** |
| Conference USA | 16-18 | **47.1%** |
| West Coast | 13-15 | **46.4%** |
| Big East | 16-19 | **45.7%** |
| Big Ten | 25-31 | **44.6%** |
| Sun Belt | 21-28 | **42.9%** |
| Big West | 15-20 | **42.9%** |
| Coastal Athletic Association | 17-24 | **41.5%** |
| Big Sky | 13-19 | **40.6%** |
| Horizon League | 12-18 | **40.0%** |
| Metro Atlantic Athletic | 16-24 | **40.0%** |
| Northeast | 11-17 | **39.3%** |
| American | 16-26 | **38.1%** |

> *A game counts for a conference if either team is a member.*

#### Combined Statistics

- **Total Predictions**: 1113
- **Overall Winner Accuracy**: 50.9%

#### 📅 Recent Predictions (2026-03-06)

| Matchup | Spread Pick | Total Pick | Confidence |
|---------|-------------|------------|------------|
| San Diego Toreros @ Seattle Redhawks | **AWAY** (+7.5) | **OVER** (140.5) | 82% |
| Gardner-Webb Bulldogs @ High Point Panthers | **AWAY** (+25.5) | **UNDER** (159.5) | 54% |
| Northern Illinois Huskies @ Akron Zips | **AWAY** (+23.5) | **UNDER** (155.5) | 84% |
| Drake Bulldogs @ Belmont Bruins | **AWAY** (+11.5) | **OVER** (153.5) | 71% |
| UNLV Rebels @ San Diego St Aztecs | **AWAY** (+9.5) | **OVER** (152.5) | 60% |
| Stetson Hatters @ Austin Peay Governors | **AWAY** (+10.5) | **OVER** (150.5) | 63% |
| Buffalo Bulls @ Toledo Rockets | **AWAY** (+8.0) | **OVER** (154.5) | 44% |
| Bellarmine Knights @ Central Arkansas Bears | **HOME** (-6.5) | **OVER** (155.5) | 64% |
| Valparaiso Beacons @ Bradley Braves | **HOME** (-3.5) | **OVER** (134.5) | 80% |
| West Georgia Wolves @ Queens University Royals | **AWAY** (+6.5) | **UNDER** (162.5) | 41% |
| Sacred Heart Pioneers @ Merrimack Warriors | **AWAY** (+7.5) | **OVER** (144.5) | 50% |
| St. John's Red Storm @ Seton Hall Pirates | **AWAY** (-4.5) | **UNDER** (136.5) | 69% |
| Western Michigan Broncos @ Kent State Golden Flashes | **AWAY** (+11.0) | **UNDER** (158.5) | 47% |
| Florida Gulf Coast Eagles @ Lipscomb Bisons | **HOME** (-3.5) | **UNDER** (150.5) | 49% |
| Presbyterian Blue Hose @ Radford Highlanders | **HOME** (-2.5) | **OVER** (145.5) | 44% |
| UCF Knights @ West Virginia Mountaineers | **HOME** (-3.5) | **UNDER** (140.5) | 41% |
| Charleston Southern Buccaneers @ Winthrop Eagles | **HOME** (-4.5) | **OVER** (161.5) | 40% |
| Georgia Southern Eagles @ South Alabama Jaguars | **AWAY** (+4.5) | **UNDER** (148.5) | 40% |
| Tenn-Martin Skyhawks @ Tennessee St Tigers | **HOME** (-2.5) | **UNDER** (138.5) | 46% |
| The Citadel Bulldogs @ Chattanooga Mocs | **AWAY** (+7.5) | **OVER** (146.0) | 27% |
| Pennsylvania Quakers @ Brown Bears | **HOME** (+2.5) | **UNDER** (142.0) | 43% |
| Southern Miss Golden Eagles @ Texas State Bobcats | **HOME** (-0.5) | **UNDER** (140.5) | 26% |
| VMI Keydets @ UNC Greensboro Spartans | **AWAY** (+7.5) | **UNDER** (155.0) | 23% |
| VCU Rams @ Dayton Flyers | **HOME** (-1.5) | **UNDER** (148.5) | 27% |
| Portland Pilots @ Washington St Cougars | **AWAY** (+4.5) | **UNDER** (152.5) | 29% |
| UIC Flames @ Murray St Racers | **HOME** (-1.5) | **OVER** (149.5) | 37% |
| Central Michigan Chippewas @ Ball State Cardinals | **HOME** (-2.0) | **UNDER** (136.0) | 21% |
| Northern Iowa Panthers @ Illinois St Redbirds | **HOME** (+1.5) | **OVER** (125.5) | 22% |
| Fairfield Stags @ Saint Peter's Peacocks | **HOME** (-1.5) | **OVER** (137.5) | 21% |
| Arkansas Razorbacks @ Missouri Tigers | **HOME** (+3.5) | **OVER** (162.5) | 20% |
| Bowling Green Falcons @ Eastern Michigan Eagles | **HOME** (+3.5) | **UNDER** (141.0) | 28% |
| Denver Pioneers @ North Dakota Fighting Hawks | **HOME** (+3.5) | **OVER** (160.5) | 25% |
| Miami (OH) RedHawks @ Ohio Bobcats | **HOME** (+5.5) | **UNDER** (158.5) | 16% |
| Omaha Mavericks @ South Dakota Coyotes | **HOME** (+2.5) | **UNDER** (150.5) | 10% |
| Longwood Lancers @ UNC Asheville Bulldogs | **HOME** (+1.5) | **OVER** (140.5) | 14% |
| Northeastern Huskies @ North Carolina A&T Aggies | **HOME** (-1.0) | **OVER** (154.5) | 13% |
| Columbia Lions @ Harvard Crimson | **AWAY** (+4.0) | **UNDER** (134.0) | 29% |
| SE Missouri St Redhawks @ Morehead St Eagles | **HOME** (+1.5) | **OVER** (141.5) | 7% |

> 📈 *ATS = Against The Spread (with Vegas lines). Updated daily via GitHub Actions.*

<!-- ACCURACY_STATS_END -->

<!-- RANKINGS_START -->

### 🏆 Top 25 Team Rankings

*Updated: March 07, 2026*

| Rank | Team | Record | Rating | Off | Def |
|------|------|--------|--------|-----|-----|
| 1 | Michigan Wolverines | 28-2 | +30.6 | 71.6 | 41.0 |
| 2 | Arizona Wildcats | 28-2 | +28.1 | 68.8 | 40.7 |
| 3 | Duke Blue Devils | 28-2 | +28.1 | 65.6 | 37.5 |
| 4 | Illinois Fighting Illini | 23-7 | +26.7 | 67.7 | 41.4 |
| 5 | Florida Gators | 24-6 | +26.3 | 67.8 | 41.8 |
| 6 | Louisville Cardinals | 21-9 | +25.5 | 68.7 | 43.7 |
| 7 | Iowa State Cyclones | 24-6 | +24.6 | 65.0 | 40.6 |
| 8 | Arkansas Razorbacks | 22-8 | +24.4 | 71.6 | 47.2 |
| 9 | Alabama Crimson Tide | 22-8 | +24.4 | 72.6 | 48.2 |
| 10 | Gonzaga Bulldogs | 28-3 | +24.3 | 65.2 | 40.9 |
| 11 | Purdue Boilermakers | 23-7 | +24.2 | 65.8 | 41.6 |
| 12 | Houston Cougars | 25-5 | +23.7 | 61.1 | 37.4 |
| 13 | UConn Huskies | 27-3 | +23.3 | 63.2 | 40.0 |
| 14 | Vanderbilt Commodores | 23-7 | +22.8 | 67.5 | 44.6 |
| 15 | Texas Tech Red Raiders | 22-8 | +22.5 | 65.2 | 42.8 |
| 16 | BYU Cougars | 20-10 | +22.3 | 68.3 | 46.2 |
| 17 | Tennessee Volunteers | 21-9 | +22.1 | 62.5 | 40.8 |
| 18 | St. John's Red Storm | 25-6 | +22.1 | 64.7 | 42.6 |
| 19 | Michigan State Spartans | 25-5 | +22.1 | 62.2 | 40.1 |
| 20 | Kansas Jayhawks | 21-9 | +21.9 | 62.4 | 40.6 |
| 21 | Georgia Bulldogs | 21-9 | +21.8 | 69.3 | 47.8 |
| 22 | Kentucky Wildcats | 19-11 | +21.4 | 64.7 | 43.6 |
| 23 | Wisconsin Badgers | 21-9 | +21.2 | 67.3 | 46.1 |
| 24 | Nebraska Cornhuskers | 25-5 | +21.1 | 61.2 | 40.1 |
| 25 | Virginia Cavaliers | 26-4 | +20.7 | 63.3 | 42.5 |

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

