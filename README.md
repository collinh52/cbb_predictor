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
| **Last 7 Days** | 130-39 | **76.9%** |
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

#### 📅 Predictions for Today (2026-02-14)

| Matchup | Spread Pick | Total Pick | Confidence |
|---------|-------------|------------|------------|
| St. Thomas (MN) Tommies @ UMKC Kangaroos | **AWAY** (-14.0) | **UNDER** (152.5) | 63% |
| Grambling St Tigers @ Texas Southern Tigers | **HOME** (+1.0) | **OVER** (141.0) | 71% |
| Nicholls St Colonels @ Incarnate Word Cardinals | **HOME** (-2.5) | **UNDER** (151.0) | 68% |
| Sam Houston St Bearkats @ Kennesaw St Owls | **HOME** (-1.0) | **UNDER** (165.5) | 88% |
| LIU Sharks @ New Haven Chargers | **HOME** (+7.0) | **UNDER** (128.5) | 65% |
| Kansas St Wildcats @ Houston Cougars | **AWAY** (+22.5) | **UNDER** (146.5) | 50% |
| Georgetown Hoyas @ UConn Huskies | **AWAY** (+16.5) | **UNDER** (138.5) | 54% |
| LSU Tigers @ Tennessee Volunteers | **AWAY** (+14.5) | **OVER** (144.5) | 58% |
| Memphis Tigers @ Utah State Aggies | **AWAY** (+13.5) | **UNDER** (154.5) | 76% |
| High Point Panthers @ Gardner-Webb Bulldogs | **HOME** (+26.0) | **UNDER** (160.0) | 75% |
| Colorado Buffaloes @ BYU Cougars | **AWAY** (+14.5) | **UNDER** (163.5) | 65% |
| West Georgia Wolves @ Central Arkansas Bears | **AWAY** (+11.5) | **OVER** (153.5) | 50% |
| Nevada Wolf Pack @ San Diego St Aztecs | **HOME** (-8.5) | **OVER** (139.5) | 66% |
| Toledo Rockets @ Bowling Green Falcons | **HOME** (-4.0) | **UNDER** (151.0) | 52% |
| Delaware St Hornets @ Norfolk St Spartans | **HOME** (-9.5) | **UNDER** (137.5) | 63% |
| Maryland-Eastern Shore Hawks @ Howard Bison | **AWAY** (+11.5) | **UNDER** (131.0) | 59% |
| South Alabama Jaguars @ Arkansas St Red Wolves | **HOME** (-7.5) | **UNDER** (151.0) | 72% |
| South Carolina Gamecocks @ Alabama Crimson Tide | **AWAY** (+17.5) | **UNDER** (168.5) | 75% |
| Auburn Tigers @ Arkansas Razorbacks | **HOME** (-8.5) | **UNDER** (165.5) | 52% |
| UL Monroe Warhawks @ Texas State Bobcats | **AWAY** (+13.5) | **UNDER** (149.5) | 81% |
| Northwestern Wildcats @ Nebraska Cornhuskers | **AWAY** (+12.5) | **UNDER** (143.5) | 66% |
| Bellarmine Knights @ Austin Peay Governors | **AWAY** (+9.5) | **UNDER** (153.5) | 56% |
| Miami Hurricanes @ NC State Wolfpack | **HOME** (-5.5) | **OVER** (155.5) | 48% |
| Stetson Hatters @ Florida Gulf Coast Eagles | **AWAY** (+10.0) | **OVER** (148.0) | 47% |
| South Carolina Upstate Spartans @ Longwood Lancers | **HOME** (-6.0) | **UNDER** (145.5) | 55% |
| Elon Phoenix @ William & Mary Tribe | **AWAY** (+7.5) | **OVER** (165.5) | 43% |
| Miss Valley St Delta Devils @ Alabama A&M Bulldogs | **AWAY** (+16.5) | **UNDER** (138.0) | 62% |
| North Florida Ospreys @ Jacksonville Dolphins | **AWAY** (+7.0) | **OVER** (154.5) | 49% |
| Pittsburgh Panthers @ North Carolina Tar Heels | **AWAY** (+10.5) | **OVER** (143.5) | 43% |
| Bryant Bulldogs @ Vermont Catamounts | **AWAY** (+12.0) | **OVER** (134.0) | 42% |
| East Carolina Pirates @ Rice Owls | **HOME** (-5.0) | **UNDER** (145.5) | 40% |
| Minnesota Golden Gophers @ Washington Huskies | **AWAY** (+6.5) | **UNDER** (138.5) | 49% |
| Montana St Bobcats @ Montana Grizzlies | **HOME** (-2.0) | **UNDER** (144.5) | 56% |
| Samford Bulldogs @ East Tennessee St Buccaneers | **AWAY** (+6.0) | **UNDER** (147.0) | 49% |
| Texas A&M Aggies @ Vanderbilt Commodores | **AWAY** (+6.5) | **UNDER** (166.5) | 48% |
| Charleston Southern Buccaneers @ Radford Highlanders | **HOME** (-4.0) | **OVER** (162.5) | 46% |
| Delaware Blue Hens @ Missouri St Bears | **AWAY** (+8.0) | **OVER** (134.0) | 57% |
| Army Knights @ American Eagles | **AWAY** (+9.5) | **UNDER** (144.5) | 37% |
| Lehigh Mountain Hawks @ Lafayette Leopards | **HOME** (-2.0) | **OVER** (139.0) | 54% |
| Northern Illinois Huskies @ Central Michigan Chippewas | **HOME** (-3.5) | **UNDER** (146.5) | 50% |
| Stanford Cardinal @ Wake Forest Demon Deacons | **HOME** (-4.0) | **UNDER** (149.0) | 37% |
| Idaho State Bengals @ Idaho Vandals | **AWAY** (+5.5) | **UNDER** (147.5) | 47% |
| Southern Utah Thunderbirds @ UT-Arlington Mavericks | **AWAY** (+8.5) | **UNDER** (145.5) | 36% |
| UC Riverside Highlanders @ UC San Diego Tritons | **AWAY** (+10.5) | **UNDER** (144.0) | 57% |
| Wagner Seahawks @ Stonehill Skyhawks | **HOME** (-3.0) | **UNDER** (128.5) | 49% |
| Georgia Tech Yellow Jackets @ Notre Dame Fighting Irish | **AWAY** (+7.5) | **UNDER** (151.5) | 39% |
| Lipscomb Bisons @ Queens University Royals | **HOME** (-2.5) | **UNDER** (165.5) | 33% |
| CSU Fullerton Titans @ UC Irvine Anteaters | **AWAY** (+8.0) | **UNDER** (153.5) | 53% |
| Arkansas-Pine Bluff Golden Lions @ Alabama St Hornets | **HOME** (-2.5) | **OVER** (150.5) | 45% |
| Long Beach St 49ers @ UC Davis Aggies | **AWAY** (+5.0) | **OVER** (149.5) | 36% |
| Chicago St Cougars @ Le Moyne Dolphins | **AWAY** (+7.0) | **OVER** (144.5) | 34% |
| McNeese Cowboys @ East Texas A&M Lions | **HOME** (+13.0) | **UNDER** (141.5) | 73% |
| Florida A&M Rattlers @ Jackson St Tigers | **HOME** (+1.0) | **OVER** (147.0) | 35% |
| Sacramento St Hornets @ Northern Arizona Lumberjacks | **HOME** (+0.0) | **UNDER** (155.0) | 36% |
| TCU Horned Frogs @ Oklahoma St Cowboys | **HOME** (-1.5) | **UNDER** (156.5) | 36% |
| Western Michigan Broncos @ Eastern Michigan Eagles | **AWAY** (+7.0) | **UNDER** (145.5) | 49% |
| Tarleton State Texans @ Abilene Christian Wildcats | **HOME** (-2.5) | **UNDER** (137.0) | 75% |
| Bethune-Cookman Wildcats @ Alcorn St Braves | **HOME** (+7.0) | **OVER** (144.5) | 42% |
| Middle Tennessee Blue Raiders @ Western Kentucky Hilltoppers | **HOME** (-3.5) | **UNDER** (144.0) | 44% |
| Wyoming Cowboys @ Colorado St Rams | **AWAY** (+4.5) | **UNDER** (138.5) | 44% |
| Bucknell Bison @ Boston Univ. Terriers | **AWAY** (+7.5) | **OVER** (140.5) | 58% |
| Florida St Seminoles @ Virginia Tech Hokies | **AWAY** (+7.5) | **UNDER** (155.5) | 36% |
| Coppin St Eagles @ North Carolina Central Eagles | **AWAY** (+11.0) | **UNDER** (144.0) | 75% |
| Fordham Rams @ Rhode Island Rams | **AWAY** (+5.5) | **UNDER** (133.0) | 54% |
| Yale Bulldogs @ Harvard Crimson | **HOME** (+5.5) | **UNDER** (142.5) | 36% |
| Presbyterian Blue Hose @ UNC Asheville Bulldogs | **AWAY** (+4.0) | **OVER** (136.5) | 43% |
| Lamar Cardinals @ Texas A&M-CC Islanders | **HOME** (-2.5) | **UNDER** (135.5) | 50% |
| Portland St Vikings @ N Colorado Bears | **HOME** (-3.0) | **UNDER** (148.0) | 46% |
| St. John's Red Storm @ Providence Friars | **HOME** (+7.5) | **OVER** (166.5) | 40% |
| Marquette Golden Eagles @ Xavier Musketeers | **HOME** (-2.5) | **UNDER** (155.5) | 33% |
| Grand Canyon Antelopes @ San José St Spartans | **HOME** (+11.5) | **UNDER** (139.5) | 39% |
| Mercer Bears @ The Citadel Bulldogs | **HOME** (+9.5) | **OVER** (147.5) | 36% |
| Georgia Bulldogs @ Oklahoma Sooners | **HOME** (-1.5) | **OVER** (164.5) | 32% |
| Arkansas-Little Rock Trojans @ Eastern Illinois Panthers | **HOME** (+2.0) | **UNDER** (135.0) | 26% |
| Air Force Falcons @ Fresno St Bulldogs | **AWAY** (+16.5) | **UNDER** (142.5) | 57% |
| Liberty Flames @ UTEP Miners | **HOME** (+7.0) | **OVER** (137.5) | 31% |
| West Virginia Mountaineers @ UCF Knights | **AWAY** (+3.5) | **UNDER** (139.5) | 32% |
| Penn State Nittany Lions @ Oregon Ducks | **AWAY** (+6.5) | **UNDER** (146.5) | 29% |
| Stephen F. Austin Lumberjacks @ UT Rio Grande Valley Vaqueros | **HOME** (+1.5) | **UNDER** (145.5) | 37% |
| Navy Midshipmen @ Colgate Raiders | **AWAY** (-1.5) | **UNDER** (138.5) | 20% |
| Cal Baptist Lancers @ Utah Tech Trailblazers | **HOME** (+3.0) | **OVER** (142.0) | 21% |
| Louisiana Tech Bulldogs @ Florida Int'l Golden Panthers | **AWAY** (+4.0) | **OVER** (145.0) | 24% |
| NJIT Highlanders @ Maine Black Bears | **AWAY** (-1.5) | **OVER** (136.5) | 25% |
| Appalachian St Mountaineers @ James Madison Dukes | **AWAY** (-1.5) | **UNDER** (135.5) | 39% |
| New Mexico St Aggies @ Jacksonville St Gamecocks | **HOME** (-1.5) | **UNDER** (139.0) | 27% |
| Mississippi St Bulldogs @ Ole Miss Rebels | **AWAY** (+3.5) | **UNDER** (144.5) | 36% |
| Georgia St Panthers @ Old Dominion Monarchs | **AWAY** (+3.5) | **OVER** (147.5) | 18% |
| Hofstra Pride @ UNC Wilmington Seahawks | **AWAY** (+2.5) | **UNDER** (139.5) | 20% |
| California Golden Bears @ Boston College Eagles | **HOME** (+3.5) | **UNDER** (140.5) | 42% |
| Mercyhurst Lakers @ St. Francis (PA) Red Flash | **HOME** (+3.0) | **OVER** (136.5) | 27% |
| VCU Rams @ Richmond Spiders | **HOME** (+7.5) | **UNDER** (156.0) | 25% |
| Central Connecticut St Blue Devils @ Fairleigh Dickinson Knights | **HOME** (+0.0) | **OVER** (137.0) | 25% |
| Western Carolina Catamounts @ Chattanooga Mocs | **HOME** (-1.0) | **UNDER** (152.0) | 24% |
| Duquesne Dukes @ St. Bonaventure Bonnies | **AWAY** (+2.0) | **OVER** (153.5) | 25% |
| UC Santa Barbara Gauchos @ Cal Poly Mustangs | **HOME** (+5.0) | **UNDER** (160.5) | 22% |
| Tulsa Golden Hurricane @ Wichita St Shockers | **HOME** (-1.5) | **OVER** (150.5) | 18% |
| Troy Trojans @ Southern Miss Golden Eagles | **HOME** (+4.5) | **UNDER** (143.5) | 17% |
| Tenn-Martin Skyhawks @ SIU-Edwardsville Cougars | **AWAY** (-1.0) | **UNDER** (127.5) | 45% |
| Texas Longhorns @ Missouri Tigers | **HOME** (+1.5) | **OVER** (150.5) | 12% |
| Loyola Marymount Lions @ Pepperdine Waves | **HOME** (+5.5) | **UNDER** (147.0) | 26% |
| Marshall Thundering Herd @ Georgia Southern Eagles | **HOME** (+2.5) | **UNDER** (163.0) | 51% |
| Albany Great Danes @ Binghamton Bearcats | **HOME** (+5.0) | **OVER** (138.0) | 21% |
| Furman Paladins @ VMI Keydets | **HOME** (+13.0) | **UNDER** (146.0) | 36% |
| Saint Mary's Gaels @ Pacific Tigers | **HOME** (+8.5) | **UNDER** (136.0) | 18% |
| Villanova Wildcats @ Creighton Bluejays | **HOME** (+3.5) | **UNDER** (144.5) | 9% |
| SE Louisiana Lions @ Northwestern St Demons | **HOME** (-1.0) | **UNDER** (130.5) | 38% |
| Kent State Golden Flashes @ Ball State Cardinals | **HOME** (+8.0) | **UNDER** (143.0) | 14% |
| Wofford Terriers @ UNC Greensboro Spartans | **HOME** (+2.0) | **OVER** (154.5) | 10% |
| Tennessee St Tigers @ Morehead St Eagles | **HOME** (+1.0) | **OVER** (151.0) | 22% |
| Morgan St Bears @ South Carolina St Bulldogs | **AWAY** (-0.0) | **UNDER** (155.0) | 40% |
| New Orleans Privateers @ Houston Christian Huskies | **HOME** (+1.0) | **OVER** (151.5) | 5% |
| Weber State Wildcats @ Eastern Washington Eagles | **AWAY** (+3.5) | **UNDER** (156.0) | 7% |
| Gonzaga Bulldogs @ Santa Clara Broncos | **HOME** (+3.5) | **UNDER** (157.5) | 10% |
| Hawai'i Rainbow Warriors @ CSU Northridge Matadors | **HOME** (+3.0) | **UNDER** (162.5) | 24% |
| Southern Jaguars @ Prairie View Panthers | **HOME** (+3.5) | **UNDER** (161.0) | 41% |
| Virginia Cavaliers @ Ohio State Buckeyes | **HOME** (+4.5) | **OVER** (147.5) | 3% |
| South Dakota St Jackrabbits @ Oral Roberts Golden Eagles | **HOME** (+6.5) | **UNDER** (146.5) | 13% |
| North Dakota St Bison @ North Dakota Fighting Hawks | **HOME** (+6.0) | **OVER** (149.0) | 21% |
| UMBC Retrievers @ New Hampshire Wildcats | **HOME** (+4.5) | **OVER** (143.0) | 5% |
| SE Missouri St Redhawks @ Lindenwood Lions | **AWAY** (+2.0) | **UNDER** (157.5) | 18% |
| SMU Mustangs @ Syracuse Orange | **HOME** (+2.5) | **UNDER** (156.5) | 9% |
| Tennessee Tech Golden Eagles @ Southern Indiana Screaming Eagles | **HOME** (+0.0) | **UNDER** (141.0) | 11% |
| Louisville Cardinals @ Baylor Bears | **HOME** (+6.5) | **UNDER** (163.5) | 33% |

