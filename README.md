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

**Last Updated**: February 19, 2026 at 12:44 PM

![ATS Accuracy](https://img.shields.io/badge/ATS_Record-52.0%25-yellowgreen)

#### 🏆 Rolling ATS Performance

| Timeframe | ATS Record | Accuracy |
|-----------|------------|----------|
| **Latest** (2026-02-18) | 32-20 | **61.5%** |
| **Last 7 Days** | 174-152 | **53.4%** |
| **Last 30 Days** | 196-181 | **52.0%** |
| **All-Time** | 196-181 | **52.0%** |

**Over/Under Accuracy**: 47.5%

#### 🎯 Accuracy by Confidence (ATS)

| Confidence | Record | Accuracy |
|------------|--------|----------|
| **50%+** | 60-48 | **55.6%** |
| **60%+** | 24-16 | **60.0%** |
| **70%+** | 10-6 | **62.5%** |
| **80%+** | 3-1 | **75.0%** |

#### 🏀 ATS Accuracy by Conference

| Conference | Record | Accuracy |
|------------|--------|----------|
| Western Athletic | 6-1 | **85.7%** |
| Big South | 7-2 | **77.8%** |
| Southeastern | 15-5 | **75.0%** |
| Southern | 9-4 | **69.2%** |
| Mid-Eastern Athletic | 6-3 | **66.7%** |
| Ohio Valley | 7-4 | **63.6%** |
| America East | 5-3 | **62.5%** |
| Big East | 8-5 | **61.5%** |
| Ivy League | 3-2 | **60.0%** |
| Southwestern Athletic | 6-4 | **60.0%** |
| American | 10-7 | **58.8%** |
| Atlantic 10 | 8-6 | **57.1%** |
| Atlantic Coast | 12-9 | **57.1%** |
| Conference USA | 7-6 | **53.8%** |
| Missouri Valley | 8-7 | **53.3%** |
| Big 12 | 9-8 | **52.9%** |
| ASUN | 8-8 | **50.0%** |
| West Coast | 5-5 | **50.0%** |
| Big West | 5-5 | **50.0%** |
| Southland | 5-5 | **50.0%** |
| Coastal Athletic Association | 5-6 | **45.5%** |
| Patriot League | 4-5 | **44.4%** |
| Mid-American | 7-9 | **43.8%** |
| Mountain West | 5-7 | **41.7%** |
| Sun Belt | 7-10 | **41.2%** |
| Horizon League | 4-6 | **40.0%** |
| Summit League | 3-5 | **37.5%** |
| Big Sky | 3-6 | **33.3%** |
| Big Ten | 6-14 | **30.0%** |
| Metro Atlantic Athletic | 3-9 | **25.0%** |
| Northeast | 1-7 | **12.5%** |

> *A game counts for a conference if either team is a member.*

#### Combined Statistics

- **Total Predictions**: 377
- **Overall Winner Accuracy**: 52.0%

#### 📅 Predictions for Today (2026-02-19)

| Matchup | Spread Pick | Total Pick | Confidence |
|---------|-------------|------------|------------|
| UMKC Kangaroos @ North Dakota Fighting Hawks | **HOME** (-10.5) | **UNDER** (150.0) | 59% |
| IUPUI Jaguars @ Wright St Raiders | **HOME** (-12.0) | **UNDER** (162.5) | 90% |
| UNC Asheville Bulldogs @ High Point Panthers | **HOME** (-13.5) | **UNDER** (152.0) | 54% |
| LIU Sharks @ St. Francis (PA) Red Flash | **HOME** (+9.0) | **UNDER** (147.0) | 50% |
| Cal Baptist Lancers @ Utah Valley Wolverines | **HOME** (-8.0) | **UNDER** (142.0) | 53% |
| Cal Poly Mustangs @ Hawai'i Rainbow Warriors | **AWAY** (+12.0) | **UNDER** (161.5) | 63% |
| Chattanooga Mocs @ Mercer Bears | **AWAY** (+10.5) | **UNDER** (152.5) | 68% |
| South Carolina Upstate Spartans @ Winthrop Eagles | **AWAY** (+13.5) | **UNDER** (154.5) | 55% |
| Florida Int'l Golden Panthers @ Liberty Flames | **AWAY** (+11.0) | **OVER** (152.5) | 47% |
| Hampton Pirates @ Hofstra Pride | **AWAY** (+11.5) | **UNDER** (136.0) | 60% |
| Wagner Seahawks @ Mercyhurst Lakers | **HOME** (-6.0) | **UNDER** (134.0) | 53% |
| Tulane Green Wave @ North Texas Mean Green | **HOME** (-6.5) | **UNDER** (136.5) | 53% |
| South Dakota Coyotes @ Denver Pioneers | **AWAY** (+6.5) | **OVER** (161.5) | 51% |
| New Hampshire Wildcats @ UMass Lowell River Hawks | **HOME** (-4.5) | **OVER** (147.5) | 51% |
| Binghamton Bearcats @ Bryant Bulldogs | **HOME** (-6.0) | **OVER** (136.0) | 57% |
| Montana St Bobcats @ Weber State Wildcats | **HOME** (+0.0) | **UNDER** (150.5) | 49% |
| Gardner-Webb Bulldogs @ Radford Highlanders | **AWAY** (+19.0) | **UNDER** (162.5) | 45% |
| Monmouth Hawks @ UNC Wilmington Seahawks | **AWAY** (+7.5) | **UNDER** (141.5) | 48% |
| Albany Great Danes @ NJIT Highlanders | **HOME** (-4.0) | **OVER** (142.5) | 39% |
| Arkansas St Red Wolves @ Louisiana Ragin' Cajuns | **HOME** (+8.0) | **UNDER** (145.0) | 39% |
| Memphis Tigers @ South Florida Bulls | **AWAY** (+8.5) | **UNDER** (159.0) | 46% |
| Marshall Thundering Herd @ Appalachian St Mountaineers | **HOME** (-2.5) | **UNDER** (144.0) | 55% |
| Lindenwood Lions @ Tennessee St Tigers | **HOME** (-3.5) | **UNDER** (162.0) | 38% |
| Alabama St Hornets @ Bethune-Cookman Wildcats | **AWAY** (+6.0) | **UNDER** (146.0) | 55% |
| Utah Tech Trailblazers @ UT-Arlington Mavericks | **HOME** (-4.5) | **OVER** (140.5) | 38% |
| UC Davis Aggies @ CSU Fullerton Titans | **HOME** (-1.5) | **UNDER** (156.0) | 57% |
| Texas Southern Tigers @ Arkansas-Pine Bluff Golden Lions | **HOME** (-3.0) | **OVER** (151.5) | 58% |
| Stonehill Skyhawks @ New Haven Chargers | **HOME** (-2.5) | **UNDER** (120.5) | 49% |
| Le Moyne Dolphins @ Central Connecticut St Blue Devils | **AWAY** (+4.5) | **OVER** (145.5) | 41% |
| William & Mary Tribe @ Campbell Fighting Camels | **HOME** (+0.0) | **UNDER** (168.5) | 49% |
| Central Arkansas Bears @ Stetson Hatters | **HOME** (+8.0) | **OVER** (149.0) | 46% |
| CSU Northridge Matadors @ UC Santa Barbara Gauchos | **HOME** (-3.5) | **UNDER** (158.5) | 39% |
| CSU Bakersfield Roadrunners @ UC Riverside Highlanders | **AWAY** (+5.5) | **UNDER** (150.5) | 42% |
| Southern Indiana Screaming Eagles @ Western Illinois Leathernecks | **HOME** (+2.5) | **UNDER** (138.5) | 33% |
| Idaho Vandals @ Portland St Vikings | **AWAY** (+4.0) | **UNDER** (142.0) | 34% |
| Morehead St Eagles @ Eastern Illinois Panthers | **HOME** (+2.0) | **OVER** (139.0) | 29% |
| SIU-Edwardsville Cougars @ Tennessee Tech Golden Eagles | **HOME** (+2.5) | **UNDER** (136.5) | 27% |
| Georgia Southern Eagles @ Georgia St Panthers | **HOME** (-1.0) | **UNDER** (154.0) | 39% |
| Southern Utah Thunderbirds @ Tarleton State Texans | **AWAY** (+5.5) | **UNDER** (144.0) | 32% |
| Vermont Catamounts @ UMBC Retrievers | **HOME** (+1.5) | **OVER** (140.5) | 23% |
| Austin Peay Governors @ North Florida Ospreys | **HOME** (+11.0) | **UNDER** (163.0) | 23% |
| Fairleigh Dickinson Knights @ Chicago St Cougars | **HOME** (+1.5) | **UNDER** (135.5) | 28% |
| Montana Grizzlies @ Idaho State Bengals | **HOME** (+1.0) | **UNDER** (149.5) | 35% |
| Longwood Lancers @ Presbyterian Blue Hose | **HOME** (-2.0) | **OVER** (140.0) | 22% |
| UC Irvine Anteaters @ Long Beach St 49ers | **HOME** (+5.5) | **UNDER** (143.5) | 16% |
| Drexel Dragons @ Northeastern Huskies | **HOME** (+0.0) | **UNDER** (144.0) | 20% |
| Charleston Cougars @ North Carolina A&T Aggies | **HOME** (+5.0) | **UNDER** (147.5) | 22% |
| Eastern Washington Eagles @ Sacramento St Hornets | **HOME** (+1.5) | **UNDER** (162.0) | 14% |
| Samford Bulldogs @ The Citadel Bulldogs | **HOME** (+10.0) | **OVER** (140.5) | 11% |
| Texas State Bobcats @ South Alabama Jaguars | **AWAY** (+3.5) | **OVER** (139.0) | 17% |
| Alabama A&M Bulldogs @ Florida A&M Rattlers | **AWAY** (+2.0) | **UNDER** (139.5) | 34% |
| Prairie View Panthers @ Miss Valley St Delta Devils | **HOME** (+9.5) | **UNDER** (153.5) | 29% |
| Tenn-Martin Skyhawks @ Arkansas-Little Rock Trojans | **HOME** (+2.5) | **UNDER** (135.0) | 5% |

> 📈 *ATS = Against The Spread (with Vegas lines). Updated daily via GitHub Actions.*

<!-- ACCURACY_STATS_END -->

<!-- RANKINGS_START -->

### 🏆 Top 25 Team Rankings

*Updated: February 19, 2026*

| Rank | Team | Record | Rating | Off | Def |
|------|------|--------|--------|-----|-----|
| 1 | Michigan Wolverines | 25-1 | +31.1 | 72.2 | 41.1 |
| 2 | Arizona Wildcats | 24-2 | +27.2 | 68.7 | 41.5 |
| 3 | Duke Blue Devils | 24-2 | +27.0 | 65.4 | 38.4 |
| 4 | Louisville Cardinals | 19-7 | +26.5 | 69.8 | 43.7 |
| 5 | Illinois Fighting Illini | 22-5 | +26.5 | 67.3 | 41.2 |
| 6 | Iowa State Cyclones | 23-3 | +25.5 | 66.3 | 40.8 |
| 7 | Alabama Crimson Tide | 19-7 | +24.7 | 73.4 | 48.9 |
| 8 | Arkansas Razorbacks | 19-7 | +24.6 | 70.5 | 46.2 |
| 9 | Gonzaga Bulldogs | 26-2 | +24.4 | 65.6 | 41.2 |
| 10 | Florida Gators | 20-6 | +24.3 | 65.4 | 41.5 |
| 11 | Purdue Boilermakers | 21-5 | +23.7 | 65.4 | 41.7 |
| 12 | Houston Cougars | 23-3 | +23.4 | 60.8 | 37.3 |
| 13 | Vanderbilt Commodores | 21-5 | +23.4 | 67.9 | 44.5 |
| 14 | BYU Cougars | 19-7 | +23.0 | 68.6 | 45.9 |
| 15 | Michigan State Spartans | 21-5 | +22.4 | 62.3 | 39.9 |
| 16 | Tennessee Volunteers | 19-7 | +22.4 | 63.6 | 41.6 |
| 17 | UConn Huskies | 24-3 | +22.2 | 62.8 | 40.6 |
| 18 | Kansas Jayhawks | 20-6 | +22.2 | 62.5 | 40.3 |
| 19 | NC State Wolfpack | 19-8 | +22.2 | 66.9 | 45.0 |
| 20 | St. John's Red Storm | 21-5 | +21.9 | 65.1 | 43.2 |
| 21 | Texas Tech Red Raiders | 19-7 | +21.7 | 64.5 | 42.7 |
| 22 | Kentucky Wildcats | 17-9 | +21.5 | 64.9 | 43.8 |
| 23 | Nebraska Cornhuskers | 22-4 | +21.2 | 61.3 | 40.1 |
| 24 | Saint Louis Billikens | 24-2 | +20.9 | 67.2 | 46.3 |
| 25 | Georgia Bulldogs | 18-8 | +20.7 | 68.9 | 48.6 |

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

