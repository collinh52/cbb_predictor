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

**Last Updated**: February 21, 2026 at 12:30 PM

![ATS Accuracy](https://img.shields.io/badge/ATS_Record-51.7%25-yellowgreen)

#### 🏆 Rolling ATS Performance

| Timeframe | ATS Record | Accuracy |
|-----------|------------|----------|
| **Latest** (2026-02-20) | 6-7 | **46.2%** |
| **Last 7 Days** | 167-149 | **52.8%** |
| **Last 30 Days** | 229-214 | **51.7%** |
| **All-Time** | 229-214 | **51.7%** |

**Over/Under Accuracy**: 48.8%

#### 🎯 Accuracy by Confidence (ATS)

| Confidence | Record | Accuracy |
|------------|--------|----------|
| **50%+** | 69-58 | **54.3%** |
| **60%+** | 29-17 | **63.0%** |
| **70%+** | 11-6 | **64.7%** |
| **80%+** | 3-1 | **75.0%** |

#### 🏀 ATS Accuracy by Conference

| Conference | Record | Accuracy |
|------------|--------|----------|
| Western Athletic | 9-1 | **90.0%** |
| Big South | 11-2 | **84.6%** |
| Southeastern | 15-5 | **75.0%** |
| Southern | 11-4 | **73.3%** |
| Ivy League | 4-2 | **66.7%** |
| Mid-Eastern Athletic | 6-3 | **66.7%** |
| Ohio Valley | 10-6 | **62.5%** |
| Big East | 8-5 | **61.5%** |
| Atlantic 10 | 9-6 | **60.0%** |
| America East | 7-5 | **58.3%** |
| Atlantic Coast | 12-9 | **57.1%** |
| Conference USA | 8-6 | **57.1%** |
| Missouri Valley | 8-7 | **53.3%** |
| Big 12 | 9-8 | **52.9%** |
| American | 10-9 | **52.6%** |
| ASUN | 9-9 | **50.0%** |
| Southwestern Athletic | 7-7 | **50.0%** |
| Southland | 5-5 | **50.0%** |
| Mountain West | 6-7 | **46.2%** |
| West Coast | 5-6 | **45.5%** |
| Patriot League | 4-5 | **44.4%** |
| Mid-American | 8-10 | **44.4%** |
| Sun Belt | 9-12 | **42.9%** |
| Horizon League | 5-7 | **41.7%** |
| Big West | 6-9 | **40.0%** |
| Big Sky | 5-8 | **38.5%** |
| Coastal Athletic Association | 6-10 | **37.5%** |
| Summit League | 3-6 | **33.3%** |
| Northeast | 4-8 | **33.3%** |
| Metro Atlantic Athletic | 5-13 | **27.8%** |
| Big Ten | 6-16 | **27.3%** |

> *A game counts for a conference if either team is a member.*

#### Combined Statistics

- **Total Predictions**: 443
- **Overall Winner Accuracy**: 51.7%

#### 📅 Predictions for Today (2026-02-21)

| Matchup | Spread Pick | Total Pick | Confidence |
|---------|-------------|------------|------------|
| UMKC Kangaroos @ North Dakota St Bison | **HOME** (-18.5) | **UNDER** (146.5) | 56% |
| Nicholls St Colonels @ Stephen F. Austin Lumberjacks | **HOME** (-13.0) | **UNDER** (148.0) | 76% |
| Grambling St Tigers @ Southern Jaguars | **HOME** (-5.0) | **OVER** (142.0) | 70% |
| Georgia Tech Yellow Jackets @ Louisville Cardinals | **AWAY** (+22.5) | **UNDER** (164.5) | 73% |
| LIU Sharks @ Mercyhurst Lakers | **HOME** (+2.5) | **OVER** (134.5) | 57% |
| Pacific Tigers @ Gonzaga Bulldogs | **AWAY** (+21.0) | **UNDER** (145.0) | 61% |
| Winthrop Eagles @ High Point Panthers | **HOME** (-8.5) | **UNDER** (165.0) | 55% |
| Texas A&M-CC Islanders @ McNeese Cowboys | **AWAY** (+14.5) | **OVER** (139.5) | 51% |
| Portland Pilots @ Seattle Redhawks | **AWAY** (+8.5) | **OVER** (140.5) | 49% |
| Boston College Eagles @ SMU Mustangs | **AWAY** (+15.5) | **UNDER** (150.5) | 69% |
| Jacksonville St Gamecocks @ Sam Houston St Bearkats | **AWAY** (+7.5) | **UNDER** (149.5) | 90% |
| North Carolina Central Eagles @ Howard Bison | **AWAY** (+12.5) | **UNDER** (142.5) | 95% |
| Penn State Nittany Lions @ Nebraska Cornhuskers | **AWAY** (+18.5) | **UNDER** (148.5) | 67% |
| Pennsylvania Quakers @ Yale Bulldogs | **HOME** (-10.5) | **UNDER** (152.0) | 64% |
| Indiana St Sycamores @ Belmont Bruins | **AWAY** (+13.5) | **OVER** (157.0) | 57% |
| Arizona St Sun Devils @ Baylor Bears | **HOME** (-6.5) | **UNDER** (157.5) | 56% |
| Creighton Bluejays @ St. John's Red Storm | **AWAY** (+12.5) | **UNDER** (153.5) | 60% |
| North Alabama Lions @ Lipscomb Bisons | **AWAY** (+13.0) | **OVER** (148.0) | 49% |
| Evansville Purple Aces @ Murray St Racers | **AWAY** (+14.0) | **UNDER** (154.5) | 65% |
| Binghamton Bearcats @ UMass Lowell River Hawks | **AWAY** (+9.0) | **OVER** (146.0) | 62% |
| Harvard Crimson @ Cornell Big Red | **HOME** (-4.0) | **OVER** (155.5) | 51% |
| Delaware St Hornets @ Morgan St Bears | **HOME** (-5.5) | **UNDER** (146.5) | 92% |
| West Georgia Wolves @ Queens University Royals | **AWAY** (+11.5) | **UNDER** (162.0) | 51% |
| San José St Spartans @ Boise State Broncos | **AWAY** (+16.0) | **OVER** (144.0) | 74% |
| Georgia Southern Eagles @ Appalachian St Mountaineers | **HOME** (-7.0) | **UNDER** (148.5) | 83% |
| Miami Hurricanes @ Virginia Cavaliers | **AWAY** (+8.5) | **UNDER** (145.5) | 54% |
| Temple Owls @ Wichita St Shockers | **AWAY** (+8.5) | **UNDER** (143.0) | 66% |
| Kansas St Wildcats @ Texas Tech Red Raiders | **AWAY** (+13.5) | **UNDER** (159.5) | 71% |
| Western Kentucky Hilltoppers @ Liberty Flames | **HOME** (-7.5) | **UNDER** (145.5) | 58% |
| South Carolina St Bulldogs @ Norfolk St Spartans | **AWAY** (+10.0) | **UNDER** (146.5) | 88% |
| Southern Illinois Salukis @ Northern Iowa Panthers | **HOME** (-6.0) | **UNDER** (132.5) | 82% |
| Duquesne Dukes @ Dayton Flyers | **HOME** (-6.0) | **OVER** (148.5) | 44% |
| North Dakota Fighting Hawks @ South Dakota St Jackrabbits | **HOME** (-6.5) | **UNDER** (152.0) | 53% |
| Valparaiso Beacons @ UIC Flames | **HOME** (-7.0) | **UNDER** (139.0) | 53% |
| Alabama A&M Bulldogs @ Bethune-Cookman Wildcats | **HOME** (-7.0) | **UNDER** (141.5) | 64% |
| Northern Arizona Lumberjacks @ N Colorado Bears | **AWAY** (+12.5) | **UNDER** (148.0) | 46% |
| UTEP Miners @ New Mexico St Aggies | **AWAY** (+7.0) | **OVER** (140.5) | 45% |
| Dartmouth Big Green @ Columbia Lions | **AWAY** (+6.5) | **UNDER** (152.0) | 54% |
| UC Santa Barbara Gauchos @ Hawai'i Rainbow Warriors | **HOME** (-3.5) | **UNDER** (147.0) | 45% |
| Wyoming Cowboys @ Grand Canyon Antelopes | **AWAY** (+8.0) | **UNDER** (145.0) | 58% |
| Albany Great Danes @ UMBC Retrievers | **AWAY** (+6.5) | **UNDER** (143.5) | 44% |
| UC San Diego Tritons @ UC Irvine Anteaters | **HOME** (-4.5) | **UNDER** (141.0) | 70% |
| Prairie View Panthers @ Arkansas-Pine Bluff Golden Lions | **HOME** (-3.0) | **UNDER** (158.5) | 48% |
| Samford Bulldogs @ Mercer Bears | **HOME** (-4.0) | **UNDER** (156.0) | 52% |
| St. Bonaventure Bonnies @ Richmond Spiders | **HOME** (-2.5) | **UNDER** (149.5) | 44% |
| North Carolina A&T Aggies @ Elon Phoenix | **AWAY** (+7.5) | **OVER** (152.0) | 43% |
| Delaware Blue Hens @ Middle Tennessee Blue Raiders | **AWAY** (+8.5) | **OVER** (137.5) | 51% |
| Louisiana Tech Bulldogs @ Kennesaw St Owls | **AWAY** (+7.0) | **UNDER** (148.0) | 42% |
| Incarnate Word Cardinals @ East Texas A&M Lions | **HOME** (-2.0) | **UNDER** (146.0) | 75% |
| Florida St Seminoles @ Clemson Tigers | **AWAY** (+8.5) | **UNDER** (145.5) | 64% |
| Notre Dame Fighting Irish @ Pittsburgh Panthers | **HOME** (-1.5) | **OVER** (137.5) | 38% |
| Eastern Washington Eagles @ Portland St Vikings | **AWAY** (+6.0) | **UNDER** (146.0) | 49% |
| SIU-Edwardsville Cougars @ Tennessee St Tigers | **HOME** (-4.5) | **OVER** (143.5) | 39% |
| Texas Longhorns @ Georgia Bulldogs | **HOME** (-2.5) | **UNDER** (164.5) | 42% |
| Montana Grizzlies @ Weber State Wildcats | **HOME** (-2.0) | **UNDER** (152.5) | 46% |
| Western Michigan Broncos @ Central Michigan Chippewas | **HOME** (-4.0) | **OVER** (150.0) | 43% |
| Southern Indiana Screaming Eagles @ Eastern Illinois Panthers | **HOME** (-4.0) | **UNDER** (136.0) | 51% |
| South Dakota Coyotes @ Oral Roberts Golden Eagles | **HOME** (-1.0) | **UNDER** (153.0) | 44% |
| Xavier Musketeers @ Butler Bulldogs | **HOME** (-3.5) | **OVER** (159.5) | 36% |
| Arkansas St Red Wolves @ UL Monroe Warhawks | **HOME** (+14.5) | **UNDER** (165.0) | 65% |
| Eastern Michigan Eagles @ Toledo Rockets | **AWAY** (+8.5) | **UNDER** (146.5) | 40% |
| Missouri St Bears @ Florida Int'l Golden Panthers | **HOME** (-4.0) | **UNDER** (155.5) | 36% |
| Mississippi St Bulldogs @ South Carolina Gamecocks | **HOME** (-1.5) | **UNDER** (151.5) | 59% |
| Pepperdine Waves @ Oregon St Beavers | **AWAY** (+9.0) | **UNDER** (147.5) | 53% |
| Hampton Pirates @ Stony Brook Seawolves | **HOME** (-4.5) | **UNDER** (135.5) | 40% |
| Loyola (MD) Greyhounds @ Colgate Raiders | **AWAY** (+8.5) | **UNDER** (152.0) | 33% |
| Wagner Seahawks @ St. Francis (PA) Red Flash | **HOME** (+1.5) | **UNDER** (152.0) | 67% |
| Georgetown Hoyas @ Seton Hall Pirates | **AWAY** (+4.5) | **UNDER** (135.5) | 52% |
| Rutgers Scarlet Knights @ Minnesota Golden Gophers | **AWAY** (+7.5) | **UNDER** (135.5) | 33% |
| Maine Black Bears @ New Hampshire Wildcats | **HOME** (-3.5) | **OVER** (134.5) | 41% |
| Saint Mary's Gaels @ Washington St Cougars | **HOME** (+8.0) | **UNDER** (149.5) | 46% |
| Oklahoma St Cowboys @ Colorado Buffaloes | **HOME** (-3.5) | **UNDER** (162.5) | 42% |
| Eastern Kentucky Colonels @ Bellarmine Knights | **HOME** (-1.5) | **OVER** (157.5) | 42% |
| Buffalo Bulls @ Massachusetts Minutemen | **AWAY** (+7.5) | **OVER** (156.5) | 36% |
| UNC Wilmington Seahawks @ Campbell Fighting Camels | **HOME** (+2.5) | **UNDER** (151.0) | 44% |
| Longwood Lancers @ Charleston Southern Buccaneers | **HOME** (-4.0) | **OVER** (152.5) | 36% |
| Southern Utah Thunderbirds @ Abilene Christian Wildcats | **AWAY** (+6.5) | **UNDER** (146.0) | 57% |
| Lindenwood Lions @ Tennessee Tech Golden Eagles | **HOME** (+2.0) | **UNDER** (154.5) | 37% |
| Old Dominion Monarchs @ Southern Miss Golden Eagles | **AWAY** (+4.0) | **UNDER** (148.0) | 47% |
| Utah State Aggies @ Nevada Wolf Pack | **HOME** (+5.0) | **OVER** (148.5) | 29% |
| Furman Paladins @ Wofford Terriers | **HOME** (+0.0) | **UNDER** (152.0) | 37% |
| New Orleans Privateers @ Lamar Cardinals | **AWAY** (+4.0) | **UNDER** (146.5) | 28% |
| Montana St Bobcats @ Idaho State Bengals | **HOME** (+2.5) | **OVER** (143.0) | 26% |
| East Carolina Pirates @ Charlotte 49ers | **AWAY** (+6.0) | **OVER** (145.0) | 39% |
| Stanford Cardinal @ California Golden Bears | **HOME** (-1.5) | **UNDER** (147.5) | 28% |
| Wake Forest Demon Deacons @ Virginia Tech Hokies | **AWAY** (+4.5) | **UNDER** (151.5) | 33% |
| West Virginia Mountaineers @ TCU Horned Frogs | **AWAY** (+5.5) | **UNDER** (131.5) | 29% |
| Illinois St Redbirds @ Bradley Braves | **AWAY** (+4.0) | **OVER** (144.0) | 31% |
| New Mexico Lobos @ Fresno St Bulldogs | **HOME** (+8.5) | **UNDER** (156.0) | 49% |
| Utah Tech Trailblazers @ Tarleton State Texans | **HOME** (-1.5) | **UNDER** (141.0) | 37% |
| Washington Huskies @ Maryland Terrapins | **HOME** (+3.5) | **UNDER** (145.5) | 54% |
| Kentucky Wildcats @ Auburn Tigers | **HOME** (-2.5) | **UNDER** (157.5) | 34% |
| Monmouth Hawks @ Charleston Cougars | **AWAY** (+4.0) | **UNDER** (147.0) | 40% |
| Texas Southern Tigers @ Miss Valley St Delta Devils | **HOME** (+13.0) | **OVER** (145.5) | 33% |
| Utah Valley Wolverines @ UT-Arlington Mavericks | **HOME** (+5.5) | **UNDER** (141.0) | 23% |
| UT Rio Grande Valley Vaqueros @ SE Louisiana Lions | **HOME** (+4.0) | **UNDER** (134.5) | 29% |
| Loyola (Chi) Ramblers @ Saint Joseph's Hawks | **AWAY** (+9.5) | **UNDER** (143.5) | 39% |
| St. Thomas (MN) Tommies @ Denver Pioneers | **HOME** (+4.5) | **OVER** (166.0) | 25% |
| Chattanooga Mocs @ The Citadel Bulldogs | **HOME** (+4.0) | **UNDER** (143.0) | 47% |
| Presbyterian Blue Hose @ South Carolina Upstate Spartans | **HOME** (+1.0) | **OVER** (140.0) | 28% |
| James Madison Dukes @ Georgia St Panthers | **HOME** (+1.5) | **OVER** (143.0) | 21% |
| Providence Friars @ DePaul Blue Demons | **HOME** (-1.5) | **OVER** (154.5) | 21% |
| Santa Clara Broncos @ San Francisco Dons | **HOME** (+7.0) | **UNDER** (158.0) | 21% |
| Iowa State Cyclones @ BYU Cougars | **HOME** (+3.5) | **UNDER** (155.5) | 29% |
| Hofstra Pride @ Northeastern Huskies | **HOME** (+8.5) | **UNDER** (149.0) | 28% |
| Maryland-Eastern Shore Hawks @ Coppin St Eagles | **HOME** (+3.0) | **OVER** (128.5) | 32% |
| Vermont Catamounts @ NJIT Highlanders | **HOME** (+4.0) | **OVER** (142.0) | 18% |
| New Haven Chargers @ Fairleigh Dickinson Knights | **AWAY** (+2.5) | **UNDER** (121.5) | 28% |
| Oregon Ducks @ USC Trojans | **AWAY** (+5.5) | **UNDER** (146.5) | 21% |
| Texas State Bobcats @ Louisiana Ragin' Cajuns | **HOME** (+2.5) | **UNDER** (134.5) | 18% |
| Alabama St Hornets @ Florida A&M Rattlers | **AWAY** (-1.5) | **UNDER** (143.5) | 40% |
| Davidson Wildcats @ Fordham Rams | **AWAY** (+1.0) | **UNDER** (132.0) | 26% |
| UCF Knights @ Utah Utes | **HOME** (+2.5) | **UNDER** (155.5) | 35% |
| Troy Trojans @ South Alabama Jaguars | **AWAY** (-2.0) | **OVER** (143.5) | 15% |
| CSU Fullerton Titans @ CSU Bakersfield Roadrunners | **HOME** (+5.5) | **UNDER** (161.0) | 35% |
| Navy Midshipmen @ Army Knights | **HOME** (+9.5) | **OVER** (138.5) | 39% |
| Jackson St Tigers @ Alcorn St Braves | **AWAY** (-1.5) | **OVER** (150.5) | 23% |
| Houston Christian Huskies @ Northwestern St Demons | **AWAY** (+2.5) | **UNDER** (134.0) | 36% |
| Illinois Fighting Illini @ UCLA Bruins | **HOME** (+6.5) | **OVER** (145.5) | 13% |
| Radford Highlanders @ UNC Asheville Bulldogs | **HOME** (-1.5) | **UNDER** (149.0) | 12% |
| North Florida Ospreys @ Stetson Hatters | **AWAY** (+3.0) | **OVER** (162.0) | 22% |
| Rhode Island Rams @ La Salle Explorers | **HOME** (+4.5) | **UNDER** (136.0) | 34% |
| Alabama Crimson Tide @ LSU Tigers | **HOME** (+7.5) | **UNDER** (172.5) | 39% |
| Morehead St Eagles @ Western Illinois Leathernecks | **HOME** (+8.5) | **OVER** (144.5) | 14% |
| Ohio Bobcats @ Northern Illinois Huskies | **HOME** (+6.0) | **UNDER** (150.5) | 45% |
| Loyola Marymount Lions @ San Diego Toreros | **HOME** (+3.0) | **OVER** (150.5) | 18% |
| Central Connecticut St Blue Devils @ Chicago St Cougars | **HOME** (+4.0) | **OVER** (139.5) | 27% |
| Marshall Thundering Herd @ Coastal Carolina Chanticleers | **HOME** (+1.5) | **UNDER** (153.5) | 20% |
| CSU Northridge Matadors @ Long Beach St 49ers | **HOME** (+3.5) | **UNDER** (158.5) | 11% |
| UNLV Rebels @ Air Force Falcons | **HOME** (+15.5) | **UNDER** (152.0) | 18% |
| UC Davis Aggies @ UC Riverside Highlanders | **HOME** (+3.0) | **UNDER** (149.0) | 35% |
| San Diego St Aztecs @ Colorado St Rams | **HOME** (+2.5) | **OVER** (136.5) | 10% |
| Idaho Vandals @ Sacramento St Hornets | **HOME** (+3.5) | **UNDER** (162.5) | 18% |
| Central Arkansas Bears @ Florida Gulf Coast Eagles | **HOME** (+1.5) | **UNDER** (151.5) | 14% |
| UConn Huskies @ Villanova Wildcats | **HOME** (+2.5) | **UNDER** (140.5) | 13% |
| East Tennessee St Buccaneers @ UNC Greensboro Spartans | **HOME** (+6.5) | **OVER** (148.5) | 22% |
| Texas A&M Aggies @ Oklahoma Sooners | **HOME** (+1.5) | **UNDER** (165.5) | 9% |
| Austin Peay Governors @ Jacksonville Dolphins | **HOME** (+7.0) | **UNDER** (141.0) | 22% |
| North Carolina Tar Heels @ Syracuse Orange | **HOME** (+1.5) | **OVER** (153.5) | 9% |
| Le Moyne Dolphins @ Stonehill Skyhawks | **HOME** (+2.5) | **UNDER** (136.5) | 14% |
| SE Missouri St Redhawks @ Arkansas-Little Rock Trojans | **HOME** (+2.0) | **OVER** (143.0) | 4% |
| Western Carolina Catamounts @ VMI Keydets | **HOME** (+9.0) | **UNDER** (155.0) | 14% |

> 📈 *ATS = Against The Spread (with Vegas lines). Updated daily via GitHub Actions.*

<!-- ACCURACY_STATS_END -->

<!-- RANKINGS_START -->

### 🏆 Top 25 Team Rankings

*Updated: February 21, 2026*

| Rank | Team | Record | Rating | Off | Def |
|------|------|--------|--------|-----|-----|
| 1 | Michigan Wolverines | 25-1 | +31.2 | 72.2 | 41.0 |
| 2 | Arizona Wildcats | 24-2 | +27.3 | 68.8 | 41.5 |
| 3 | Duke Blue Devils | 24-2 | +27.0 | 65.5 | 38.4 |
| 4 | Illinois Fighting Illini | 22-5 | +26.5 | 67.3 | 41.1 |
| 5 | Louisville Cardinals | 19-7 | +26.5 | 69.8 | 43.7 |
| 6 | Iowa State Cyclones | 23-3 | +25.6 | 66.4 | 40.8 |
| 7 | Alabama Crimson Tide | 19-7 | +24.8 | 73.5 | 48.8 |
| 8 | Arkansas Razorbacks | 19-7 | +24.6 | 70.6 | 46.2 |
| 9 | Purdue Boilermakers | 22-5 | +24.6 | 66.2 | 41.6 |
| 10 | Gonzaga Bulldogs | 26-2 | +24.5 | 65.7 | 41.2 |
| 11 | Florida Gators | 20-6 | +24.4 | 65.5 | 41.4 |
| 12 | Houston Cougars | 23-3 | +23.5 | 60.8 | 37.3 |
| 13 | Vanderbilt Commodores | 21-5 | +23.5 | 68.0 | 44.6 |
| 14 | BYU Cougars | 19-7 | +23.1 | 68.7 | 45.8 |
| 15 | Tennessee Volunteers | 19-7 | +22.4 | 63.7 | 41.6 |
| 16 | Michigan State Spartans | 21-5 | +22.4 | 62.3 | 39.9 |
| 17 | UConn Huskies | 24-3 | +22.4 | 62.9 | 40.5 |
| 18 | Kansas Jayhawks | 20-6 | +22.2 | 62.6 | 40.3 |
| 19 | NC State Wolfpack | 19-8 | +22.2 | 67.0 | 45.0 |
| 20 | St. John's Red Storm | 21-5 | +22.0 | 65.3 | 43.2 |
| 21 | Texas Tech Red Raiders | 19-7 | +21.8 | 64.5 | 42.7 |
| 22 | Kentucky Wildcats | 17-9 | +21.6 | 65.0 | 43.8 |
| 23 | Nebraska Cornhuskers | 22-4 | +21.3 | 61.4 | 40.1 |
| 24 | Saint Louis Billikens | 25-2 | +21.1 | 67.4 | 46.3 |
| 25 | Georgia Bulldogs | 18-8 | +20.8 | 69.0 | 48.5 |

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

