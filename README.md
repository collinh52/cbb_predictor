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

**Last Updated**: February 12, 2026 at 03:15 AM

![ATS Accuracy](https://img.shields.io/badge/ATS_Record-60.4%25-brightgreen)

#### 🏆 Rolling ATS Performance

| Timeframe | ATS Record | Accuracy |
|-----------|------------|----------|
| **Yesterday** (2026-02-10) | 8-13 | **38.1%** |
| **Last 7 Days** | 201-93 | **68.4%** |
| **Last 30 Days** | 324-212 | **60.4%** |
| **All-Time** | 324-212 | **60.4%** |

**Over/Under Accuracy**: 49.8%

#### 🎯 Accuracy by Confidence (ATS)

| Confidence | Record | Accuracy |
|------------|--------|----------|
| **50%+** | 176-118 | **59.9%** |
| **60%+** | 106-75 | **58.6%** |
| **70%+** | 61-43 | **58.7%** |
| **80%+** | 34-20 | **63.0%** |

#### 🏀 ATS Accuracy by Conference

| Conference | Record | Accuracy |
|------------|--------|----------|
| Western Athletic | 7-1 | **87.5%** |
| America East | 9-2 | **81.8%** |
| Southland | 16-5 | **76.2%** |
| Northeast | 9-3 | **75.0%** |
| Mid-Eastern Athletic | 9-3 | **75.0%** |
| Ohio Valley | 9-3 | **75.0%** |
| Big West | 8-3 | **72.7%** |
| Sun Belt | 20-9 | **69.0%** |
| Atlantic 10 | 15-7 | **68.2%** |
| Coastal Athletic Association | 12-6 | **66.7%** |
| Atlantic Coast | 22-11 | **66.7%** |
| Southern | 14-7 | **66.7%** |
| Conference USA | 10-5 | **66.7%** |
| Big South | 7-4 | **63.6%** |
| Southwestern Athletic | 12-7 | **63.2%** |
| Summit League | 7-5 | **58.3%** |
| Horizon League | 7-5 | **58.3%** |
| Southeastern | 15-11 | **57.7%** |
| West Coast | 9-7 | **56.2%** |
| ASUN | 13-11 | **54.2%** |
| Big Ten | 14-12 | **53.8%** |
| Mid-American | 15-13 | **53.6%** |
| Big 12 | 15-13 | **53.6%** |
| Mountain West | 9-8 | **52.9%** |
| American | 9-8 | **52.9%** |
| Big Sky | 8-8 | **50.0%** |
| Ivy League | 3-3 | **50.0%** |
| Metro Atlantic Athletic | 9-10 | **47.4%** |
| Patriot League | 5-6 | **45.5%** |
| Big East | 8-10 | **44.4%** |
| Missouri Valley | 8-12 | **40.0%** |

> *A game counts for a conference if either team is a member.*

#### Straight-Up Predictions (Games Without Vegas Lines)

| **7-Day** | 0/0 (0.0%) |
| **30-Day** | 1/3 (33.3%) |
| **All-Time** | 1/3 (33.3%) |

#### Combined Statistics

- **Total Predictions**: 539
- **Overall Winner Accuracy**: 60.3%

#### 📅 Recent Predictions (2026-02-11)

| Matchup | Spread Pick | Total Pick | Confidence |
|---------|-------------|------------|------------|
| Seattle Redhawks @ Santa Clara Broncos | **HOME** (-13.5) | **OVER** (146.0) | 62% |
| Pepperdine Waves @ Saint Mary's Gaels | **HOME** (-24.5) | **UNDER** (141.5) | 60% |
| UL Monroe Warhawks @ Arkansas St Red Wolves | **HOME** (-19.5) | **UNDER** (160.5) | 87% |
| UAB Blazers @ Tulsa Golden Hurricane | **HOME** (-10.5) | **UNDER** (160.5) | 54% |
| Chattanooga Mocs @ East Tennessee St Buccaneers | **HOME** (-11.0) | **UNDER** (144.5) | 57% |
| Missouri Tigers @ Texas A&M Aggies | **HOME** (-7.5) | **UNDER** (157.5) | 50% |
| Bellarmine Knights @ Central Arkansas Bears | **HOME** (-8.0) | **OVER** (152.5) | 66% |
| Colorado Buffaloes @ Texas Tech Red Raiders | **HOME** (-14.0) | **UNDER** (156.5) | 60% |
| Michigan Wolverines @ Northwestern Wildcats | **AWAY** (-15.5) | **UNDER** (153.0) | 64% |
| Furman Paladins @ Mercer Bears | **HOME** (-2.5) | **UNDER** (152.0) | 54% |
| Eastern Kentucky Colonels @ Lipscomb Bisons | **HOME** (-6.5) | **OVER** (161.0) | 56% |
| USC Trojans @ Ohio State Buckeyes | **HOME** (-8.0) | **OVER** (152.0) | 44% |
| Virginia Tech Hokies @ Clemson Tigers | **HOME** (-9.0) | **UNDER** (138.0) | 54% |
| North Florida Ospreys @ Florida Gulf Coast Eagles | **HOME** (-12.5) | **UNDER** (164.0) | 46% |
| Eastern Michigan Eagles @ Kent State Golden Flashes | **HOME** (-10.5) | **UNDER** (144.5) | 44% |
| UTEP Miners @ Jacksonville St Gamecocks | **HOME** (-7.0) | **UNDER** (131.5) | 41% |
| Penn State Nittany Lions @ Washington Huskies | **HOME** (-13.0) | **UNDER** (155.0) | 59% |
| Loyola Marymount Lions @ Pacific Tigers | **HOME** (-6.0) | **UNDER** (140.5) | 44% |
| The Citadel Bulldogs @ Western Carolina Catamounts | **HOME** (-7.5) | **OVER** (146.0) | 49% |
| California Golden Bears @ Syracuse Orange | **HOME** (-5.5) | **UNDER** (149.0) | 50% |
| Portland Pilots @ San Diego Toreros | **HOME** (-2.5) | **OVER** (154.0) | 38% |
| Austin Peay Governors @ Queens University Royals | **HOME** (-1.5) | **UNDER** (161.0) | 52% |
| Wofford Terriers @ Samford Bulldogs | **HOME** (-4.5) | **UNDER** (151.0) | 41% |
| VCU Rams @ La Salle Explorers | **AWAY** (-12.5) | **UNDER** (147.5) | 50% |
| Florida Gators @ Georgia Bulldogs | **AWAY** (-9.5) | **UNDER** (167.0) | 49% |
| Bowling Green Falcons @ Northern Illinois Huskies | **AWAY** (-7.0) | **UNDER** (143.0) | 45% |
| Boston Univ. Terriers @ Army Knights | **HOME** (+3.5) | **OVER** (142.5) | 69% |
| Providence Friars @ Seton Hall Pirates | **HOME** (-4.5) | **OVER** (150.0) | 38% |
| Buffalo Bulls @ Ball State Cardinals | **HOME** (+1.0) | **UNDER** (141.5) | 31% |
| American Eagles @ Lehigh Mountain Hawks | **AWAY** (-1.5) | **OVER** (138.5) | 37% |
| Alabama Crimson Tide @ Ole Miss Rebels | **AWAY** (-7.0) | **UNDER** (165.0) | 54% |
| UConn Huskies @ Butler Bulldogs | **AWAY** (-11.5) | **OVER** (145.0) | 24% |
| VMI Keydets @ UNC Greensboro Spartans | **HOME** (-9.0) | **UNDER** (150.0) | 29% |
| Appalachian St Mountaineers @ Georgia Southern Eagles | **AWAY** (-3.0) | **UNDER** (143.0) | 55% |
| North Dakota Fighting Hawks @ South Dakota Coyotes | **HOME** (-2.0) | **OVER** (156.5) | 36% |
| Loyola (MD) Greyhounds @ Lafayette Leopards | **HOME** (-3.0) | **UNDER** (145.5) | 22% |
| Toledo Rockets @ Western Michigan Broncos | **HOME** (+6.0) | **UNDER** (156.0) | 35% |
| Tennessee Volunteers @ Mississippi St Bulldogs | **AWAY** (-7.0) | **UNDER** (148.5) | 30% |
| Creighton Bluejays @ DePaul Blue Demons | **HOME** (-1.0) | **UNDER** (143.0) | 34% |
| West Georgia Wolves @ North Alabama Lions | **HOME** (-1.0) | **OVER** (145.0) | 16% |
| Temple Owls @ Tulane Green Wave | **HOME** (+0.0) | **UNDER** (145.0) | 29% |
| South Florida Bulls @ Wichita St Shockers | **HOME** (-1.0) | **UNDER** (160.0) | 16% |
| New Mexico Lobos @ Grand Canyon Antelopes | **HOME** (-1.0) | **UNDER** (151.0) | 35% |
| Troy Trojans @ Texas State Bobcats | **AWAY** (-5.5) | **OVER** (140.5) | 19% |
| Marshall Thundering Herd @ Old Dominion Monarchs | **AWAY** (-2.5) | **UNDER** (154.5) | 22% |
| Iowa Hawkeyes @ Maryland Terrapins | **AWAY** (-10.5) | **UNDER** (140.5) | 20% |
| Stanford Cardinal @ Boston College Eagles | **AWAY** (-2.0) | **UNDER** (139.5) | 35% |
| Colgate Raiders @ Holy Cross Crusaders | **AWAY** (-6.5) | **UNDER** (142.5) | 15% |
| Jacksonville Dolphins @ Stetson Hatters | **AWAY** (-1.0) | **OVER** (137.5) | 28% |
| UTSA Roadrunners @ East Carolina Pirates | **HOME** (-11.0) | **UNDER** (149.5) | 24% |
| Liberty Flames @ New Mexico St Aggies | **HOME** (+3.5) | **OVER** (142.5) | 15% |
| Wake Forest Demon Deacons @ Georgia Tech Yellow Jackets | **AWAY** (-2.5) | **UNDER** (159.5) | 14% |
| Cincinnati Bearcats @ Kansas St Wildcats | **HOME** (+2.0) | **UNDER** (149.0) | 31% |
| Florida Atlantic Owls @ Rice Owls | **AWAY** (-3.0) | **OVER** (151.5) | 3% |

> 📈 *ATS = Against The Spread (with Vegas lines). Updated daily via GitHub Actions.*

<!-- ACCURACY_STATS_END -->

<!-- RANKINGS_START -->

### 🏆 Top 25 Team Rankings

*Updated: February 12, 2026*

| Rank | Team | Record | Rating | Off | Def |
|------|------|--------|--------|-----|-----|
| 1 | Michigan Wolverines | 22-1 | +30.8 | 72.0 | 41.1 |
| 2 | Arizona Wildcats | 23-1 | +27.7 | 69.4 | 41.7 |
| 3 | Louisville Cardinals | 18-6 | +27.0 | 70.2 | 43.6 |
| 4 | Duke Blue Devils | 22-2 | +26.0 | 64.5 | 38.5 |
| 5 | Illinois Fighting Illini | 20-5 | +25.3 | 67.1 | 42.0 |
| 6 | Iowa State Cyclones | 21-3 | +24.7 | 65.8 | 41.2 |
| 7 | Alabama Crimson Tide | 17-7 | +24.5 | 72.6 | 48.3 |
| 8 | Florida Gators | 18-6 | +24.4 | 65.2 | 41.1 |
| 9 | Gonzaga Bulldogs | 24-2 | +24.4 | 65.7 | 41.3 |
| 10 | Purdue Boilermakers | 20-4 | +23.9 | 65.8 | 41.9 |
| 11 | Arkansas Razorbacks | 18-6 | +23.8 | 70.0 | 46.1 |
| 12 | Vanderbilt Commodores | 20-4 | +23.7 | 68.4 | 44.7 |
| 13 | Houston Cougars | 22-2 | +23.6 | 60.8 | 37.2 |
| 14 | BYU Cougars | 18-6 | +23.1 | 68.7 | 45.8 |
| 15 | UConn Huskies | 23-2 | +22.8 | 62.6 | 39.8 |
| 16 | Kansas Jayhawks | 19-5 | +22.7 | 63.3 | 40.6 |
| 17 | St. John's Red Storm | 19-5 | +22.4 | 66.1 | 43.7 |
| 18 | Tennessee Volunteers | 16-7 | +22.2 | 63.6 | 41.9 |
| 19 | Texas Tech Red Raiders | 18-6 | +21.7 | 64.6 | 42.9 |
| 20 | Michigan State Spartans | 20-4 | +21.7 | 61.3 | 39.7 |
| 21 | Kentucky Wildcats | 17-7 | +21.7 | 64.9 | 43.6 |
| 22 | NC State Wolfpack | 18-7 | +21.5 | 66.9 | 45.7 |
| 23 | Saint Louis Billikens | 23-1 | +21.5 | 67.5 | 46.0 |
| 24 | Georgia Bulldogs | 17-7 | +21.2 | 69.5 | 48.7 |
| 25 | Nebraska Cornhuskers | 21-3 | +21.0 | 61.5 | 40.8 |

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