> 📈 *ATS = Against The Spread (with Vegas lines). Updated daily via GitHub Actions.*

<!-- ACCURACY_STATS_END -->

<!-- RANKINGS_START -->

### 🏆 Top 25 Team Rankings

*Updated: February 14, 2026*

| Rank | Team | Record | Rating | Off | Def |
|------|------|--------|--------|-----|-----|
| 1 | Michigan Wolverines | 23-1 | +30.5 | 71.8 | 41.3 |
| 2 | Arizona Wildcats | 23-1 | +27.9 | 69.4 | 41.6 |
| 3 | Louisville Cardinals | 18-6 | +27.1 | 70.5 | 43.7 |
| 4 | Duke Blue Devils | 22-2 | +26.0 | 64.5 | 38.5 |
| 5 | Illinois Fighting Illini | 20-5 | +25.5 | 67.1 | 42.0 |
| 6 | Iowa State Cyclones | 21-3 | +24.8 | 65.9 | 41.2 |
| 7 | Alabama Crimson Tide | 17-7 | +24.6 | 72.7 | 48.4 |
| 8 | Florida Gators | 18-6 | +24.6 | 65.3 | 41.1 |
| 9 | Gonzaga Bulldogs | 24-2 | +24.5 | 65.7 | 41.2 |
| 10 | Purdue Boilermakers | 20-4 | +24.0 | 65.9 | 41.9 |
| 11 | Arkansas Razorbacks | 18-6 | +23.9 | 70.0 | 46.1 |
| 12 | Vanderbilt Commodores | 20-4 | +23.7 | 68.4 | 44.7 |
| 13 | Houston Cougars | 22-2 | +23.7 | 60.9 | 37.2 |
| 14 | BYU Cougars | 18-6 | +23.4 | 68.8 | 45.7 |
| 15 | UConn Huskies | 23-2 | +22.9 | 62.7 | 39.8 |
| 16 | Kansas Jayhawks | 19-5 | +22.8 | 63.3 | 40.5 |
| 17 | St. John's Red Storm | 19-5 | +22.6 | 66.3 | 43.7 |
| 18 | Tennessee Volunteers | 17-7 | +22.0 | 63.5 | 41.9 |
| 19 | Texas Tech Red Raiders | 18-6 | +21.9 | 64.7 | 42.8 |
| 20 | Kentucky Wildcats | 17-7 | +21.7 | 65.0 | 43.6 |
| 21 | NC State Wolfpack | 18-7 | +21.6 | 67.0 | 45.7 |
| 22 | Michigan State Spartans | 20-5 | +21.6 | 61.7 | 40.1 |
| 23 | Saint Louis Billikens | 24-1 | +21.4 | 67.2 | 45.8 |
| 24 | Georgia Bulldogs | 17-7 | +21.2 | 69.6 | 48.8 |
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

