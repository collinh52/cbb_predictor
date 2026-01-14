---
name: UKF Basketball Predictor
overview: Build a college basketball game outcome predictor using Unscented Kalman Filter (UKF) to track team offensive/defensive ratings and predict spreads/totals. Includes API data collection, UKF implementation, FastAPI backend, and web frontend.
todos:
  - id: setup_project
    content: Create project structure, requirements.txt, and config.py with API key placeholders
    status: pending
  - id: data_collector
    content: Implement data_collector.py to fetch games, scores, spreads, totals, player injuries, and team stats (pace, recent results, travel) from API
    status: pending
    dependencies:
      - setup_project
  - id: feature_calculator
    content: Create feature_calculator.py to compute momentum, fatigue, health status, and home advantage from collected data
    status: pending
    dependencies:
      - data_collector
  - id: ukf_implementation
    content: Implement UKF model in ukf_model.py with expanded state vector (offensive_rating, defensive_rating, home_advantage, health_status, momentum, fatigue, pace) per team
    status: pending
    dependencies:
      - setup_project
  - id: predictor_engine
    content: Create predictor.py to process historical games, update all state components via UKF, and generate predictions using full state vector (ratings + health + momentum + fatigue + pace + home advantage)
    status: pending
    dependencies:
      - data_collector
      - feature_calculator
      - ukf_implementation
  - id: api_backend
    content: Build FastAPI backend with endpoints for games and predictions
    status: pending
    dependencies:
      - predictor_engine
  - id: web_frontend
    content: Create HTML/CSS/JS frontend to display games and predictions with confidence scores
    status: pending
    dependencies:
      - api_backend
---

#

UKF College Basketball Predictor

A web application that uses the Unscented Kalman Filter to predict college basketball game outcomes, including spread coverage and over/under probabilities.

## Architecture Overview

```javascript
Data Collection → UKF Processing → Prediction API → Web Frontend
```



## Implementation Plan

### 1. Project Structure

- `requirements.txt` - Python dependencies (numpy, scipy, fastapi, uvicorn, requests, pandas)

- `README.md` - Setup and usage instructions

- `config.py` - Configuration for API keys and settings

- `data/` - Directory for cached game data

- `src/` - Main source code

- `data_collector.py` - API integration for fetching game data, injuries, team stats

- `feature_calculator.py` - Calculate momentum, fatigue, health status, home advantage

- `ukf_model.py` - UKF implementation with expanded state vector

- `predictor.py` - Main prediction logic using full state vector

- `api.py` - FastAPI backend endpoints

- `static/` - Frontend assets (HTML, CSS, JavaScript)

- `templates/` - HTML templates

### 2. Data Collection Module (`src/data_collector.py`)

- Integrate with college basketball API (e.g., ESPN API, SportsDataIO, or The Odds API)

- Fetch completed games with scores, spreads, and totals

- Fetch upcoming games with current spreads and totals

- Collect player injury/health data (aggregate team health score based on key player availability)

- Collect team statistics: pace (possessions per game), recent game results, travel information

- Calculate derived features:
  - Momentum: Recent win/loss record and point differential trend (last 5-10 games)
  - Fatigue: Games played in recent days + travel distance/rest days
  - Home court advantage: Per-team historical home vs away performance

- Cache data locally to minimize API calls

- Handle API rate limiting and errors

### 3. UKF Model (`src/ukf_model.py`)

- Implement Unscented Kalman Filter from scratch or use library (filterpy)

- Expanded state vector per team (see Technical Details section for full specification):
  - `offensive_rating` - Team's offensive strength
  - `defensive_rating` - Team's defensive strength  
  - `home_advantage` - Team-specific home court advantage (points)
  - `health_status` - Aggregate team health score (0-1, based on key player availability)
  - `momentum` - Recent performance momentum (normalized score)
  - `fatigue` - Fatigue factor (0-1, higher = more fatigued)
  - `pace` - Team's preferred pace/tempo (possessions per game)

- Process model: Each state component evolves with appropriate dynamics (see Technical Details section for component-specific process models)

- Measurement model: Use actual game scores, pace, and game context to update all state components

- Track both:

- Team offensive/defensive ratings (for spread prediction)
- Expected game totals (for over/under prediction)

