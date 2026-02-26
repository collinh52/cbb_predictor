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

**Last Updated**: February 26, 2026 at 12:46 PM

![ATS Accuracy](https://img.shields.io/badge/ATS_Record-50.9%25-yellowgreen)

#### 🏆 Rolling ATS Performance

| Timeframe | ATS Record | Accuracy |
|-----------|------------|----------|
| **Latest** (2026-02-25) | 23-26 | **46.9%** |
| **Last 7 Days** | 158-160 | **49.7%** |
| **Last 30 Days** | 355-343 | **50.9%** |
| **All-Time** | 355-343 | **50.9%** |

**Over/Under Accuracy**: 49.6%

#### 🎯 Accuracy by Confidence (ATS)

| Confidence | Record | Accuracy |
|------------|--------|----------|
| **50%+** | 107-103 | **51.0%** |
| **60%+** | 43-35 | **55.1%** |
| **70%+** | 16-15 | **51.6%** |
| **80%+** | 5-5 | **50.0%** |

#### 🏀 ATS Accuracy by Conference

| Conference | Record | Accuracy |
|------------|--------|----------|
| Western Athletic | 10-3 | **76.9%** |
| Big South | 12-5 | **70.6%** |
| Atlantic 10 | 15-9 | **62.5%** |
| Southeastern | 22-14 | **61.1%** |
| Mountain West | 15-10 | **60.0%** |
| Ohio Valley | 13-9 | **59.1%** |
| Atlantic Coast | 22-16 | **57.9%** |
| Mid-American | 16-12 | **57.1%** |
| Mid-Eastern Athletic | 8-6 | **57.1%** |
| Southern | 13-10 | **56.5%** |
| Ivy League | 5-4 | **55.6%** |
| Summit League | 7-6 | **53.8%** |
| ASUN | 15-13 | **53.6%** |
| Conference USA | 10-9 | **52.6%** |
| Big 12 | 17-16 | **51.5%** |
| Big East | 12-12 | **50.0%** |
| America East | 8-8 | **50.0%** |
| Big Sky | 9-9 | **50.0%** |
| Missouri Valley | 12-13 | **48.0%** |
| Horizon League | 10-11 | **47.6%** |
| Southwestern Athletic | 9-10 | **47.4%** |
| Northeast | 8-9 | **47.1%** |
| Patriot League | 7-8 | **46.7%** |
| Big Ten | 17-20 | **45.9%** |
| American | 12-17 | **41.4%** |
| Coastal Athletic Association | 9-13 | **40.9%** |
| Southland | 8-12 | **40.0%** |
| Sun Belt | 13-21 | **38.2%** |
| Metro Atlantic Athletic | 9-15 | **37.5%** |
| West Coast | 7-12 | **36.8%** |
| Big West | 7-13 | **35.0%** |

> *A game counts for a conference if either team is a member.*

#### Combined Statistics

- **Total Predictions**: 698
- **Overall Winner Accuracy**: 50.9%

#### 📅 Predictions for Today (2026-02-26)

| Matchup | Spread Pick | Total Pick | Confidence |
|---------|-------------|------------|------------|
| South Dakota St Jackrabbits @ UMKC Kangaroos | **AWAY** (-11.5) | **UNDER** (148.5) | 66% |
| Bethune-Cookman Wildcats @ Grambling St Tigers | **AWAY** (-2.0) | **OVER** (142.0) | 62% |
| Tarleton State Texans @ Utah Valley Wolverines | **AWAY** (+17.0) | **UNDER** (142.5) | 74% |
| Chicago St Cougars @ LIU Sharks | **AWAY** (+12.5) | **UNDER** (139.5) | 54% |
| Florida Int'l Golden Panthers @ Sam Houston St Bearkats | **AWAY** (+6.5) | **UNDER** (164.5) | 87% |
| High Point Panthers @ Presbyterian Blue Hose | **HOME** (+11.0) | **OVER** (151.0) | 47% |
| North Carolina A&T Aggies @ UNC Wilmington Seahawks | **AWAY** (+13.5) | **UNDER** (146.5) | 62% |
| Northern Arizona Lumberjacks @ Idaho Vandals | **AWAY** (+10.5) | **UNDER** (146.5) | 54% |
| Michigan St Spartans @ Purdue Boilermakers | **HOME** (-7.5) | **OVER** (141.5) | 47% |
| VMI Keydets @ Samford Bulldogs | **AWAY** (+17.5) | **UNDER** (154.5) | 66% |
| Florida A&M Rattlers @ Southern Jaguars | **AWAY** (+9.5) | **UNDER** (149.0) | 45% |
| Maine Black Bears @ Albany Great Danes | **HOME** (-6.5) | **UNDER** (135.5) | 50% |
| Northeastern Huskies @ William & Mary Tribe | **AWAY** (+11.5) | **UNDER** (164.5) | 52% |
| Elon Phoenix @ Towson Tigers | **HOME** (-5.5) | **UNDER** (144.0) | 43% |
| Sacramento St Hornets @ Montana Grizzlies | **AWAY** (+7.5) | **UNDER** (162.0) | 54% |
| Alcorn St Braves @ Texas Southern Tigers | **AWAY** (+7.5) | **OVER** (149.0) | 42% |
| UC Riverside Highlanders @ UC Santa Barbara Gauchos | **AWAY** (+11.5) | **OVER** (144.0) | 50% |
| Bryant Bulldogs @ UMBC Retrievers | **AWAY** (+9.5) | **OVER** (139.0) | 42% |
| Temple Owls @ Florida Atlantic Owls | **HOME** (-4.5) | **UNDER** (146.0) | 55% |
| Western Illinois Leathernecks @ SIU-Edwardsville Cougars | **AWAY** (+14.5) | **UNDER** (133.5) | 54% |
| Stetson Hatters @ Jacksonville Dolphins | **HOME** (-6.0) | **UNDER** (140.0) | 43% |
| Delaware Blue Hens @ Jacksonville St Gamecocks | **AWAY** (+7.5) | **OVER** (134.0) | 47% |
| Missouri St Bears @ Louisiana Tech Bulldogs | **HOME** (-2.5) | **OVER** (136.5) | 39% |
| Wichita St Shockers @ Memphis Tigers | **HOME** (-1.5) | **UNDER** (146.5) | 58% |
| UTEP Miners @ Middle Tennessee Blue Raiders | **AWAY** (+7.0) | **OVER** (139.5) | 39% |
| South Carolina Upstate Spartans @ Radford Highlanders | **AWAY** (+6.5) | **UNDER** (154.0) | 44% |
| North Dakota St Bison @ St. Thomas (MN) Tommies | **HOME** (-4.0) | **OVER** (154.5) | 41% |
| Mercyhurst Lakers @ Central Connecticut St Blue Devils | **HOME** (-5.0) | **OVER** (138.5) | 61% |
| Tennessee Tech Golden Eagles @ Tenn-Martin Skyhawks | **AWAY** (+8.5) | **UNDER** (134.0) | 56% |
| CSU Bakersfield Roadrunners @ UC San Diego Tritons | **AWAY** (+14.5) | **UNDER** (150.5) | 68% |
| UMass Lowell River Hawks @ Vermont Catamounts | **AWAY** (+10.5) | **OVER** (146.5) | 33% |
| Fairleigh Dickinson Knights @ Le Moyne Dolphins | **AWAY** (+5.0) | **OVER** (139.5) | 34% |
| New Mexico St Aggies @ Western Kentucky Hilltoppers | **AWAY** (+5.5) | **UNDER** (151.0) | 42% |
| Eastern Illinois Panthers @ Lindenwood Lions | **AWAY** (+8.0) | **UNDER** (145.5) | 41% |
| Tennessee St Tigers @ SE Missouri St Redhawks | **HOME** (-3.5) | **UNDER** (155.5) | 49% |
| Stony Brook Seawolves @ Monmouth Hawks | **AWAY** (+4.5) | **UNDER** (143.5) | 34% |
| Long Beach St 49ers @ Cal Poly Mustangs | **AWAY** (+5.0) | **UNDER** (160.0) | 36% |
| Abilene Christian Wildcats @ Utah Tech Trailblazers | **HOME** (-3.5) | **UNDER** (139.5) | 43% |
| UT-Arlington Mavericks @ Cal Baptist Lancers | **AWAY** (+6.5) | **UNDER** (133.5) | 55% |
| UNC Greensboro Spartans @ Chattanooga Mocs | **AWAY** (+4.0) | **OVER** (156.5) | 26% |
| St. Francis (PA) Red Flash @ Stonehill Skyhawks | **AWAY** (+5.5) | **UNDER** (140.5) | 32% |
| Miami (OH) RedHawks @ Western Michigan Broncos | **HOME** (+12.5) | **UNDER** (164.5) | 33% |
| UC Irvine Anteaters @ CSU Northridge Matadors | **HOME** (-1.0) | **UNDER** (154.0) | 39% |
| N Colorado Bears @ Eastern Washington Eagles | **HOME** (+0.0) | **UNDER** (156.0) | 26% |
| Morehead St Eagles @ Arkansas-Little Rock Trojans | **AWAY** (+3.0) | **OVER** (140.5) | 40% |
| Portland St Vikings @ Montana St Bobcats | **HOME** (-2.5) | **UNDER** (140.5) | 42% |
| Jackson St Tigers @ Prairie View Panthers | **AWAY** (+5.5) | **UNDER** (164.5) | 35% |
| Rhode Island Rams @ St. Bonaventure Bonnies | **AWAY** (+2.5) | **UNDER** (145.0) | 22% |
| Liberty Flames @ Kennesaw St Owls | **HOME** (+1.5) | **OVER** (153.5) | 19% |
| Campbell Fighting Camels @ Drexel Dragons | **HOME** (-1.0) | **UNDER** (142.0) | 12% |
| Charleston Cougars @ Hampton Pirates | **HOME** (+5.0) | **UNDER** (140.5) | 30% |
| Denver Pioneers @ Oral Roberts Golden Eagles | **HOME** (+4.5) | **UNDER** (155.5) | 18% |
| Winthrop Eagles @ Charleston Southern Buccaneers | **HOME** (+6.0) | **OVER** (162.5) | 8% |
| New Haven Chargers @ Wagner Seahawks | **AWAY** (+2.0) | **UNDER** (131.5) | 25% |
| UNC Asheville Bulldogs @ Gardner-Webb Bulldogs | **HOME** (+13.5) | **UNDER** (145.5) | 18% |
| Hawai'i Rainbow Warriors @ UC Davis Aggies | **HOME** (+2.0) | **UNDER** (150.0) | 23% |
| New Hampshire Wildcats @ Binghamton Bearcats | **HOME** (+2.0) | **OVER** (141.5) | 12% |
| Florida Gulf Coast Eagles @ North Florida Ospreys | **HOME** (+5.5) | **UNDER** (162.0) | 8% |

> 📈 *ATS = Against The Spread (with Vegas lines). Updated daily via GitHub Actions.*

<!-- ACCURACY_STATS_END -->

<!-- RANKINGS_START -->

### 🏆 Top 25 Team Rankings

*Updated: February 26, 2026*

| Rank | Team | Record | Rating | Off | Def |
|------|------|--------|--------|-----|-----|
| 1 | Michigan Wolverines | 26-2 | +30.6 | 71.9 | 41.2 |
| 2 | Duke Blue Devils | 26-2 | +27.3 | 65.3 | 38.0 |
| 3 | Arizona Wildcats | 26-2 | +27.0 | 68.4 | 41.3 |
| 4 | Illinois Fighting Illini | 22-6 | +26.4 | 67.7 | 41.7 |
| 5 | Louisville Cardinals | 20-8 | +25.7 | 69.2 | 43.9 |
| 6 | Alabama Crimson Tide | 21-7 | +25.0 | 73.4 | 48.7 |
| 7 | Iowa State Cyclones | 24-4 | +24.8 | 65.3 | 40.5 |
| 8 | Florida Gators | 22-6 | +24.6 | 65.9 | 41.6 |
| 9 | Gonzaga Bulldogs | 28-2 | +24.6 | 65.6 | 41.0 |
| 10 | Purdue Boilermakers | 22-5 | +24.5 | 66.2 | 41.7 |
| 11 | Arkansas Razorbacks | 21-7 | +24.5 | 71.1 | 46.6 |
| 12 | Vanderbilt Commodores | 22-6 | +23.3 | 67.6 | 44.4 |
| 13 | BYU Cougars | 20-8 | +23.2 | 68.9 | 45.9 |
| 14 | UConn Huskies | 26-3 | +23.1 | 62.7 | 39.7 |
| 15 | Houston Cougars | 23-5 | +22.8 | 60.3 | 37.5 |
| 16 | Texas Tech Red Raiders | 21-7 | +22.4 | 65.3 | 42.9 |
| 17 | Michigan State Spartans | 22-5 | +22.3 | 61.9 | 39.6 |
| 18 | Kansas Jayhawks | 21-7 | +22.3 | 62.9 | 40.7 |
| 19 | Tennessee Volunteers | 20-8 | +21.8 | 62.8 | 41.3 |
| 20 | St. John's Red Storm | 22-6 | +21.3 | 64.2 | 42.9 |
| 21 | Nebraska Cornhuskers | 24-4 | +21.2 | 61.5 | 40.3 |
| 22 | NC State Wolfpack | 19-9 | +21.2 | 66.2 | 45.3 |
| 23 | Virginia Cavaliers | 25-3 | +21.2 | 63.7 | 42.6 |
| 24 | Kentucky Wildcats | 18-10 | +21.1 | 64.2 | 43.5 |
| 25 | Georgia Bulldogs | 19-9 | +21.1 | 69.0 | 48.3 |

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

