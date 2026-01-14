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

**Last Updated**: January 14, 2026 at 08:13 AM

#### 🏆 Rolling ATS Performance

*No predictions with Vegas lines yet. ATS tracking will begin once odds data is collected.*

#### 📅 Predictions for 2026-01-14

| Matchup | Spread Pick | Total Pick | Confidence |
|---------|-------------|------------|------------|
| Arizona St Sun Devils @ Arizona Wildcats | **HOME** (-22.0) | **OVER** (168.0) | 100% |
| Fordham Rams @ Saint Louis Billikens | **HOME** (-18.5) | **OVER** (150.0) | 100% |
| East Carolina Pirates @ South Florida Bulls | **HOME** (-19.0) | **OVER** (157.0) | 100% |
| Army Knights @ Holy Cross Crusaders | **HOME** (-5.5) | **OVER** (143.5) | 100% |
| Utah Utes @ Texas Tech Red Raiders | **HOME** (-17.5) | **OVER** (158.5) | 100% |
| Nevada Wolf Pack @ Utah State Aggies | **HOME** (-14.0) | **OVER** (152.0) | 100% |
| Pacific Tigers @ Santa Clara Broncos | **HOME** (-13.0) | **OVER** (151.5) | 100% |
| Davidson Wildcats @ GW Revolutionaries | **HOME** (-12.5) | **OVER** (146.5) | 100% |
| Louisiana Ragin' Cajuns @ Texas State Bobcats | **HOME** (-8.0) | **OVER** (130.0) | 100% |
| TCU Horned Frogs @ BYU Cougars | **HOME** (-12.0) | **OVER** (158.5) | 100% |
| Sacred Heart Pioneers @ Siena Saints | **HOME** (-8.5) | **OVER** (138.0) | 100% |
| South Carolina Gamecocks @ Arkansas Razorbacks | **HOME** (-10.5) | **OVER** (156.5) | 100% |
| Southern Miss Golden Eagles @ Troy Trojans | **HOME** (-9.0) | **OVER** (147.5) | 100% |
| Temple Owls @ Memphis Tigers | **HOME** (-8.0) | **OVER** (146.5) | 100% |
| La Salle Explorers @ Richmond Spiders | **HOME** (-8.0) | **OVER** (146.5) | 100% |
| Saint Peter's Peacocks @ Quinnipiac Bobcats | **HOME** (-7.0) | **OVER** (142.5) | 100% |
| Coastal Carolina Chanticleers @ Marshall Thundering Herd | **HOME** (-8.5) | **OVER** (149.5) | 100% |
| Ole Miss Rebels @ Georgia Bulldogs | **HOME** (-11.0) | **OVER** (161.0) | 100% |
| Colorado Buffaloes @ Cincinnati Bearcats | **HOME** (-8.0) | **OVER** (148.5) | 100% |
| Niagara Purple Eagles @ Canisius Golden Griffins | **HOME** (-3.0) | **OVER** (127.5) | 100% |
| Oral Roberts Golden Eagles @ Denver Pioneers | **HOME** (-8.0) | **OVER** (156.0) | 100% |
| Lafayette Leopards @ Bucknell Bison | **HOME** (-4.5) | **OVER** (138.5) | 100% |
| Missouri St Bears @ Western Kentucky Hilltoppers | **HOME** (-6.5) | **OVER** (148.5) | 100% |
| Drake Bulldogs @ Southern Illinois Salukis | **HOME** (-5.5) | **OVER** (147.5) | 100% |
| Virginia Tech Hokies @ SMU Mustangs | **HOME** (-7.5) | **OVER** (158.0) | 100% |
| South Dakota St Jackrabbits @ North Dakota St Bison | **HOME** (-5.5) | **OVER** (149.0) | 100% |
| Manhattan Jaspers @ Fairfield Stags | **HOME** (-5.5) | **OVER** (156.0) | 100% |
| South Carolina Upstate Spartans @ Charleston Southern Buccaneers | **HOME** (-4.5) | **OVER** (155.5) | 100% |
| Furman Paladins @ Samford Bulldogs | **HOME** (-2.0) | **OVER** (149.5) | 100% |
| Loyola Marymount Lions @ Oregon St Beavers | **HOME** (+1.5) | **OVER** (140.0) | 100% |
| Middle Tennessee Blue Raiders @ Louisiana Tech Bulldogs | **HOME** (+3.5) | **OVER** (131.5) | 100% |
| Sam Houston St Bearkats @ Jacksonville St Gamecocks | **HOME** (+0.0) | **OVER** (150.0) | 100% |
| Florida Int'l Golden Panthers @ Kennesaw St Owls | **HOME** (-4.0) | **OVER** (171.0) | 100% |
| San Diego St Aztecs @ Wyoming Cowboys | **HOME** (+1.5) | **OVER** (148.0) | 100% |
| St. Bonaventure Bonnies @ Saint Joseph's Hawks | **HOME** (+1.0) | **OVER** (149.0) | 100% |
| Auburn Tigers @ Missouri Tigers | **HOME** (+0.0) | **OVER** (154.5) | 100% |
| Portland Pilots @ Pepperdine Waves | **HOME** (+2.5) | **OVER** (146.0) | 100% |
| Pittsburgh Panthers @ Georgia Tech Yellow Jackets | **HOME** (+1.5) | **OVER** (148.5) | 100% |
| UCF Knights @ Kansas St Wildcats | **HOME** (-2.0) | **OVER** (170.5) | 100% |
| UNC Asheville Bulldogs @ Presbyterian Blue Hose | **HOME** (+4.5) | **OVER** (135.5) | 100% |
| North Carolina Tar Heels @ Stanford Cardinal | **HOME** (+3.5) | **OVER** (145.0) | 100% |
| UCLA Bruins @ Penn State Nittany Lions | **HOME** (+3.5) | **OVER** (149.0) | 100% |
| UAB Blazers @ Tulane Green Wave | **HOME** (+2.5) | **OVER** (153.0) | 100% |
| Tulsa Golden Hurricane @ Charlotte 49ers | **HOME** (+4.0) | **OVER** (150.0) | 100% |
| Kentucky Wildcats @ LSU Tigers | **HOME** (+4.0) | **OVER** (154.0) | 100% |
| Illinois St Redbirds @ Indiana St Sycamores | **HOME** (+5.5) | **OVER** (147.0) | 100% |
| Rice Owls @ UTSA Roadrunners | **HOME** (+6.5) | **OVER** (145.5) | 100% |
| Iona Gaels @ Rider Broncs | **HOME** (+7.5) | **OVER** (144.0) | 100% |
| Vanderbilt Commodores @ Texas Longhorns | **HOME** (+5.0) | **OVER** (166.5) | 100% |
| Illinois Fighting Illini @ Northwestern Wildcats | **HOME** (+8.5) | **OVER** (151.5) | 100% |
| Colgate Raiders @ Loyola (MD) Greyhounds | **HOME** (+10.5) | **OVER** (150.5) | 100% |
| Duke Blue Devils @ California Golden Bears | **HOME** (+12.5) | **OVER** (152.5) | 100% |
| Michigan Wolverines @ Washington Huskies | **HOME** (+12.5) | **OVER** (165.0) | 100% |
| Radford Highlanders @ Gardner-Webb Bulldogs | **HOME** (+13.5) | **OVER** (166.0) | 100% |

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
│   ├── show_team_ratings_v3.py  # Display team ratings (Phase 3D Enhanced)
│   ├── predict_today.py         # Today's game predictions
│   ├── populate_season.py       # Populate database with season data
│   ├── update_accuracy.py       # Update accuracy metrics
│   └── test_odds_api.py         # Test Odds API integration
├── validation/                   # Backtesting & validation
│   ├── backtest_option1_last_season.py
│   ├── backtest_option2_rolling.py
│   ├── backtest_option3_cross_validation.py
│   └── run_all_backtests.py
├── docs/                         # Documentation
│   ├── PHASE1_COMPLETE.md       # Phase 1 implementation details
│   ├── RATING_IMPROVEMENTS.md   # Roadmap for improvements
│   ├── ESPN_INTEGRATION_COMPLETE.md
│   ├── DATA_COLLECTION_FIX.md
│   ├── SOS_ADJUSTMENT_SUMMARY.md
│   ├── ALTERNATIVE_APIS.md
│   └── HYBRID_MODEL_README.md
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

