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

**Last Updated**: November 02, 2026 at 09:08 PM

![ATS Accuracy](https://img.shields.io/badge/ATS_Record-50.5%25-yellowgreen)

#### 🏆 Rolling ATS Performance

| Timeframe | ATS Record | Accuracy |
|-----------|------------|----------|
| **Latest** (2026-11-01) | 0-1 | **0.0%** |
| **Last 7 Days** | 0-1 | **0.0%** |
| **Last 30 Days** | 0-1 | **0.0%** |
| **All-Time** | 764-750 | **50.5%** |

**Over/Under Accuracy**: 50.8%

#### 🎯 Accuracy by Confidence (ATS)

| Confidence | Record | Accuracy |
|------------|--------|----------|
| **50%+** | 239-238 | **50.1%** |
| **60%+** | 104-97 | **51.7%** |
| **70%+** | 31-36 | **46.3%** |
| **80%+** | 6-10 | **37.5%** |

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
| Atlantic Coast | 56-42 | **57.1%** |
| Missouri Valley | 27-22 | **55.1%** |
| Ohio Valley | 22-18 | **55.0%** |
| Atlantic 10 | 39-34 | **53.4%** |
| America East | 19-17 | **52.8%** |
| West Coast | 20-18 | **52.6%** |
| Southwestern Athletic | 24-22 | **52.2%** |
| Southland | 19-18 | **51.4%** |
| Southeastern | 54-54 | **50.0%** |
| Big East | 31-31 | **50.0%** |
| Mid-American | 28-29 | **49.1%** |
| Big West | 24-25 | **49.0%** |
| Big 12 | 47-51 | **48.0%** |
| Atlantic Sun | 23-25 | **47.9%** |
| Metro | 21-25 | **45.7%** |
| Conference USA | 22-27 | **44.9%** |
| Sun Belt | 24-32 | **42.9%** |
| Big Ten | 48-65 | **42.5%** |
| Coastal Athletic Association | 23-32 | **41.8%** |
| Northeast | 12-17 | **41.4%** |
| Horizon League | 14-22 | **38.9%** |
| American | 25-40 | **38.5%** |
| Ivy League | 10-16 | **38.5%** |
| Big Sky | 15-27 | **35.7%** |

> *A game counts for a conference if either team is a member.*

#### Combined Statistics

- **Total Predictions**: 1514
- **Overall Winner Accuracy**: 50.5%

#### 📅 Predictions for Today (2026-11-02)

| Matchup | Spread Pick | Total Pick | Confidence |
|---------|-------------|------------|------------|
| UMKC Kangaroos @ Creighton Bluejays | **HOME** (-26.0) | **UNDER** (153.0) | 80% |
| Fairleigh Dickinson Knights @ Illinois Fighting Illini | **AWAY** (+39.5) | **UNDER** (156.5) | 89% |
| LIU Sharks @ Florida Atlantic Owls | **HOME** (-10.5) | **UNDER** (153.5) | 80% |
| Seattle Redhawks @ Hawai'i Rainbow Warriors | **HOME** (-1.5) | **UNDER** (145.5) | 58% |
| Chicago St Cougars @ Texas Longhorns | **AWAY** (+40.5) | **UNDER** (149.5) | 55% |
| Le Moyne Dolphins @ Nebraska Cornhuskers | **AWAY** (+34.5) | **UNDER** (151.5) | 85% |
| Eastern Illinois Panthers @ Indiana Hoosiers | **AWAY** (+33.5) | **UNDER** (142.5) | 54% |
| La Salle Explorers @ Houston Cougars | **AWAY** (+29.0) | **UNDER** (139.5) | 64% |
| Quinnipiac Bobcats @ Michigan St Spartans | **AWAY** (+30.0) | **UNDER** (149.0) | 56% |
| North Carolina Central Eagles @ Georgia Bulldogs | **AWAY** (+39.5) | **UNDER** (163.5) | 79% |
| Bellarmine Knights @ Vanderbilt Commodores | **AWAY** (+35.5) | **OVER** (158.5) | 62% |
| Lehigh Mountain Hawks @ Saint Louis Billikens | **AWAY** (+25.0) | **UNDER** (157.0) | 56% |
| St. Thomas (MN) Tommies @ Presbyterian Blue Hose | **HOME** (+3.5) | **UNDER** (143.5) | 58% |
| Bucknell Bison @ Maryland Terrapins | **AWAY** (+31.5) | **UNDER** (147.5) | 82% |
| Northwestern St Demons @ Baylor Bears | **AWAY** (+31.5) | **UNDER** (151.5) | 88% |
| Chattanooga Mocs @ Louisville Cardinals | **AWAY** (+31.5) | **UNDER** (158.0) | 62% |
| Niagara Purple Eagles @ West Virginia Mountaineers | **AWAY** (+27.5) | **UNDER** (139.5) | 93% |
| Idaho State Bengals @ Utah State Aggies | **AWAY** (+25.5) | **OVER** (146.5) | 60% |
| Fordham Rams @ Kansas Jayhawks | **AWAY** (+23.5) | **UNDER** (145.5) | 92% |
| East Texas A&M Lions @ Oklahoma Sooners | **AWAY** (+30.5) | **UNDER** (149.5) | 84% |
| Jackson St Tigers @ Texas Tech Red Raiders | **AWAY** (+38.5) | **UNDER** (158.5) | 65% |
| Gardner-Webb Bulldogs @ UConn Huskies | **AWAY** (+38.5) | **UNDER** (147.5) | 79% |
| Wofford Terriers @ Tennessee Volunteers | **AWAY** (+28.0) | **UNDER** (153.0) | 75% |
| Maryland-Eastern Shore Hawks @ Wake Forest Demon Deacons | **AWAY** (+33.5) | **OVER** (144.5) | 55% |
| American Eagles @ Cincinnati Bearcats | **AWAY** (+25.5) | **UNDER** (153.5) | 95% |
| Lindenwood Lions @ TCU Horned Frogs | **AWAY** (+28.0) | **UNDER** (155.0) | 72% |
| Incarnate Word Cardinals @ Oklahoma St Cowboys | **AWAY** (+27.5) | **OVER** (161.0) | 53% |
| New Haven Chargers @ Syracuse Orange | **AWAY** (+26.5) | **OVER** (131.5) | 58% |
| Campbell Fighting Camels @ NC State Wolfpack | **AWAY** (+22.5) | **OVER** (159.0) | 67% |
| Maine Black Bears @ Providence Friars | **AWAY** (+31.5) | **UNDER** (151.5) | 58% |
| Milwaukee Panthers @ USC Trojans | **AWAY** (+25.0) | **UNDER** (158.0) | 75% |
| Mercyhurst Lakers @ Marquette Golden Eagles | **AWAY** (+31.5) | **UNDER** (146.5) | 62% |
| Denver Pioneers @ Wisconsin Badgers | **AWAY** (+22.5) | **OVER** (159.0) | 71% |
| Canisius Golden Griffins @ Penn State Nittany Lions | **AWAY** (+21.0) | **UNDER** (152.0) | 88% |
| Binghamton Bearcats @ Northwestern Wildcats | **AWAY** (+20.5) | **UNDER** (146.5) | 69% |
| Charleston Southern Buccaneers @ South Florida Bulls | **AWAY** (+21.5) | **OVER** (158.5) | 69% |
| Utah Tech Trailblazers @ New Mexico Lobos | **AWAY** (+21.0) | **OVER** (155.0) | 60% |
| Mt. St. Mary's Mountaineers @ Xavier Musketeers | **AWAY** (+26.0) | **UNDER** (156.5) | 62% |
| Texas Southern Tigers @ Grand Canyon Antelopes | **AWAY** (+28.5) | **OVER** (143.0) | 58% |
| Rider Broncs @ Pittsburgh Panthers | **AWAY** (+26.0) | **UNDER** (141.0) | 61% |
| Towson Tigers @ Santa Clara Broncos | **AWAY** (+15.0) | **UNDER** (148.5) | 64% |
| Southern Jaguars @ SMU Mustangs | **AWAY** (+25.5) | **UNDER** (160.0) | 59% |
| North Dakota Fighting Hawks @ Minnesota Golden Gophers | **AWAY** (+25.5) | **UNDER** (147.0) | 82% |
| Loyola (MD) Greyhounds @ Georgetown Hoyas | **AWAY** (+27.5) | **UNDER** (152.5) | 71% |
| Arkansas-Little Rock Trojans @ VCU Rams | **AWAY** (+19.5) | **UNDER** (153.5) | 67% |
| Tennessee Tech Golden Eagles @ Mississippi St Bulldogs | **AWAY** (+17.5) | **UNDER** (157.5) | 76% |
| Lafayette Leopards @ Butler Bulldogs | **AWAY** (+19.5) | **UNDER** (149.5) | 53% |
| Long Beach St 49ers @ Utah Utes | **AWAY** (+18.5) | **UNDER** (148.5) | 53% |
| Alcorn St Braves @ Ole Miss Rebels | **AWAY** (+30.0) | **UNDER** (148.5) | 67% |
| Abilene Christian Wildcats @ Colorado Buffaloes | **AWAY** (+18.0) | **UNDER** (151.5) | 71% |
| Florida A&M Rattlers @ Florida St Seminoles | **AWAY** (+24.5) | **UNDER** (155.5) | 71% |
| Montana Grizzlies @ Oregon Ducks | **AWAY** (+17.5) | **UNDER** (153.0) | 88% |
| Saint Peter's Peacocks @ Seton Hall Pirates | **AWAY** (+20.5) | **UNDER** (139.0) | 87% |
| Southern Indiana Screaming Eagles @ Belmont Bruins | **AWAY** (+17.5) | **UNDER** (153.5) | 49% |
| Weber State Wildcats @ Oregon St Beavers | **AWAY** (+17.0) | **UNDER** (156.0) | 72% |
| East Tennessee St Buccaneers @ Arizona St Sun Devils | **AWAY** (+17.0) | **UNDER** (146.0) | 64% |
| Western Carolina Catamounts @ North Carolina Tar Heels | **AWAY** (+22.0) | **UNDER** (155.0) | 60% |
| Florida Gulf Coast Eagles @ UCF Knights | **AWAY** (+22.5) | **UNDER** (154.0) | 69% |
| NJIT Highlanders @ Dayton Flyers | **AWAY** (+23.5) | **UNDER** (144.5) | 89% |
| Robert Morris Colonials @ Nevada Wolf Pack | **AWAY** (+13.0) | **UNDER** (144.5) | 74% |
| Colgate Raiders @ Washington Huskies | **AWAY** (+14.5) | **UNDER** (154.5) | 63% |
| Stetson Hatters @ Clemson Tigers | **AWAY** (+22.0) | **UNDER** (144.5) | 67% |
| Montana St Bobcats @ Colorado St Rams | **AWAY** (+12.0) | **UNDER** (145.0) | 66% |
| Morehead St Eagles @ Western Kentucky Hilltoppers | **AWAY** (+16.5) | **UNDER** (153.0) | 54% |
| Navy Midshipmen @ GW Revolutionaries | **AWAY** (+18.5) | **UNDER** (149.0) | 66% |
| Radford Highlanders @ San Francisco Dons | **AWAY** (+13.5) | **OVER** (154.0) | 53% |
| West Georgia Wolves @ DePaul Blue Demons | **AWAY** (+22.5) | **UNDER** (145.0) | 82% |
| Illinois St Redbirds @ Saint Mary's Gaels | **HOME** (-6.5) | **UNDER** (148.5) | 90% |
| Central Connecticut St Blue Devils @ Temple Owls | **AWAY** (+15.0) | **UNDER** (145.5) | 71% |
| Purdue Boilermakers @ Gonzaga Bulldogs | **HOME** (-5.5) | **UNDER** (155.5) | 82% |
| Eastern Washington Eagles @ Stanford Cardinal | **AWAY** (+13.5) | **UNDER** (154.0) | 62% |
| UCLA Bruins @ Arizona Wildcats | **HOME** (-4.5) | **UNDER** (149.5) | 48% |
| UNC Asheville Bulldogs @ Richmond Spiders | **AWAY** (+15.5) | **UNDER** (152.5) | 77% |
| Oral Roberts Golden Eagles @ Central Arkansas Bears | **AWAY** (+8.0) | **UNDER** (154.5) | 51% |
| Massachusetts Minutemen @ Troy Trojans | **HOME** (-2.5) | **UNDER** (154.5) | 54% |
| South Carolina Upstate Spartans @ East Carolina Pirates | **AWAY** (+14.5) | **UNDER** (152.0) | 63% |
| Youngstown St Penguins @ St. Bonaventure Bonnies | **AWAY** (+10.0) | **UNDER** (153.5) | 61% |
| The Citadel Bulldogs @ Loyola (Chi) Ramblers | **AWAY** (+15.0) | **UNDER** (143.0) | 51% |
| Tenn-Martin Skyhawks @ Tulane Green Wave | **AWAY** (+8.5) | **UNDER** (144.5) | 82% |
| Western Illinois Leathernecks @ Valparaiso Beacons | **AWAY** (+19.0) | **UNDER** (143.0) | 41% |
| Ohio State Buckeyes @ BYU Cougars | **HOME** (-3.5) | **UNDER** (160.5) | 50% |
| Dartmouth Big Green @ Marist Red Foxes | **AWAY** (+6.0) | **UNDER** (141.5) | 51% |
| Elon Phoenix @ Columbia Lions | **HOME** (-3.5) | **UNDER** (151.0) | 64% |
| Texas A&M-CC Islanders @ Texas State Bobcats | **AWAY** (+10.5) | **UNDER** (142.5) | 48% |
| Akron Zips @ Louisiana Ragin' Cajuns | **HOME** (+5.0) | **UNDER** (149.0) | 49% |
| New Hampshire Wildcats @ Brown Bears | **AWAY** (+9.0) | **UNDER** (145.0) | 46% |
| Bethune-Cookman Wildcats @ Furman Paladins | **AWAY** (+4.5) | **UNDER** (153.5) | 57% |
| North Alabama Lions @ UC Davis Aggies | **AWAY** (+9.0) | **UNDER** (148.0) | 59% |
| Davidson Wildcats @ Washington St Cougars | **HOME** (-3.0) | **UNDER** (149.0) | 54% |
| Toledo Rockets @ Arkansas St Red Wolves | **HOME** (-3.5) | **UNDER** (163.0) | 36% |
| Northeastern Huskies @ Boston Univ. Terriers | **HOME** (-1.5) | **OVER** (148.5) | 43% |
| Buffalo Bulls @ Marshall Thundering Herd | **HOME** (-2.0) | **OVER** (157.0) | 27% |
| Charlotte 49ers @ Indiana St Sycamores | **HOME** (+4.0) | **UNDER** (152.5) | 42% |
| Western Michigan Broncos @ Old Dominion Monarchs | **AWAY** (-1.0) | **UNDER** (157.5) | 18% |
| Eastern Michigan Eagles @ Coastal Carolina Chanticleers | **AWAY** (+1.0) | **UNDER** (143.0) | 31% |
| Vermont Catamounts @ Iona Gaels | **AWAY** (+1.0) | **UNDER** (145.0) | 42% |
| Central Michigan Chippewas @ UL Monroe Warhawks | **HOME** (+3.0) | **UNDER** (154.0) | 19% |
| Ohio Bobcats @ South Alabama Jaguars | **HOME** (-1.0) | **UNDER** (153.0) | 14% |
| Siena Saints @ Bryant Bulldogs | **HOME** (+5.0) | **UNDER** (158.5) | 56% |
| Kent State Golden Flashes @ Louisiana Tech Bulldogs | **HOME** (+5.5) | **UNDER** (145.0) | 9% |
| Lipscomb Bisons @ SE Missouri St Redhawks | **HOME** (+1.5) | **UNDER** (156.0) | 48% |
| Howard Bison @ Yale Bulldogs | **AWAY** (+7.0) | **UNDER** (152.5) | 31% |
| Miami (OH) RedHawks @ James Madison Dukes | **AWAY** (-0.0) | **OVER** (155.0) | 14% |
| Ball State Cardinals @ Georgia Southern Eagles | **HOME** (+2.5) | **UNDER** (158.0) | 46% |
| Air Force Falcons @ Wright St Raiders | **AWAY** (+10.5) | **UNDER** (159.5) | 41% |
| UMBC Retrievers @ George Mason Patriots | **AWAY** | - | 50% |

> 📈 *ATS = Against The Spread (with Vegas lines). Updated daily via GitHub Actions.*

<!-- ACCURACY_STATS_END -->

<!-- RANKINGS_START -->

### 🏆 Top 25 Team Rankings

*Updated: November 02, 2026*

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

