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

**Last Updated**: March 08, 2026 at 05:06 AM

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

#### 📅 Recent Predictions (2026-03-07)

| Matchup | Spread Pick | Total Pick | Confidence |
|---------|-------------|------------|------------|
| Seattle Redhawks @ Pacific Tigers | **HOME** (-1.5) | **OVER** (129.5) | 66% |
| Sam Houston St Bearkats @ Liberty Flames | **HOME** (-4.5) | **UNDER** (156.0) | 83% |
| North Carolina Tar Heels @ Duke Blue Devils | **AWAY** (+17.5) | **UNDER** (146.5) | 68% |
| Arizona St Sun Devils @ Iowa State Cyclones | **AWAY** (+15.5) | **UNDER** (148.5) | 68% |
| Wagner Seahawks @ LIU Sharks | **AWAY** (+8.5) | **UNDER** (140.5) | 60% |
| UNC Asheville Bulldogs @ High Point Panthers | **HOME** (-10.5) | **UNDER** (149.5) | 55% |
| Virginia Tech Hokies @ Virginia Cavaliers | **HOME** (-11.5) | **UNDER** (144.5) | 55% |
| Utah Utes @ Baylor Bears | **AWAY** (+12.5) | **UNDER** (149.5) | 65% |
| Stanford Cardinal @ NC State Wolfpack | **HOME** (-8.5) | **UNDER** (152.5) | 54% |
| Long Beach St 49ers @ Hawai'i Rainbow Warriors | **AWAY** (+13.5) | **OVER** (150.0) | 50% |
| Princeton Tigers @ Yale Bulldogs | **AWAY** (+14.0) | **UNDER** (136.0) | 49% |
| Kansas St Wildcats @ Kansas Jayhawks | **AWAY** (+16.5) | **UNDER** (155.5) | 79% |
| North Dakota Fighting Hawks @ St. Thomas (MN) Tommies | **AWAY** (+12.5) | **OVER** (154.5) | 54% |
| Omaha Mavericks @ North Dakota St Bison | **HOME** (-6.5) | **OVER** (141.5) | 65% |
| Xavier Musketeers @ Villanova Wildcats | **AWAY** (+11.5) | **OVER** (153.5) | 58% |
| Georgia Tech Yellow Jackets @ Clemson Tigers | **AWAY** (+17.5) | **UNDER** (143.5) | 60% |
| Fresno St Bulldogs @ Grand Canyon Antelopes | **AWAY** (+13.0) | **UNDER** (146.5) | 77% |
| New Hampshire Wildcats @ UMBC Retrievers | **AWAY** (+12.5) | **UNDER** (138.0) | 47% |
| Auburn Tigers @ Alabama Crimson Tide | **AWAY** (+8.5) | **UNDER** (176.5) | 59% |
| Wisconsin Badgers @ Purdue Boilermakers | **AWAY** (+8.5) | **OVER** (155.5) | 53% |
| Air Force Falcons @ Nevada Wolf Pack | **AWAY** (+25.0) | **UNDER** (142.5) | 50% |
| The Citadel Bulldogs @ East Tennessee St Buccaneers | **AWAY** (+14.5) | **OVER** (138.5) | 51% |
| Florida Atlantic Owls @ Wichita St Shockers | **AWAY** (+7.5) | **UNDER** (150.0) | 51% |
| UC Davis Aggies @ UC Irvine Anteaters | **AWAY** (+9.0) | **UNDER** (146.0) | 75% |
| New Mexico Lobos @ Utah State Aggies | **AWAY** (+7.5) | **UNDER** (156.5) | 50% |
| Presbyterian Blue Hose @ Winthrop Eagles | **AWAY** (+7.5) | **OVER** (145.5) | 48% |
| Florida Gulf Coast Eagles @ Central Arkansas Bears | **HOME** (-5.5) | **OVER** (145.5) | 54% |
| Saint Louis Billikens @ George Mason Patriots | **HOME** (+7.5) | **UNDER** (148.5) | 64% |
| Maine Black Bears @ NJIT Highlanders | **HOME** (-4.0) | **OVER** (132.5) | 47% |
| Houston Cougars @ Oklahoma St Cowboys | **HOME** (+12.5) | **OVER** (148.5) | 45% |
| Sacramento St Hornets @ Idaho Vandals | **AWAY** (+6.5) | **UNDER** (159.0) | 48% |
| Morehead St Eagles @ Tennessee St Tigers | **HOME** (-3.5) | **OVER** (149.5) | 53% |
| Bryant Bulldogs @ Vermont Catamounts | **AWAY** (+13.0) | **OVER** (134.0) | 38% |
| Drake Bulldogs @ UIC Flames | **HOME** (-5.5) | **OVER** (141.5) | 54% |
| Oklahoma Sooners @ Texas Longhorns | **AWAY** (+7.5) | **OVER** (154.5) | 42% |
| Southern Miss Golden Eagles @ Appalachian St Mountaineers | **HOME** (-3.5) | **UNDER** (136.5) | 46% |
| California Golden Bears @ Wake Forest Demon Deacons | **AWAY** (+5.5) | **UNDER** (150.5) | 37% |
| Arizona Wildcats @ Colorado Buffaloes | **HOME** (+14.5) | **UNDER** (155.5) | 54% |
| Albany Great Danes @ UMass Lowell River Hawks | **HOME** (-2.5) | **UNDER** (148.0) | 42% |
| Richmond Spiders @ Duquesne Dukes | **HOME** (-5.0) | **OVER** (149.5) | 38% |
| La Salle Explorers @ Saint Joseph's Hawks | **AWAY** (+10.0) | **UNDER** (141.0) | 69% |
| UConn Huskies @ Marquette Golden Eagles | **HOME** (+9.5) | **UNDER** (143.5) | 48% |
| Vanderbilt Commodores @ Tennessee Volunteers | **HOME** (-4.5) | **UNDER** (147.5) | 46% |
| Elon Phoenix @ William & Mary Tribe | **AWAY** (+5.0) | **UNDER** (164.0) | 47% |
| Pittsburgh Panthers @ Syracuse Orange | **AWAY** (+6.5) | **OVER** (141.5) | 34% |
| Hampton Pirates @ Towson Tigers | **AWAY** (+6.0) | **UNDER** (131.5) | 46% |
| CSU Bakersfield Roadrunners @ Cal Poly Mustangs | **AWAY** (+9.5) | **UNDER** (173.0) | 56% |
| GW Revolutionaries @ Loyola (Chi) Ramblers | **HOME** (+10.0) | **UNDER** (152.0) | 44% |
| Florida Gators @ Kentucky Wildcats | **HOME** (+6.5) | **UNDER** (160.5) | 58% |
| CSU Fullerton Titans @ CSU Northridge Matadors | **AWAY** (+5.0) | **UNDER** (170.5) | 42% |
| Portland Pilots @ San Francisco Dons | **AWAY** (+4.5) | **OVER** (144.5) | 29% |
| Stonehill Skyhawks @ Mercyhurst Lakers | **AWAY** (+6.0) | **OVER** (133.0) | 50% |
| Furman Paladins @ Samford Bulldogs | **HOME** (-1.5) | **UNDER** (146.5) | 39% |
| Northwestern Wildcats @ Minnesota Golden Gophers | **HOME** (-3.0) | **UNDER** (133.0) | 36% |
| Utah Valley Wolverines @ Utah Tech Trailblazers | **HOME** (+6.5) | **UNDER** (148.0) | 25% |
| Washington Huskies @ Oregon Ducks | **HOME** (-1.5) | **UNDER** (141.5) | 51% |
| Kennesaw St Owls @ New Mexico St Aggies | **HOME** (-2.5) | **OVER** (155.0) | 27% |
| Queens University Royals @ Austin Peay Governors | **HOME** (-1.5) | **OVER** (161.5) | 33% |
| Indiana Hoosiers @ Ohio State Buckeyes | **AWAY** (+4.5) | **UNDER** (148.5) | 29% |
| UC San Diego Tritons @ UC Santa Barbara Gauchos | **HOME** (+0.0) | **UNDER** (139.5) | 39% |
| Northeastern Huskies @ Drexel Dragons | **AWAY** (+4.5) | **UNDER** (139.5) | 23% |
| Mt. St. Mary's Mountaineers @ Siena Saints | **AWAY** (+3.5) | **OVER** (131.5) | 33% |
| Texas Tech Red Raiders @ BYU Cougars | **HOME** (-1.5) | **UNDER** (159.5) | 26% |
| UNC Greensboro Spartans @ Wofford Terriers | **AWAY** (+3.5) | **OVER** (155.5) | 50% |
| Providence Friars @ Georgetown Hoyas | **HOME** (-1.5) | **OVER** (156.5) | 32% |
| Boise State Broncos @ Colorado St Rams | **HOME** (-1.5) | **OVER** (143.5) | 22% |
| Northern Arizona Lumberjacks @ Idaho State Bengals | **AWAY** (+4.5) | **OVER** (142.0) | 22% |
| Rhode Island Rams @ Fordham Rams | **HOME** (-1.0) | **UNDER** (134.5) | 52% |
| UCLA Bruins @ USC Trojans | **HOME** (+6.5) | **OVER** (150.5) | 19% |
| SMU Mustangs @ Florida St Seminoles | **HOME** (-1.5) | **OVER** (159.5) | 19% |
| UT-Arlington Mavericks @ Abilene Christian Wildcats | **HOME** (-1.0) | **UNDER** (134.5) | 48% |
| Western Carolina Catamounts @ Mercer Bears | **HOME** (-2.0) | **OVER** (155.5) | 29% |
| South Carolina Gamecocks @ Ole Miss Rebels | **AWAY** (+6.5) | **OVER** (146.5) | 16% |
| Butler Bulldogs @ DePaul Blue Demons | **AWAY** (+2.5) | **UNDER** (142.5) | 33% |
| Jacksonville St Gamecocks @ UTEP Miners | **HOME** (+1.5) | **UNDER** (139.5) | 27% |
| Middle Tennessee Blue Raiders @ Missouri St Bears | **HOME** (-1.0) | **OVER** (145.0) | 32% |
| Cornell Big Red @ Dartmouth Big Green | **HOME** (+5.0) | **UNDER** (166.0) | 25% |
| Georgia Bulldogs @ Mississippi St Bulldogs | **HOME** (+5.5) | **UNDER** (163.5) | 16% |
| Western Kentucky Hilltoppers @ Florida Int'l Golden Panthers | **HOME** (+1.0) | **UNDER** (160.0) | 10% |
| Notre Dame Fighting Irish @ Boston College Eagles | **HOME** (+1.5) | **UNDER** (142.5) | 17% |
| Northern Iowa Panthers @ Bradley Braves | **HOME** (+4.5) | **OVER** (127.5) | 37% |
| Cal Baptist Lancers @ Southern Utah Thunderbirds | **HOME** (+6.0) | **UNDER** (146.5) | 9% |
| Louisiana Tech Bulldogs @ Delaware Blue Hens | **HOME** (+2.0) | **OVER** (133.0) | 22% |
| Georgia Southern Eagles @ Coastal Carolina Chanticleers | **AWAY** (+1.5) | **UNDER** (150.5) | 16% |
| Cincinnati Bearcats @ TCU Horned Frogs | **AWAY** (+1.5) | **UNDER** (139.5) | 12% |
| Wyoming Cowboys @ San José St Spartans | **HOME** (+6.5) | **UNDER** (148.5) | 12% |
| Marist Red Foxes @ Quinnipiac Bobcats | **AWAY** (+1.0) | **OVER** (130.5) | 9% |
| Louisville Cardinals @ Miami Hurricanes | **AWAY** (+1.5) | **UNDER** (156.5) | 11% |
| Davidson Wildcats @ St. Bonaventure Bonnies | **AWAY** (+3.0) | **OVER** (142.0) | 9% |
| Campbell Fighting Camels @ Stony Brook Seawolves | **HOME** (+3.0) | **UNDER** (147.0) | 3% |
| Texas A&M Aggies @ LSU Tigers | **HOME** (+3.5) | **UNDER** (159.5) | 4% |

