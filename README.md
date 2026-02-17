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

**Last Updated**: February 10, 2026 at 12:51 PM

![ATS Accuracy](https://img.shields.io/badge/ATS_Record-63.0%25-brightgreen)

#### 🏆 Rolling ATS Performance

| Timeframe | ATS Record | Accuracy |
|-----------|------------|----------|
| **Latest** (2026-02-09) | 18-7 | **72.0%** |
| **Last 7 Days** | 0-0 | **0.0%** |
| **Last 30 Days** | 297-175 | **62.9%** |
| **All-Time** | 298-175 | **63.0%** |

**Over/Under Accuracy**: 49.7%

#### 🎯 Accuracy by Confidence (ATS)

| Confidence | Record | Accuracy |
|------------|--------|----------|
| **50%+** | 167-106 | **61.2%** |
| **60%+** | 104-73 | **58.8%** |
| **70%+** | 60-43 | **58.3%** |
| **80%+** | 33-20 | **62.3%** |

#### 🏀 ATS Accuracy by Conference

| Conference | Record | Accuracy |
|------------|--------|----------|
| Western Athletic | 7-1 | **87.5%** |
| America East | 9-2 | **81.8%** |
| Southland | 16-5 | **76.2%** |
| Northeast | 9-3 | **75.0%** |
| Mid-Eastern Athletic | 9-3 | **75.0%** |
| Atlantic Coast | 19-7 | **73.1%** |
| Big West | 8-3 | **72.7%** |
| Ohio Valley | 8-3 | **72.7%** |
| Atlantic 10 | 13-5 | **72.2%** |
| Sun Belt | 18-7 | **72.0%** |
| Conference USA | 10-4 | **71.4%** |
| Coastal Athletic Association | 12-6 | **66.7%** |
| ASUN | 12-6 | **66.7%** |
| Big Ten | 14-8 | **63.6%** |
| Big South | 7-4 | **63.6%** |
| Summit League | 7-4 | **63.6%** |
| Southwestern Athletic | 12-7 | **63.2%** |
| Big 12 | 13-9 | **59.1%** |
| Mid-American | 14-10 | **58.3%** |
| American | 7-5 | **58.3%** |
| Horizon League | 7-5 | **58.3%** |
| Mountain West | 8-6 | **57.1%** |
| Southern | 9-7 | **56.2%** |
| Patriot League | 5-4 | **55.6%** |
| Southeastern | 11-9 | **55.0%** |
| West Coast | 8-7 | **53.3%** |
| Big Sky | 8-8 | **50.0%** |
| Ivy League | 3-3 | **50.0%** |
| Metro Atlantic Athletic | 9-10 | **47.4%** |
| Big East | 7-8 | **46.7%** |
| Missouri Valley | 8-12 | **40.0%** |

> *A game counts for a conference if either team is a member.*

#### Straight-Up Predictions (Games Without Vegas Lines)

| **7-Day** | 0/0 (0.0%) |
| **30-Day** | 0/0 (0.0%) |
| **All-Time** | 1/3 (33.3%) |

#### Combined Statistics

- **Total Predictions**: 476
- **Overall Winner Accuracy**: 62.8%

#### 📅 Predictions for Today (2026-02-17)

| Matchup | Spread Pick | Total Pick | Confidence |
|---------|-------------|------------|------------|
| South Carolina Gamecocks @ Florida Gators | **AWAY** (+23.5) | **UNDER** (153.5) | 72% |
| Air Force Falcons @ New Mexico Lobos | **AWAY** (+27.5) | **UNDER** (148.5) | 61% |
| Saint Louis Billikens @ Rhode Island Rams | **AWAY** (-10.5) | **UNDER** (152.5) | 66% |
| Boston College Eagles @ Florida St Seminoles | **AWAY** (+11.5) | **UNDER** (148.0) | 76% |
| Kent State Golden Flashes @ Bowling Green Falcons | **HOME** (-3.0) | **OVER** (151.0) | 52% |
| Grand Canyon Antelopes @ San Diego St Aztecs | **AWAY** (+8.5) | **OVER** (138.5) | 49% |
| North Carolina Tar Heels @ NC State Wolfpack | **HOME** (-6.5) | **UNDER** (158.5) | 45% |
| LSU Tigers @ Texas Longhorns | **AWAY** (+10.5) | **UNDER** (151.5) | 45% |
| UCLA Bruins @ Michigan St Spartans | **AWAY** (+8.5) | **OVER** (139.5) | 54% |
| Fresno St Bulldogs @ Wyoming Cowboys | **AWAY** (+8.5) | **UNDER** (147.5) | 59% |
| Ball State Cardinals @ Ohio Bobcats | **AWAY** (+9.5) | **UNDER** (143.0) | 61% |
| Virginia Tech Hokies @ Miami Hurricanes | **AWAY** (+8.5) | **UNDER** (150.5) | 45% |
| GW Revolutionaries @ VCU Rams | **HOME** (-6.5) | **UNDER** (162.5) | 58% |
| Georgia Bulldogs @ Kentucky Wildcats | **AWAY** (+6.5) | **UNDER** (161.5) | 41% |
| Minnesota Golden Gophers @ Oregon Ducks | **HOME** (-4.5) | **UNDER** (135.5) | 49% |
| Gardner-Webb Bulldogs @ Charleston Southern Buccaneers | **AWAY** (+17.5) | **OVER** (160.5) | 40% |
| Nebraska Cornhuskers @ Iowa Hawkeyes | **HOME** (-1.5) | **UNDER** (139.5) | 55% |
| SE Missouri St Redhawks @ Tenn-Martin Skyhawks | **HOME** (-3.5) | **UNDER** (140.5) | 59% |
| Akron Zips @ Western Michigan Broncos | **HOME** (+14.0) | **UNDER** (158.5) | 41% |
| Miami (OH) RedHawks @ Massachusetts Minutemen | **AWAY** (-3.5) | **OVER** (163.5) | 51% |
| Louisville Cardinals @ SMU Mustangs | **AWAY** (-3.5) | **UNDER** (166.5) | 49% |
| TCU Horned Frogs @ UCF Knights | **HOME** (-2.5) | **UNDER** (155.5) | 37% |
| Texas Tech Red Raiders @ Arizona St Sun Devils | **HOME** (+8.5) | **UNDER** (154.5) | 45% |
| Central Michigan Chippewas @ Eastern Michigan Eagles | **AWAY** (+5.0) | **OVER** (144.0) | 19% |
| Michigan Wolverines @ Purdue Boilermakers | **HOME** (+2.5) | **UNDER** (156.5) | 30% |
| Northern Illinois Huskies @ Buffalo Bulls | **AWAY** (+9.0) | **UNDER** (148.0) | 47% |
| Nevada Wolf Pack @ San José St Spartans | **HOME** (+10.5) | **OVER** (140.5) | 14% |
| Baylor Bears @ Kansas St Wildcats | **HOME** (+4.5) | **UNDER** (161.5) | 24% |
| Wisconsin Badgers @ Ohio State Buckeyes | **HOME** (+1.5) | **OVER** (157.5) | 9% |
| Villanova Wildcats @ Xavier Musketeers | **HOME** (+4.5) | **OVER** (152.5) | 5% |

> 📈 *ATS = Against The Spread (with Vegas lines). Updated daily via GitHub Actions.*

<!-- ACCURACY_STATS_END -->

<!-- RANKINGS_START -->

### 🏆 Top 25 Team Rankings

*Updated: February 17, 2026*

| Rank | Team | Record | Rating | Off | Def |
|------|------|--------|--------|-----|-----|
| 1 | Michigan Wolverines | 24-1 | +31.2 | 72.1 | 40.9 |
| 2 | Arizona Wildcats | 23-2 | +27.4 | 69.0 | 41.6 |
| 3 | Duke Blue Devils | 24-2 | +27.1 | 65.5 | 38.4 |
| 4 | Louisville Cardinals | 19-6 | +27.0 | 70.1 | 43.5 |
| 5 | Illinois Fighting Illini | 21-5 | +25.9 | 67.0 | 41.4 |
| 6 | Iowa State Cyclones | 23-3 | +25.5 | 66.3 | 40.8 |
| 7 | Florida Gators | 19-6 | +24.7 | 65.8 | 41.5 |
| 8 | Gonzaga Bulldogs | 25-2 | +24.6 | 66.0 | 41.4 |
| 9 | Alabama Crimson Tide | 18-7 | +24.4 | 72.7 | 48.4 |
| 10 | Arkansas Razorbacks | 19-6 | +24.4 | 70.2 | 45.9 |
| 11 | Purdue Boilermakers | 21-4 | +23.9 | 65.4 | 41.5 |
| 12 | Vanderbilt Commodores | 21-4 | +23.8 | 68.3 | 44.4 |
| 13 | Houston Cougars | 23-3 | +23.5 | 60.7 | 37.2 |
| 14 | BYU Cougars | 19-6 | +23.0 | 69.0 | 46.0 |
| 15 | UConn Huskies | 24-2 | +22.7 | 62.7 | 40.0 |
| 16 | St. John's Red Storm | 20-5 | +22.4 | 65.7 | 43.3 |
| 17 | Kansas Jayhawks | 19-6 | +22.4 | 62.8 | 40.4 |
| 18 | Texas Tech Red Raiders | 19-6 | +22.1 | 64.9 | 42.7 |
| 19 | Tennessee Volunteers | 18-7 | +22.0 | 63.4 | 41.8 |
| 20 | Kentucky Wildcats | 17-8 | +21.8 | 65.1 | 43.7 |
| 21 | Michigan State Spartans | 20-5 | +21.7 | 61.8 | 40.1 |
| 22 | NC State Wolfpack | 18-8 | +21.5 | 66.8 | 45.6 |
| 23 | Saint Louis Billikens | 24-1 | +21.5 | 67.3 | 45.8 |
| 24 | Nebraska Cornhuskers | 22-3 | +21.4 | 61.3 | 40.3 |
| 25 | Wisconsin Badgers | 18-7 | +20.8 | 67.6 | 46.8 |

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

