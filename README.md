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

**Last Updated**: March 12, 2026 at 12:41 PM

![ATS Accuracy](https://img.shields.io/badge/ATS_Record-51.0%25-yellowgreen)

#### 🏆 Rolling ATS Performance

| Timeframe | ATS Record | Accuracy |
|-----------|------------|----------|
| **Latest** (2026-03-11) | 20-14 | **58.8%** |
| **Last 7 Days** | 144-136 | **51.4%** |
| **Last 30 Days** | 670-645 | **51.0%** |
| **All-Time** | 670-645 | **51.0%** |

**Over/Under Accuracy**: 51.6%

#### 🎯 Accuracy by Confidence (ATS)

| Confidence | Record | Accuracy |
|------------|--------|----------|
| **50%+** | 196-187 | **51.2%** |
| **60%+** | 82-71 | **53.6%** |
| **70%+** | 26-24 | **52.0%** |
| **80%+** | 6-6 | **50.0%** |

#### 🏀 ATS Accuracy by Conference

| Conference | Record | Accuracy |
|------------|--------|----------|
| Big South | 25-8 | **75.8%** |
| Western Athletic | 17-9 | **65.4%** |
| Summit League | 16-9 | **64.0%** |
| Southern | 24-15 | **61.5%** |
| Mountain West | 28-19 | **59.6%** |
| Atlantic 10 | 29-20 | **59.2%** |
| Missouri Valley | 24-17 | **58.5%** |
| Atlantic Coast | 41-31 | **56.9%** |
| Ohio Valley | 22-17 | **56.4%** |
| Patriot League | 14-11 | **56.0%** |
| Big 12 | 35-30 | **53.8%** |
| Southwestern Athletic | 22-19 | **53.7%** |
| Mid-Eastern Athletic | 15-13 | **53.6%** |
| Southeastern | 34-30 | **53.1%** |
| West Coast | 18-16 | **52.9%** |
| Mid-American | 25-25 | **50.0%** |
| America East | 17-17 | **50.0%** |
| ASUN | 23-24 | **48.9%** |
| Southland | 17-18 | **48.6%** |
| Ivy League | 10-11 | **47.6%** |
| Big East | 20-23 | **46.5%** |
| Big Ten | 33-38 | **46.5%** |
| Big West | 19-23 | **45.2%** |
| Metro Atlantic Athletic | 20-25 | **44.4%** |
| Coastal Athletic Association | 23-29 | **44.2%** |
| Conference USA | 19-24 | **44.2%** |
| Sun Belt | 23-31 | **42.6%** |
| Northeast | 12-17 | **41.4%** |
| Horizon League | 13-21 | **38.2%** |
| American | 19-31 | **38.0%** |
| Big Sky | 15-26 | **36.6%** |

> *A game counts for a conference if either team is a member.*

#### Combined Statistics

- **Total Predictions**: 1315
- **Overall Winner Accuracy**: 51.0%

#### 📅 Predictions for Today (2026-03-12)

| Matchup | Spread Pick | Total Pick | Confidence |
|---------|-------------|------------|------------|
| Florida St Seminoles @ Duke Blue Devils | **HOME** (-17.5) | **UNDER** (151.5) | 77% |
| UCF Knights @ Arizona Wildcats | **AWAY** (+15.5) | **UNDER** (160.5) | 56% |
| Providence Friars @ St. John's Red Storm | **HOME** (-11.5) | **UNDER** (158.5) | 49% |
| Xavier Musketeers @ UConn Huskies | **AWAY** (+15.5) | **OVER** (151.5) | 54% |
| BYU Cougars @ Houston Cougars | **HOME** (-9.5) | **OVER** (145.5) | 57% |
| Rutgers Scarlet Knights @ UCLA Bruins | **AWAY** (+11.5) | **OVER** (141.5) | 71% |
| Northwestern Wildcats @ Purdue Boilermakers | **AWAY** (+11.5) | **UNDER** (144.5) | 53% |
| San José St Spartans @ New Mexico Lobos | **AWAY** (+13.5) | **OVER** (152.5) | 60% |
| Washington Huskies @ Wisconsin Badgers | **HOME** (-7.0) | **UNDER** (156.5) | 56% |
| Georgetown Hoyas @ Villanova Wildcats | **HOME** (-6.5) | **OVER** (140.5) | 48% |
| Ole Miss Rebels @ Georgia Bulldogs | **HOME** (-6.0) | **OVER** (156.5) | 66% |
| TCU Horned Frogs @ Kansas Jayhawks | **HOME** (-5.5) | **UNDER** (142.5) | 51% |
| UNLV Rebels @ Utah State Aggies | **HOME** (-6.5) | **OVER** (157.0) | 65% |
| Auburn Tigers @ Tennessee Volunteers | **HOME** (-6.0) | **UNDER** (148.5) | 43% |
| St. Bonaventure Bonnies @ George Mason Patriots | **HOME** (-3.5) | **UNDER** (142.0) | 51% |
| Clemson Tigers @ North Carolina Tar Heels | **HOME** (-1.5) | **UNDER** (141.5) | 58% |
| Nevada Wolf Pack @ Grand Canyon Antelopes | **HOME** (-2.5) | **UNDER** (139.5) | 46% |
| Colorado St Rams @ San Diego St Aztecs | **HOME** (-5.5) | **OVER** (142.5) | 47% |
| Loyola (Chi) Ramblers @ Davidson Wildcats | **AWAY** (+6.5) | **UNDER** (132.0) | 37% |
| Kennesaw St Owls @ Western Kentucky Hilltoppers | **HOME** (-1.5) | **UNDER** (159.5) | 44% |
| Maryland-Eastern Shore Hawks @ North Carolina Central Eagles | **HOME** (-1.5) | **OVER** (133.0) | 42% |
| NC State Wolfpack @ Virginia Cavaliers | **AWAY** (+6.5) | **OVER** (149.0) | 41% |
| Iowa Hawkeyes @ Ohio State Buckeyes | **HOME** (-1.5) | **OVER** (138.5) | 32% |
| Oklahoma Sooners @ Texas A&M Aggies | **HOME** (-2.5) | **OVER** (161.5) | 30% |
| Southern Utah Thunderbirds @ UT-Arlington Mavericks | **AWAY** (+4.5) | **OVER** (141.0) | 39% |
| UC Davis Aggies @ CSU Fullerton Titans | **HOME** (+1.5) | **UNDER** (157.5) | 30% |
| Iowa State Cyclones @ Texas Tech Red Raiders | **HOME** (+5.5) | **UNDER** (143.5) | 30% |
| UC San Diego Tritons @ CSU Northridge Matadors | **HOME** (+3.5) | **UNDER** (151.5) | 33% |
| Abilene Christian Wildcats @ Utah Tech Trailblazers | **AWAY** (+2.5) | **OVER** (141.5) | 14% |
| Louisville Cardinals @ Miami Hurricanes | **AWAY** (-1.0) | **OVER** (154.5) | 9% |
| Tulane Green Wave @ Charlotte 49ers | **AWAY** (+1.5) | **OVER** (144.5) | 7% |
| Kentucky Wildcats @ Missouri Tigers | **HOME** (+3.5) | **OVER** (148.5) | 3% |
| Florida Atlantic Owls @ North Texas Mean Green | **HOME** (+1.5) | **OVER** (137.5) | 8% |

> 📈 *ATS = Against The Spread (with Vegas lines). Updated daily via GitHub Actions.*

<!-- ACCURACY_STATS_END -->

<!-- RANKINGS_START -->

### 🏆 Top 25 Team Rankings

*Updated: March 12, 2026*

| Rank | Team | Record | Rating | Off | Def |
|------|------|--------|--------|-----|-----|
| 1 | Michigan Wolverines | 29-2 | +30.4 | 71.7 | 41.3 |
| 2 | Duke Blue Devils | 29-2 | +27.9 | 65.3 | 37.5 |
| 3 | Arizona Wildcats | 29-2 | +27.5 | 68.4 | 40.8 |
| 4 | Florida Gators | 25-6 | +26.0 | 67.7 | 41.9 |
| 5 | Illinois Fighting Illini | 24-7 | +25.9 | 67.1 | 41.6 |
| 6 | Iowa State Cyclones | 26-6 | +25.2 | 65.1 | 40.3 |
| 7 | Louisville Cardinals | 23-9 | +24.6 | 67.8 | 43.6 |
| 8 | Alabama Crimson Tide | 23-8 | +24.4 | 72.8 | 48.4 |
| 9 | Purdue Boilermakers | 23-8 | +24.1 | 66.0 | 42.2 |
| 10 | Arkansas Razorbacks | 23-8 | +23.9 | 71.3 | 47.4 |
| 11 | Gonzaga Bulldogs | 30-3 | +23.6 | 64.5 | 40.8 |
| 12 | Houston Cougars | 26-5 | +23.2 | 60.7 | 37.5 |
| 13 | Vanderbilt Commodores | 24-7 | +22.7 | 67.5 | 44.8 |
| 14 | UConn Huskies | 27-4 | +22.5 | 62.6 | 40.1 |
| 15 | BYU Cougars | 23-10 | +22.4 | 68.2 | 45.9 |
| 16 | Michigan State Spartans | 25-6 | +22.1 | 62.5 | 40.4 |
| 17 | Texas Tech Red Raiders | 22-9 | +22.0 | 64.9 | 42.9 |
| 18 | Kansas Jayhawks | 22-9 | +22.0 | 63.1 | 41.1 |
| 19 | St. John's Red Storm | 25-6 | +22.0 | 64.7 | 42.7 |
| 20 | Tennessee Volunteers | 21-10 | +21.9 | 62.6 | 41.1 |
| 21 | Wisconsin Badgers | 22-9 | +21.3 | 67.6 | 46.2 |
| 22 | Georgia Bulldogs | 22-9 | +21.3 | 69.4 | 48.4 |
| 23 | Nebraska Cornhuskers | 26-5 | +21.1 | 61.6 | 40.4 |
| 24 | Kentucky Wildcats | 20-12 | +21.1 | 64.8 | 44.0 |
| 25 | Ohio State Buckeyes | 20-11 | +20.5 | 65.1 | 44.9 |

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

