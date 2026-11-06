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

**Last Updated**: November 06, 2026 at 06:43 PM

![ATS Accuracy](https://img.shields.io/badge/ATS_Record-50.4%25-yellowgreen)

#### 🏆 Rolling ATS Performance

| Timeframe | ATS Record | Accuracy |
|-----------|------------|----------|
| **Latest** (2026-11-05) | 2-1 | **66.7%** |
| **Last 7 Days** | 5-8 | **38.5%** |
| **Last 30 Days** | 5-8 | **38.5%** |
| **All-Time** | 768-758 | **50.4%** |

**Over/Under Accuracy**: 50.9%

#### 🎯 Accuracy by Confidence (ATS)

| Confidence | Record | Accuracy |
|------------|--------|----------|
| **50%+** | 243-242 | **50.1%** |
| **60%+** | 107-100 | **51.7%** |
| **70%+** | 32-37 | **46.4%** |
| **80%+** | 7-11 | **38.9%** |

#### 🏀 ATS Accuracy by Conference

| Conference | Record | Accuracy |
|------------|--------|----------|
| Big South | 27-8 | **77.1%** |
| Southern | 25-15 | **62.5%** |
| Mountain West | 41-25 | **62.1%** |
| Summit League | 16-10 | **61.5%** |
| United Athletic | 20-13 | **60.6%** |
| Patriot League | 16-11 | **59.3%** |
| Mid-Eastern Athletic | 20-14 | **58.8%** |
| Atlantic Coast | 57-42 | **57.6%** |
| Missouri Valley | 27-22 | **55.1%** |
| Atlantic 10 | 40-34 | **54.1%** |
| Ohio Valley | 22-19 | **53.7%** |
| America East | 19-17 | **52.8%** |
| West Coast | 20-18 | **52.6%** |
| Mid-American | 31-29 | **51.7%** |
| Southwestern Athletic | 24-23 | **51.1%** |
| Big East | 31-32 | **49.2%** |
| Big 12 | 49-51 | **49.0%** |
| Big West | 24-25 | **49.0%** |
| Southland | 19-20 | **48.7%** |
| Southeastern | 54-58 | **48.2%** |
| Atlantic Sun | 24-27 | **47.1%** |
| Conference USA | 22-27 | **44.9%** |
| Metro | 21-26 | **44.7%** |
| Big Ten | 49-65 | **43.0%** |
| Sun Belt | 24-32 | **42.9%** |
| Coastal Athletic Association | 23-32 | **41.8%** |
| Northeast | 12-17 | **41.4%** |
| Horizon League | 15-23 | **39.5%** |
| Ivy League | 10-16 | **38.5%** |
| American | 25-41 | **37.9%** |
| Big Sky | 15-27 | **35.7%** |

> *A game counts for a conference if either team is a member.*

#### Combined Statistics

- **Total Predictions**: 1526
- **Overall Winner Accuracy**: 50.4%

#### 📅 Predictions for Today (2026-11-06)

| Matchup | Spread Pick | Total Pick | Confidence |
|---------|-------------|------------|------------|
| St. Thomas (MN) Tommies @ Minnesota Golden Gophers | **HOME** (-15.5) | **UNDER** (147.0) | 89% |
| West Florida Argonauts @ Florida Int'l Golden Panthers | **HOME** (-16.5) | **UNDER** (161.5) | 85% |
| Nicholls St Colonels @ UAB Blazers | **HOME** (-15.5) | **UNDER** (155.5) | 84% |
| Southern Miss Golden Eagles @ Iowa State Cyclones | **AWAY** (+30.0) | **UNDER** (149.0) | 72% |
| Wagner Seahawks @ Miami Hurricanes | **AWAY** (+38.5) | **UNDER** (146.5) | 71% |
| Eastern Illinois Panthers @ Iowa Hawkeyes | **AWAY** (+35.5) | **UNDER** (136.5) | 59% |
| Middle Tennessee Blue Raiders @ Kansas Jayhawks | **AWAY** (+27.0) | **UNDER** (150.5) | 75% |
| North Florida Ospreys @ UCLA Bruins | **AWAY** (+33.5) | **OVER** (156.5) | 50% |
| Holy Cross Crusaders @ Villanova Wildcats | **AWAY** (+33.5) | **UNDER** (151.5) | 79% |
| Miss Valley St Delta Devils @ Oklahoma Sooners | **AWAY** (+41.5) | **UNDER** (152.5) | 69% |
| James Madison Dukes @ Kentucky Wildcats | **AWAY** (+24.0) | **UNDER** (156.0) | 75% |
| Omaha Mavericks @ BYU Cougars | **AWAY** (+29.0) | **UNDER** (160.5) | 74% |
| Southern Illinois Salukis @ UMKC Kangaroos | **AWAY** (-4.0) | **UNDER** (145.5) | 92% |
| Arkansas-Pine Bluff Golden Lions @ Baylor Bears | **AWAY** (+37.5) | **UNDER** (161.5) | 59% |
| Delaware Blue Hens @ Wisconsin Badgers | **AWAY** (+24.5) | **OVER** (152.5) | 50% |
| Northern Kentucky Norse @ Texas A&M Aggies | **AWAY** (+25.0) | **UNDER** (166.5) | 57% |
| Texas Southern Tigers @ LSU Tigers | **AWAY** (+36.5) | **UNDER** (162.5) | 70% |
| Arkansas St Red Wolves @ Alabama Crimson Tide | **AWAY** (+25.5) | **OVER** (168.5) | 71% |
| Presbyterian Blue Hose @ Georgia Bulldogs | **AWAY** (+24.5) | **UNDER** (156.5) | 50% |
| New Haven Chargers @ Rutgers Scarlet Knights | **AWAY** (+24.5) | **UNDER** (138.5) | 69% |
| Detroit Mercy Titans @ Marquette Golden Eagles | **AWAY** (+30.5) | **UNDER** (154.0) | 80% |
| Stetson Hatters @ West Virginia Mountaineers | **AWAY** (+27.5) | **UNDER** (141.5) | 82% |
| N Colorado Bears @ Arizona St Sun Devils | **AWAY** (+15.0) | **UNDER** (150.0) | 48% |
| Southern Jaguars @ TCU Horned Frogs | **AWAY** (+27.5) | **UNDER** (152.5) | 54% |
| Wofford Terriers @ North Carolina Tar Heels | **AWAY** (+23.0) | **OVER** (154.5) | 50% |
| Coppin St Eagles @ George Mason Patriots | **AWAY** (+27.5) | **UNDER** (140.5) | 85% |
| Stony Brook Seawolves @ Northwestern Wildcats | **AWAY** (+14.0) | **UNDER** (144.0) | 70% |
| Idaho State Bengals @ Wyoming Cowboys | **AWAY** (+19.0) | **UNDER** (147.0) | 52% |
| Eastern Michigan Eagles @ Xavier Musketeers | **AWAY** (+21.5) | **UNDER** (154.0) | 49% |
| Troy Trojans @ Florida St Seminoles | **AWAY** (+19.5) | **UNDER** (154.5) | 65% |
| East Tennessee St Buccaneers @ NC State Wolfpack | **AWAY** (+15.0) | **OVER** (152.5) | 54% |
| Queens University Royals @ Oklahoma St Cowboys | **AWAY** (+18.5) | **UNDER** (178.5) | 54% |
| Idaho Vandals @ Colorado St Rams | **AWAY** (+16.0) | **UNDER** (148.0) | 81% |
| Cal Baptist Lancers @ Oregon St Beavers | **AWAY** (+16.0) | **UNDER** (151.0) | 91% |
| CSU Northridge Matadors @ Kansas St Wildcats | **HOME** (-10.0) | **OVER** (159.0) | 73% |
| American Eagles @ Clemson Tigers | **AWAY** (+15.5) | **UNDER** (141.5) | 85% |
| Central Arkansas Bears @ Ole Miss Rebels | **AWAY** (+19.0) | **OVER** (150.5) | 53% |
| Robert Morris Colonials @ UIC Flames | **AWAY** (+11.0) | **UNDER** (143.5) | 71% |
| Yale Bulldogs @ UCF Knights | **AWAY** (+10.0) | **OVER** (151.5) | 55% |
| Oakland Golden Grizzlies @ Stanford Cardinal | **AWAY** (+14.5) | **OVER** (150.0) | 59% |
| Georgia Southern Eagles @ Georgia Tech Yellow Jackets | **AWAY** (+16.0) | **OVER** (154.5) | 53% |
| Tarleton State Texans @ San Diego Toreros | **HOME** (-6.0) | **UNDER** (150.0) | 60% |
| Indiana St Sycamores @ Ball State Cardinals | **HOME** (-4.0) | **UNDER** (145.0) | 71% |
| Florida Atlantic Owls @ Wright St Raiders | **HOME** (-3.0) | **UNDER** (155.5) | 58% |
| North Dakota St Bison @ San Francisco Dons | **AWAY** (+7.0) | **UNDER** (146.5) | 43% |
| Loyola (MD) Greyhounds @ Mt. St. Mary's Mountaineers | **AWAY** (+6.5) | **UNDER** (149.5) | 52% |
| Missouri Tigers @ Saint Louis Billikens | **HOME** (+3.0) | **UNDER** (163.0) | 63% |
| Austin Peay Governors @ Kennesaw St Owls | **AWAY** (+6.0) | **UNDER** (157.0) | 33% |
| Boston Univ. Terriers @ Brown Bears | **HOME** (-2.5) | **UNDER** (146.5) | 43% |
| UConn Huskies @ Michigan Wolverines | **HOME** (+5.5) | **UNDER** (146.5) | 51% |
| South Carolina St Bulldogs @ South Carolina Upstate Spartans | **AWAY** (+3.5) | **UNDER** (148.5) | 62% |
| Texas A&M-CC Islanders @ Louisiana Ragin' Cajuns | **AWAY** (+3.5) | **OVER** (129.5) | 30% |
| Portland Pilots @ UT-Arlington Mavericks | **AWAY** (-1.5) | **UNDER** (149.0) | 62% |
| UNC Greensboro Spartans @ Elon Phoenix | **AWAY** (+7.0) | **UNDER** (154.5) | 5% |

> 📈 *ATS = Against The Spread (with Vegas lines). Updated daily via GitHub Actions.*

<!-- ACCURACY_STATS_END -->

<!-- RANKINGS_START -->

### 🏆 Top 25 Team Rankings

*Updated: November 06, 2026*

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

