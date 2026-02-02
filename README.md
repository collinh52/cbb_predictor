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

**Last Updated**: January 14, 2026 at 03:57 PM

![ATS Accuracy](https://img.shields.io/badge/ATS_Record-100.0%25-brightgreen)

#### 🏆 Rolling ATS Performance

| Timeframe | ATS Record | Accuracy |
|-----------|------------|----------|
| **Last 7 Days** | 0-0 | **0.0%** |
| **Last 30 Days** | 1-0 | **100.0%** |
| **All-Time** | 1-0 | **100.0%** |

#### 🎯 Accuracy by Confidence (ATS)

| Confidence | Record | Accuracy |
|------------|--------|----------|
| **50%+** | 1-0 | **100.0%** |

#### Straight-Up Predictions (Games Without Vegas Lines)

| **7-Day** | 0/0 (0.0%) |
| **30-Day** | 1/3 (33.3%) |
| **All-Time** | 1/3 (33.3%) |

#### Combined Statistics

- **Total Predictions**: 4
- **Overall Winner Accuracy**: 50.0%

#### 📅 Predictions for 2026-01-31

| Matchup | Spread Pick | Total Pick | Confidence |
|---------|-------------|------------|------------|
| NJIT Highlanders @ Vermont Catamounts | **AWAY** (+13.0) | **UNDER** (139.0) | 95% |
| UConn Huskies @ Creighton Bluejays | **HOME** (-7.5) | **UNDER** (142.5) | 95% |
| Tenn-Martin Skyhawks @ Western Illinois Leathernecks | **HOME** (-9.5) | **UNDER** (137.5) | 95% |
| Norfolk St Spartans @ Howard Bison | **AWAY** (+6.5) | **UNDER** (146.0) | 95% |
| Hampton Pirates @ Towson Tigers | **AWAY** (+22.5) | **UNDER** (139.5) | 94% |
| Austin Peay Governors @ West Georgia Wolves | **HOME** (-7.5) | **UNDER** (150.5) | 94% |
| New Haven Chargers @ St. Francis (PA) Red Flash | **HOME** (+1.0) | **UNDER** (131.5) | 94% |
| Idaho Vandals @ Northern Arizona Lumberjacks | **HOME** (-5.5) | **UNDER** (146.0) | 94% |
| North Carolina Tar Heels @ Georgia Tech Yellow Jackets | **HOME** (-18.5) | **UNDER** (174.5) | 93% |
| Queens University Royals @ Bellarmine Knights | **HOME** (-3.5) | **UNDER** (161.5) | 93% |
| Texas A&M Aggies @ Georgia Bulldogs | **HOME** (-12.5) | - | 91% |
| North Dakota St Bison @ South Dakota Coyotes | **HOME** (-8.0) | **UNDER** (153.5) | 93% |
| SIU-Edwardsville Cougars @ Southern Indiana Screaming Eagles | **HOME** (-2.5) | **UNDER** (132.5) | 93% |
| Ohio Bobcats @ Buffalo Bulls | **HOME** (-13.5) | **UNDER** (158.5) | 92% |
| Purdue Boilermakers @ Maryland Terrapins | **HOME** (-14.5) | **UNDER** (150.5) | 92% |
| UT Rio Grande Valley Vaqueros @ Incarnate Word Cardinals | **HOME** (-3.0) | **UNDER** (141.0) | 91% |
| Fresno St Bulldogs @ Air Force Falcons | **HOME** (-8.5) | **UNDER** (141.0) | 91% |
| Bowling Green Falcons @ Central Michigan Chippewas | **HOME** (-9.0) | **UNDER** (150.0) | 89% |
| Bethune-Cookman Wildcats @ Alabama St Hornets | **HOME** (-2.5) | **UNDER** (153.5) | 88% |
| Iowa State Cyclones @ Kansas St Wildcats | **HOME** (-12.0) | **UNDER** (155.5) | 88% |
| New Mexico Lobos @ San José St Spartans | **HOME** (-15.0) | **UNDER** (149.0) | 87% |
| Hawai'i Rainbow Warriors @ Long Beach St 49ers | **HOME** (-8.5) | **UNDER** (145.0) | 87% |
| Nicholls St Colonels @ East Texas A&M Lions | **AWAY** (+2.5) | **UNDER** (146.5) | 86% |
| Saint Peter's Peacocks @ Rider Broncs | **HOME** (-8.0) | **UNDER** (135.0) | 85% |
| Montana Grizzlies @ Sacramento St Hornets | **HOME** (-4.0) | **UNDER** (156.0) | 84% |
| Southern Jaguars @ Alcorn St Braves | **HOME** (-7.5) | **UNDER** (148.0) | 84% |
| Minnesota Golden Gophers @ Penn State Nittany Lions | **HOME** (-1.0) | **UNDER** (141.5) | 83% |
| Lipscomb Bisons @ North Florida Ospreys | **HOME** (+1.5) | **UNDER** (171.5) | 83% |
| Southern Utah Thunderbirds @ Abilene Christian Wildcats | **AWAY** (+6.5) | **UNDER** (151.0) | 83% |
| Valparaiso Beacons @ Indiana St Sycamores | **HOME** (-2.5) | - | 71% |
| Stanford Cardinal @ Florida St Seminoles | **HOME** (+2.5) | **UNDER** (150.5) | 82% |
| Siena Saints @ Canisius Golden Griffins | **HOME** (-9.0) | **UNDER** (130.0) | 82% |
| Robert Morris Colonials @ Fort Wayne Mastodons | **AWAY** (+10.5) | - | 68% |
| Grambling St Tigers @ Jackson St Tigers | **HOME** (-2.5) | **UNDER** (148.5) | 81% |
| UC San Diego Tritons @ CSU Northridge Matadors | **HOME** (-2.5) | **UNDER** (160.0) | 81% |
| Ole Miss Rebels @ Vanderbilt Commodores | **HOME** (+10.5) | **UNDER** (150.5) | 81% |
| Jacksonville St Gamecocks @ Missouri St Bears | **HOME** (+4.5) | **UNDER** (135.5) | 80% |
| Arizona Wildcats @ Arizona St Sun Devils | **HOME** (-11.5) | **UNDER** (160.5) | 80% |
| Boston Univ. Terriers @ Bucknell Bison | **HOME** (+3.5) | **UNDER** (135.5) | 80% |
| Ohio State Buckeyes @ Wisconsin Badgers | **HOME** (+7.5) | **UNDER** (174.5) | 80% |
| SMU Mustangs @ Louisville Cardinals | **HOME** (+4.5) | **UNDER** (178.5) | 80% |
| DePaul Blue Demons @ Xavier Musketeers | **HOME** (+0.5) | - | 65% |
| Princeton Tigers @ Columbia Lions | **HOME** (+5.5) | **UNDER** (140.5) | 79% |
| Houston Christian Huskies @ Texas A&M-CC Islanders | **AWAY** (+8.5) | **UNDER** (134.5) | 79% |
| Holy Cross Crusaders @ Army Knights | **HOME** (+1.5) | **UNDER** (138.5) | 79% |
| Louisiana Tech Bulldogs @ Sam Houston St Bearkats | **HOME** (+8.5) | **UNDER** (141.0) | 78% |
| Eastern Kentucky Colonels @ Central Arkansas Bears | **HOME** (+6.0) | **UNDER** (152.0) | 78% |
| New Hampshire Wildcats @ Bryant Bulldogs | **HOME** (-1.0) | **UNDER** (132.0) | 77% |
| Eastern Michigan Eagles @ Massachusetts Minutemen | **AWAY** (+8.0) | **UNDER** (148.0) | 77% |
| Rhode Island Rams @ Duquesne Dukes | **HOME** (+3.0) | **UNDER** (144.5) | 77% |
| Fordham Rams @ GW Revolutionaries | **HOME** (+4.5) | **UNDER** (143.5) | 76% |
| UAB Blazers @ North Texas Mean Green | **AWAY** (+1.0) | **UNDER** (140.5) | 76% |
| Colorado St Rams @ Wyoming Cowboys | **HOME** (+1.0) | **UNDER** (138.5) | 75% |
| Idaho State Bengals @ Weber State Wildcats | **HOME** (+2.5) | **UNDER** (151.0) | 75% |
| Northern Illinois Huskies @ Miami (OH) RedHawks | **AWAY** (+17.0) | **UNDER** (156.5) | 75% |
| Fairleigh Dickinson Knights @ Wagner Seahawks | **HOME** (-2.5) | - | 54% |
| Florida Gulf Coast Eagles @ Jacksonville Dolphins | **AWAY** (+1.0) | **UNDER** (136.5) | 74% |
| Saint Mary's Gaels @ Gonzaga Bulldogs | **HOME** (+8.5) | **UNDER** (144.5) | 74% |
| Texas Southern Tigers @ Prairie View Panthers | **AWAY** (-0.0) | **UNDER** (158.5) | 74% |
| North Carolina A&T Aggies @ Drexel Dragons | **AWAY** (+9.5) | **UNDER** (122.5) | 73% |
| Kentucky Wildcats @ Arkansas Razorbacks | **HOME** (+6.5) | **UNDER** (161.5) | 73% |
| Wright St Raiders @ Green Bay Phoenix | **HOME** (-5.0) | **UNDER** (146.0) | 73% |
| Santa Clara Broncos @ Loyola Marymount Lions | **HOME** (-9.5) | **UNDER** (153.0) | 72% |
| Oregon St Beavers @ San Diego Toreros | **HOME** (+2.5) | **UNDER** (151.0) | 72% |
| Georgia St Panthers @ South Alabama Jaguars | **AWAY** (+5.0) | **UNDER** (138.5) | 72% |
| George Mason Patriots @ St. Bonaventure Bonnies | **HOME** (+1.0) | **UNDER** (142.0) | 71% |
| Loyola (MD) Greyhounds @ Navy Midshipmen | **AWAY** (+10.0) | **UNDER** (144.0) | 71% |
| Arkansas-Pine Bluff Golden Lions @ Miss Valley St Delta Devils | **AWAY** (-10.0) | **UNDER** (143.5) | 70% |
| Alabama Crimson Tide @ Florida Gators | **HOME** (+6.5) | **UNDER** (172.5) | 70% |
| Manhattan Jaspers @ Mt. St. Mary's Mountaineers | **AWAY** (+6.5) | **UNDER** (148.5) | 70% |
| Florida A&M Rattlers @ Alabama A&M Bulldogs | **HOME** (+3.0) | **UNDER** (139.0) | 69% |
| UC Davis Aggies @ CSU Bakersfield Roadrunners | **HOME** (-5.5) | **UNDER** (154.5) | 69% |
| Hofstra Pride @ Monmouth Hawks | **HOME** (-5.5) | **UNDER** (144.5) | 69% |
| Wichita St Shockers @ Tulsa Golden Hurricane | **HOME** (+6.5) | **UNDER** (152.0) | 69% |
| SE Missouri St Redhawks @ Eastern Illinois Panthers | **HOME** (-4.5) | **UNDER** (138.0) | 69% |
| LSU Tigers @ South Carolina Gamecocks | **HOME** (+1.5) | **UNDER** (173.5) | 68% |
| Rutgers Scarlet Knights @ USC Trojans | **AWAY** (+12.5) | **UNDER** (146.5) | 67% |
| Maine Black Bears @ UMass Lowell River Hawks | **HOME** (+12.5) | **UNDER** (150.5) | 67% |
| San Diego St Aztecs @ Utah State Aggies | **HOME** (+4.5) | **UNDER** (140.5) | 66% |
| Davidson Wildcats @ Richmond Spiders | **HOME** (+1.0) | **UNDER** (139.5) | 66% |
| McNeese Cowboys @ Lamar Cardinals | **HOME** (-10.0) | **UNDER** (143.5) | 65% |
| Baylor Bears @ West Virginia Mountaineers | **AWAY** (+2.5) | **UNDER** (138.5) | 65% |
| Western Kentucky Hilltoppers @ Middle Tennessee Blue Raiders | **AWAY** (+7.0) | **UNDER** (138.0) | 64% |
| New Mexico St Aggies @ Kennesaw St Owls | **HOME** (+2.0) | **UNDER** (159.0) | 63% |
| Mercyhurst Lakers @ Chicago St Cougars | **HOME** (+2.5) | **UNDER** (133.5) | 62% |
| Lindenwood Lions @ Morehead St Eagles | **HOME** (+1.0) | **UNDER** (150.0) | 62% |
| Georgia Southern Eagles @ Louisiana Ragin' Cajuns | **AWAY** (-3.0) | **UNDER** (144.0) | 62% |
| Sacred Heart Pioneers @ Merrimack Warriors | **AWAY** (+6.5) | **UNDER** (146.0) | 61% |
| James Madison Dukes @ Southern Miss Golden Eagles | **AWAY** (+1.5) | **UNDER** (143.0) | 61% |
| Cal Baptist Lancers @ UT-Arlington Mavericks | **HOME** (-1.0) | **UNDER** (134.5) | 60% |
| Omaha Mavericks @ Denver Pioneers | **HOME** (+2.0) | **UNDER** (157.0) | 60% |
| Murray St Racers @ Belmont Bruins | **HOME** (+3.0) | **UNDER** (166.0) | 59% |
| Washington Huskies @ Northwestern Wildcats | **HOME** (+1.5) | **UNDER** (146.5) | 59% |
| Chattanooga Mocs @ Furman Paladins | **AWAY** (+8.5) | **UNDER** (141.0) | 59% |
| Indiana Hoosiers @ UCLA Bruins | **AWAY** (+4.5) | **UNDER** (142.5) | 59% |
| Quinnipiac Bobcats @ Fairfield Stags | **HOME** (-2.0) | **UNDER** (152.0) | 59% |
| LIU Sharks @ Central Connecticut St Blue Devils | **AWAY** (-4.5) | **UNDER** (148.5) | 59% |
| Pacific Tigers @ San Francisco Dons | **HOME** (+5.5) | **UNDER** (136.0) | 58% |
| Montana St Bobcats @ Portland St Vikings | **AWAY** (+4.5) | **UNDER** (140.0) | 58% |
| Texas Longhorns @ Oklahoma Sooners | **HOME** (+1.5) | **UNDER** (144.5) | 58% |
| Oral Roberts Golden Eagles @ South Dakota St Jackrabbits | **AWAY** (+13.5) | **UNDER** (151.5) | 58% |
| Harvard Crimson @ Yale Bulldogs | **HOME** (+12.5) | **UNDER** (142.5) | 58% |
| Cal Poly Mustangs @ UC Riverside Highlanders | **AWAY** (+1.5) | **UNDER** (160.5) | 58% |
| Saint Joseph's Hawks @ La Salle Explorers | **HOME** (-2.5) | **UNDER** (145.5) | 58% |
| UIC Flames @ Southern Illinois Salukis | **AWAY** (+3.5) | **UNDER** (143.5) | 58% |
| Delaware Blue Hens @ UTEP Miners | **HOME** (+5.0) | **UNDER** (128.5) | 58% |
| California Golden Bears @ Miami Hurricanes | **AWAY** (+11.5) | **UNDER** (148.5) | 57% |
| South Florida Bulls @ Temple Owls | **HOME** (-9.5) | **UNDER** (155.0) | 57% |
| Marist Red Foxes @ Niagara Purple Eagles | **HOME** (-10.0) | **UNDER** (127.5) | 57% |
| Pennsylvania Quakers @ Cornell Big Red | **AWAY** (+7.0) | **UNDER** (174.5) | 57% |
| Morgan St Bears @ Coppin St Eagles | **AWAY** (-2.5) | **UNDER** (154.5) | 57% |
| BYU Cougars @ Kansas Jayhawks | **AWAY** (+3.5) | **UNDER** (157.5) | 56% |
| Notre Dame Fighting Irish @ Syracuse Orange | **HOME** (+4.5) | **UNDER** (147.5) | 56% |
| Northwestern St Demons @ New Orleans Privateers | **AWAY** (+5.0) | **UNDER** (153.0) | 56% |
| Utah Tech Trailblazers @ Tarleton State Texans | **AWAY** (+1.0) | **UNDER** (148.0) | 55% |
| Eastern Washington Eagles @ N Colorado Bears | **AWAY** (+6.0) | **UNDER** (157.0) | 55% |
| TCU Horned Frogs @ Colorado Buffaloes | **AWAY** (-2.0) | **UNDER** (153.5) | 55% |
| Dartmouth Big Green @ Brown Bears | **AWAY** (+1.5) | **UNDER** (143.0) | 55% |
| High Point Panthers @ Longwood Lancers | **HOME** (-9.0) | **UNDER** (157.0) | 55% |
| Mississippi St Bulldogs @ Missouri Tigers | **AWAY** (+6.5) | **UNDER** (148.5) | 54% |
| Maryland-Eastern Shore Hawks @ Delaware St Hornets | **HOME** (-2.0) | **UNDER** (128.0) | 54% |
| North Alabama Lions @ Stetson Hatters | **AWAY** (-3.5) | **UNDER** (138.5) | 53% |
| Virginia Cavaliers @ Boston College Eagles | **AWAY** (-8.5) | **UNDER** (143.5) | 52% |
| SE Louisiana Lions @ Stephen F. Austin Lumberjacks | **AWAY** (+11.0) | **UNDER** (136.5) | 52% |
| Marshall Thundering Herd @ Arkansas St Red Wolves | **HOME** (+4.0) | **UNDER** (165.5) | 52% |
| Old Dominion Monarchs @ Texas State Bobcats | **AWAY** (+7.5) | **UNDER** (153.5) | 52% |
| Lafayette Leopards @ American Eagles | **HOME** (+6.5) | **UNDER** (135.5) | 52% |
| UMBC Retrievers @ Albany Great Danes | **AWAY** (-2.5) | **UNDER** (141.0) | 52% |
| Portland Pilots @ Washington St Cougars | **AWAY** (+8.5) | **UNDER** (152.5) | 51% |
| Arkansas-Little Rock Trojans @ Tennessee Tech Golden Eagles | **HOME** (-2.5) | **UNDER** (141.5) | 51% |
| Appalachian St Mountaineers @ Troy Trojans | **HOME** (+8.0) | **UNDER** (137.0) | 51% |
| VMI Keydets @ Mercer Bears | **AWAY** (+15.5) | **UNDER** (162.5) | 51% |
| Charleston Cougars @ Northeastern Huskies | **HOME** (-2.5) | **UNDER** (163.5) | 50% |
| Colgate Raiders @ Lehigh Mountain Hawks | **AWAY** (-1.5) | **UNDER** (142.5) | 50% |
| Evansville Purple Aces @ Northern Iowa Panthers | **HOME** (+11.0) | **UNDER** (128.5) | 50% |
| CSU Fullerton Titans @ UC Santa Barbara Gauchos | **AWAY** (+8.5) | **UNDER** (153.5) | 50% |
| Oklahoma St Cowboys @ Utah Utes | **AWAY** (+1.5) | **UNDER** (167.5) | 49% |
| Auburn Tigers @ Tennessee Volunteers | **HOME** (+5.5) | **UNDER** (147.5) | 49% |
| Bradley Braves @ Drake Bulldogs | **AWAY** (+1.5) | **UNDER** (151.5) | 48% |
| Radford Highlanders @ Presbyterian Blue Hose | **AWAY** (+2.5) | **UNDER** (149.5) | 48% |

> 📈 *ATS = Against The Spread (with Vegas lines). Updated daily via GitHub Actions.*

<!-- ACCURACY_STATS_END -->

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

