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
| **Last 7 Days** | 1-0 | **100.0%** |
| **Last 30 Days** | 1-0 | **100.0%** |
| **All-Time** | 1-0 | **100.0%** |

#### 🎯 Accuracy by Confidence (ATS)

| Confidence | Record | Accuracy |
|------------|--------|----------|
| **50%+** | 1-0 | **100.0%** |

#### Straight-Up Predictions (Games Without Vegas Lines)

| **7-Day** | 1/3 (33.3%) |
| **30-Day** | 1/3 (33.3%) |
| **All-Time** | 1/3 (33.3%) |

#### Combined Statistics

- **Total Predictions**: 4
- **Overall Winner Accuracy**: 50.0%

#### 📅 Predictions for 2026-01-15

| Matchup | Spread Pick | Total Pick | Confidence |
|---------|-------------|------------|------------|
| Bellarmine Knights @ Lipscomb Bisons | **HOME** (-10.5) | **OVER** (155.0) | 97% |
| Eastern Kentucky Colonels @ Austin Peay Governors | **HOME** (-7.0) | **OVER** (154.0) | 84% |
| Elon Phoenix @ Northeastern Huskies | **HOME** (+3.5) | **OVER** (161.5) | 100% |
| Oakland Golden Grizzlies @ Milwaukee Panthers | **HOME** (+3.0) | **OVER** (166.5) | 78% |
| Idaho Vandals @ Idaho State Bengals | **HOME** (-2.5) | **OVER** (149.0) | 100% |
| UC Riverside Highlanders @ Long Beach St 49ers | **HOME** (-4.5) | **OVER** (141.0) | 100% |
| The Citadel Bulldogs @ UNC Greensboro Spartans | **HOME** (-9.0) | **OVER** (147.0) | 97% |
| San Diego Toreros @ Seattle Redhawks | **HOME** (-8.5) | **OVER** (148.0) | 100% |
| North Carolina A&T Aggies @ William & Mary Tribe | **HOME** (-13.5) | **OVER** (163.0) | 100% |
| Tarleton State Texans @ Southern Utah Thunderbirds | **HOME** (+4.5) | **OVER** (150.5) | 100% |
| Cal Baptist Lancers @ Abilene Christian Wildcats | **HOME** (-2.0) | **OVER** (139.5) | 100% |
| Charleston Cougars @ Towson Tigers | **HOME** (-1.5) | **OVER** (141.5) | 98% |
| N Colorado Bears @ Portland St Vikings | **HOME** (-3.0) | **OVER** (156.0) | 98% |
| Eastern Washington Eagles @ Weber State Wildcats | **HOME** (-4.5) | **UNDER** (159.5) | 52% |
| Detroit Mercy Titans @ Northern Kentucky Norse | **HOME** (-10.0) | **OVER** (157.5) | 100% |
| Green Bay Phoenix @ Cleveland St Vikings | **HOME** (+4.0) | **OVER** (149.5) | 100% |
| Drexel Dragons @ Monmouth Hawks | **HOME** (-5.5) | **OVER** (130.0) | 100% |
| Youngstown St Penguins @ Wright St Raiders | **HOME** (-6.0) | **OVER** (143.0) | 100% |
| Morehead St Eagles @ Tennessee St Tigers | **HOME** (-8.5) | **OVER** (148.5) | 100% |
| Maine Black Bears @ Vermont Catamounts | **HOME** (-14.0) | **OVER** (130.0) | 100% |
| UTEP Miners @ Delaware Blue Hens | **HOME** (-1.5) | **OVER** (127.0) | 99% |
| Jacksonville Dolphins @ Central Arkansas Bears | **HOME** (-7.5) | **OVER** (137.0) | 99% |
| UMKC Kangaroos @ South Dakota Coyotes | **HOME** (-7.5) | **OVER** (158.5) | 99% |
| Lindenwood Lions @ SE Missouri St Redhawks | **HOME** (-6.5) | **OVER** (155.0) | 99% |
| CSU Northridge Matadors @ UC San Diego Tritons | **HOME** (-7.5) | **OVER** (159.0) | 99% |
| St. Thomas (MN) Tommies @ North Dakota Fighting Hawks | **HOME** (+9.0) | **OVER** (150.5) | 93% |
| Old Dominion Monarchs @ Georgia Southern Eagles | **HOME** (-6.0) | **OVER** (162.5) | 99% |
| Northern Arizona Lumberjacks @ Sacramento St Hornets | **HOME** (-3.5) | **OVER** (155.0) | 68% |
| Eastern Illinois Panthers @ Arkansas-Little Rock Trojans | **HOME** (-6.5) | **OVER** (134.0) | 98% |
| Queens University Royals @ Florida Gulf Coast Eagles | **HOME** (-1.5) | **OVER** (167.0) | 98% |
| SIU-Edwardsville Cougars @ Tenn-Martin Skyhawks | **HOME** (-8.0) | **OVER** (132.0) | 97% |
| Hawai'i Rainbow Warriors @ Cal Poly Mustangs | **HOME** (+5.0) | **OVER** (156.5) | 94% |
| West Georgia Wolves @ Stetson Hatters | **HOME** (+3.5) | **OVER** (150.0) | 63% |
| Gonzaga Bulldogs @ Washington St Cougars | **AWAY** (+17.5) | **OVER** (157.0) | 93% |
| Southern Indiana Screaming Eagles @ Tennessee Tech Golden Eagles | **HOME** (-5.5) | **OVER** (143.5) | 93% |
| CSU Fullerton Titans @ UC Davis Aggies | **HOME** (-3.5) | **OVER** (168.5) | 93% |
| Wichita St Shockers @ Florida Atlantic Owls | **HOME** (-4.5) | **OVER** (155.0) | 93% |
| Hofstra Pride @ Stony Brook Seawolves | **HOME** (+7.5) | **OVER** (134.5) | 90% |
| UT-Arlington Mavericks @ Utah Tech Trailblazers | **HOME** (-1.0) | **OVER** (143.0) | 89% |
| UC Santa Barbara Gauchos @ CSU Bakersfield Roadrunners | **HOME** (+6.5) | **UNDER** (145.0) | 51% |
| North Florida Ospreys @ North Alabama Lions | **HOME** (-9.5) | **OVER** (157.5) | 88% |
| Arkansas St Red Wolves @ South Alabama Jaguars | **HOME** (+3.0) | **OVER** (154.0) | 59% |

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

