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

**Last Updated**: February 07, 2026 at 12:28 PM

![ATS Accuracy](https://img.shields.io/badge/ATS_Record-55.1%25-brightgreen)

#### 🏆 Rolling ATS Performance

| Timeframe | ATS Record | Accuracy |
|-----------|------------|----------|
| **Yesterday** (2026-02-06) | 6-2 | **75.0%** |
| **Last 7 Days** | 165-135 | **55.0%** |
| **Last 30 Days** | 166-135 | **55.1%** |
| **All-Time** | 165-136 | **55.1%** |

**Over/Under Accuracy**: 49.2%

#### 🎯 Accuracy by Confidence (ATS)

| Confidence | Record | Accuracy |
|------------|--------|----------|
| **50%+** | 111-98 | **53.1%** |
| **60%+** | 72-72 | **50.0%** |
| **70%+** | 44-43 | **50.6%** |
| **80%+** | 26-20 | **56.5%** |

#### Straight-Up Predictions (Games Without Vegas Lines)

| **7-Day** | 0/0 (0.0%) |
| **30-Day** | 1/3 (33.3%) |
| **All-Time** | 1/3 (33.3%) |

#### Combined Statistics

- **Total Predictions**: 304
- **Overall Winner Accuracy**: 54.9%

#### 📅 Predictions for Today (2026-02-07)

| Matchup | Spread Pick | Total Pick | Confidence |
|---------|-------------|------------|------------|
| La Salle Explorers @ Saint Louis Billikens | **HOME** (-23.5) | **UNDER** (153.5) | 78% |
| Sam Houston St Bearkats @ Louisiana Tech Bulldogs | **HOME** (+3.0) | **UNDER** (141.5) | 80% |
| Seattle Redhawks @ Portland Pilots | **HOME** (+3.5) | **OVER** (141.5) | 55% |
| Alabama St Hornets @ Grambling St Tigers | **AWAY** (+5.0) | **OVER** (144.0) | 56% |
| Radford Highlanders @ High Point Panthers | **HOME** (-13.5) | **OVER** (164.0) | 56% |
| Utah Utes @ Kansas Jayhawks | **HOME** (-18.5) | **OVER** (150.5) | 51% |
| Texas A&M-CC Islanders @ Nicholls St Colonels | **AWAY** (+1.0) | **UNDER** (137.0) | 55% |
| Incarnate Word Cardinals @ McNeese Cowboys | **HOME** (-16.0) | **UNDER** (146.0) | 51% |
| Cleveland St Vikings @ IUPUI Jaguars | **AWAY** (+1.5) | **UNDER** (169.5) | 92% |
| Oregon Ducks @ Purdue Boilermakers | **HOME** (-19.5) | **UNDER** (143.5) | 59% |
| UT-Arlington Mavericks @ Utah Valley Wolverines | **HOME** (-10.5) | **UNDER** (142.0) | 68% |
| Oklahoma Sooners @ Vanderbilt Commodores | **HOME** (-12.5) | **UNDER** (159.5) | 54% |
| Baylor Bears @ Iowa State Cyclones | **HOME** (-14.5) | **OVER** (151.5) | 53% |
| Gonzaga Bulldogs @ Oregon St Beavers | **AWAY** (-17.5) | **UNDER** (146.5) | 57% |
| Virginia Tech Hokies @ NC State Wolfpack | **HOME** (-10.5) | **OVER** (152.5) | 54% |
| Ole Miss Rebels @ Texas Longhorns | **HOME** (-9.5) | **UNDER** (146.5) | 51% |
| San Francisco Dons @ Saint Mary's Gaels | **HOME** (-11.5) | **UNDER** (142.0) | 61% |
| North Florida Ospreys @ Queens University Royals | **HOME** (-15.5) | **OVER** (176.5) | 54% |
| Syracuse Orange @ Virginia Cavaliers | **HOME** (-12.5) | **OVER** (147.5) | 53% |
| Missouri St Bears @ Liberty Flames | **HOME** (-10.0) | **OVER** (139.0) | 60% |
| Longwood Lancers @ Winthrop Eagles | **HOME** (-10.5) | **UNDER** (150.0) | 50% |
| Oral Roberts Golden Eagles @ St. Thomas (MN) Tommies | **HOME** (-17.5) | **UNDER** (151.5) | 69% |
| UC San Diego Tritons @ Hawai'i Rainbow Warriors | **HOME** (-7.0) | **UNDER** (146.0) | 74% |
| North Alabama Lions @ Austin Peay Governors | **HOME** (-13.0) | **UNDER** (145.5) | 67% |
| Niagara Purple Eagles @ Quinnipiac Bobcats | **HOME** (-14.0) | **OVER** (137.0) | 70% |
| Prairie View Panthers @ Bethune-Cookman Wildcats | **HOME** (-11.0) | **UNDER** (152.5) | 76% |
| Fresno St Bulldogs @ Nevada Wolf Pack | **HOME** (-10.5) | **UNDER** (145.0) | 80% |
| Northwestern St Demons @ East Texas A&M Lions | **HOME** (-2.0) | **UNDER** (142.0) | 93% |
| Southern Indiana Screaming Eagles @ SE Missouri St Redhawks | **HOME** (-11.0) | **UNDER** (140.5) | 57% |
| Binghamton Bearcats @ NJIT Highlanders | **HOME** (-9.0) | **OVER** (140.0) | 62% |
| Western Illinois Leathernecks @ Tennessee St Tigers | **HOME** (-14.5) | **UNDER** (151.5) | 50% |
| San José St Spartans @ Colorado St Rams | **HOME** (-14.0) | **UNDER** (136.0) | 52% |
| Omaha Mavericks @ North Dakota St Bison | **HOME** (-10.0) | **OVER** (144.5) | 45% |
| Morehead St Eagles @ Tenn-Martin Skyhawks | **HOME** (-8.5) | **OVER** (135.5) | 54% |
| Stonehill Skyhawks @ LIU Sharks | **AWAY** (+10.5) | **UNDER** (133.5) | 50% |
| South Dakota Coyotes @ South Dakota St Jackrabbits | **HOME** (-11.0) | **OVER** (157.0) | 45% |
| CSU Bakersfield Roadrunners @ CSU Fullerton Titans | **HOME** (-10.0) | **OVER** (157.0) | 44% |
| Wagner Seahawks @ Central Connecticut St Blue Devils | **HOME** (-6.0) | **UNDER** (136.5) | 60% |
| South Carolina St Bulldogs @ Howard Bison | **HOME** (-15.0) | **UNDER** (142.5) | 90% |
| Alabama A&M Bulldogs @ Southern Jaguars | **HOME** (-7.5) | **UNDER** (144.0) | 66% |
| San Diego St Aztecs @ Air Force Falcons | **AWAY** (-22.0) | **OVER** (136.5) | 42% |
| Alcorn St Braves @ Arkansas-Pine Bluff Golden Lions | **HOME** (-8.0) | **OVER** (145.5) | 80% |
| Kansas St Wildcats @ TCU Horned Frogs | **HOME** (-9.5) | **UNDER** (152.5) | 43% |
| Louisville Cardinals @ Wake Forest Demon Deacons | **AWAY** (-9.5) | **UNDER** (160.5) | 66% |
| Wisconsin Badgers @ Indiana Hoosiers | **HOME** (-3.5) | **UNDER** (155.5) | 55% |
| Maryland-Eastern Shore Hawks @ Morgan St Bears | **HOME** (+0.0) | **UNDER** (141.0) | 59% |
| Tarleton State Texans @ Southern Utah Thunderbirds | **HOME** (-1.5) | **UNDER** (149.5) | 44% |
| Delaware St Hornets @ Coppin St Eagles | **HOME** (+3.0) | **UNDER** (133.5) | 78% |
| The Citadel Bulldogs @ Chattanooga Mocs | **HOME** (-9.5) | **OVER** (138.5) | 45% |
| Idaho Vandals @ Montana Grizzlies | **HOME** (-2.5) | **UNDER** (152.0) | 61% |
| Chicago St Cougars @ New Haven Chargers | **HOME** (-6.0) | **UNDER** (127.5) | 68% |
| Georgia Tech Yellow Jackets @ Stanford Cardinal | **HOME** (-7.5) | **UNDER** (151.5) | 69% |
| American Eagles @ Navy Midshipmen | **HOME** (-4.5) | **UNDER** (134.0) | 46% |
| Miami Hurricanes @ Boston College Eagles | **AWAY** (-7.5) | **UNDER** (140.5) | 46% |
| UC Riverside Highlanders @ CSU Northridge Matadors | **HOME** (-9.0) | **UNDER** (160.0) | 63% |
| Lamar Cardinals @ Stephen F. Austin Lumberjacks | **HOME** (-8.0) | **UNDER** (138.5) | 67% |
| Denver Pioneers @ North Dakota Fighting Hawks | **HOME** (-3.5) | **OVER** (162.0) | 55% |
| Saint Joseph's Hawks @ George Mason Patriots | **HOME** (-8.0) | **UNDER** (139.0) | 39% |
| Eastern Michigan Eagles @ Appalachian St Mountaineers | **HOME** (-6.5) | **OVER** (130.5) | 38% |
| St. Francis (PA) Red Flash @ Le Moyne Dolphins | **HOME** (-8.0) | **UNDER** (150.5) | 71% |
| Milwaukee Panthers @ Northern Kentucky Norse | **HOME** (-7.0) | **UNDER** (156.5) | 44% |
| Fort Wayne Mastodons @ Wright St Raiders | **HOME** (-7.5) | **UNDER** (150.0) | 74% |
| Northeastern Huskies @ Stony Brook Seawolves | **HOME** (-4.0) | **OVER** (152.5) | 48% |
| Washington Huskies @ UCLA Bruins | **HOME** (-5.5) | **UNDER** (144.5) | 56% |
| Nebraska Cornhuskers @ Rutgers Scarlet Knights | **AWAY** (-12.5) | **UNDER** (142.5) | 45% |
| Northern Arizona Lumberjacks @ Weber State Wildcats | **HOME** (-6.5) | **UNDER** (152.5) | 35% |
| Boise State Broncos @ New Mexico Lobos | **HOME** (-6.0) | **UNDER** (153.5) | 43% |
| Robert Morris Colonials @ Youngstown St Penguins | **HOME** (-4.0) | **OVER** (144.5) | 50% |
| UMass Lowell River Hawks @ Albany Great Danes | **HOME** (-3.5) | **UNDER** (145.0) | 43% |
| Illinois Fighting Illini @ Michigan St Spartans | **HOME** (-1.5) | **UNDER** (143.5) | 41% |
| New Hampshire Wildcats @ Vermont Catamounts | **HOME** (-10.0) | **UNDER** (137.5) | 39% |
| Gardner-Webb Bulldogs @ Presbyterian Blue Hose | **HOME** (-17.0) | **UNDER** (147.0) | 41% |
| Santa Clara Broncos @ Washington St Cougars | **AWAY** (-7.5) | **UNDER** (161.0) | 51% |
| Tennessee Volunteers @ Kentucky Wildcats | **HOME** (-1.5) | **OVER** (143.5) | 42% |
| Stetson Hatters @ Eastern Kentucky Colonels | **HOME** (-8.5) | **OVER** (152.0) | 54% |
| Maine Black Bears @ Bryant Bulldogs | **HOME** (-2.0) | **UNDER** (126.5) | 46% |
| Eastern Washington Eagles @ Montana St Bobcats | **HOME** (-5.5) | **OVER** (148.0) | 40% |
| Abilene Christian Wildcats @ Cal Baptist Lancers | **HOME** (-10.0) | **UNDER** (136.0) | 71% |
| Detroit Mercy Titans @ Green Bay Phoenix | **HOME** (-3.5) | **OVER** (151.5) | 33% |
| Campbell Fighting Camels @ North Carolina A&T Aggies | **AWAY** (-4.0) | **OVER** (159.5) | 41% |
| Eastern Illinois Panthers @ Tennessee Tech Golden Eagles | **HOME** (-5.0) | **UNDER** (140.0) | 53% |
| Seton Hall Pirates @ Creighton Bluejays | **HOME** (-1.5) | **UNDER** (138.5) | 35% |
| North Carolina Central Eagles @ Norfolk St Spartans | **HOME** (-4.5) | **UNDER** (149.0) | 78% |
| Missouri Tigers @ South Carolina Gamecocks | **HOME** (+1.5) | **UNDER** (146.5) | 49% |
| Harvard Crimson @ Dartmouth Big Green | **HOME** (+1.5) | **OVER** (142.0) | 33% |
| Mt. St. Mary's Mountaineers @ Iona Gaels | **HOME** (-4.0) | **UNDER** (139.5) | 54% |
| Northern Illinois Huskies @ Georgia St Panthers | **HOME** (-5.5) | **UNDER** (144.0) | 46% |
| DePaul Blue Demons @ Providence Friars | **HOME** (-5.5) | **OVER** (155.5) | 42% |
| Lehigh Mountain Hawks @ Holy Cross Crusaders | **HOME** (+1.5) | **OVER** (139.0) | 47% |
| Florida Int'l Golden Panthers @ Western Kentucky Hilltoppers | **HOME** (-4.0) | **UNDER** (158.5) | 49% |
| Cal Poly Mustangs @ UC Davis Aggies | **HOME** (-6.5) | **UNDER** (169.5) | 51% |
| San Diego Toreros @ Loyola Marymount Lions | **HOME** (-5.0) | **OVER** (151.5) | 30% |
| SIU-Edwardsville Cougars @ Arkansas-Little Rock Trojans | **HOME** (-2.0) | **OVER** (132.0) | 37% |
| Princeton Tigers @ Pennsylvania Quakers | **HOME** (-3.5) | **UNDER** (141.5) | 45% |
| Mercyhurst Lakers @ Fairleigh Dickinson Knights | **HOME** (-2.0) | **UNDER** (130.0) | 34% |
| Central Arkansas Bears @ Lipscomb Bisons | **HOME** (-3.0) | **OVER** (155.0) | 38% |
| Charleston Southern Buccaneers @ South Carolina Upstate Spartans | **HOME** (+1.0) | **OVER** (149.5) | 26% |
| Drexel Dragons @ Elon Phoenix | **HOME** (-4.0) | **UNDER** (140.0) | 29% |
| UC Irvine Anteaters @ UC Santa Barbara Gauchos | **HOME** (-1.5) | **UNDER** (138.5) | 26% |
| Massachusetts Minutemen @ Coastal Carolina Chanticleers | **HOME** (+1.0) | **UNDER** (148.5) | 38% |
| Western Carolina Catamounts @ Wofford Terriers | **HOME** (-5.0) | **OVER** (156.5) | 40% |
| Lafayette Leopards @ Army Knights | **HOME** (+1.0) | **OVER** (143.0) | 53% |
| Arizona St Sun Devils @ Colorado Buffaloes | **HOME** (-3.5) | **OVER** (157.5) | 33% |
| Akron Zips @ Troy Trojans | **AWAY** (-4.5) | **OVER** (155.0) | 39% |
| Arkansas Razorbacks @ Mississippi St Bulldogs | **AWAY** (-6.5) | **UNDER** (163.5) | 42% |
| Cornell Big Red @ Columbia Lions | **HOME** (-1.5) | **OVER** (170.0) | 31% |
| Texas Southern Tigers @ Florida A&M Rattlers | **AWAY** (+2.0) | **UNDER** (146.0) | 30% |
| Richmond Spiders @ Rhode Island Rams | **HOME** (-5.5) | **UNDER** (140.0) | 24% |
| Ohio Bobcats @ Old Dominion Monarchs | **AWAY** (-3.0) | **UNDER** (154.0) | 38% |
| Western Michigan Broncos @ Texas State Bobcats | **HOME** (-5.5) | **UNDER** (146.0) | 27% |
| Loyola (MD) Greyhounds @ Boston Univ. Terriers | **HOME** (-4.5) | **OVER** (145.0) | 35% |
| Marist Red Foxes @ Fairfield Stags | **HOME** (-1.0) | **OVER** (139.0) | 25% |
| Houston Christian Huskies @ SE Louisiana Lions | **HOME** (-5.0) | **UNDER** (135.0) | 22% |
| Utah State Aggies @ Wyoming Cowboys | **AWAY** (-8.0) | **OVER** (146.0) | 27% |
| St. Bonaventure Bonnies @ Fordham Rams | **HOME** (+1.0) | **UNDER** (139.5) | 26% |
| Pacific Tigers @ Pepperdine Waves | **AWAY** (-8.0) | **UNDER** (139.0) | 24% |
| Towson Tigers @ Hofstra Pride | **HOME** (-3.5) | **UNDER** (138.5) | 28% |
| Buffalo Bulls @ South Alabama Jaguars | **HOME** (-3.0) | **OVER** (142.5) | 22% |
| Siena Saints @ Saint Peter's Peacocks | **HOME** (+1.0) | **UNDER** (138.0) | 18% |
| Butler Bulldogs @ Marquette Golden Eagles | **HOME** (-2.5) | **OVER** (156.5) | 19% |
| Clemson Tigers @ California Golden Bears | **HOME** (+3.5) | **UNDER** (135.5) | 22% |
| Colgate Raiders @ Bucknell Bison | **HOME** (+3.5) | **OVER** (141.5) | 31% |
| N Colorado Bears @ Idaho State Bengals | **HOME** (+1.5) | **UNDER** (153.5) | 15% |
| GW Revolutionaries @ Duquesne Dukes | **HOME** (-1.0) | **OVER** (159.5) | 20% |
| Georgia Bulldogs @ LSU Tigers | **HOME** (+1.5) | **UNDER** (163.5) | 16% |
| Sacred Heart Pioneers @ Manhattan Jaspers | **HOME** (+1.5) | **OVER** (160.5) | 21% |
| Kennesaw St Owls @ Jacksonville St Gamecocks | **HOME** (-1.0) | **UNDER** (149.0) | 17% |
| Grand Canyon Antelopes @ UNLV Rebels | **HOME** (+3.5) | **UNDER** (149.0) | 40% |
| Central Michigan Chippewas @ Louisiana Ragin' Cajuns | **AWAY** (+2.5) | **OVER** (133.0) | 18% |
| Ball State Cardinals @ UL Monroe Warhawks | **HOME** (+4.5) | **UNDER** (141.5) | 50% |
| North Texas Mean Green @ UTSA Roadrunners | **HOME** (+10.0) | **UNDER** (138.5) | 32% |
| East Tennessee St Buccaneers @ VMI Keydets | **AWAY** (-15.0) | **UNDER** (145.0) | 36% |
| Villanova Wildcats @ Georgetown Hoyas | **AWAY** (-3.5) | **UNDER** (138.5) | 11% |
| Portland St Vikings @ Sacramento St Hornets | **HOME** (+4.5) | **UNDER** (152.0) | 18% |
| Middle Tennessee Blue Raiders @ Delaware Blue Hens | **AWAY** (-4.0) | **OVER** (130.0) | 12% |
| Houston Cougars @ BYU Cougars | **HOME** (+2.5) | **UNDER** (149.5) | 10% |
| Kent State Golden Flashes @ Southern Miss Golden Eagles | **AWAY** (-5.0) | **OVER** (149.5) | 10% |
| UT Rio Grande Valley Vaqueros @ New Orleans Privateers | **HOME** (+2.0) | **UNDER** (150.5) | 28% |
| Temple Owls @ East Carolina Pirates | **HOME** (+2.0) | **UNDER** (139.5) | 10% |
| Merrimack Warriors @ Rider Broncs | **AWAY** (-9.5) | **UNDER** (138.0) | 15% |
| Florida St Seminoles @ Notre Dame Fighting Irish | **AWAY** (+2.5) | **UNDER** (152.5) | 20% |
| SMU Mustangs @ Pittsburgh Panthers | **HOME** (+4.5) | **OVER** (147.5) | 21% |
| Jackson St Tigers @ Miss Valley St Delta Devils | **AWAY** (-8.5) | **OVER** (144.0) | 13% |
| New Mexico St Aggies @ UTEP Miners | **HOME** (+1.0) | **OVER** (137.5) | 6% |
| Jacksonville Dolphins @ West Georgia Wolves | **AWAY** (-1.0) | **OVER** (137.0) | 11% |
| Toledo Rockets @ James Madison Dukes | **HOME** (+1.5) | **UNDER** (152.0) | 5% |
| William & Mary Tribe @ Hampton Pirates | **AWAY** (-4.5) | **UNDER** (152.5) | 30% |
| Mercer Bears @ Samford Bulldogs | **AWAY** (-1.5) | **UNDER** (162.0) | 16% |
| Bowling Green Falcons @ Arkansas St Red Wolves | **HOME** (-2.0) | **OVER** (154.5) | 22% |
| Florida Gulf Coast Eagles @ Bellarmine Knights | **HOME** (+1.5) | **OVER** (153.5) | 11% |
| Florida Gators @ Texas A&M Aggies | **AWAY** (-5.5) | **UNDER** (164.5) | 19% |
| Miami (OH) RedHawks @ Marshall Thundering Herd | **HOME** (+2.5) | **OVER** (162.5) | 23% |

> 📈 *ATS = Against The Spread (with Vegas lines). Updated daily via GitHub Actions.*

<!-- ACCURACY_STATS_END -->

<!-- RANKINGS_START -->

### 🏆 Top 25 Team Rankings

*Updated: February 07, 2026*

| Rank | Team | Record | Rating | Off | Def |
|------|------|--------|--------|-----|-----|
| 1 | Michigan Wolverines | 21-1 | +30.9 | 72.5 | 41.6 |
| 2 | Arizona Wildcats | 22-0 | +27.4 | 69.8 | 42.4 |
| 3 | Duke Blue Devils | 21-1 | +26.1 | 64.9 | 38.8 |
| 4 | Iowa State Cyclones | 20-2 | +25.9 | 67.3 | 41.4 |
| 5 | Louisville Cardinals | 16-6 | +25.7 | 68.8 | 43.5 |
| 6 | Illinois Fighting Illini | 20-3 | +25.5 | 66.8 | 41.4 |
| 7 | Florida Gators | 16-6 | +24.6 | 66.0 | 41.9 |
| 8 | Purdue Boilermakers | 18-4 | +24.4 | 66.1 | 41.7 |
| 9 | Gonzaga Bulldogs | 22-2 | +24.2 | 65.8 | 41.6 |
| 10 | Alabama Crimson Tide | 15-7 | +24.1 | 72.3 | 48.2 |
| 11 | Vanderbilt Commodores | 19-3 | +24.0 | 68.6 | 44.5 |
| 12 | Houston Cougars | 20-2 | +24.0 | 61.8 | 37.9 |
| 13 | BYU Cougars | 17-5 | +23.2 | 68.2 | 45.3 |
| 14 | Arkansas Razorbacks | 16-6 | +23.1 | 70.2 | 47.2 |
| 15 | UConn Huskies | 22-2 | +22.9 | 62.7 | 39.8 |
| 16 | Kansas Jayhawks | 17-5 | +22.8 | 63.4 | 40.7 |
| 17 | St. John's Red Storm | 18-5 | +22.8 | 66.0 | 43.3 |
| 18 | Tennessee Volunteers | 16-6 | +22.2 | 63.6 | 41.8 |
| 19 | NC State Wolfpack | 17-6 | +22.0 | 67.0 | 45.3 |
| 20 | Kentucky Wildcats | 16-7 | +21.6 | 65.1 | 43.8 |
| 21 | Saint Louis Billikens | 22-1 | +21.5 | 67.7 | 46.2 |
| 22 | Texas Tech Red Raiders | 16-6 | +21.4 | 65.0 | 43.6 |
| 23 | Michigan State Spartans | 19-4 | +21.3 | 60.7 | 39.5 |
| 24 | Georgia Bulldogs | 16-6 | +21.2 | 70.1 | 49.3 |
| 25 | Nebraska Cornhuskers | 20-2 | +20.8 | 61.0 | 40.6 |

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

