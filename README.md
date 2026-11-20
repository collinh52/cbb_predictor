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

**Last Updated**: November 20, 2026 at 07:29 PM

![ATS Accuracy](https://img.shields.io/badge/ATS_Record-50.6%25-yellowgreen)

#### 🏆 Rolling ATS Performance

| Timeframe | ATS Record | Accuracy |
|-----------|------------|----------|
| **Latest** (2026-11-19) | 4-0 | **100.0%** |
| **Last 7 Days** | 15-9 | **62.5%** |
| **Last 30 Days** | 28-23 | **54.9%** |
| **All-Time** | 792-772 | **50.6%** |

**Over/Under Accuracy**: 50.9%

#### 🎯 Accuracy by Confidence (ATS)

| Confidence | Record | Accuracy |
|------------|--------|----------|
| **50%+** | 260-253 | **50.7%** |
| **60%+** | 119-106 | **52.9%** |
| **70%+** | 39-39 | **50.0%** |
| **80%+** | 11-13 | **45.8%** |

#### 🏀 ATS Accuracy by Conference

| Conference | Record | Accuracy |
|------------|--------|----------|
| Big South | 27-8 | **77.1%** |
| Southern | 25-15 | **62.5%** |
| Mountain West | 43-26 | **62.3%** |
| United Athletic | 21-13 | **61.8%** |
| Patriot League | 17-12 | **58.6%** |
| Atlantic Coast | 59-44 | **57.3%** |
| Summit League | 16-12 | **57.1%** |
| West Coast | 24-18 | **57.1%** |
| Missouri Valley | 27-22 | **55.1%** |
| Mid-Eastern Athletic | 20-17 | **54.1%** |
| Atlantic 10 | 41-35 | **53.9%** |
| Ohio Valley | 23-20 | **53.5%** |
| Southwestern Athletic | 26-23 | **53.1%** |
| Big 12 | 55-52 | **51.4%** |
| America East | 19-18 | **51.4%** |
| Mid-American | 31-31 | **50.0%** |
| Big East | 31-32 | **49.2%** |
| Conference USA | 26-27 | **49.1%** |
| Big West | 25-26 | **49.0%** |
| Southland | 20-21 | **48.8%** |
| Southeastern | 58-61 | **48.7%** |
| Metro | 22-26 | **45.8%** |
| Sun Belt | 26-32 | **44.8%** |
| Atlantic Sun | 24-30 | **44.4%** |
| Big Ten | 52-67 | **43.7%** |
| Northeast | 12-17 | **41.4%** |
| Coastal Athletic Association | 23-33 | **41.1%** |
| Big Sky | 19-29 | **39.6%** |
| Horizon League | 15-23 | **39.5%** |
| Ivy League | 10-16 | **38.5%** |
| American | 25-42 | **37.3%** |

> *A game counts for a conference if either team is a member.*

#### Combined Statistics

- **Total Predictions**: 1564
- **Overall Winner Accuracy**: 50.6%

#### 📅 Predictions for Today (2026-11-20)

| Matchup | Spread Pick | Total Pick | Confidence |
|---------|-------------|------------|------------|
| Sam Houston St Bearkats @ Boise State Broncos | **HOME** (-12.5) | **UNDER** (170.0) | 95% |
| Eastern Illinois Panthers @ Illinois Fighting Illini | **AWAY** (+47.5) | **UNDER** (165.0) | 94% |
| Loyola (MD) Greyhounds @ Virginia Cavaliers | **AWAY** (+41.5) | **UNDER** (151.5) | 60% |
| Wagner Seahawks @ Maryland Terrapins | **AWAY** (+34.0) | **UNDER** (148.0) | 92% |
| UMKC Kangaroos @ Iona Gaels | **HOME** (-4.5) | **OVER** (140.5) | 52% |
| Le Moyne Dolphins @ Missouri Tigers | **AWAY** (+36.5) | **UNDER** (155.5) | 74% |
| Manhattan Jaspers @ Miami Hurricanes | **AWAY** (+36.0) | **UNDER** (151.0) | 52% |
| Coastal Carolina Chanticleers @ Tennessee Volunteers | **AWAY** (+27.0) | **UNDER** (146.5) | 79% |
| Miss Valley St Delta Devils @ Arkansas Razorbacks | **AWAY** (+38.0) | **OVER** (152.5) | 70% |
| Oakland Golden Grizzlies @ Purdue Boilermakers | **AWAY** (+21.5) | **OVER** (147.0) | 81% |
| Marshall Thundering Herd @ North Carolina Tar Heels | **AWAY** (+19.0) | **OVER** (158.0) | 56% |
| Campbell Fighting Camels @ Kansas St Wildcats | **AWAY** (+17.0) | **OVER** (155.0) | 71% |
| South Alabama Jaguars @ SMU Mustangs | **AWAY** (+15.0) | **OVER** (147.0) | 58% |
| UCF Knights @ Vanderbilt Commodores | **AWAY** (+17.0) | **OVER** (157.0) | 56% |
| Central Michigan Chippewas @ Pittsburgh Panthers | **AWAY** (+21.5) | **UNDER** (144.5) | 61% |
| SE Louisiana Lions @ Kennesaw St Owls | **AWAY** (+11.5) | **UNDER** (155.0) | 76% |
| Tulsa Golden Hurricane @ Mississippi St Bulldogs | **HOME** (-7.0) | **OVER** (152.0) | 73% |
| Murray St Racers @ Wisconsin Badgers | **HOME** (-3.5) | **OVER** (162.0) | 66% |
| East Carolina Pirates @ Utah Valley Wolverines | **HOME** (-4.0) | **OVER** (148.0) | 63% |
| Indiana St Sycamores @ Stephen F. Austin Lumberjacks | **HOME** (-4.0) | **UNDER** (146.0) | 65% |
| Delaware Blue Hens @ CSU Northridge Matadors | **AWAY** (+7.5) | **OVER** (152.0) | 53% |
| Niagara Purple Eagles @ Delaware St Hornets | **HOME** (-1.5) | **UNDER** (134.0) | 66% |
| Georgia Bulldogs @ Georgia Tech Yellow Jackets | **HOME** (+8.0) | **UNDER** (166.0) | 45% |
| Kentucky Wildcats @ Indiana Hoosiers | **HOME** (-3.0) | **UNDER** (153.0) | 55% |
| Bellarmine Knights @ Eastern Kentucky Colonels | **AWAY** (+8.0) | **OVER** (144.0) | 80% |
| NC State Wolfpack @ Seton Hall Pirates | **AWAY** (-3.5) | **OVER** (140.5) | 40% |
| Northwestern Wildcats @ Virginia Tech Hokies | **AWAY** (+11.5) | **UNDER** (143.0) | 36% |
| South Carolina St Bulldogs @ The Citadel Bulldogs | **HOME** (-3.5) | **UNDER** (143.5) | 47% |
| Saint Louis Billikens @ Saint Mary's Gaels | **HOME** (-1.5) | **UNDER** (161.5) | 69% |
| Western Michigan Broncos @ Mt. St. Mary's Mountaineers | **HOME** (+7.0) | **UNDER** (143.0) | 35% |
| Western Illinois Leathernecks @ Albany Great Danes | **AWAY** (+6.5) | **OVER** (138.5) | 27% |
| Alabama St Hornets @ Fresno St Bulldogs | **AWAY** (+8.5) | **UNDER** (146.0) | 43% |
| CSU Bakersfield Roadrunners @ Idaho Vandals | **HOME** (-2.0) | **UNDER** (153.0) | 34% |
| Harvard Crimson @ Holy Cross Crusaders | **HOME** (+12.5) | **UNDER** (137.0) | 43% |
| North Texas Mean Green @ Appalachian St Mountaineers | **HOME** (+2.0) | **OVER** (132.0) | 23% |
| Monmouth Hawks @ Princeton Tigers | **AWAY** (+4.0) | **UNDER** (140.5) | 46% |
| Rhode Island Rams @ Liberty Flames | **HOME** (-1.0) | **UNDER** (141.5) | 47% |
| South Dakota St Jackrabbits @ Idaho State Bengals | **HOME** (+5.5) | **OVER** (143.0) | 28% |
| Dayton Flyers @ Utah Utes | **HOME** (-1.5) | **UNDER** (139.5) | 46% |
| Georgia St Panthers @ Jacksonville St Gamecocks | **HOME** (-1.0) | **OVER** (137.5) | 27% |
| Saint Joseph's Hawks @ Drexel Dragons | **HOME** (+3.5) | **UNDER** (138.5) | 45% |
| Lipscomb Bisons @ Alabama A&M Bulldogs | **HOME** (+4.5) | **UNDER** (149.0) | 25% |
| Iowa Hawkeyes @ Xavier Musketeers | **AWAY** (+3.5) | **OVER** (146.0) | 30% |
| Mercyhurst Lakers @ Canisius Golden Griffins | **HOME** (+3.5) | **UNDER** (136.0) | 6% |
| UT-Arlington Mavericks @ Northwestern St Demons | **HOME** (+3.5) | **UNDER** (145.5) | 51% |
| Western Kentucky Hilltoppers @ Richmond Spiders | **AWAY** (-0.0) | **OVER** (149.0) | 12% |
| Tenn-Martin Skyhawks @ Southern Illinois Salukis | **AWAY** (+2.5) | **UNDER** (149.0) | 51% |

> 📈 *ATS = Against The Spread (with Vegas lines). Updated daily via GitHub Actions.*

<!-- ACCURACY_STATS_END -->

<!-- RANKINGS_START -->

### 🏆 Top 25 Team Rankings

*Updated: November 20, 2026*

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

