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

**Last Updated**: February 24, 2026 at 12:46 PM

![ATS Accuracy](https://img.shields.io/badge/ATS_Record-50.6%25-yellowgreen)

#### 🏆 Rolling ATS Performance

| Timeframe | ATS Record | Accuracy |
|-----------|------------|----------|
| **Latest** (2026-02-23) | 4-3 | **57.1%** |
| **Last 7 Days** | 163-153 | **51.6%** |
| **Last 30 Days** | 309-302 | **50.6%** |
| **All-Time** | 309-302 | **50.6%** |

**Over/Under Accuracy**: 48.9%

#### 🎯 Accuracy by Confidence (ATS)

| Confidence | Record | Accuracy |
|------------|--------|----------|
| **50%+** | 95-86 | **52.5%** |
| **60%+** | 40-31 | **56.3%** |
| **70%+** | 15-13 | **53.6%** |
| **80%+** | 5-5 | **50.0%** |

#### 🏀 ATS Accuracy by Conference

| Conference | Record | Accuracy |
|------------|--------|----------|
| Western Athletic | 10-3 | **76.9%** |
| Big South | 12-5 | **70.6%** |
| Southeastern | 19-9 | **67.9%** |
| Mid-Eastern Athletic | 8-5 | **61.5%** |
| Atlantic Coast | 19-12 | **61.3%** |
| Atlantic 10 | 12-8 | **60.0%** |
| Mountain West | 11-8 | **57.9%** |
| Ohio Valley | 12-9 | **57.1%** |
| Big East | 10-8 | **55.6%** |
| Ivy League | 5-4 | **55.6%** |
| Southern | 11-9 | **55.0%** |
| Big 12 | 14-12 | **53.8%** |
| Horizon League | 9-8 | **52.9%** |
| Conference USA | 10-9 | **52.6%** |
| Patriot League | 6-6 | **50.0%** |
| ASUN | 12-12 | **50.0%** |
| Summit League | 6-6 | **50.0%** |
| America East | 8-8 | **50.0%** |
| Big Sky | 9-9 | **50.0%** |
| Southwestern Athletic | 9-10 | **47.4%** |
| Sun Belt | 13-15 | **46.4%** |
| Mid-American | 10-12 | **45.5%** |
| Missouri Valley | 9-11 | **45.0%** |
| Northeast | 7-9 | **43.8%** |
| Coastal Athletic Association | 9-13 | **40.9%** |
| American | 10-15 | **40.0%** |
| Southland | 8-12 | **40.0%** |
| West Coast | 6-10 | **37.5%** |
| Metro Atlantic Athletic | 9-15 | **37.5%** |
| Big Ten | 11-19 | **36.7%** |
| Big West | 7-13 | **35.0%** |

> *A game counts for a conference if either team is a member.*

#### Combined Statistics

- **Total Predictions**: 611
- **Overall Winner Accuracy**: 50.6%

#### 📅 Predictions for Today (2026-02-24)

| Matchup | Spread Pick | Total Pick | Confidence |
|---------|-------------|------------|------------|
| Minnesota Golden Gophers @ Michigan Wolverines | **AWAY** (+22.5) | **UNDER** (145.5) | 69% |
| Buffalo Bulls @ Akron Zips | **AWAY** (+15.5) | **UNDER** (158.0) | 54% |
| Duke Blue Devils @ Notre Dame Fighting Irish | **HOME** (+17.5) | **UNDER** (140.5) | 51% |
| Iowa State Cyclones @ Utah Utes | **HOME** (+12.5) | **UNDER** (144.5) | 75% |
| Southern Miss Golden Eagles @ Arkansas St Red Wolves | **HOME** (-9.5) | **UNDER** (156.5) | 55% |
| UCF Knights @ BYU Cougars | **AWAY** (+11.5) | **UNDER** (163.5) | 56% |
| Western Michigan Broncos @ Bowling Green Falcons | **AWAY** (+12.0) | **UNDER** (150.0) | 59% |
| Louisiana Ragin' Cajuns @ Troy Trojans | **AWAY** (+12.0) | **OVER** (134.0) | 49% |
| Northwestern Wildcats @ Indiana Hoosiers | **AWAY** (+8.5) | **UNDER** (146.5) | 56% |
| USC Trojans @ UCLA Bruins | **HOME** (-6.5) | **OVER** (150.5) | 50% |
| Fresno St Bulldogs @ Colorado St Rams | **AWAY** (+9.0) | **UNDER** (146.5) | 52% |
| Wyoming Cowboys @ Boise State Broncos | **AWAY** (+8.5) | **OVER** (148.0) | 52% |
| Southern Indiana Screaming Eagles @ Morehead St Eagles | **AWAY** (+8.5) | **OVER** (143.0) | 42% |
| Arizona St Sun Devils @ TCU Horned Frogs | **AWAY** (+6.5) | **UNDER** (148.5) | 51% |
| Old Dominion Monarchs @ Marshall Thundering Herd | **AWAY** (+6.5) | **OVER** (160.0) | 39% |
| Northern Illinois Huskies @ Toledo Rockets | **AWAY** (+12.0) | **UNDER** (150.0) | 66% |
| Cincinnati Bearcats @ Texas Tech Red Raiders | **AWAY** (+6.5) | **UNDER** (142.5) | 58% |
| St. Francis (PA) Red Flash @ New Haven Chargers | **AWAY** (+6.5) | **UNDER** (142.5) | 56% |
| Bradley Braves @ UIC Flames | **HOME** (-3.5) | **UNDER** (143.0) | 35% |
| NC State Wolfpack @ Virginia Cavaliers | **AWAY** (+5.5) | **UNDER** (152.5) | 39% |
| Central Michigan Chippewas @ Kent State Golden Flashes | **AWAY** (+11.0) | **UNDER** (157.0) | 32% |
| Coastal Carolina Chanticleers @ Georgia St Panthers | **HOME** (+0.0) | **OVER** (141.0) | 29% |
| Saint Louis Billikens @ Dayton Flyers | **HOME** (+4.5) | **UNDER** (156.5) | 47% |
| Xavier Musketeers @ Providence Friars | **AWAY** (+5.5) | **OVER** (170.5) | 47% |
| Miami (OH) RedHawks @ Eastern Michigan Eagles | **HOME** (+10.5) | **UNDER** (153.5) | 25% |
| San José St Spartans @ Air Force Falcons | **HOME** (+6.5) | **OVER** (141.5) | 25% |
| West Virginia Mountaineers @ Oklahoma St Cowboys | **HOME** (-1.5) | **UNDER** (141.5) | 40% |
| Auburn Tigers @ Oklahoma Sooners | **HOME** (+1.5) | **UNDER** (159.5) | 26% |
| Massachusetts Minutemen @ Ball State Cardinals | **HOME** (+5.0) | **OVER** (141.0) | 25% |
| Miami Hurricanes @ Florida St Seminoles | **HOME** (+2.5) | **UNDER** (156.5) | 35% |
| Wake Forest Demon Deacons @ Boston College Eagles | **HOME** (+4.5) | **UNDER** (144.5) | 32% |
| Marquette Golden Eagles @ Georgetown Hoyas | **AWAY** (+3.5) | **UNDER** (150.5) | 39% |
| GW Revolutionaries @ La Salle Explorers | **HOME** (+7.0) | **UNDER** (146.5) | 48% |
| New Mexico Lobos @ Nevada Wolf Pack | **HOME** (+1.5) | **UNDER** (151.5) | 20% |
| Washington Huskies @ Rutgers Scarlet Knights | **HOME** (+4.5) | **UNDER** (142.5) | 23% |
| Arizona Wildcats @ Baylor Bears | **HOME** (+8.5) | **UNDER** (154.5) | 22% |
| Kentucky Wildcats @ South Carolina Gamecocks | **HOME** (+6.5) | **UNDER** (148.5) | 12% |
| Tennessee Volunteers @ Missouri Tigers | **HOME** (+3.5) | **UNDER** (144.5) | 6% |

> 📈 *ATS = Against The Spread (with Vegas lines). Updated daily via GitHub Actions.*

<!-- ACCURACY_STATS_END -->

<!-- RANKINGS_START -->

### 🏆 Top 25 Team Rankings

*Updated: February 24, 2026*

| Rank | Team | Record | Rating | Off | Def |
|------|------|--------|--------|-----|-----|
| 1 | Michigan Wolverines | 25-2 | +30.9 | 71.9 | 41.0 |
| 2 | Arizona Wildcats | 25-2 | +27.5 | 68.7 | 41.3 |
| 3 | Duke Blue Devils | 25-2 | +27.2 | 65.4 | 38.2 |
| 4 | Illinois Fighting Illini | 22-6 | +26.3 | 67.7 | 41.6 |
| 5 | Louisville Cardinals | 20-8 | +25.8 | 69.2 | 43.8 |
| 6 | Iowa State Cyclones | 23-4 | +25.2 | 66.0 | 40.8 |
| 7 | Alabama Crimson Tide | 20-7 | +24.7 | 73.2 | 48.8 |
| 8 | Florida Gators | 21-6 | +24.6 | 66.0 | 41.7 |
| 9 | Purdue Boilermakers | 22-5 | +24.5 | 66.2 | 41.7 |
| 10 | Arkansas Razorbacks | 20-7 | +24.3 | 71.0 | 46.6 |
| 11 | Gonzaga Bulldogs | 27-2 | +24.1 | 65.6 | 41.5 |
| 12 | BYU Cougars | 20-7 | +23.5 | 69.0 | 45.5 |
| 13 | Vanderbilt Commodores | 21-6 | +23.3 | 67.7 | 44.5 |
| 14 | Houston Cougars | 23-5 | +23.0 | 60.4 | 37.5 |
| 15 | St. John's Red Storm | 22-5 | +22.4 | 65.4 | 43.0 |
| 16 | Kansas Jayhawks | 21-7 | +22.3 | 62.9 | 40.6 |
| 17 | UConn Huskies | 25-3 | +22.3 | 62.6 | 40.4 |
| 18 | Michigan State Spartans | 22-5 | +22.3 | 61.9 | 39.6 |
| 19 | Tennessee Volunteers | 20-7 | +22.3 | 63.3 | 41.3 |
| 20 | Texas Tech Red Raiders | 20-7 | +22.3 | 65.2 | 42.9 |
| 21 | NC State Wolfpack | 19-8 | +22.2 | 67.0 | 45.2 |
| 22 | Kentucky Wildcats | 17-10 | +21.5 | 64.9 | 43.8 |
| 23 | Nebraska Cornhuskers | 23-4 | +21.4 | 61.7 | 40.3 |
| 24 | Saint Louis Billikens | 25-2 | +21.3 | 67.5 | 46.2 |
| 25 | Georgia Bulldogs | 19-8 | +21.3 | 69.4 | 48.4 |

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

