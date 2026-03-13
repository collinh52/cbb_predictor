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

**Last Updated**: March 13, 2026 at 12:39 PM

![ATS Accuracy](https://img.shields.io/badge/ATS_Record-50.6%25-yellowgreen)

#### 🏆 Rolling ATS Performance

| Timeframe | ATS Record | Accuracy |
|-----------|------------|----------|
| **Latest** (2026-03-12) | 11-22 | **33.3%** |
| **Last 7 Days** | 134-137 | **49.4%** |
| **Last 30 Days** | 682-667 | **50.6%** |
| **All-Time** | 682-667 | **50.6%** |

**Over/Under Accuracy**: 51.4%

#### 🎯 Accuracy by Confidence (ATS)

| Confidence | Record | Accuracy |
|------------|--------|----------|
| **50%+** | 198-198 | **50.0%** |
| **60%+** | 84-74 | **53.2%** |
| **70%+** | 26-26 | **50.0%** |
| **80%+** | 6-6 | **50.0%** |

#### 🏀 ATS Accuracy by Conference

| Conference | Record | Accuracy |
|------------|--------|----------|
| Big South | 25-8 | **75.8%** |
| Summit League | 16-9 | **64.0%** |
| Southern | 24-15 | **61.5%** |
| Mountain West | 31-20 | **60.8%** |
| Western Athletic | 17-11 | **60.7%** |
| Atlantic 10 | 31-21 | **59.6%** |
| Missouri Valley | 24-17 | **58.5%** |
| Ohio Valley | 22-17 | **56.4%** |
| Patriot League | 14-11 | **56.0%** |
| Mid-Eastern Athletic | 16-13 | **55.2%** |
| Atlantic Coast | 41-35 | **53.9%** |
| Southwestern Athletic | 22-19 | **53.7%** |
| West Coast | 18-16 | **52.9%** |
| Southeastern | 35-33 | **51.5%** |
| Big 12 | 35-34 | **50.7%** |
| Mid-American | 25-25 | **50.0%** |
| America East | 17-17 | **50.0%** |
| ASUN | 23-24 | **48.9%** |
| Southland | 17-18 | **48.6%** |
| Big West | 21-23 | **47.7%** |
| Ivy League | 10-11 | **47.6%** |
| Big East | 21-25 | **45.7%** |
| Big Ten | 34-41 | **45.3%** |
| Metro Atlantic Athletic | 20-25 | **44.4%** |
| Coastal Athletic Association | 23-29 | **44.2%** |
| Conference USA | 19-25 | **43.2%** |
| Sun Belt | 23-31 | **42.6%** |
| Northeast | 12-17 | **41.4%** |
| American | 20-32 | **38.5%** |
| Horizon League | 13-21 | **38.2%** |
| Big Sky | 15-26 | **36.6%** |

> *A game counts for a conference if either team is a member.*

#### Combined Statistics

- **Total Predictions**: 1349
- **Overall Winner Accuracy**: 50.6%

#### 📅 Predictions for Today (2026-03-13)

| Matchup | Spread Pick | Total Pick | Confidence |
|---------|-------------|------------|------------|
| Clemson Tigers @ Duke Blue Devils | **HOME** (-11.5) | **UNDER** (134.5) | 71% |
| Kennesaw St Owls @ Sam Houston St Bearkats | **AWAY** (+4.5) | **UNDER** (161.5) | 83% |
| South Carolina St Bulldogs @ Howard Bison | **AWAY** (+15.5) | **UNDER** (144.5) | 80% |
| Kentucky Wildcats @ Florida Gators | **HOME** (-10.5) | **UNDER** (160.0) | 64% |
| GW Revolutionaries @ Saint Louis Billikens | **HOME** (-7.0) | **UNDER** (161.5) | 57% |
| Georgetown Hoyas @ UConn Huskies | **AWAY** (+13.5) | **UNDER** (139.5) | 58% |
| Ohio State Buckeyes @ Michigan Wolverines | **AWAY** (+12.5) | **UNDER** (154.5) | 50% |
| North Texas Mean Green @ Tulsa Golden Hurricane | **HOME** (-7.5) | **UNDER** (143.5) | 48% |
| Seton Hall Pirates @ St. John's Red Storm | **HOME** (-7.5) | **UNDER** (133.5) | 68% |
| Kent State Golden Flashes @ Akron Zips | **HOME** (-6.5) | **OVER** (163.0) | 51% |
| Ole Miss Rebels @ Alabama Crimson Tide | **AWAY** (+10.5) | **OVER** (163.5) | 62% |
| UT-Arlington Mavericks @ Utah Valley Wolverines | **HOME** (-8.5) | **OVER** (134.5) | 58% |
| Wisconsin Badgers @ Illinois Fighting Illini | **HOME** (-8.0) | **OVER** (157.0) | 52% |
| Nevada Wolf Pack @ Utah State Aggies | **HOME** (-6.5) | **OVER** (145.0) | 58% |
| Duquesne Dukes @ VCU Rams | **AWAY** (+8.5) | **UNDER** (153.5) | 50% |
| Oklahoma Sooners @ Arkansas Razorbacks | **HOME** (-6.5) | **OVER** (168.5) | 50% |
| St. Bonaventure Bonnies @ Dayton Flyers | **HOME** (-6.5) | **OVER** (141.0) | 45% |
| Kansas Jayhawks @ Houston Cougars | **HOME** (-5.5) | **UNDER** (135.5) | 47% |
| Miami Hurricanes @ Virginia Cavaliers | **HOME** (-4.0) | **UNDER** (144.0) | 43% |
| Utah Tech Trailblazers @ Cal Baptist Lancers | **HOME** (-6.5) | **OVER** (137.5) | 69% |
| Massachusetts Minutemen @ Toledo Rockets | **HOME** (-3.5) | **OVER** (158.5) | 51% |
| Delaware St Hornets @ North Carolina Central Eagles | **HOME** (-4.5) | **UNDER** (133.5) | 58% |
| Missouri St Bears @ Louisiana Tech Bulldogs | **HOME** (-1.5) | **OVER** (134.5) | 51% |
| Iowa State Cyclones @ Arizona Wildcats | **HOME** (-4.5) | **UNDER** (143.5) | 44% |
| CSU Northridge Matadors @ UC Irvine Anteaters | **HOME** (-4.5) | **OVER** (149.5) | 38% |
| CSU Fullerton Titans @ Hawai'i Rainbow Warriors | **HOME** (-3.5) | **UNDER** (158.5) | 35% |
| UCLA Bruins @ Michigan St Spartans | **AWAY** (+5.5) | **OVER** (142.5) | 42% |
| Charlotte 49ers @ UAB Blazers | **AWAY** (+5.0) | **UNDER** (145.5) | 31% |
| New Mexico Lobos @ San Diego St Aztecs | **HOME** (-1.5) | **OVER** (149.5) | 39% |
| Tennessee Volunteers @ Vanderbilt Commodores | **HOME** (-1.5) | **OVER** (147.5) | 24% |
| Purdue Boilermakers @ Nebraska Cornhuskers | **HOME** (+3.5) | **UNDER** (143.0) | 17% |
| Davidson Wildcats @ Saint Joseph's Hawks | **AWAY** (+2.5) | **OVER** (131.5) | 22% |
| Prairie View Panthers @ Alabama A&M Bulldogs | **HOME** (+0.0) | **UNDER** (142.5) | 14% |
| Southern Jaguars @ Florida A&M Rattlers | **HOME** (+2.5) | **OVER** (144.5) | 21% |

> 📈 *ATS = Against The Spread (with Vegas lines). Updated daily via GitHub Actions.*

<!-- ACCURACY_STATS_END -->

<!-- RANKINGS_START -->

### 🏆 Top 25 Team Rankings

*Updated: March 13, 2026*

| Rank | Team | Record | Rating | Off | Def |
|------|------|--------|--------|-----|-----|
| 1 | Michigan Wolverines | 29-2 | +30.3 | 71.7 | 41.4 |
| 2 | Arizona Wildcats | 30-2 | +27.5 | 68.1 | 40.6 |
| 3 | Duke Blue Devils | 30-2 | +27.2 | 65.0 | 37.8 |
| 4 | Florida Gators | 25-6 | +26.0 | 67.7 | 42.0 |
| 5 | Illinois Fighting Illini | 24-7 | +25.8 | 67.0 | 41.7 |
| 6 | Iowa State Cyclones | 27-6 | +25.3 | 64.8 | 39.8 |
| 7 | Alabama Crimson Tide | 23-8 | +24.3 | 72.9 | 48.5 |
| 8 | Louisville Cardinals | 23-10 | +24.2 | 67.4 | 43.6 |
| 9 | Purdue Boilermakers | 24-8 | +24.0 | 66.1 | 42.3 |
| 10 | Arkansas Razorbacks | 23-8 | +23.8 | 71.3 | 47.5 |
| 11 | Gonzaga Bulldogs | 30-3 | +23.6 | 64.5 | 40.9 |
| 12 | Houston Cougars | 27-5 | +23.1 | 60.7 | 37.6 |
| 13 | UConn Huskies | 28-4 | +22.7 | 62.9 | 40.2 |
| 14 | Vanderbilt Commodores | 24-7 | +22.6 | 67.5 | 44.9 |
| 15 | BYU Cougars | 23-11 | +22.1 | 67.9 | 45.8 |
| 16 | Michigan State Spartans | 25-6 | +22.0 | 62.5 | 40.5 |
| 17 | Kansas Jayhawks | 23-9 | +21.9 | 63.3 | 41.4 |
| 18 | Tennessee Volunteers | 22-10 | +21.9 | 62.6 | 41.1 |
| 19 | St. John's Red Storm | 26-6 | +21.9 | 64.6 | 42.8 |
| 20 | Texas Tech Red Raiders | 22-10 | +21.6 | 64.5 | 42.9 |
| 21 | Wisconsin Badgers | 23-9 | +21.1 | 67.5 | 46.4 |
| 22 | Nebraska Cornhuskers | 26-5 | +21.0 | 61.6 | 40.5 |
| 23 | Kentucky Wildcats | 21-12 | +20.9 | 64.6 | 44.0 |
| 24 | Georgia Bulldogs | 22-10 | +20.9 | 69.1 | 48.5 |
| 25 | Virginia Cavaliers | 28-4 | +20.5 | 63.1 | 42.6 |

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