> 📈 *ATS = Against The Spread (with Vegas lines). Updated daily via GitHub Actions.*

<!-- ACCURACY_STATS_END -->

<!-- RANKINGS_START -->

### 🏆 Top 25 Team Rankings

*Updated: March 08, 2026*

| Rank | Team | Record | Rating | Off | Def |
|------|------|--------|--------|-----|-----|
| 1 | Michigan Wolverines | 28-2 | +30.5 | 71.6 | 41.0 |
| 2 | Duke Blue Devils | 29-2 | +28.0 | 65.4 | 37.4 |
| 3 | Arizona Wildcats | 28-3 | +27.1 | 67.0 | 39.9 |
| 4 | Illinois Fighting Illini | 23-7 | +26.7 | 67.7 | 41.4 |
| 5 | Florida Gators | 25-6 | +26.2 | 67.8 | 41.9 |
| 6 | Louisville Cardinals | 22-9 | +25.2 | 68.8 | 44.0 |
| 7 | Iowa State Cyclones | 25-6 | +24.7 | 65.0 | 40.6 |
| 8 | Alabama Crimson Tide | 23-8 | +24.5 | 72.8 | 48.3 |
| 9 | Purdue Boilermakers | 23-8 | +24.4 | 66.3 | 42.2 |
| 10 | Gonzaga Bulldogs | 28-3 | +24.2 | 65.2 | 41.0 |
| 11 | Arkansas Razorbacks | 23-8 | +24.0 | 71.3 | 47.3 |
| 12 | Houston Cougars | 26-5 | +23.3 | 60.8 | 37.5 |
| 13 | Vanderbilt Commodores | 24-7 | +22.8 | 67.6 | 44.7 |
| 14 | UConn Huskies | 27-4 | +22.7 | 62.7 | 40.0 |
| 15 | Texas Tech Red Raiders | 22-8 | +22.4 | 65.2 | 42.8 |
| 16 | BYU Cougars | 20-10 | +22.2 | 68.2 | 46.3 |
| 17 | Kansas Jayhawks | 22-9 | +22.1 | 63.3 | 41.2 |
| 18 | St. John's Red Storm | 25-6 | +22.1 | 64.7 | 42.6 |
| 19 | Michigan State Spartans | 25-5 | +22.1 | 62.2 | 40.1 |
| 20 | Tennessee Volunteers | 21-10 | +22.0 | 62.7 | 41.1 |
| 21 | Wisconsin Badgers | 22-9 | +21.5 | 67.7 | 46.2 |
| 22 | Georgia Bulldogs | 22-9 | +21.5 | 69.5 | 48.3 |
| 23 | Kentucky Wildcats | 19-12 | +21.4 | 64.7 | 43.7 |
| 24 | Nebraska Cornhuskers | 25-5 | +21.1 | 61.3 | 40.2 |
| 25 | Ohio State Buckeyes | 20-11 | +20.7 | 65.3 | 44.8 |

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

