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

**Last Updated**: November 17, 2026 at 12:35 PM

![ATS Accuracy](https://img.shields.io/badge/ATS_Record-50.4%25-yellowgreen)

#### 🏆 Rolling ATS Performance

| Timeframe | ATS Record | Accuracy |
|-----------|------------|----------|
| **Latest** (2026-11-16) | 1-1 | **50.0%** |
| **Last 7 Days** | 7-8 | **46.7%** |
| **Last 30 Days** | 17-20 | **45.9%** |
| **All-Time** | 781-769 | **50.4%** |

**Over/Under Accuracy**: 50.9%

#### 🎯 Accuracy by Confidence (ATS)

| Confidence | Record | Accuracy |
|------------|--------|----------|
| **50%+** | 253-251 | **50.2%** |
| **60%+** | 114-106 | **51.8%** |
| **70%+** | 36-39 | **48.0%** |
| **80%+** | 10-13 | **43.5%** |

#### 🏀 ATS Accuracy by Conference

| Conference | Record | Accuracy |
|------------|--------|----------|
| Big South | 27-8 | **77.1%** |
| Southern | 25-15 | **62.5%** |
| Mountain West | 41-25 | **62.1%** |
| United Athletic | 21-13 | **61.8%** |
| Patriot League | 17-12 | **58.6%** |
| Atlantic Coast | 59-44 | **57.3%** |
| Summit League | 16-12 | **57.1%** |
| Mid-Eastern Athletic | 20-16 | **55.6%** |
| Missouri Valley | 27-22 | **55.1%** |
| West Coast | 22-18 | **55.0%** |
| Atlantic 10 | 41-34 | **54.7%** |
| Ohio Valley | 23-20 | **53.5%** |
| Southwestern Athletic | 26-23 | **53.1%** |
| America East | 19-18 | **51.4%** |
| Mid-American | 31-31 | **50.0%** |
| Big 12 | 51-51 | **50.0%** |
| Big East | 31-32 | **49.2%** |
| Big West | 24-26 | **48.0%** |
| Southeastern | 56-61 | **47.9%** |
| Southland | 19-21 | **47.5%** |
| Conference USA | 23-27 | **46.0%** |
| Metro | 22-26 | **45.8%** |
| Sun Belt | 26-32 | **44.8%** |
| Atlantic Sun | 24-30 | **44.4%** |
| Big Ten | 50-67 | **42.7%** |
| Northeast | 12-17 | **41.4%** |
| Coastal Athletic Association | 23-33 | **41.1%** |
| Horizon League | 15-23 | **39.5%** |
| Big Sky | 18-28 | **39.1%** |
| Ivy League | 10-16 | **38.5%** |
| American | 25-42 | **37.3%** |

> *A game counts for a conference if either team is a member.*

#### Combined Statistics

- **Total Predictions**: 1550
- **Overall Winner Accuracy**: 50.4%

#### 📅 Predictions for Today (2026-11-17)

| Matchup | Spread Pick | Total Pick | Confidence |
|---------|-------------|------------|------------|
| Sam Houston St Bearkats @ Wyoming Cowboys | **HOME** (-9.5) | **UNDER** (152.0) | 82% |
| Eastern Illinois Panthers @ Vanderbilt Commodores | **AWAY** (+43.0) | **UNDER** (148.0) | 51% |
| Rider Broncs @ Miami Hurricanes | **AWAY** (+42.5) | **UNDER** (149.5) | 61% |
| Montana St Bobcats @ Gonzaga Bulldogs | **HOME** (-23.5) | **UNDER** (151.5) | 82% |
| Old Dominion Monarchs @ Virginia Cavaliers | **AWAY** (+30.0) | **OVER** (150.0) | 49% |
| Seattle Redhawks @ Cal Baptist Lancers | **HOME** (+6.5) | **UNDER** (135.5) | 49% |
| Kennesaw St Owls @ Alabama Crimson Tide | **AWAY** (+25.5) | **UNDER** (172.0) | 51% |
| Sacred Heart Pioneers @ Providence Friars | **AWAY** (+31.0) | **OVER** (152.5) | 85% |
| Cleveland St Vikings @ Xavier Musketeers | **AWAY** (+34.0) | **OVER** (158.5) | 90% |
| Oral Roberts Golden Eagles @ SMU Mustangs | **AWAY** (+26.5) | **UNDER** (159.0) | 71% |
| Ball State Cardinals @ Florida St Seminoles | **AWAY** (+24.5) | **UNDER** (148.5) | 67% |
| UNLV Rebels @ Kansas Jayhawks | **AWAY** (+17.5) | **UNDER** (155.5) | 69% |
| Monmouth Hawks @ Wake Forest Demon Deacons | **AWAY** (+15.5) | **OVER** (144.0) | 62% |
| Lindenwood Lions @ Northern Iowa Panthers | **AWAY** (+12.5) | **UNDER** (154.0) | 93% |
| Illinois Fighting Illini @ Duke Blue Devils | **HOME** (-7.5) | **UNDER** (162.5) | 92% |
| Tennessee St Tigers @ South Florida Bulls | **AWAY** (+11.0) | **UNDER** (163.0) | 62% |
| Eastern Washington Eagles @ Utah Utes | **AWAY** (+11.0) | **UNDER** (150.0) | 53% |
| Central Michigan Chippewas @ Dayton Flyers | **AWAY** (+10.5) | **UNDER** (148.0) | 77% |
| Jacksonville St Gamecocks @ Louisiana Tech Bulldogs | **HOME** (+0.0) | **UNDER** (136.5) | 59% |
| Western Carolina Catamounts @ Butler Bulldogs | **AWAY** (+12.0) | **UNDER** (158.5) | 52% |
| Indiana Hoosiers @ Arkansas Razorbacks | **HOME** (-2.5) | **OVER** (154.5) | 59% |
| Charlotte 49ers @ Davidson Wildcats | **HOME** (-3.0) | **UNDER** (136.0) | 34% |
| Fordham Rams @ Manhattan Jaspers | **HOME** (+12.0) | **UNDER** (142.5) | 58% |
| West Virginia Mountaineers @ Auburn Tigers | **HOME** (-1.5) | **UNDER** (142.5) | 65% |
| UC Irvine Anteaters @ Stanford Cardinal | **AWAY** (+6.5) | **UNDER** (144.0) | 45% |
| Middle Tennessee Blue Raiders @ Georgia Southern Eagles | **HOME** (+2.0) | **OVER** (152.5) | 25% |
| CSU Northridge Matadors @ Troy Trojans | **HOME** (+0.0) | **OVER** (151.5) | 31% |
| SIU-Edwardsville Cougars @ North Dakota Fighting Hawks | **HOME** (-1.0) | **UNDER** (149.5) | 65% |
| Villanova Wildcats @ Pittsburgh Panthers | **HOME** (-1.5) | **UNDER** (147.5) | 50% |
| Florida Int'l Golden Panthers @ UAB Blazers | **AWAY** (+4.0) | **UNDER** (164.5) | 52% |
| Michigan St Spartans @ Tennessee Volunteers | **HOME** (+3.5) | **UNDER** (150.5) | 47% |
| UT-Arlington Mavericks @ Southern Miss Golden Eagles | **AWAY** (+2.0) | **UNDER** (148.5) | 53% |
| East Tennessee St Buccaneers @ Marshall Thundering Herd | **AWAY** (+1.5) | **OVER** (147.0) | 32% |
| Bowling Green Falcons @ William & Mary Tribe | **AWAY** (+2.0) | **UNDER** (169.0) | 48% |
| Mississippi St Bulldogs @ UCF Knights | **AWAY** (+1.0) | **OVER** (155.5) | 19% |

> 📈 *ATS = Against The Spread (with Vegas lines). Updated daily via GitHub Actions.*

<!-- ACCURACY_STATS_END -->

<!-- RANKINGS_START -->

### 🏆 Top 25 Team Rankings

*Updated: November 17, 2026*

| Rank | Team | Record | Rating | Off | Def |
|------|------|--------|--------|-----|-----|
| 1 | Michigan Wolverines | 31-3 | +29.0 | 70.3 | 41.4 |
| 2 | Arizona Wildcats | 32-2 | +27.6 | 68.6 | 40.9 |
| 3 | Duke Blue Devils | 32-2 | +26.5 | 64.6 | 38.0 |
| 4 | Illinois Fighting Illini | 24-8 | +25.4 | 67.0 | 42.1 |
| 5 | Iowa State Cyclones | 27-7 | +25.3 | 64.9 | 39.9 |
| 6 | Florida Gators | 26-7 | +24.8 | 66.6 | 42.2 |
| 7 | Louisville Cardinals | 23-10 | +24.0 | 67.3 | 43.7 |
| 8 | Alabama Crimson Tide | 23-9 | +23.7 | 72.5 | 48.8 |
| 9 | Gonzaga Bulldogs | 30-3 | +23.5 | 64.4 | 40.9 |
| 10 | Houston Cougars | 28-6 | +23.4 | 60.7 | 37.2 |
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
| 23 | Georgia Bulldogs | 22-10 | +20.7 | 69.0 | 48.6 |
| 24 | Kentucky Wildcats | 21-13 | +20.6 | 64.3 | 43.9 |
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

