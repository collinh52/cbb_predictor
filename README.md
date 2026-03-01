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

**Last Updated**: March 01, 2026 at 05:15 AM

![ATS Accuracy](https://img.shields.io/badge/ATS_Record-50.8%25-yellowgreen)

#### 🏆 Rolling ATS Performance

| Timeframe | ATS Record | Accuracy |
|-----------|------------|----------|
| **Latest** (2026-02-28) | 69-58 | **54.3%** |
| **Last 7 Days** | 165-154 | **51.7%** |
| **Last 30 Days** | 459-444 | **50.8%** |
| **All-Time** | 459-444 | **50.8%** |

**Over/Under Accuracy**: 50.5%

#### 🎯 Accuracy by Confidence (ATS)

| Confidence | Record | Accuracy |
|------------|--------|----------|
| **50%+** | 132-135 | **49.4%** |
| **60%+** | 54-49 | **52.4%** |
| **70%+** | 19-17 | **52.8%** |
| **80%+** | 5-5 | **50.0%** |

#### 🏀 ATS Accuracy by Conference

| Conference | Record | Accuracy |
|------------|--------|----------|
| Big South | 19-6 | **76.0%** |
| Western Athletic | 14-5 | **73.7%** |
| Southern | 19-11 | **63.3%** |
| Summit League | 11-7 | **61.1%** |
| Ivy League | 10-7 | **58.8%** |
| Mountain West | 17-12 | **58.6%** |
| Atlantic Coast | 27-20 | **57.4%** |
| Southeastern | 25-19 | **56.8%** |
| Mid-American | 19-15 | **55.9%** |
| Atlantic 10 | 17-14 | **54.8%** |
| America East | 13-11 | **54.2%** |
| ASUN | 19-17 | **52.8%** |
| Southwestern Athletic | 14-13 | **51.9%** |
| Patriot League | 9-9 | **50.0%** |
| Big East | 14-14 | **50.0%** |
| Missouri Valley | 13-13 | **50.0%** |
| Ohio Valley | 16-16 | **50.0%** |
| Mid-Eastern Athletic | 9-9 | **50.0%** |
| Big 12 | 20-21 | **48.8%** |
| Coastal Athletic Association | 16-17 | **48.5%** |
| Conference USA | 14-15 | **48.3%** |
| Southland | 12-13 | **48.0%** |
| Big Sky | 12-15 | **44.4%** |
| Horizon League | 11-14 | **44.0%** |
| Big Ten | 19-25 | **43.2%** |
| West Coast | 10-14 | **41.7%** |
| Big West | 12-17 | **41.4%** |
| Northeast | 10-15 | **40.0%** |
| Metro Atlantic Athletic | 12-18 | **40.0%** |
| Sun Belt | 16-25 | **39.0%** |
| American | 12-19 | **38.7%** |

> *A game counts for a conference if either team is a member.*

#### Combined Statistics

- **Total Predictions**: 903
- **Overall Winner Accuracy**: 50.8%

#### 📅 Recent Predictions (2026-02-28)

| Matchup | Spread Pick | Total Pick | Confidence |
|---------|-------------|------------|------------|
| Seattle Redhawks @ Loyola Marymount Lions | **HOME** (+0.0) | **OVER** (137.5) | 55% |
| Oral Roberts Golden Eagles @ UMKC Kangaroos | **AWAY** (-4.5) | **UNDER** (148.5) | 71% |
| Fort Wayne Mastodons @ IUPUI Jaguars | **AWAY** (-1.0) | **UNDER** (161.5) | 95% |
| Florida A&M Rattlers @ Grambling St Tigers | **AWAY** (+5.0) | **OVER** (139.0) | 52% |
| Duquesne Dukes @ Saint Louis Billikens | **HOME** (-15.5) | **UNDER** (161.5) | 67% |
| SE Louisiana Lions @ Nicholls St Colonels | **AWAY** (+5.0) | **UNDER** (140.0) | 61% |
| Colorado Buffaloes @ Houston Cougars | **AWAY** (+19.5) | **UNDER** (139.5) | 60% |
| Abilene Christian Wildcats @ Utah Valley Wolverines | **AWAY** (+15.0) | **UNDER** (140.5) | 65% |
| Fairleigh Dickinson Knights @ LIU Sharks | **AWAY** (+9.0) | **UNDER** (137.0) | 56% |
| Seton Hall Pirates @ UConn Huskies | **HOME** (-13.5) | **UNDER** (130.5) | 74% |
| Oregon St Beavers @ Santa Clara Broncos | **AWAY** (+16.5) | **UNDER** (153.0) | 48% |
| Omaha Mavericks @ St. Thomas (MN) Tommies | **HOME** (-12.0) | **UNDER** (157.5) | 49% |
| Fordham Rams @ VCU Rams | **AWAY** (+12.5) | **UNDER** (143.5) | 71% |
| Missouri St Bears @ Sam Houston St Bearkats | **AWAY** (+7.0) | **UNDER** (154.5) | 81% |
| Massachusetts Minutemen @ Bowling Green Falcons | **HOME** (-6.0) | **OVER** (153.0) | 57% |
| Colgate Raiders @ Navy Midshipmen | **HOME** (-7.0) | **UNDER** (143.0) | 55% |
| Boston College Eagles @ Miami Hurricanes | **AWAY** (+15.5) | **UNDER** (143.5) | 62% |
| Stony Brook Seawolves @ Hofstra Pride | **AWAY** (+12.5) | **UNDER** (141.0) | 64% |
| Villanova Wildcats @ St. John's Red Storm | **HOME** (-7.5) | **UNDER** (146.5) | 67% |
| North Dakota Fighting Hawks @ North Dakota St Bison | **AWAY** (+11.5) | **OVER** (151.0) | 53% |
| Grand Canyon Antelopes @ Utah State Aggies | **AWAY** (+9.5) | **UNDER** (148.5) | 62% |
| Arkansas Razorbacks @ Florida Gators | **HOME** (-8.5) | **UNDER** (167.5) | 56% |
| Delaware Blue Hens @ Kennesaw St Owls | **AWAY** (+11.0) | **OVER** (145.0) | 64% |
| Virginia Tech Hokies @ North Carolina Tar Heels | **HOME** (-6.5) | **UNDER** (149.5) | 60% |
| Brown Bears @ Cornell Big Red | **AWAY** (+9.5) | **UNDER** (158.5) | 56% |
| Oklahoma St Cowboys @ Cincinnati Bearcats | **AWAY** (+9.5) | **UNDER** (149.5) | 47% |
| Detroit Mercy Titans @ Oakland Golden Grizzlies | **HOME** (-8.0) | **UNDER** (161.5) | 63% |
| Presbyterian Blue Hose @ Winthrop Eagles | **AWAY** (+9.0) | **UNDER** (149.0) | 47% |
| South Carolina Gamecocks @ Georgia Bulldogs | **AWAY** (+11.5) | **UNDER** (159.5) | 57% |
| UTEP Miners @ Western Kentucky Hilltoppers | **AWAY** (+9.5) | **UNDER** (144.5) | 53% |
| Northwestern St Demons @ Texas A&M-CC Islanders | **HOME** (-7.0) | **UNDER** (134.0) | 70% |
| Cleveland St Vikings @ Robert Morris Colonials | **AWAY** (+13.0) | **UNDER** (158.5) | 46% |
| Ole Miss Rebels @ Auburn Tigers | **AWAY** (+9.5) | **OVER** (152.5) | 53% |
| Air Force Falcons @ Wyoming Cowboys | **AWAY** (+21.5) | **UNDER** (147.5) | 58% |
| UNC Greensboro Spartans @ Samford Bulldogs | **AWAY** (+9.0) | **OVER** (157.0) | 50% |
| East Texas A&M Lions @ UT Rio Grande Valley Vaqueros | **AWAY** (+10.5) | **UNDER** (146.0) | 80% |
| Sacramento St Hornets @ Montana St Bobcats | **AWAY** (+9.5) | **OVER** (157.5) | 47% |
| Eastern Illinois Panthers @ SIU-Edwardsville Cougars | **HOME** (-6.0) | **UNDER** (130.0) | 61% |
| N Colorado Bears @ Idaho Vandals | **HOME** (-2.5) | **UNDER** (155.0) | 57% |
| Miss Valley St Delta Devils @ Arkansas-Pine Bluff Golden Lions | **AWAY** (+13.5) | **OVER** (147.5) | 47% |
| St. Bonaventure Bonnies @ George Mason Patriots | **HOME** (-4.5) | **UNDER** (146.5) | 50% |
| Northern Arizona Lumberjacks @ Eastern Washington Eagles | **AWAY** (+10.0) | **UNDER** (147.5) | 42% |
| McNeese Cowboys @ New Orleans Privateers | **HOME** (+8.5) | **OVER** (152.5) | 38% |
| Utah Utes @ Arizona St Sun Devils | **AWAY** (+6.5) | **UNDER** (150.5) | 62% |
| Texas Longhorns @ Texas A&M Aggies | **HOME** (-3.5) | **UNDER** (161.5) | 38% |
| The Citadel Bulldogs @ Wofford Terriers | **AWAY** (+12.5) | **UNDER** (149.0) | 47% |
| Tarleton State Texans @ Cal Baptist Lancers | **AWAY** (+7.5) | **UNDER** (139.0) | 70% |
| Tennessee Tech Golden Eagles @ SE Missouri St Redhawks | **AWAY** (+7.5) | **UNDER** (141.5) | 54% |
| Providence Friars @ Creighton Bluejays | **HOME** (-2.5) | **OVER** (166.5) | 34% |
| Georgetown Hoyas @ Xavier Musketeers | **HOME** (-4.5) | **UNDER** (154.5) | 38% |
| Furman Paladins @ Western Carolina Catamounts | **HOME** (+0.0) | **UNDER** (148.0) | 45% |
| Alabama Crimson Tide @ Tennessee Volunteers | **HOME** (-4.5) | **UNDER** (164.5) | 40% |
| Southern Indiana Screaming Eagles @ Arkansas-Little Rock Trojans | **AWAY** (+6.5) | **UNDER** (140.5) | 38% |
| Alcorn St Braves @ Prairie View Panthers | **AWAY** (+6.0) | **UNDER** (154.5) | 50% |
| Northeastern Huskies @ Hampton Pirates | **HOME** (-4.5) | **UNDER** (146.5) | 36% |
| Boston Univ. Terriers @ American Eagles | **HOME** (-2.5) | **UNDER** (142.5) | 37% |
| Cal Poly Mustangs @ UC San Diego Tritons | **AWAY** (+6.5) | **UNDER** (162.5) | 65% |
| Oregon Ducks @ Northwestern Wildcats | **HOME** (-4.5) | **UNDER** (142.5) | 58% |
| San Francisco Dons @ Pacific Tigers | **HOME** (-4.0) | **UNDER** (142.0) | 41% |
| Queens University Royals @ Central Arkansas Bears | **HOME** (-2.5) | **OVER** (164.5) | 35% |
| Ball State Cardinals @ Northern Illinois Huskies | **HOME** (-1.0) | **UNDER** (132.5) | 61% |
| Campbell Fighting Camels @ Towson Tigers | **AWAY** (+4.5) | **UNDER** (142.5) | 47% |
| St. Francis (PA) Red Flash @ Central Connecticut St Blue Devils | **AWAY** (+8.5) | **UNDER** (156.5) | 35% |
| Elon Phoenix @ Monmouth Hawks | **HOME** (-3.5) | **UNDER** (153.5) | 38% |
| VMI Keydets @ Chattanooga Mocs | **AWAY** (+12.0) | **UNDER** (153.0) | 57% |
| Charleston Southern Buccaneers @ UNC Asheville Bulldogs | **AWAY** (+4.5) | **UNDER** (149.5) | 31% |
| Tennessee St Tigers @ Tenn-Martin Skyhawks | **HOME** (-3.0) | **UNDER** (144.0) | 48% |
| Valparaiso Beacons @ Evansville Purple Aces | **HOME** (+4.5) | **UNDER** (137.5) | 39% |
| Gardner-Webb Bulldogs @ South Carolina Upstate Spartans | **AWAY** (+12.5) | **UNDER** (152.5) | 50% |
| NC State Wolfpack @ Notre Dame Fighting Irish | **HOME** (+6.5) | **UNDER** (153.5) | 30% |
| San Diego St Aztecs @ New Mexico Lobos | **HOME** (-2.5) | **UNDER** (148.5) | 29% |
| East Tennessee St Buccaneers @ Mercer Bears | **HOME** (-1.0) | **UNDER** (151.5) | 31% |
| Jackson St Tigers @ Texas Southern Tigers | **AWAY** (+6.0) | **OVER** (152.0) | 66% |
| New Hampshire Wildcats @ Albany Great Danes | **HOME** (-3.0) | **UNDER** (140.0) | 38% |
| North Alabama Lions @ West Georgia Wolves | **AWAY** (+5.5) | **UNDER** (145.0) | 30% |
| UC Santa Barbara Gauchos @ UC Irvine Anteaters | **HOME** (-3.0) | **UNDER** (140.0) | 37% |
| Wright St Raiders @ Northern Kentucky Norse | **HOME** (-2.0) | **UNDER** (153.0) | 34% |
| San Diego Toreros @ Portland Pilots | **HOME** (-3.5) | **OVER** (149.5) | 38% |
| Saint Joseph's Hawks @ Rhode Island Rams | **HOME** (-3.5) | **UNDER** (140.5) | 44% |
| Florida Int'l Golden Panthers @ Louisiana Tech Bulldogs | **HOME** (-2.5) | **UNDER** (145.5) | 31% |
| TCU Horned Frogs @ Kansas St Wildcats | **HOME** (+3.5) | **UNDER** (157.5) | 45% |
| Vanderbilt Commodores @ Kentucky Wildcats | **HOME** (-1.5) | **UNDER** (154.5) | 42% |
| South Carolina St Bulldogs @ Maryland-Eastern Shore Hawks | **AWAY** (+6.0) | **UNDER** (136.0) | 58% |
| Pittsburgh Panthers @ California Golden Bears | **AWAY** (+7.5) | **UNDER** (141.5) | 30% |
| New Mexico St Aggies @ Middle Tennessee Blue Raiders | **AWAY** (+5.0) | **OVER** (147.0) | 28% |
| Howard Bison @ Morgan St Bears | **HOME** (+9.0) | **UNDER** (155.0) | 49% |
| Louisville Cardinals @ Clemson Tigers | **AWAY** (-1.5) | **UNDER** (146.5) | 49% |
| Toledo Rockets @ Ohio Bobcats | **HOME** (-1.0) | **UNDER** (159.0) | 36% |
| Boise State Broncos @ Fresno St Bulldogs | **HOME** (+7.0) | **OVER** (149.5) | 24% |
| Utah Tech Trailblazers @ Southern Utah Thunderbirds | **HOME** (+1.5) | **OVER** (156.5) | 33% |
| UMBC Retrievers @ UMass Lowell River Hawks | **HOME** (+1.5) | **UNDER** (147.5) | 27% |
| Stephen F. Austin Lumberjacks @ Houston Christian Huskies | **HOME** (+8.0) | **UNDER** (139.0) | 36% |
| Mercyhurst Lakers @ Stonehill Skyhawks | **HOME** (+1.5) | **OVER** (135.5) | 31% |
| Maine Black Bears @ Binghamton Bearcats | **HOME** (-1.0) | **OVER** (132.5) | 39% |
| Nevada Wolf Pack @ UNLV Rebels | **HOME** (+1.5) | **OVER** (151.5) | 23% |
| Syracuse Orange @ Wake Forest Demon Deacons | **AWAY** (+3.5) | **OVER** (151.5) | 25% |
| Iowa Hawkeyes @ Penn State Nittany Lions | **HOME** (+9.5) | **UNDER** (145.5) | 40% |
| Portland St Vikings @ Montana Grizzlies | **HOME** (+0.0) | **UNDER** (143.5) | 52% |
| Oklahoma Sooners @ LSU Tigers | **HOME** (-1.5) | **OVER** (155.5) | 28% |
| Lamar Cardinals @ Incarnate Word Cardinals | **HOME** (+1.5) | **UNDER** (142.5) | 48% |
| Harvard Crimson @ Pennsylvania Quakers | **HOME** (-1.5) | **UNDER** (137.5) | 41% |
| Bucknell Bison @ Lehigh Mountain Hawks | **AWAY** (+6.0) | **OVER** (140.0) | 40% |
| Weber State Wildcats @ Idaho State Bengals | **HOME** (-2.0) | **OVER** (153.5) | 22% |
| Missouri Tigers @ Mississippi St Bulldogs | **HOME** (+1.5) | **UNDER** (155.5) | 26% |
| Le Moyne Dolphins @ New Haven Chargers | **HOME** (+1.0) | **UNDER** (136.0) | 21% |
| Washington St Cougars @ Pepperdine Waves | **HOME** (+7.5) | **OVER** (158.0) | 19% |
| Long Beach St 49ers @ CSU Bakersfield Roadrunners | **HOME** (+4.5) | **UNDER** (153.5) | 15% |
| Radford Highlanders @ Longwood Lancers | **HOME** (+1.0) | **OVER** (154.0) | 14% |
| CSU Northridge Matadors @ UC Riverside Highlanders | **HOME** (+4.5) | **UNDER** (157.0) | 28% |
| Bethune-Cookman Wildcats @ Southern Jaguars | **AWAY** (+1.5) | **OVER** (151.0) | 28% |
| Nebraska Cornhuskers @ USC Trojans | **HOME** (+4.5) | **UNDER** (147.5) | 35% |
| BYU Cougars @ West Virginia Mountaineers | **HOME** (+2.5) | **UNDER** (142.5) | 19% |
| Youngstown St Penguins @ Green Bay Phoenix | **HOME** (-1.0) | **UNDER** (143.0) | 11% |
| North Carolina Central Eagles @ Delaware St Hornets | **HOME** (+2.0) | **UNDER** (135.5) | 45% |
| Norfolk St Spartans @ Coppin St Eagles | **HOME** (+8.5) | **OVER** (143.0) | 27% |
| South Dakota St Jackrabbits @ South Dakota Coyotes | **HOME** (+3.0) | **UNDER** (151.0) | 13% |
| Jacksonville Dolphins @ North Florida Ospreys | **HOME** (+1.0) | **OVER** (150.0) | 8% |
| Chicago St Cougars @ Wagner Seahawks | **AWAY** (+5.0) | **UNDER** (136.0) | 18% |
| William & Mary Tribe @ North Carolina A&T Aggies | **HOME** (+6.0) | **UNDER** (164.0) | 28% |
| Colorado St Rams @ San José St Spartans | **HOME** (+8.0) | **OVER** (145.0) | 9% |
| SMU Mustangs @ Stanford Cardinal | **HOME** (+1.5) | **UNDER** (155.5) | 25% |
| Baylor Bears @ UCF Knights | **AWAY** (+2.5) | **UNDER** (158.5) | 10% |
| Lipscomb Bisons @ Eastern Kentucky Colonels | **HOME** (+2.5) | **UNDER** (159.0) | 7% |
| Hawai'i Rainbow Warriors @ CSU Fullerton Titans | **HOME** (+3.0) | **UNDER** (158.5) | 18% |
| Dartmouth Big Green @ Princeton Tigers | **AWAY** (+1.5) | **UNDER** (143.5) | 32% |
| Army Knights @ Lafayette Leopards | **AWAY** (+4.5) | **OVER** (142.5) | 20% |
| Loyola (MD) Greyhounds @ Holy Cross Crusaders | **AWAY** (+1.5) | **UNDER** (149.5) | 5% |
| Lindenwood Lions @ Western Illinois Leathernecks | **HOME** (+11.0) | **UNDER** (149.0) | 20% |
| Liberty Flames @ Jacksonville St Gamecocks | **HOME** (+4.0) | **UNDER** (140.0) | 5% |
| Yale Bulldogs @ Columbia Lions | **HOME** (+5.5) | **UNDER** (151.5) | 26% |
| Austin Peay Governors @ Bellarmine Knights | **HOME** (+4.5) | **UNDER** (156.5) | 16% |
| Florida Gulf Coast Eagles @ Stetson Hatters | **HOME** (+2.5) | **OVER** (150.5) | 6% |
| NJIT Highlanders @ Bryant Bulldogs | **HOME** (+2.5) | **OVER** (140.0) | 3% |
| Central Michigan Chippewas @ Buffalo Bulls | **AWAY** (+5.5) | **OVER** (150.5) | 11% |
| Gonzaga Bulldogs @ Saint Mary's Gaels | **HOME** (+1.5) | **UNDER** (143.5) | 18% |
| Richmond Spiders @ Loyola (Chi) Ramblers | **HOME** (+4.5) | **UNDER** (146.0) | 9% |
| Florida St Seminoles @ Georgia Tech Yellow Jackets | **HOME** (+5.5) | **UNDER** (159.5) | 17% |
| UCLA Bruins @ Minnesota Golden Gophers | **HOME** (+1.5) | **OVER** (135.5) | 3% |
| Wisconsin Badgers @ Washington Huskies | **HOME** (+1.5) | **UNDER** (153.5) | 20% |
| Alabama St Hornets @ Alabama A&M Bulldogs | **AWAY** (+2.0) | **UNDER** (142.0) | 26% |

> 📈 *ATS = Against The Spread (with Vegas lines). Updated daily via GitHub Actions.*

<!-- ACCURACY_STATS_END -->

<!-- RANKINGS_START -->

### 🏆 Top 25 Team Rankings

*Updated: March 01, 2026*

| Rank | Team | Record | Rating | Off | Def |
|------|------|--------|--------|-----|-----|
| 1 | Michigan Wolverines | 27-2 | +30.7 | 71.8 | 41.1 |
| 2 | Duke Blue Devils | 27-2 | +28.1 | 65.7 | 37.6 |
| 3 | Arizona Wildcats | 27-2 | +27.8 | 68.9 | 41.1 |
| 4 | Illinois Fighting Illini | 22-7 | +26.4 | 67.7 | 41.8 |
| 5 | Florida Gators | 23-6 | +25.6 | 66.8 | 41.5 |
| 6 | Louisville Cardinals | 20-9 | +25.6 | 69.0 | 43.9 |
| 7 | Alabama Crimson Tide | 22-7 | +24.9 | 72.9 | 48.2 |
| 8 | Iowa State Cyclones | 24-5 | +24.9 | 65.3 | 40.7 |
| 9 | Gonzaga Bulldogs | 28-2 | +24.8 | 65.7 | 40.9 |
| 10 | Purdue Boilermakers | 22-6 | +24.4 | 66.1 | 41.7 |
| 11 | Arkansas Razorbacks | 21-8 | +23.9 | 71.0 | 47.1 |
| 12 | Houston Cougars | 24-5 | +23.6 | 61.0 | 37.4 |
| 13 | UConn Huskies | 27-3 | +23.2 | 63.1 | 39.9 |
| 14 | Vanderbilt Commodores | 22-7 | +23.2 | 67.5 | 44.3 |
| 15 | BYU Cougars | 20-9 | +23.0 | 68.6 | 46.0 |
| 16 | Texas Tech Red Raiders | 22-7 | +22.8 | 65.5 | 42.7 |
| 17 | St. John's Red Storm | 23-6 | +22.5 | 65.0 | 42.5 |
| 18 | Michigan State Spartans | 23-5 | +22.4 | 62.0 | 39.6 |
| 19 | Kansas Jayhawks | 21-8 | +22.2 | 62.8 | 40.6 |
| 20 | Tennessee Volunteers | 20-9 | +22.0 | 62.7 | 41.1 |
| 21 | Kentucky Wildcats | 19-10 | +21.9 | 65.0 | 43.4 |
| 22 | Georgia Bulldogs | 20-9 | +21.6 | 69.2 | 47.9 |
| 23 | Nebraska Cornhuskers | 25-4 | +21.2 | 61.4 | 40.2 |
| 24 | Saint Louis Billikens | 26-3 | +21.0 | 67.1 | 46.1 |
| 25 | NC State Wolfpack | 19-10 | +20.9 | 66.4 | 45.8 |

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

