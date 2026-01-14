# Hybrid UKF + ML Model Implementation

## Overview

The hybrid prediction system combines the Unscented Kalman Filter (UKF) for dynamic team state tracking with a Neural Network (ML) model for pattern recognition. All predictions and results are stored in a database for accuracy tracking and model improvement.

## Components

### 1. Database (`src/database.py`)
- PostgreSQL database with SQLite fallback
- Stores predictions, game results, accuracy metrics, and model versions
- Tracks prediction accuracy over time

### 2. Feature Engineering (`src/ml_features.py`)
- Combines UKF state estimates with contextual features
- Includes pregame lines, rest days, recent form, head-to-head history
- StandardScaler for feature normalization

### 3. Neural Network Model (`src/ml_model.py`)
- TensorFlow/Keras implementation
- Architecture: 3-4 hidden layers (256, 128, 64 neurons)
- Outputs: predicted margin and total points
- Includes dropout and batch normalization

### 4. Hybrid Predictor (`src/hybrid_predictor.py`)
- Combines UKF and ML predictions with weighted averaging
- Configurable weights (default: 0.5 UKF, 0.5 ML)
- Stores predictions in database automatically

### 5. Training Script (`src/train_model.py`)
- Trains model on historical data from database
- Saves models with versioning
- Updates model_versions table

## Setup

1. **Install dependencies:**
```bash
pip install -r requirements.txt
```

2. **Set up database:**
   - For PostgreSQL: Set `DATABASE_URL` in `.env` file:
     ```
     DATABASE_URL=postgresql://user:password@localhost/basketball_db
     ```
   - For SQLite (development): Defaults to `sqlite:///./basketball_predictor.db`

3. **Configure settings in `.env`:**
```
BASKETBALL_API_KEY=your_api_key
DATABASE_URL=postgresql://...
HYBRID_WEIGHT_UKF=0.5
HYBRID_WEIGHT_ML=0.5
```

## Usage

### Making Predictions

The API automatically uses the hybrid predictor:
```bash
GET /api/games/today
GET /api/predictions/{game_id}
```

### Training the Model

Train on historical data:
```bash
python -m src.train_model --season 2026 --limit 1000
```

Options:
- `--season`: Season year to train on
- `--limit`: Limit number of training examples
- `--epochs`: Number of training epochs
- `--batch-size`: Batch size

### Submitting Game Results

After games complete, submit results:
```bash
POST /api/predictions/{game_id}/result
Body: {"home_score": 75, "away_score": 68}
```

### Viewing Accuracy

Get accuracy statistics:
```bash
GET /api/predictions/accuracy?start_date=2026-01-01&end_date=2026-12-31
```

## API Endpoints

- `GET /api/games/today` - Today's games with hybrid predictions
- `GET /api/predictions/{game_id}` - Detailed prediction for a game
- `GET /api/predictions/accuracy` - Accuracy statistics
- `POST /api/predictions/{game_id}/result` - Submit game result
- `GET /api/models/versions` - List all model versions
- `POST /api/models/train` - Trigger model retraining
- `GET /api/predictions/history` - Historical predictions

## Database Schema

- **predictions**: All game predictions (UKF, ML, hybrid)
- **game_results**: Actual game results
- **model_accuracy**: Daily accuracy metrics
- **model_versions**: Model version tracking

## Model Workflow

1. **Pre-game:** 
   - UKF tracks team states
   - Features engineered (UKF + pregame lines + context)
   - ML model generates prediction
   - UKF and ML combined → Hybrid prediction
   - Prediction stored in database

2. **Post-game:**
   - Game result submitted
   - Result linked to prediction
   - Accuracy metrics updated
   - Model can be retrained with new data

3. **Training:**
   - Load historical predictions + results
   - Train new model version
   - Save and activate if validation accuracy improved

## Configuration

Edit `config.py` or set environment variables:
- `HYBRID_WEIGHT_UKF`: Weight for UKF predictions (0.0-1.0)
- `HYBRID_WEIGHT_ML`: Weight for ML predictions (0.0-1.0)
- `NN_HIDDEN_LAYERS`: Neural network architecture
- `NN_DROPOUT_RATE`: Dropout regularization
- `NN_LEARNING_RATE`: Learning rate for training

## Notes

- Model must be trained at least once before making ML predictions
- If no trained model exists, system falls back to UKF-only predictions
- Database automatically tracks all predictions for accuracy analysis
- Model versions allow A/B testing and rollback

