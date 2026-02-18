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

**Last Updated**: February 18, 2026 at 06:00 PM

![ATS Accuracy](https://img.shields.io/badge/ATS_Record-49.5%25-yellow)

#### 🏆 Rolling ATS Performance

| Timeframe | ATS Record | Accuracy |
|-----------|------------|----------|
| **Latest** (2026-02-16) | 9-12 | **42.9%** |
| **Last 7 Days** | 146-149 | **49.5%** |
| **Last 30 Days** | 146-149 | **49.5%** |
| **All-Time** | 146-149 | **49.5%** |

**Over/Under Accuracy**: 46.8%

#### 🎯 Accuracy by Confidence (ATS)

| Confidence | Record | Accuracy |
|------------|--------|----------|
| **50%+** | 45-36 | **55.6%** |
| **60%+** | 17-12 | **58.6%** |
| **70%+** | 7-6 | **53.8%** |
| **80%+** | 3-1 | **75.0%** |

#### 🏀 ATS Accuracy by Conference

| Conference | Record | Accuracy |
|------------|--------|----------|
| Western Athletic | 6-1 | **85.7%** |
| Southeastern | 9-3 | **75.0%** |
| Big South | 6-2 | **75.0%** |
| Southern | 7-3 | **70.0%** |
| Ohio Valley | 7-3 | **70.0%** |
| America East | 5-3 | **62.5%** |
| Mid-Eastern Athletic | 5-3 | **62.5%** |
| Missouri Valley | 6-4 | **60.0%** |
| Ivy League | 3-2 | **60.0%** |
| Southwestern Athletic | 6-4 | **60.0%** |
| Big 12 | 6-5 | **54.5%** |
| American | 7-6 | **53.8%** |
| Atlantic Coast | 8-7 | **53.3%** |
| Mid-American | 5-5 | **50.0%** |
| West Coast | 4-4 | **50.0%** |
| Horizon League | 4-4 | **50.0%** |
| Big West | 5-5 | **50.0%** |
| Southland | 5-5 | **50.0%** |
| Coastal Athletic Association | 5-6 | **45.5%** |
| Patriot League | 3-4 | **42.9%** |
| Atlantic 10 | 3-4 | **42.9%** |
| ASUN | 5-7 | **41.7%** |
| Conference USA | 4-6 | **40.0%** |
| Sun Belt | 6-9 | **40.0%** |
| Big East | 3-5 | **37.5%** |
| Summit League | 2-4 | **33.3%** |
| Big Sky | 3-6 | **33.3%** |
| Mountain West | 2-5 | **28.6%** |
| Metro Atlantic Athletic | 3-9 | **25.0%** |
| Big Ten | 3-10 | **23.1%** |
| Northeast | 1-7 | **12.5%** |

> *A game counts for a conference if either team is a member.*

#### Combined Statistics

- **Total Predictions**: 295
- **Overall Winner Accuracy**: 49.5%

#### 📅 Predictions for Today (2026-02-18)

| Matchup | Spread Pick | Total Pick | Confidence |
|---------|-------------|------------|------------|
| Saint Mary's Gaels @ Seattle Redhawks | **AWAY** (-10.0) | **UNDER** (136.5) | 48% |
| Lehigh Mountain Hawks @ Navy Midshipmen | **HOME** (-10.0) | **OVER** (140.0) | 71% |
| BYU Cougars @ Arizona Wildcats | **HOME** (-11.5) | **UNDER** (165.5) | 64% |
| Creighton Bluejays @ UConn Huskies | **AWAY** (+17.5) | **OVER** (142.5) | 52% |
| Middle Tennessee Blue Raiders @ Sam Houston St Bearkats | **AWAY** (+5.5) | **UNDER** (152.5) | 75% |
| Charlotte 49ers @ Tulsa Golden Hurricane | **AWAY** (+13.0) | **OVER** (149.5) | 60% |
| Utah Utes @ West Virginia Mountaineers | **HOME** (-10.0) | **UNDER** (131.0) | 60% |
| Ole Miss Rebels @ Texas A&M Aggies | **HOME** (-9.5) | **UNDER** (154.5) | 56% |
| Boise State Broncos @ Utah State Aggies | **HOME** (-9.5) | **OVER** (152.5) | 74% |
| Oklahoma Sooners @ Tennessee Volunteers | **AWAY** (+10.5) | **OVER** (149.5) | 51% |
| Gonzaga Bulldogs @ San Francisco Dons | **HOME** (+14.5) | **OVER** (149.5) | 47% |
| Richmond Spiders @ Davidson Wildcats | **HOME** (-5.5) | **OVER** (141.5) | 48% |
| Cleveland St Vikings @ Youngstown St Penguins | **AWAY** (+10.5) | **OVER** (157.0) | 48% |
| Illinois Fighting Illini @ USC Trojans | **HOME** (+9.5) | **UNDER** (151.5) | 44% |
| DePaul Blue Demons @ Seton Hall Pirates | **AWAY** (+8.5) | **UNDER** (131.5) | 69% |
| La Salle Explorers @ Duquesne Dukes | **AWAY** (+11.0) | **UNDER** (144.5) | 46% |
| UNC Greensboro Spartans @ Western Carolina Catamounts | **HOME** (-5.0) | **OVER** (155.5) | 61% |
| Jacksonville St Gamecocks @ Louisiana Tech Bulldogs | **HOME** (-2.5) | **UNDER** (132.5) | 51% |
| VMI Keydets @ Wofford Terriers | **AWAY** (+13.5) | **UNDER** (154.5) | 43% |
| Maryland Terrapins @ Northwestern Wildcats | **AWAY** (+8.0) | **UNDER** (143.5) | 60% |
| Troy Trojans @ UL Monroe Warhawks | **HOME** (+16.0) | **UNDER** (153.0) | 56% |
| Murray St Racers @ Illinois St Redbirds | **HOME** (-2.5) | **UNDER** (156.5) | 38% |
| Virginia Cavaliers @ Georgia Tech Yellow Jackets | **HOME** (+13.5) | **UNDER** (147.5) | 39% |
| Rutgers Scarlet Knights @ Penn State Nittany Lions | **HOME** (-4.5) | **UNDER** (148.5) | 37% |
| North Dakota St Bison @ South Dakota St Jackrabbits | **HOME** (+0.0) | **UNDER** (147.0) | 36% |
| St. John's Red Storm @ Marquette Golden Eagles | **HOME** (+9.5) | **UNDER** (157.5) | 53% |
| Queens University Royals @ North Alabama Lions | **HOME** (+8.5) | **OVER** (155.0) | 34% |
| Fort Wayne Mastodons @ Northern Kentucky Norse | **AWAY** (+6.0) | **UNDER** (151.5) | 57% |
| Jacksonville Dolphins @ Florida Gulf Coast Eagles | **AWAY** (+6.5) | **UNDER** (136.5) | 34% |
| West Georgia Wolves @ Eastern Kentucky Colonels | **AWAY** (+5.5) | **OVER** (156.0) | 25% |
| Saint Joseph's Hawks @ St. Bonaventure Bonnies | **AWAY** (+4.0) | **UNDER** (147.0) | 38% |
| Northern Iowa Panthers @ Indiana St Sycamores | **HOME** (+4.5) | **UNDER** (136.5) | 30% |
| Arkansas Razorbacks @ Alabama Crimson Tide | **AWAY** (+3.5) | **UNDER** (183.5) | 55% |
| Oral Roberts Golden Eagles @ Omaha Mavericks | **AWAY** (+9.5) | **UNDER** (151.0) | 36% |
| Loyola (Chi) Ramblers @ Fordham Rams | **AWAY** (+8.5) | **UNDER** (138.0) | 49% |
| Wichita St Shockers @ East Carolina Pirates | **HOME** (+7.5) | **UNDER** (145.0) | 27% |
| Pepperdine Waves @ Portland Pilots | **AWAY** (+6.5) | **UNDER** (150.5) | 35% |
| Butler Bulldogs @ Georgetown Hoyas | **AWAY** (+6.5) | **OVER** (145.5) | 21% |
| Southern Illinois Salukis @ Drake Bulldogs | **HOME** (+1.5) | **UNDER** (149.5) | 49% |
| Lafayette Leopards @ Holy Cross Crusaders | **HOME** (-1.5) | **UNDER** (137.5) | 26% |
| UIC Flames @ Evansville Purple Aces | **HOME** (+8.0) | **UNDER** (139.0) | 41% |
| Army Knights @ Loyola (MD) Greyhounds | **AWAY** (+5.0) | **OVER** (147.0) | 42% |
| Colorado St Rams @ UNLV Rebels | **AWAY** (+1.5) | **UNDER** (149.5) | 17% |
| Dayton Flyers @ George Mason Patriots | **AWAY** (+1.5) | **UNDER** (136.5) | 31% |
| Kennesaw St Owls @ Missouri St Bears | **AWAY** (+2.0) | **OVER** (153.5) | 18% |
| Vanderbilt Commodores @ Missouri Tigers | **HOME** (+4.5) | **UNDER** (153.5) | 18% |
| Pacific Tigers @ Washington St Cougars | **AWAY** (+1.5) | **OVER** (144.5) | 10% |
| Bradley Braves @ Valparaiso Beacons | **HOME** (+2.0) | **OVER** (142.0) | 18% |
| Clemson Tigers @ Wake Forest Demon Deacons | **HOME** (+3.5) | **UNDER** (138.5) | 18% |
| Auburn Tigers @ Mississippi St Bulldogs | **HOME** (+4.5) | **UNDER** (154.5) | 13% |
| Kansas Jayhawks @ Oklahoma St Cowboys | **HOME** (+5.5) | **UNDER** (156.5) | 23% |
| James Madison Dukes @ Coastal Carolina Chanticleers | **HOME** (+1.0) | **OVER** (141.5) | 8% |
| East Tennessee St Buccaneers @ Furman Paladins | **HOME** (+0.0) | **UNDER** (141.0) | 11% |
| Florida Atlantic Owls @ UTSA Roadrunners | **HOME** (+12.5) | **UNDER** (157.5) | 16% |
| Lipscomb Bisons @ Bellarmine Knights | **HOME** (+3.0) | **UNDER** (158.5) | 10% |
| Western Kentucky Hilltoppers @ Delaware Blue Hens | **HOME** (+4.0) | **UNDER** (141.0) | 18% |
| American Eagles @ Bucknell Bison | **HOME** (+2.5) | **OVER** (139.0) | 4% |
| North Carolina Central Eagles @ South Carolina St Bulldogs | **HOME** (+3.0) | **UNDER** (140.0) | 50% |
| UAB Blazers @ Temple Owls | **HOME** (+0.0) | **UNDER** (146.0) | 21% |

> 📈 *ATS = Against The Spread (with Vegas lines). Updated daily via GitHub Actions.*

<!-- ACCURACY_STATS_END -->

<!-- RANKINGS_START -->

### 🏆 Top 25 Team Rankings

*Updated: February 18, 2026*

| Rank | Team | Record | Rating | Off | Def |
|------|------|--------|--------|-----|-----|
| 1 | Michigan Wolverines | 25-1 | +31.2 | 72.2 | 41.0 |
| 2 | Arizona Wildcats | 23-2 | +27.4 | 69.1 | 41.6 |
| 3 | Duke Blue Devils | 24-2 | +27.0 | 65.4 | 38.4 |
| 4 | Louisville Cardinals | 19-7 | +26.5 | 69.9 | 43.8 |
| 5 | Illinois Fighting Illini | 21-5 | +25.9 | 67.0 | 41.4 |
| 6 | Iowa State Cyclones | 23-3 | +25.5 | 66.3 | 40.8 |
| 7 | Gonzaga Bulldogs | 25-2 | +24.5 | 66.0 | 41.5 |
| 8 | Alabama Crimson Tide | 18-7 | +24.4 | 72.7 | 48.4 |
| 9 | Arkansas Razorbacks | 19-6 | +24.3 | 70.2 | 45.9 |
| 10 | Florida Gators | 20-6 | +24.3 | 65.3 | 41.4 |
| 11 | Vanderbilt Commodores | 21-4 | +23.8 | 68.3 | 44.4 |
| 12 | Purdue Boilermakers | 21-5 | +23.8 | 65.5 | 41.7 |
| 13 | Houston Cougars | 23-3 | +23.5 | 60.7 | 37.2 |
| 14 | BYU Cougars | 19-6 | +22.9 | 69.0 | 46.0 |
| 15 | UConn Huskies | 24-2 | +22.6 | 62.6 | 40.0 |
| 16 | Michigan State Spartans | 21-5 | +22.4 | 62.3 | 39.9 |
| 17 | Kansas Jayhawks | 19-6 | +22.4 | 62.8 | 40.5 |
| 18 | St. John's Red Storm | 20-5 | +22.3 | 65.6 | 43.3 |
| 19 | NC State Wolfpack | 19-8 | +22.3 | 67.0 | 45.0 |
| 20 | Tennessee Volunteers | 18-7 | +21.9 | 63.4 | 41.8 |
| 21 | Texas Tech Red Raiders | 19-7 | +21.7 | 64.4 | 42.7 |
| 22 | Kentucky Wildcats | 17-9 | +21.5 | 65.0 | 43.8 |
| 23 | Nebraska Cornhuskers | 22-4 | +21.2 | 61.3 | 40.1 |
| 24 | Saint Louis Billikens | 24-2 | +20.9 | 67.1 | 46.2 |
| 25 | Georgia Bulldogs | 18-8 | +20.8 | 68.9 | 48.5 |

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

