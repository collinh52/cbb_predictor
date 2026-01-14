# UKF College Basketball Predictor

A web application that uses the Unscented Kalman Filter (UKF) to predict college basketball game outcomes, including spread coverage and over/under probabilities.

## Features

- Tracks team offensive/defensive ratings, home court advantage, health status, momentum, fatigue, and pace
- Predicts game outcomes with confidence scores
- Shows spread coverage probabilities
- Shows over/under probabilities
- Web interface for viewing today's games and predictions

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up API key:
   - Get an API key from a college basketball data provider (e.g., SportsDataIO, ESPN API, The Odds API)
   - Create a `.env` file in the project root:
     ```bash
     BASKETBALL_API_KEY=your_api_key_here
     ```
   - Alternatively, set it as an environment variable:
     ```bash
     export BASKETBALL_API_KEY="your_api_key_here"
     ```
   - **Note:** The `.env` file is automatically loaded and should be added to `.gitignore` to keep your API key secure

3. Create data directory:
```bash
mkdir -p data/cache
```

4. Run the application:
```bash
uvicorn src.api:app --reload
```

5. Open your browser to `http://localhost:8000`

## Project Structure

```
.
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── .env                  # API key (create this file, not in git)
├── data/                 # Data storage
│   └── cache/           # Cached API responses
├── src/                  # Source code
│   ├── data_collector.py # API integration
│   ├── feature_calculator.py # Feature computation
│   ├── ukf_model.py     # UKF implementation
│   ├── predictor.py     # Prediction engine
│   └── api.py           # FastAPI backend
├── static/               # Frontend assets
└── templates/           # HTML templates
```

## State Vector

Each team's state is represented by 7 dimensions:
- `offensive_rating`: Team's offensive strength
- `defensive_rating`: Team's defensive strength
- `home_advantage`: Team-specific home court advantage (points)
- `health_status`: Aggregate team health score (0-1)
- `momentum`: Recent performance momentum
- `fatigue`: Fatigue factor (0-1, higher = more fatigued)
- `pace`: Team's preferred pace/tempo (possessions per game)

## API Endpoints

- `GET /` - Main dashboard
- `GET /api/games/today` - Get today's games with predictions
- `GET /api/games/upcoming` - Get upcoming games
- `GET /api/predictions/{game_id}` - Get detailed predictions for a game
- `GET /api/teams/ratings` - Get current team ratings

## Prediction Tracking & Accuracy ⭐ **NEW**

The system now includes automatic prediction storage and accuracy tracking!

### Daily Workflow

1. **Generate Predictions**:
   ```bash
   python scripts/predict_today.py
   ```
   - Generates predictions using Phase 2.5 enhancements
   - Automatically stores predictions for tracking
   - Shows recent accuracy if available

2. **Check Accuracy (after games complete)**:
   ```bash
   python scripts/check_prediction_accuracy.py
   ```
   - Checks stored predictions against actual results
   - Calculates spread and total accuracy
   - Shows confidence-weighted performance
   - Displays individual game results

### Features

- **Automatic Storage**: All predictions saved to `data/predictions.json`
- **Result Checking**: Compares predictions vs actual scores
- **Accuracy Metrics**:
  - Raw accuracy (% correct picks)
  - Confidence-weighted accuracy (accounts for prediction certainty)
  - Individual game breakdowns
- **Historical Tracking**: Maintains accuracy history over time

### Data Files

- `data/predictions.json`: Stored predictions by date
- `data/results.json`: Accuracy results for completed games

## Notes

- The UKF parameters in `config.py` may need tuning based on data characteristics
- Some features (health status, momentum, fatigue) may have limited historical data
- The system handles missing data gracefully with default values
- Prediction tracking requires games to have been generated with the current system