- Initialize state from historical data or use prior estimates

- Handle missing data (e.g., if injury data unavailable, use default health score)

### 4. Prediction Engine (`src/predictor.py`)

- Load all completed games from current season

- Calculate game-specific features for upcoming games:
  - Home team's home advantage
  - Both teams' current health status
  - Both teams' momentum scores
  - Both teams' fatigue levels
  - Expected game pace (average of both teams' pace)

- Run UKF to estimate current team states (ratings + all features)

- For upcoming games:

- Predict point differential using:
  - Team offensive/defensive ratings
  - Home court advantage (if home team)
  - Health status impact
  - Momentum impact
  - Fatigue impact

- Predict total points using:
  - Both teams' offensive ratings
  - Expected game pace
  - Health status (affects offensive output)
  - Fatigue (affects pace and scoring)

- Calculate spread coverage probability (P(team covers))

- Calculate over/under probability

- Return confidence scores (0-100%) for each prediction based on UKF uncertainty estimates

### 5. FastAPI Backend (`src/api.py`)

- `/api/games/today` - Get today's games with predictions

- `/api/games/upcoming` - Get upcoming games

- `/api/predictions/{game_id}` - Get detailed predictions for a game

- `/api/teams/ratings` - Get current team ratings

- Serve static frontend files

### 6. Web Frontend (`static/` and `templates/`)

- Main dashboard showing today's games

- For each game display:
- Teams and matchup

- Current spread and total

- Predicted winner with confidence

- Spread coverage confidence (team covers/doesn't cover)

- Over/under confidence

- Visual indicators (color coding) for confidence levels

- Refresh button to update predictions

### 7. Configuration (`config.py`)

- API key management

- Season configuration (current season year)

- UKF parameters (process noise, measurement noise)

- Data refresh intervals

## Technical Details

### UKF State Model

- For each team: `[offensive_rating, defensive_rating, home_advantage, health_status, momentum, fatigue, pace]`

- State vector size: 7 dimensions per team × number of teams

- Process model: Component-specific dynamics:
  - `offensive_rating_k = offensive_rating_{k-1} + w_off` (random walk)
  - `defensive_rating_k = defensive_rating_{k-1} + w_def` (random walk)
  - `home_advantage_k = home_advantage_{k-1} + w_home` (slow drift)
  - `health_status_k = f(injury_reports)` (can change quickly)
  - `momentum_k = α × momentum_{k-1} + (1-α) × recent_performance` (exponential decay)
  - `fatigue_k = f(games_recent, travel, rest_days)` (accumulates/decays)
  - `pace_k = pace_{k-1} + w_pace` (relatively stable)

- Measurement: Actual game scores, game pace, and contextual factors

- Update: Use score differential, total points, and game pace to update all relevant state components for both teams

- Prediction model for game outcome:
  - `predicted_margin = (home_off - away_def) - (away_off - home_def) + home_advantage + health_impact + momentum_impact - fatigue_impact`
  - `predicted_total = (home_off + away_off) × pace_factor × health_factor`

### Prediction Logic

- **Spread Coverage**: `P(team_covers) = P(predicted_margin > spread)`

- **Over/Under**: `P(over) = P(predicted_total > total_line)`

- Use UKF uncertainty estimates to calculate confidence intervals

### Data Flow

1. Fetch completed games → Update UKF with historical data

2. Fetch today's games → Generate predictions using current ratings

3. Display predictions with confidence scores

## Dependencies

- `numpy` - Numerical computations

- `scipy` - Statistical functions

- `filterpy` - Kalman filter implementation (optional, can implement UKF manually)

- `fastapi` - Web framework
- `uvicorn` - ASGI server

- `requests` - API calls

- `pandas` - Data manipulation

- `python-dateutil` - Date handling

## Notes

- Will need API key for college basketball data (user must provide)

- UKF parameters may need tuning based on data characteristics

- State vector is significantly larger (7 dimensions per team), requiring careful initialization and tuning

- Some features (health status, momentum, fatigue) may have limited historical data - need robust handling of missing data

- Home advantage, momentum, and fatigue require game-by-game calculation, not just team-level tracking

- Consider dimensionality reduction or feature selection if state space becomes too large for performance