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

**Last Updated**: March 10, 2026 at 12:42 PM

![ATS Accuracy](https://img.shields.io/badge/ATS_Record-50.9%25-yellowgreen)

#### 🏆 Rolling ATS Performance

| Timeframe | ATS Record | Accuracy |
|-----------|------------|----------|
| **Latest** (2026-03-09) | 6-6 | **50.0%** |
| **Last 7 Days** | 152-148 | **50.7%** |
| **Last 30 Days** | 634-612 | **50.9%** |
| **All-Time** | 634-612 | **50.9%** |

**Over/Under Accuracy**: 51.6%

#### 🎯 Accuracy by Confidence (ATS)

| Confidence | Record | Accuracy |
|------------|--------|----------|
| **50%+** | 188-178 | **51.4%** |
| **60%+** | 76-69 | **52.4%** |
| **70%+** | 24-24 | **50.0%** |
| **80%+** | 6-6 | **50.0%** |

#### 🏀 ATS Accuracy by Conference

| Conference | Record | Accuracy |
|------------|--------|----------|
| Big South | 25-8 | **75.8%** |
| Summit League | 16-9 | **64.0%** |
| Western Athletic | 16-9 | **64.0%** |
| Southern | 24-15 | **61.5%** |
| Mountain West | 26-17 | **60.5%** |
| Missouri Valley | 24-17 | **58.5%** |
| Atlantic Coast | 38-27 | **58.5%** |
| Mid-Eastern Athletic | 15-11 | **57.7%** |
| Atlantic 10 | 26-20 | **56.5%** |
| Ohio Valley | 22-17 | **56.4%** |
| Southeastern | 33-27 | **55.0%** |
| Big 12 | 31-26 | **54.4%** |
| Patriot League | 13-11 | **54.2%** |
| Southwestern Athletic | 19-17 | **52.8%** |
| West Coast | 17-16 | **51.5%** |
| America East | 16-16 | **50.0%** |
| Southland | 16-16 | **50.0%** |
| ASUN | 23-24 | **48.9%** |
| Mid-American | 22-24 | **47.8%** |
| Ivy League | 10-11 | **47.6%** |
| Big Ten | 30-35 | **46.2%** |
| Conference USA | 18-21 | **46.2%** |
| Big East | 18-21 | **46.2%** |
| Metro Atlantic Athletic | 19-25 | **43.2%** |
| Coastal Athletic Association | 22-29 | **43.1%** |
| Sun Belt | 23-31 | **42.6%** |
| Big West | 17-23 | **42.5%** |
| Northeast | 12-17 | **41.4%** |
| Horizon League | 13-20 | **39.4%** |
| American | 18-30 | **37.5%** |
| Big Sky | 14-24 | **36.8%** |

> *A game counts for a conference if either team is a member.*

#### Combined Statistics

- **Total Predictions**: 1246
- **Overall Winner Accuracy**: 50.9%

#### 📅 Predictions for Today (2026-03-10)

| Matchup | Spread Pick | Total Pick | Confidence |
|---------|-------------|------------|------------|
| Grambling St Tigers @ Jackson St Tigers | **HOME** (+6.5) | **OVER** (142.5) | 83% |
| Mercyhurst Lakers @ LIU Sharks | **AWAY** (+6.5) | **OVER** (136.5) | 66% |
| Utah Utes @ Cincinnati Bearcats | **AWAY** (+11.5) | **UNDER** (138.5) | 58% |
| Santa Clara Broncos @ Gonzaga Bulldogs | **HOME** (-6.5) | **UNDER** (162.5) | 73% |
| UT Rio Grande Valley Vaqueros @ McNeese Cowboys | **HOME** (-7.5) | **UNDER** (142.5) | 53% |
| UMass Lowell River Hawks @ UMBC Retrievers | **AWAY** (+7.5) | **OVER** (146.5) | 43% |
| Monmouth Hawks @ Hofstra Pride | **HOME** (-4.5) | **OVER** (134.5) | 46% |
| Ole Miss Rebels @ Texas Longhorns | **HOME** (-5.5) | **OVER** (149.5) | 60% |
| LSU Tigers @ Kentucky Wildcats | **HOME** (-6.5) | **OVER** (151.5) | 53% |
| Kansas St Wildcats @ BYU Cougars | **AWAY** (+10.5) | **UNDER** (165.5) | 45% |
| Air Force Falcons @ Nevada Wolf Pack | **AWAY** (+20.5) | **UNDER** (141.5) | 41% |
| Syracuse Orange @ SMU Mustangs | **HOME** (-5.5) | **OVER** (156.5) | 44% |
| NJIT Highlanders @ Vermont Catamounts | **AWAY** (+11.5) | **UNDER** (137.5) | 47% |
| Missouri St Bears @ Florida Int'l Golden Panthers | **HOME** (-1.5) | **OVER** (153.5) | 35% |
| Texas A&M-CC Islanders @ Stephen F. Austin Lumberjacks | **AWAY** (+6.5) | **OVER** (135.5) | 47% |
| Detroit Mercy Titans @ Wright St Raiders | **HOME** (-3.5) | **OVER** (152.5) | 36% |
| Wyoming Cowboys @ UNLV Rebels | **HOME** (-3.5) | **UNDER** (158.0) | 34% |
| California Golden Bears @ Florida St Seminoles | **HOME** (-2.5) | **UNDER** (153.0) | 42% |
| Oklahoma St Cowboys @ Colorado Buffaloes | **HOME** (-1.5) | **OVER** (163.5) | 41% |
| Tulane Green Wave @ Memphis Tigers | **HOME** (-4.0) | **OVER** (150.0) | 36% |
| Montana Grizzlies @ Portland St Vikings | **HOME** (-2.5) | **UNDER** (142.5) | 52% |
| Alcorn St Braves @ Prairie View Panthers | **AWAY** (+6.5) | **UNDER** (145.5) | 44% |
| Xavier Musketeers @ Marquette Golden Eagles | **HOME** (-3.5) | **OVER** (154.5) | 29% |
| Mississippi St Bulldogs @ Auburn Tigers | **AWAY** (+7.5) | **OVER** (158.5) | 38% |
| USC Trojans @ Washington Huskies | **AWAY** (+5.5) | **UNDER** (153.0) | 43% |
| Pittsburgh Panthers @ Stanford Cardinal | **AWAY** (+5.5) | **UNDER** (138.5) | 32% |
| Siena Saints @ Merrimack Warriors | **AWAY** (+3.5) | **OVER** (126.5) | 47% |
| Loyola (Chi) Ramblers @ Richmond Spiders | **AWAY** (+6.5) | **UNDER** (143.0) | 36% |
| Providence Friars @ Butler Bulldogs | **HOME** (+1.5) | **UNDER** (165.5) | 26% |
| Wake Forest Demon Deacons @ Virginia Tech Hokies | **HOME** (-2.5) | **UNDER** (151.5) | 30% |
| Penn State Nittany Lions @ Northwestern Wildcats | **AWAY** (+6.5) | **UNDER** (144.5) | 32% |
| Baylor Bears @ Arizona St Sun Devils | **HOME** (+3.5) | **UNDER** (153.5) | 18% |
| Maryland Terrapins @ Oregon Ducks | **AWAY** (+3.5) | **UNDER** (138.5) | 35% |
| Idaho Vandals @ Eastern Washington Eagles | **HOME** (-1.5) | **UNDER** (153.5) | 31% |
| New Mexico St Aggies @ Jacksonville St Gamecocks | **HOME** (+1.5) | **OVER** (140.5) | 18% |
| St. Bonaventure Bonnies @ La Salle Explorers | **HOME** (+5.5) | **UNDER** (148.0) | 8% |
| Boston Univ. Terriers @ Lehigh Mountain Hawks | **HOME** (+1.5) | **OVER** (141.5) | 32% |

> 📈 *ATS = Against The Spread (with Vegas lines). Updated daily via GitHub Actions.*

<!-- ACCURACY_STATS_END -->

<!-- RANKINGS_START -->

### 🏆 Top 25 Team Rankings

*Updated: March 10, 2026*

| Rank | Team | Record | Rating | Off | Def |
|------|------|--------|--------|-----|-----|
| 1 | Michigan Wolverines | 29-2 | +30.6 | 71.8 | 41.2 |
| 2 | Duke Blue Devils | 29-2 | +27.9 | 65.4 | 37.4 |
| 3 | Arizona Wildcats | 29-2 | +27.6 | 68.4 | 40.8 |
| 4 | Florida Gators | 25-6 | +26.1 | 67.8 | 41.9 |
| 5 | Illinois Fighting Illini | 24-7 | +26.0 | 67.1 | 41.5 |
| 6 | Louisville Cardinals | 22-9 | +25.1 | 68.7 | 44.0 |
| 7 | Iowa State Cyclones | 25-6 | +24.7 | 64.9 | 40.6 |
| 8 | Alabama Crimson Tide | 23-8 | +24.4 | 72.8 | 48.4 |
| 9 | Purdue Boilermakers | 23-8 | +24.2 | 66.1 | 42.1 |
| 10 | Arkansas Razorbacks | 23-8 | +23.9 | 71.3 | 47.3 |
| 11 | Gonzaga Bulldogs | 29-3 | +23.7 | 64.5 | 40.9 |
| 12 | Houston Cougars | 26-5 | +23.3 | 60.7 | 37.5 |
| 13 | Vanderbilt Commodores | 24-7 | +22.7 | 67.5 | 44.7 |
| 14 | UConn Huskies | 27-4 | +22.7 | 62.7 | 40.0 |
| 15 | Michigan State Spartans | 25-6 | +22.2 | 62.5 | 40.3 |
| 16 | BYU Cougars | 21-10 | +22.1 | 68.3 | 46.2 |
| 17 | Texas Tech Red Raiders | 22-9 | +22.1 | 64.9 | 42.8 |
| 18 | St. John's Red Storm | 25-6 | +22.1 | 64.7 | 42.6 |
| 19 | Kansas Jayhawks | 22-9 | +22.0 | 63.2 | 41.1 |
| 20 | Tennessee Volunteers | 21-10 | +22.0 | 62.7 | 41.1 |
| 21 | Wisconsin Badgers | 22-9 | +21.4 | 67.7 | 46.2 |
| 22 | Georgia Bulldogs | 22-9 | +21.4 | 69.5 | 48.3 |
| 23 | Kentucky Wildcats | 19-12 | +21.3 | 64.7 | 43.8 |
| 24 | Nebraska Cornhuskers | 26-5 | +21.2 | 61.6 | 40.4 |
| 25 | Ohio State Buckeyes | 20-11 | +20.7 | 65.2 | 44.8 |

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

