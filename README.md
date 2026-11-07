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

**Last Updated**: November 07, 2026 at 05:14 PM

![ATS Accuracy](https://img.shields.io/badge/ATS_Record-50.5%25-yellowgreen)

#### 🏆 Rolling ATS Performance

| Timeframe | ATS Record | Accuracy |
|-----------|------------|----------|
| **Latest** (2026-11-06) | 3-0 | **100.0%** |
| **Last 7 Days** | 8-8 | **50.0%** |
| **Last 30 Days** | 8-8 | **50.0%** |
| **All-Time** | 771-758 | **50.5%** |

**Over/Under Accuracy**: 50.9%

#### 🎯 Accuracy by Confidence (ATS)

| Confidence | Record | Accuracy |
|------------|--------|----------|
| **50%+** | 246-242 | **50.4%** |
| **60%+** | 109-100 | **52.2%** |
| **70%+** | 33-37 | **47.1%** |
| **80%+** | 8-11 | **42.1%** |

#### 🏀 ATS Accuracy by Conference

| Conference | Record | Accuracy |
|------------|--------|----------|
| Big South | 27-8 | **77.1%** |
| Southern | 25-15 | **62.5%** |
| Mountain West | 41-25 | **62.1%** |
| United Athletic | 21-13 | **61.8%** |
| Summit League | 16-10 | **61.5%** |
| Patriot League | 16-11 | **59.3%** |
| Mid-Eastern Athletic | 20-14 | **58.8%** |
| Atlantic Coast | 58-42 | **58.0%** |
| Missouri Valley | 27-22 | **55.1%** |
| Atlantic 10 | 40-34 | **54.1%** |
| West Coast | 21-18 | **53.8%** |
| Ohio Valley | 22-19 | **53.7%** |
| America East | 19-17 | **52.8%** |
| Southwestern Athletic | 25-23 | **52.1%** |
| Mid-American | 31-29 | **51.7%** |
| Big East | 31-32 | **49.2%** |
| Big 12 | 49-51 | **49.0%** |
| Big West | 24-25 | **49.0%** |
| Southland | 19-20 | **48.7%** |
| Southeastern | 55-58 | **48.7%** |
| Atlantic Sun | 24-27 | **47.1%** |
| Conference USA | 22-27 | **44.9%** |
| Metro | 21-26 | **44.7%** |
| Sun Belt | 25-32 | **43.9%** |
| Big Ten | 49-65 | **43.0%** |
| Coastal Athletic Association | 23-32 | **41.8%** |
| Northeast | 12-17 | **41.4%** |
| Horizon League | 15-23 | **39.5%** |
| Ivy League | 10-16 | **38.5%** |
| American | 25-41 | **37.9%** |
| Big Sky | 15-27 | **35.7%** |

> *A game counts for a conference if either team is a member.*

#### Combined Statistics

- **Total Predictions**: 1529
- **Overall Winner Accuracy**: 50.5%

#### 📅 Predictions for Today (2026-11-07)

| Matchup | Spread Pick | Total Pick | Confidence |
|---------|-------------|------------|------------|
| New Mexico St Aggies @ Gonzaga Bulldogs | **AWAY** (+28.5) | **UNDER** (151.5) | 81% |
| LIU Sharks @ La Salle Explorers | **HOME** (-4.5) | **UNDER** (149.5) | 74% |
| Tenn-Martin Skyhawks @ IUPUI Jaguars | **AWAY** (-2.0) | **UNDER** (166.0) | 95% |
| Omaha Mavericks @ Utah State Aggies | **AWAY** (+29.0) | **UNDER** (153.0) | 75% |
| Northern Arizona Lumberjacks @ New Mexico Lobos | **AWAY** (+27.5) | **UNDER** (158.0) | 86% |
| Sacramento St Hornets @ Santa Clara Broncos | **AWAY** (+20.0) | **UNDER** (170.5) | 77% |
| Washington St Cougars @ High Point Panthers | **HOME** (-12.5) | **OVER** (156.5) | 51% |
| Northwestern St Demons @ Murray St Racers | **AWAY** (+24.5) | **UNDER** (155.5) | 85% |
| Hampton Pirates @ GW Revolutionaries | **AWAY** (+19.0) | **OVER** (146.5) | 53% |
| Portland St Vikings @ Seattle Redhawks | **AWAY** (+10.5) | **UNDER** (144.0) | 73% |
| Bethune-Cookman Wildcats @ Grand Canyon Antelopes | **AWAY** (+21.5) | **UNDER** (155.5) | 78% |
| Lafayette Leopards @ Saint Joseph's Hawks | **AWAY** (+16.5) | **UNDER** (148.5) | 78% |
| Bellarmine Knights @ Miami (OH) RedHawks | **AWAY** (+20.5) | **OVER** (159.5) | 78% |
| North Carolina A&T Aggies @ Ohio Bobcats | **AWAY** (+14.0) | **UNDER** (161.0) | 58% |
| Samford Bulldogs @ UNLV Rebels | **AWAY** (+11.0) | **OVER** (158.0) | 48% |
| SIU-Edwardsville Cougars @ Lipscomb Bisons | **AWAY** (+8.5) | **UNDER** (144.5) | 81% |
| Providence Friars @ Nebraska Cornhuskers | **HOME** (-2.5) | **UNDER** (158.5) | 70% |
| Northern Illinois Huskies @ Dayton Flyers | **AWAY** (+19.0) | **UNDER** (147.5) | 91% |
| Oakland Golden Grizzlies @ UC Santa Barbara Gauchos | **AWAY** (+13.0) | **OVER** (149.0) | 56% |
| Mercer Bears @ Davidson Wildcats | **AWAY** (+11.0) | **UNDER** (149.5) | 67% |
| Southern Indiana Screaming Eagles @ Evansville Purple Aces | **HOME** (-7.5) | **UNDER** (143.0) | 63% |
| Long Beach St 49ers @ Montana St Bobcats | **AWAY** (+10.5) | **OVER** (145.5) | 55% |
| North Carolina Central Eagles @ Longwood Lancers | **AWAY** (+12.5) | **UNDER** (148.5) | 50% |
| SE Louisiana Lions @ Arkansas-Little Rock Trojans | **AWAY** (+10.5) | **UNDER** (145.5) | 63% |
| Northern Iowa Panthers @ Furman Paladins | **HOME** (-5.0) | **UNDER** (149.0) | 80% |
| Fresno St Bulldogs @ UC San Diego Tritons | **AWAY** (+11.0) | **UNDER** (150.5) | 79% |
| Maryland Terrapins @ Georgetown Hoyas | **AWAY** (-3.0) | **UNDER** (146.5) | 72% |
| Monmouth Hawks @ Rhode Island Rams | **AWAY** (+6.0) | **UNDER** (145.5) | 72% |
| St. Bonaventure Bonnies @ Canisius Golden Griffins | **HOME** (+9.5) | **UNDER** (147.5) | 55% |
| Prairie View Panthers @ UT Rio Grande Valley Vaqueros | **AWAY** (+8.5) | **UNDER** (149.5) | 63% |
| San José St Spartans @ UC Irvine Anteaters | **AWAY** (+8.0) | **OVER** (146.0) | 32% |
| Colorado Buffaloes @ San Diego St Aztecs | **HOME** (-3.0) | **UNDER** (151.5) | 38% |
| Arkansas Razorbacks @ Virginia Cavaliers | **HOME** (-2.5) | **OVER** (158.5) | 25% |
| Denver Pioneers @ UC Riverside Highlanders | **HOME** (-2.0) | **OVER** (156.0) | 31% |
| Morgan St Bears @ Niagara Purple Eagles | **AWAY** (+3.5) | **UNDER** (149.5) | 40% |
| Utah Valley Wolverines @ Weber State Wildcats | **HOME** (+7.5) | **UNDER** (156.5) | 24% |
| Lamar Cardinals @ Abilene Christian Wildcats | **HOME** (+1.5) | **UNDER** (165.5) | 65% |
| Colgate Raiders @ Drexel Dragons | **HOME** (-1.5) | **UNDER** (140.5) | 23% |
| Houston Christian Huskies @ Western Illinois Leathernecks | **HOME** (+9.5) | **UNDER** (136.5) | 19% |
| Western Carolina Catamounts @ UNC Asheville Bulldogs | **HOME** (+3.5) | **UNDER** (152.5) | 38% |
| Pacific Tigers @ Bradley Braves | **AWAY** (-0.0) | **OVER** (139.5) | 22% |
| CSU Fullerton Titans @ South Dakota Coyotes | **AWAY** (+1.0) | **UNDER** (176.0) | 54% |
| Toledo Rockets @ Marshall Thundering Herd | **AWAY** (+2.5) | **OVER** (158.0) | 20% |
| VMI Keydets @ UTSA Roadrunners | **AWAY** (+4.5) | **UNDER** (163.5) | 48% |
| VCU Rams @ Memphis Tigers | **HOME** (+2.0) | **UNDER** (159.0) | 23% |
| UNC Wilmington Seahawks @ East Carolina Pirates | **HOME** (+4.0) | **UNDER** (151.0) | 19% |
| Old Dominion Monarchs @ Bucknell Bison | **HOME** (+5.5) | **OVER** (140.5) | 35% |

> 📈 *ATS = Against The Spread (with Vegas lines). Updated daily via GitHub Actions.*

<!-- ACCURACY_STATS_END -->

<!-- RANKINGS_START -->

### 🏆 Top 25 Team Rankings

*Updated: November 07, 2026*

| Rank | Team | Record | Rating | Off | Def |
|------|------|--------|--------|-----|-----|
| 1 | Michigan Wolverines | 31-3 | +29.0 | 70.3 | 41.4 |
| 2 | Arizona Wildcats | 32-2 | +27.6 | 68.6 | 40.9 |
| 3 | Duke Blue Devils | 32-2 | +26.6 | 64.6 | 38.0 |
| 4 | Illinois Fighting Illini | 24-8 | +25.4 | 67.0 | 42.1 |
| 5 | Iowa State Cyclones | 27-7 | +25.3 | 64.9 | 39.9 |
| 6 | Florida Gators | 26-7 | +24.8 | 66.7 | 42.2 |
| 7 | Louisville Cardinals | 23-10 | +24.0 | 67.3 | 43.7 |
| 8 | Alabama Crimson Tide | 23-9 | +23.7 | 72.5 | 48.8 |
| 9 | Houston Cougars | 28-6 | +23.5 | 60.7 | 37.2 |
| 10 | Gonzaga Bulldogs | 30-3 | +23.5 | 64.4 | 40.9 |
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
| 23 | Georgia Bulldogs | 22-10 | +20.7 | 69.1 | 48.6 |
| 24 | Kentucky Wildcats | 21-13 | +20.7 | 64.3 | 43.9 |
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

