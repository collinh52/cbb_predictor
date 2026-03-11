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

**Last Updated**: March 11, 2026 at 05:08 AM

![ATS Accuracy](https://img.shields.io/badge/ATS_Record-50.8%25-yellowgreen)

#### 🏆 Rolling ATS Performance

| Timeframe | ATS Record | Accuracy |
|-----------|------------|----------|
| **Latest** (2026-03-10) | 15-16 | **48.4%** |
| **Last 7 Days** | 140-140 | **50.0%** |
| **Last 30 Days** | 649-628 | **50.8%** |
| **All-Time** | 649-628 | **50.8%** |

**Over/Under Accuracy**: 51.3%

#### 🎯 Accuracy by Confidence (ATS)

| Confidence | Record | Accuracy |
|------------|--------|----------|
| **50%+** | 191-180 | **51.5%** |
| **60%+** | 78-69 | **53.1%** |
| **70%+** | 25-24 | **51.0%** |
| **80%+** | 6-6 | **50.0%** |

#### 🏀 ATS Accuracy by Conference

| Conference | Record | Accuracy |
|------------|--------|----------|
| Big South | 25-8 | **75.8%** |
| Summit League | 16-9 | **64.0%** |
| Western Athletic | 16-9 | **64.0%** |
| Southern | 24-15 | **61.5%** |
| Mountain West | 27-17 | **61.4%** |
| Missouri Valley | 24-17 | **58.5%** |
| Atlantic Coast | 40-29 | **58.0%** |
| Mid-Eastern Athletic | 15-11 | **57.7%** |
| Atlantic 10 | 27-20 | **57.4%** |
| Ohio Valley | 22-17 | **56.4%** |
| Patriot League | 14-11 | **56.0%** |
| Southeastern | 34-27 | **55.7%** |
| Big 12 | 33-28 | **54.1%** |
| West Coast | 18-16 | **52.9%** |
| Southwestern Athletic | 19-18 | **51.4%** |
| America East | 17-17 | **50.0%** |
| Southland | 17-17 | **50.0%** |
| ASUN | 23-24 | **48.9%** |
| Mid-American | 22-24 | **47.8%** |
| Ivy League | 10-11 | **47.6%** |
| Big East | 19-22 | **46.3%** |
| Big Ten | 31-37 | **45.6%** |
| Metro Atlantic Athletic | 20-25 | **44.4%** |
| Coastal Athletic Association | 23-29 | **44.2%** |
| Conference USA | 18-23 | **43.9%** |
| Sun Belt | 23-31 | **42.6%** |
| Big West | 17-23 | **42.5%** |
| Northeast | 12-17 | **41.4%** |
| Horizon League | 13-21 | **38.2%** |
| American | 18-31 | **36.7%** |
| Big Sky | 14-26 | **35.0%** |

> *A game counts for a conference if either team is a member.*

#### Combined Statistics

- **Total Predictions**: 1277
- **Overall Winner Accuracy**: 50.8%

#### 📅 Predictions for Today (2026-03-11)

| Matchup | Spread Pick | Total Pick | Confidence |
|---------|-------------|------------|------------|
| Buffalo Bulls @ Akron Zips | **HOME** (-12.5) | **UNDER** (164.0) | 69% |
| Massachusetts Minutemen @ Miami (OH) RedHawks | **HOME** (-7.5) | **OVER** (162.0) | 69% |
| San José St Spartans @ Boise State Broncos | **AWAY** (+14.5) | **OVER** (147.0) | 65% |
| Delaware St Hornets @ Morgan St Bears | **HOME** (-2.5) | **UNDER** (142.5) | 57% |
| Ohio Bobcats @ Kent State Golden Flashes | **HOME** (-4.0) | **OVER** (161.0) | 46% |
| Rutgers Scarlet Knights @ Minnesota Golden Gophers | **AWAY** (+5.0) | **UNDER** (137.0) | 35% |
| South Carolina Gamecocks @ Oklahoma Sooners | **AWAY** (+6.5) | **UNDER** (149.5) | 45% |
| UC Santa Barbara Gauchos @ UC Davis Aggies | **HOME** (-4.0) | **UNDER** (143.0) | 38% |
| Middle Tennessee Blue Raiders @ Louisiana Tech Bulldogs | **HOME** (+2.0) | **OVER** (132.0) | 49% |
| Fresno St Bulldogs @ Colorado St Rams | **AWAY** (+5.0) | **UNDER** (146.5) | 45% |
| Georgetown Hoyas @ DePaul Blue Demons | **HOME** (-1.5) | **UNDER** (137.5) | 50% |
| Temple Owls @ Florida Atlantic Owls | **HOME** (-2.0) | **UNDER** (147.5) | 34% |
| Tarleton State Texans @ Abilene Christian Wildcats | **HOME** (+1.0) | **UNDER** (142.0) | 62% |
| Rhode Island Rams @ Duquesne Dukes | **HOME** (-1.0) | **UNDER** (138.5) | 31% |
| Cal Poly Mustangs @ UC San Diego Tritons | **AWAY** (+7.0) | **UNDER** (159.5) | 44% |
| GW Revolutionaries @ Fordham Rams | **HOME** (+5.5) | **UNDER** (141.5) | 27% |
| Creighton Bluejays @ Seton Hall Pirates | **AWAY** (+3.0) | **UNDER** (136.5) | 36% |
| Bowling Green Falcons @ Toledo Rockets | **AWAY** (+1.0) | **UNDER** (154.0) | 20% |

> 📈 *ATS = Against The Spread (with Vegas lines). Updated daily via GitHub Actions.*

<!-- ACCURACY_STATS_END -->

<!-- RANKINGS_START -->

### 🏆 Top 25 Team Rankings

*Updated: March 11, 2026*

| Rank | Team | Record | Rating | Off | Def |
|------|------|--------|--------|-----|-----|
| 1 | Michigan Wolverines | 29-2 | +30.6 | 71.8 | 41.2 |
| 2 | Duke Blue Devils | 29-2 | +27.9 | 65.4 | 37.4 |
| 3 | Arizona Wildcats | 29-2 | +27.5 | 68.3 | 40.8 |
| 4 | Florida Gators | 25-6 | +26.1 | 67.7 | 41.9 |
| 5 | Illinois Fighting Illini | 24-7 | +26.0 | 67.1 | 41.5 |
| 6 | Louisville Cardinals | 22-9 | +25.1 | 68.7 | 44.0 |
| 7 | Iowa State Cyclones | 25-6 | +24.6 | 65.0 | 40.6 |
| 8 | Alabama Crimson Tide | 23-8 | +24.4 | 72.8 | 48.4 |
| 9 | Purdue Boilermakers | 23-8 | +24.2 | 66.1 | 42.1 |
| 10 | Arkansas Razorbacks | 23-8 | +23.9 | 71.2 | 47.3 |
| 11 | Gonzaga Bulldogs | 30-3 | +23.7 | 64.5 | 40.8 |
| 12 | Houston Cougars | 26-5 | +23.2 | 60.7 | 37.5 |
| 13 | Vanderbilt Commodores | 24-7 | +22.7 | 67.5 | 44.7 |
| 14 | UConn Huskies | 27-4 | +22.6 | 62.6 | 40.0 |
| 15 | BYU Cougars | 22-10 | +22.2 | 68.8 | 46.6 |
| 16 | Michigan State Spartans | 25-6 | +22.2 | 62.5 | 40.3 |
| 17 | Texas Tech Red Raiders | 22-9 | +22.1 | 64.9 | 42.8 |
| 18 | St. John's Red Storm | 25-6 | +22.0 | 64.7 | 42.7 |
| 19 | Kansas Jayhawks | 22-9 | +22.0 | 63.1 | 41.1 |
| 20 | Tennessee Volunteers | 21-10 | +21.9 | 62.7 | 41.1 |
| 21 | Wisconsin Badgers | 22-9 | +21.4 | 67.7 | 46.2 |
| 22 | Georgia Bulldogs | 22-9 | +21.4 | 69.4 | 48.3 |
| 23 | Kentucky Wildcats | 19-12 | +21.3 | 64.7 | 43.8 |
| 24 | Nebraska Cornhuskers | 26-5 | +21.2 | 61.6 | 40.4 |
| 25 | Ohio State Buckeyes | 20-11 | +20.6 | 65.2 | 44.9 |

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

