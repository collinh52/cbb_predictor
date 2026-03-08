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

**Last Updated**: March 08, 2026 at 12:31 PM

![ATS Accuracy](https://img.shields.io/badge/ATS_Record-50.5%25-yellowgreen)

#### 🏆 Rolling ATS Performance

| Timeframe | ATS Record | Accuracy |
|-----------|------------|----------|
| **Latest** (2026-03-07) | 38-47 | **44.7%** |
| **Last 7 Days** | 143-150 | **48.8%** |
| **Last 30 Days** | 606-594 | **50.5%** |
| **All-Time** | 606-594 | **50.5%** |

**Over/Under Accuracy**: 51.7%

#### 🎯 Accuracy by Confidence (ATS)

| Confidence | Record | Accuracy |
|------------|--------|----------|
| **50%+** | 176-172 | **50.6%** |
| **60%+** | 72-68 | **51.4%** |
| **70%+** | 24-24 | **50.0%** |
| **80%+** | 6-6 | **50.0%** |

#### 🏀 ATS Accuracy by Conference

| Conference | Record | Accuracy |
|------------|--------|----------|
| Big South | 24-8 | **75.0%** |
| Western Athletic | 16-9 | **64.0%** |
| Summit League | 15-9 | **62.5%** |
| Southern | 22-14 | **61.1%** |
| Missouri Valley | 24-16 | **60.0%** |
| Mountain West | 25-17 | **59.5%** |
| Atlantic Coast | 38-27 | **58.5%** |
| Mid-Eastern Athletic | 15-11 | **57.7%** |
| Atlantic 10 | 26-20 | **56.5%** |
| Ohio Valley | 22-17 | **56.4%** |
| Southeastern | 33-27 | **55.0%** |
| Patriot League | 12-10 | **54.5%** |
| Big 12 | 30-26 | **53.6%** |
| Southwestern Athletic | 18-17 | **51.4%** |
| ASUN | 23-23 | **50.0%** |
| America East | 16-16 | **50.0%** |
| Southland | 15-15 | **50.0%** |
| Mid-American | 22-24 | **47.8%** |
| Ivy League | 10-11 | **47.6%** |
| Conference USA | 18-21 | **46.2%** |
| Big East | 18-21 | **46.2%** |
| West Coast | 13-16 | **44.8%** |
| Big Ten | 27-34 | **44.3%** |
| Sun Belt | 22-29 | **43.1%** |
| Northeast | 12-17 | **41.4%** |
| Big West | 16-23 | **41.0%** |
| Metro Atlantic Athletic | 17-25 | **40.5%** |
| Coastal Athletic Association | 18-27 | **40.0%** |
| Horizon League | 12-18 | **40.0%** |
| Big Sky | 13-21 | **38.2%** |
| American | 16-27 | **37.2%** |

> *A game counts for a conference if either team is a member.*

#### Combined Statistics

- **Total Predictions**: 1200
- **Overall Winner Accuracy**: 50.5%

#### 📅 Predictions for Today (2026-03-08)

| Matchup | Spread Pick | Total Pick | Confidence |
|---------|-------------|------------|------------|
| Northwestern St Demons @ Nicholls St Colonels | **AWAY** (+2.5) | **UNDER** (141.5) | 84% |
| Charlotte 49ers @ South Florida Bulls | **AWAY** (+16.0) | **OVER** (152.5) | 58% |
| Temple Owls @ Tulsa Golden Hurricane | **HOME** (-11.5) | **UNDER** (153.0) | 67% |
| Winthrop Eagles @ High Point Panthers | **HOME** (-6.5) | **UNDER** (161.5) | 53% |
| Michigan St Spartans @ Michigan Wolverines | **HOME** (-9.5) | **UNDER** (150.5) | 66% |
| Boston Univ. Terriers @ Navy Midshipmen | **HOME** (-7.5) | **OVER** (137.5) | 54% |
| Pacific Tigers @ Santa Clara Broncos | **AWAY** (+10.5) | **UNDER** (149.5) | 51% |
| North Dakota Fighting Hawks @ North Dakota St Bison | **AWAY** (+9.5) | **OVER** (147.5) | 64% |
| Southern Miss Golden Eagles @ Troy Trojans | **HOME** (-4.5) | **UNDER** (144.5) | 55% |
| William & Mary Tribe @ Hofstra Pride | **HOME** (-5.5) | **UNDER** (154.5) | 66% |
| Illinois Fighting Illini @ Maryland Terrapins | **HOME** (+15.5) | **UNDER** (146.5) | 51% |
| Iowa Hawkeyes @ Nebraska Cornhuskers | **HOME** (-6.5) | **UNDER** (134.5) | 62% |
| East Carolina Pirates @ UAB Blazers | **AWAY** (+10.5) | **UNDER** (148.0) | 43% |
| Idaho State Bengals @ Portland St Vikings | **AWAY** (+6.5) | **UNDER** (139.5) | 37% |
| Campbell Fighting Camels @ UNC Wilmington Seahawks | **AWAY** (+7.0) | **UNDER** (149.0) | 48% |
| UNC Greensboro Spartans @ Furman Paladins | **AWAY** (+6.5) | **OVER** (148.5) | 40% |
| Queens University Royals @ Central Arkansas Bears | **HOME** (-2.5) | **OVER** (157.5) | 54% |
| Drexel Dragons @ Monmouth Hawks | **HOME** (-3.0) | **UNDER** (138.5) | 51% |
| Houston Christian Huskies @ New Orleans Privateers | **AWAY** (+5.0) | **OVER** (142.5) | 32% |
| UTSA Roadrunners @ Rice Owls | **AWAY** (+12.0) | **UNDER** (150.5) | 33% |
| Georgia Southern Eagles @ Marshall Thundering Herd | **HOME** (-3.5) | **UNDER** (170.5) | 51% |
| Fairfield Stags @ Siena Saints | **HOME** (-3.0) | **UNDER** (140.5) | 27% |
| Penn State Nittany Lions @ Rutgers Scarlet Knights | **AWAY** (+5.5) | **OVER** (149.0) | 25% |
| Marist Red Foxes @ Merrimack Warriors | **AWAY** (+3.5) | **OVER** (125.5) | 36% |
| Idaho Vandals @ Montana St Bobcats | **HOME** (-2.5) | **OVER** (142.5) | 22% |
| Towson Tigers @ Charleston Cougars | **AWAY** (+2.5) | **UNDER** (133.5) | 22% |
| Western Carolina Catamounts @ East Tennessee St Buccaneers | **AWAY** (+2.5) | **UNDER** (149.5) | 14% |
| Northern Kentucky Norse @ Green Bay Phoenix | **HOME** (+2.5) | **OVER** (146.0) | 21% |
| San Francisco Dons @ Oregon St Beavers | **HOME** (+3.5) | **OVER** (142.5) | 10% |
| Colgate Raiders @ Lehigh Mountain Hawks | **HOME** (+2.0) | **OVER** (147.5) | 32% |
| Memphis Tigers @ Tulane Green Wave | **HOME** (+1.0) | **UNDER** (152.0) | 37% |
| Northern Iowa Panthers @ UIC Flames | **HOME** (+3.5) | **OVER** (123.5) | 19% |

> 📈 *ATS = Against The Spread (with Vegas lines). Updated daily via GitHub Actions.*

<!-- ACCURACY_STATS_END -->

<!-- RANKINGS_START -->

### 🏆 Top 25 Team Rankings

*Updated: March 08, 2026*

| Rank | Team | Record | Rating | Off | Def |
|------|------|--------|--------|-----|-----|
| 1 | Michigan Wolverines | 28-2 | +30.5 | 71.5 | 41.0 |
| 2 | Duke Blue Devils | 29-2 | +28.0 | 65.4 | 37.4 |
| 3 | Arizona Wildcats | 29-2 | +27.6 | 68.4 | 40.8 |
| 4 | Illinois Fighting Illini | 23-7 | +26.6 | 67.6 | 41.4 |
| 5 | Florida Gators | 25-6 | +26.2 | 67.8 | 41.9 |
| 6 | Louisville Cardinals | 22-9 | +25.2 | 68.8 | 44.0 |
| 7 | Iowa State Cyclones | 25-6 | +24.7 | 65.0 | 40.5 |
| 8 | Alabama Crimson Tide | 23-8 | +24.5 | 72.8 | 48.3 |
| 9 | Purdue Boilermakers | 23-8 | +24.3 | 66.2 | 42.1 |
| 10 | Gonzaga Bulldogs | 28-3 | +24.2 | 65.2 | 40.9 |
| 11 | Arkansas Razorbacks | 23-8 | +24.0 | 71.3 | 47.3 |
| 12 | Houston Cougars | 26-5 | +23.3 | 60.7 | 37.5 |
| 13 | Vanderbilt Commodores | 24-7 | +22.8 | 67.6 | 44.7 |
| 14 | UConn Huskies | 27-4 | +22.7 | 62.7 | 40.0 |
| 15 | Texas Tech Red Raiders | 22-9 | +22.2 | 64.9 | 42.8 |
| 16 | BYU Cougars | 21-10 | +22.2 | 68.3 | 46.1 |
| 17 | St. John's Red Storm | 25-6 | +22.1 | 64.7 | 42.6 |
| 18 | Kansas Jayhawks | 22-9 | +22.1 | 63.2 | 41.1 |
| 19 | Michigan State Spartans | 25-5 | +22.0 | 62.1 | 40.1 |
| 20 | Tennessee Volunteers | 21-10 | +22.0 | 62.7 | 41.1 |
| 21 | Wisconsin Badgers | 22-9 | +21.5 | 67.7 | 46.2 |
| 22 | Georgia Bulldogs | 22-9 | +21.5 | 69.5 | 48.3 |
| 23 | Kentucky Wildcats | 19-12 | +21.4 | 64.7 | 43.7 |
| 24 | Nebraska Cornhuskers | 25-5 | +21.0 | 61.2 | 40.2 |
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

