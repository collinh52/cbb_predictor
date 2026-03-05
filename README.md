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

**Last Updated**: March 05, 2026 at 12:42 PM

![ATS Accuracy](https://img.shields.io/badge/ATS_Record-50.8%25-yellowgreen)

#### 🏆 Rolling ATS Performance

| Timeframe | ATS Record | Accuracy |
|-----------|------------|----------|
| **Latest** (2026-03-04) | 16-20 | **44.4%** |
| **Last 7 Days** | 169-165 | **50.6%** |
| **Last 30 Days** | 525-508 | **50.8%** |
| **All-Time** | 525-508 | **50.8%** |

**Over/Under Accuracy**: 52.1%

#### 🎯 Accuracy by Confidence (ATS)

| Confidence | Record | Accuracy |
|------------|--------|----------|
| **50%+** | 147-150 | **49.5%** |
| **60%+** | 59-58 | **50.4%** |
| **70%+** | 21-20 | **51.2%** |
| **80%+** | 5-5 | **50.0%** |

#### 🏀 ATS Accuracy by Conference

| Conference | Record | Accuracy |
|------------|--------|----------|
| Big South | 20-6 | **76.9%** |
| Western Athletic | 14-5 | **73.7%** |
| Southern | 19-11 | **63.3%** |
| Summit League | 11-7 | **61.1%** |
| Mountain West | 22-14 | **61.1%** |
| Ivy League | 10-7 | **58.8%** |
| Southeastern | 30-22 | **57.7%** |
| Atlantic Coast | 32-24 | **57.1%** |
| Atlantic 10 | 22-17 | **56.4%** |
| Big 12 | 27-22 | **55.1%** |
| Mid-Eastern Athletic | 12-10 | **54.5%** |
| America East | 15-13 | **53.6%** |
| Southwestern Athletic | 16-14 | **53.3%** |
| Patriot League | 10-9 | **52.6%** |
| Missouri Valley | 16-15 | **51.6%** |
| ASUN | 20-20 | **50.0%** |
| Ohio Valley | 17-17 | **50.0%** |
| Southland | 15-15 | **50.0%** |
| Conference USA | 14-15 | **48.3%** |
| Mid-American | 19-21 | **47.5%** |
| Metro Atlantic Athletic | 16-20 | **44.4%** |
| Big East | 15-19 | **44.1%** |
| West Coast | 11-14 | **44.0%** |
| Big Ten | 23-30 | **43.4%** |
| Big West | 13-17 | **43.3%** |
| Coastal Athletic Association | 17-23 | **42.5%** |
| Sun Belt | 19-26 | **42.2%** |
| American | 16-23 | **41.0%** |
| Big Sky | 13-19 | **40.6%** |
| Horizon League | 12-18 | **40.0%** |
| Northeast | 11-17 | **39.3%** |

> *A game counts for a conference if either team is a member.*

#### Combined Statistics

- **Total Predictions**: 1033
- **Overall Winner Accuracy**: 50.8%

#### 📅 Predictions for Today (2026-03-05)

| Matchup | Spread Pick | Total Pick | Confidence |
|---------|-------------|------------|------------|
| Grambling St Tigers @ Alabama St Hornets | **HOME** (-3.5) | **OVER** (142.5) | 49% |
| Sam Houston St Bearkats @ Delaware Blue Hens | **HOME** (+6.5) | **UNDER** (148.0) | 66% |
| Bucknell Bison @ Navy Midshipmen | **AWAY** (+16.5) | **OVER** (133.5) | 63% |
| Rutgers Scarlet Knights @ Michigan St Spartans | **AWAY** (+19.5) | **OVER** (140.5) | 49% |
| Evansville Purple Aces @ Northern Iowa Panthers | **AWAY** (+14.5) | **OVER** (125.5) | 56% |
| Georgia Southern Eagles @ Arkansas St Red Wolves | **HOME** (-6.5) | **UNDER** (168.5) | 66% |
| UC Riverside Highlanders @ Hawai'i Rainbow Warriors | **AWAY** (+11.0) | **UNDER** (149.0) | 51% |
| Coppin St Eagles @ Morgan St Bears | **AWAY** (+7.5) | **UNDER** (151.5) | 68% |
| Oral Roberts Golden Eagles @ North Dakota St Bison | **AWAY** (+8.5) | **OVER** (146.5) | 44% |
| South Dakota St Jackrabbits @ St. Thomas (MN) Tommies | **HOME** (-6.0) | **UNDER** (149.0) | 43% |
| Louisiana Tech Bulldogs @ Liberty Flames | **AWAY** (+9.0) | **OVER** (138.0) | 46% |
| Cal Poly Mustangs @ UC Irvine Anteaters | **AWAY** (+9.5) | **UNDER** (155.5) | 60% |
| South Carolina St Bulldogs @ North Carolina Central Eagles | **AWAY** (+8.0) | **UNDER** (145.5) | 86% |
| Abilene Christian Wildcats @ Cal Baptist Lancers | **AWAY** (+9.0) | **UNDER** (135.5) | 64% |
| Miss Valley St Delta Devils @ Jackson St Tigers | **AWAY** (+10.5) | **OVER** (145.0) | 61% |
| Eastern Illinois Panthers @ Tenn-Martin Skyhawks | **AWAY** (+6.5) | **UNDER** (121.5) | 41% |
| Tulsa Golden Hurricane @ East Carolina Pirates | **HOME** (+9.5) | **OVER** (155.5) | 41% |
| Prairie View Panthers @ Texas Southern Tigers | **HOME** (-3.5) | **UNDER** (155.5) | 56% |
| Manhattan Jaspers @ Fairfield Stags | **AWAY** (+5.5) | **UNDER** (150.0) | 42% |
| Jacksonville St Gamecocks @ New Mexico St Aggies | **HOME** (-5.0) | **OVER** (142.5) | 40% |
| Delaware St Hornets @ Maryland-Eastern Shore Hawks | **AWAY** (+6.5) | **OVER** (126.0) | 36% |
| Middle Tennessee Blue Raiders @ Florida Int'l Golden Panthers | **HOME** (-2.0) | **OVER** (154.5) | 43% |
| Michigan Wolverines @ Iowa Hawkeyes | **HOME** (+9.5) | **UNDER** (146.5) | 52% |
| Drake Bulldogs @ Southern Illinois Salukis | **AWAY** (+5.5) | **UNDER** (135.5) | 31% |
| Lindenwood Lions @ SE Missouri St Redhawks | **HOME** (-1.5) | **UNDER** (149.5) | 36% |
| Loyola (MD) Greyhounds @ Colgate Raiders | **AWAY** (+7.0) | **OVER** (151.5) | 42% |
| Sacred Heart Pioneers @ Iona Gaels | **HOME** (-3.5) | **OVER** (148.0) | 30% |
| Utah Valley Wolverines @ Southern Utah Thunderbirds | **HOME** (+10.0) | **OVER** (151.0) | 38% |
| Holy Cross Crusaders @ Lehigh Mountain Hawks | **AWAY** (+6.5) | **OVER** (141.5) | 46% |
| Howard Bison @ Norfolk St Spartans | **HOME** (+5.0) | **OVER** (145.5) | 43% |
| Pepperdine Waves @ Portland Pilots | **HOME** (-2.0) | **OVER** (152.5) | 30% |
| San Diego Toreros @ Loyola Marymount Lions | **AWAY** (+5.5) | **OVER** (146.0) | 41% |
| UT-Arlington Mavericks @ Tarleton State Texans | **HOME** (-2.0) | **UNDER** (136.5) | 53% |
| American Eagles @ Boston Univ. Terriers | **AWAY** (+3.0) | **UNDER** (142.0) | 24% |
| Southern Jaguars @ Alabama A&M Bulldogs | **HOME** (+1.0) | **UNDER** (149.5) | 22% |
| Western Kentucky Hilltoppers @ Missouri St Bears | **AWAY** (-1.5) | **OVER** (151.0) | 17% |
| UC San Diego Tritons @ CSU Fullerton Titans | **HOME** (+3.5) | **UNDER** (156.5) | 41% |
| Bethune-Cookman Wildcats @ Florida A&M Rattlers | **HOME** (+2.5) | **OVER** (146.0) | 13% |
| James Madison Dukes @ Southern Miss Golden Eagles | **HOME** (+2.5) | **UNDER** (142.5) | 18% |
| Tulane Green Wave @ Temple Owls | **AWAY** (+4.5) | **UNDER** (144.5) | 34% |
| CSU Northridge Matadors @ CSU Bakersfield Roadrunners | **HOME** (+8.0) | **UNDER** (165.0) | 18% |
| Indiana St Sycamores @ Valparaiso Beacons | **AWAY** (+2.5) | **OVER** (136.0) | 37% |
| UC Davis Aggies @ Long Beach St 49ers | **HOME** (+2.0) | **UNDER** (150.0) | 9% |
| South Florida Bulls @ Memphis Tigers | **HOME** (+6.0) | **UNDER** (160.5) | 27% |
| Kennesaw St Owls @ UTEP Miners | **HOME** (+2.5) | **UNDER** (149.5) | 12% |
| Arkansas-Pine Bluff Golden Lions @ Alcorn St Braves | **HOME** (+1.5) | **OVER** (149.5) | 12% |

> 📈 *ATS = Against The Spread (with Vegas lines). Updated daily via GitHub Actions.*

<!-- ACCURACY_STATS_END -->

<!-- RANKINGS_START -->

### 🏆 Top 25 Team Rankings

*Updated: March 05, 2026*

| Rank | Team | Record | Rating | Off | Def |
|------|------|--------|--------|-----|-----|
| 1 | Michigan Wolverines | 27-2 | +30.9 | 71.9 | 41.1 |
| 2 | Arizona Wildcats | 28-2 | +28.1 | 68.8 | 40.7 |
| 3 | Duke Blue Devils | 28-2 | +28.1 | 65.6 | 37.5 |
| 4 | Illinois Fighting Illini | 23-7 | +26.7 | 67.7 | 41.4 |
| 5 | Florida Gators | 24-6 | +26.2 | 67.7 | 41.8 |
| 6 | Louisville Cardinals | 21-9 | +25.4 | 68.7 | 43.8 |
| 7 | Iowa State Cyclones | 24-6 | +24.6 | 64.9 | 40.6 |
| 8 | Arkansas Razorbacks | 22-8 | +24.5 | 71.7 | 47.2 |
| 9 | Alabama Crimson Tide | 22-8 | +24.3 | 72.6 | 48.2 |
| 10 | Gonzaga Bulldogs | 28-3 | +24.3 | 65.2 | 40.9 |
| 11 | Purdue Boilermakers | 23-7 | +24.2 | 65.9 | 41.7 |
| 12 | Houston Cougars | 25-5 | +23.6 | 61.0 | 37.4 |
| 13 | UConn Huskies | 27-3 | +23.2 | 63.2 | 40.0 |
| 14 | Vanderbilt Commodores | 23-7 | +22.9 | 67.4 | 44.6 |
| 15 | Michigan State Spartans | 24-5 | +22.6 | 62.0 | 39.4 |
| 16 | Texas Tech Red Raiders | 22-8 | +22.4 | 65.2 | 42.8 |
| 17 | BYU Cougars | 20-10 | +22.3 | 68.3 | 46.3 |
| 18 | St. John's Red Storm | 24-6 | +22.2 | 64.8 | 42.6 |
| 19 | Tennessee Volunteers | 21-9 | +22.0 | 62.5 | 40.8 |
| 20 | Kansas Jayhawks | 21-9 | +21.9 | 62.4 | 40.6 |
| 21 | Georgia Bulldogs | 21-9 | +21.8 | 69.3 | 47.8 |
| 22 | Kentucky Wildcats | 19-11 | +21.5 | 64.8 | 43.7 |
| 23 | Wisconsin Badgers | 21-9 | +21.2 | 67.4 | 46.1 |
| 24 | Nebraska Cornhuskers | 25-5 | +21.1 | 61.2 | 40.2 |
| 25 | Virginia Cavaliers | 26-4 | +20.8 | 63.3 | 42.5 |

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

