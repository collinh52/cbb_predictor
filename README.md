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

**Last Updated**: November 25, 2026 at 08:53 PM

![ATS Accuracy](https://img.shields.io/badge/ATS_Record-50.7%25-yellowgreen)

#### 🏆 Rolling ATS Performance

| Timeframe | ATS Record | Accuracy |
|-----------|------------|----------|
| **Latest** (2026-11-24) | 2-1 | **66.7%** |
| **Last 7 Days** | 16-6 | **72.7%** |
| **Last 30 Days** | 35-27 | **56.5%** |
| **All-Time** | 798-777 | **50.7%** |

**Over/Under Accuracy**: 51.0%

#### 🎯 Accuracy by Confidence (ATS)

| Confidence | Record | Accuracy |
|------------|--------|----------|
| **50%+** | 264-256 | **50.8%** |
| **60%+** | 123-108 | **53.2%** |
| **70%+** | 43-41 | **51.2%** |
| **80%+** | 14-14 | **50.0%** |

#### 🏀 ATS Accuracy by Conference

| Conference | Record | Accuracy |
|------------|--------|----------|
| Big South | 27-8 | **77.1%** |
| Mountain West | 45-26 | **63.4%** |
| Southern | 25-15 | **62.5%** |
| United Athletic | 21-14 | **60.0%** |
| Patriot League | 17-12 | **58.6%** |
| West Coast | 25-18 | **58.1%** |
| Atlantic Coast | 59-44 | **57.3%** |
| Mid-Eastern Athletic | 21-17 | **55.3%** |
| Summit League | 16-13 | **55.2%** |
| Atlantic 10 | 42-35 | **54.5%** |
| Missouri Valley | 27-23 | **54.0%** |
| Ohio Valley | 24-21 | **53.3%** |
| Southwestern Athletic | 26-24 | **52.0%** |
| Big 12 | 55-52 | **51.4%** |
| America East | 19-18 | **51.4%** |
| Mid-American | 31-31 | **50.0%** |
| Big East | 32-32 | **50.0%** |
| Big West | 25-26 | **49.0%** |
| Southland | 20-21 | **48.8%** |
| Southeastern | 58-61 | **48.7%** |
| Conference USA | 26-28 | **48.1%** |
| Metro | 23-26 | **46.9%** |
| Northeast | 14-17 | **45.2%** |
| Sun Belt | 26-32 | **44.8%** |
| Atlantic Sun | 25-31 | **44.6%** |
| Big Ten | 54-67 | **44.6%** |
| Coastal Athletic Association | 23-33 | **41.1%** |
| Horizon League | 16-23 | **41.0%** |
| Big Sky | 19-29 | **39.6%** |
| Ivy League | 10-16 | **38.5%** |
| American | 25-42 | **37.3%** |

> *A game counts for a conference if either team is a member.*

#### Combined Statistics

- **Total Predictions**: 1575
- **Overall Winner Accuracy**: 50.7%

#### 📅 Predictions for Today (2026-11-25)

| Matchup | Spread Pick | Total Pick | Confidence |
|---------|-------------|------------|------------|
| St. Thomas (MN) Tommies @ UNC Wilmington Seahawks | **HOME** (-7.0) | **UNDER** (158.0) | 95% |
| Grambling St Tigers @ New Orleans Privateers | **HOME** (-3.5) | **UNDER** (148.5) | 50% |
| West Florida Argonauts @ Northwestern St Demons | **HOME** (+0.0) | **UNDER** (139.5) | 84% |
| Southern Jaguars @ Nebraska Cornhuskers | **AWAY** (+34.5) | **UNDER** (149.5) | 73% |
| Norfolk St Spartans @ NC State Wolfpack | **AWAY** (+27.5) | **OVER** (150.5) | 93% |
| Northeastern Huskies @ Wisconsin Badgers | **AWAY** (+21.5) | **OVER** (158.5) | 66% |
| Miss Valley St Delta Devils @ New Mexico Lobos | **AWAY** (+35.5) | **UNDER** (151.5) | 64% |
| Albany Great Danes @ Syracuse Orange | **AWAY** (+24.5) | **UNDER** (146.5) | 55% |
| Incarnate Word Cardinals @ Hawai'i Rainbow Warriors | **AWAY** (+17.0) | **OVER** (139.0) | 68% |
| Stanford Cardinal @ Saint Louis Billikens | **HOME** (-4.0) | **UNDER** (152.5) | 54% |
| Tennessee Volunteers @ Iowa State Cyclones | **HOME** (-2.5) | **UNDER** (139.5) | 73% |
| Jacksonville St Gamecocks @ Pacific Tigers | **HOME** (-5.5) | **UNDER** (133.5) | 60% |
| Longwood Lancers @ George Mason Patriots | **AWAY** (+16.5) | **UNDER** (145.5) | 77% |
| Georgetown Hoyas @ Texas Longhorns | **HOME** (-8.5) | **UNDER** (154.0) | 77% |
| Wake Forest Demon Deacons @ Mississippi St Bulldogs | **HOME** (-5.0) | **OVER** (151.0) | 66% |
| Holy Cross Crusaders @ Dartmouth Big Green | **AWAY** (+11.5) | **UNDER** (147.5) | 50% |
| Alcorn St Braves @ Texas State Bobcats | **AWAY** (+26.5) | **UNDER** (146.5) | 67% |
| CSU Bakersfield Roadrunners @ Pepperdine Waves | **AWAY** (+10.5) | **OVER** (161.0) | 45% |
| Saint Mary's Gaels @ UCLA Bruins | **HOME** (-7.0) | **UNDER** (153.0) | 84% |
| Eastern Washington Eagles @ Loyola Marymount Lions | **AWAY** (+7.0) | **UNDER** (152.0) | 63% |
| Colorado Buffaloes @ Grand Canyon Antelopes | **AWAY** (+9.5) | **UNDER** (154.5) | 62% |
| Georgia St Panthers @ Florida Gulf Coast Eagles | **HOME** (+1.5) | **UNDER** (143.5) | 47% |
| Miami Hurricanes @ Michigan Wolverines | **HOME** (+2.5) | **UNDER** (160.5) | 74% |
| Boston College Eagles @ UCF Knights | **HOME** (-2.5) | **UNDER** (145.0) | 43% |
| Oklahoma Sooners @ Purdue Boilermakers | **HOME** (-5.5) | **OVER** (141.0) | 70% |
| South Carolina Upstate Spartans @ The Citadel Bulldogs | **HOME** (-3.5) | **OVER** (138.5) | 40% |
| Washington Huskies @ VCU Rams | **HOME** (-3.5) | **OVER** (144.5) | 43% |
| Omaha Mavericks @ UC Davis Aggies | **AWAY** (+7.0) | **UNDER** (145.5) | 44% |
| South Carolina Gamecocks @ Arizona St Sun Devils | **AWAY** (+4.5) | **OVER** (140.0) | 30% |
| Bellarmine Knights @ Northern Kentucky Norse | **AWAY** (+6.5) | **OVER** (146.0) | 74% |
| BYU Cougars @ Providence Friars | **AWAY** (-2.5) | **OVER** (154.5) | 70% |
| Georgia Bulldogs @ Cincinnati Bearcats | **HOME** (-1.0) | **UNDER** (156.5) | 49% |
| Bethune-Cookman Wildcats @ Richmond Spiders | **AWAY** (+11.5) | **OVER** (146.0) | 36% |
| Prairie View Panthers @ Marshall Thundering Herd | **AWAY** (+15.0) | **UNDER** (150.5) | 25% |
| Arkansas Razorbacks @ Michigan St Spartans | **AWAY** (+6.0) | **OVER** (150.5) | 63% |
| Northern Illinois Huskies @ SIU-Edwardsville Cougars | **HOME** (+4.5) | **UNDER** (138.5) | 60% |
| Utah State Aggies @ SMU Mustangs | **HOME** (+4.5) | **UNDER** (169.0) | 57% |
| Maryland Terrapins @ San Diego St Aztecs | **HOME** (+4.5) | **UNDER** (153.5) | 57% |
| Clemson Tigers @ Colorado St Rams | **HOME** (+3.5) | **UNDER** (148.5) | 56% |
| Utah State Aggies @ USC Trojans | **AWAY** (+3.0) | **UNDER** (162.5) | 43% |
| TCU Horned Frogs @ Creighton Bluejays | **HOME** (+1.5) | **UNDER** (155.5) | 41% |
| Duke Blue Devils @ UConn Huskies | **AWAY** (+2.0) | **UNDER** (149.0) | 53% |
| Eastern Michigan Eagles @ UTEP Miners | **AWAY** (+1.0) | **OVER** (130.0) | 12% |
| Kennesaw St Owls @ Charleston Cougars | **AWAY** (+1.5) | **UNDER** (160.0) | 33% |

> 📈 *ATS = Against The Spread (with Vegas lines). Updated daily via GitHub Actions.*

<!-- ACCURACY_STATS_END -->

<!-- RANKINGS_START -->

### 🏆 Top 25 Team Rankings

*Updated: November 25, 2026*

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

