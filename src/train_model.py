"""
Training script for the neural network model.
Loads historical data from database, trains model, and saves it.
"""
import os
import sys
from datetime import datetime
from typing import List, Dict, Optional
import numpy as np

from src.database import get_database
from src.ml_model import SpreadPredictionModel, prepare_training_data
from src.ml_features import MLFeatureEngineer
from src.predictor import Predictor
from src.data_collector import DataCollector
from src.feature_calculator import FeatureCalculator
from src.ukf_model import TeamUKF
import config


def recompute_ukf_features(training_data: List[Dict], predictor: Predictor) -> List[np.ndarray]:
    """
    Recompute UKF features for training data.
    This ensures features are computed correctly even if they weren't stored.
    """
    feature_arrays = []

    # Fetch completed games ONCE before the loop
    all_games = predictor.collector.get_completed_games()

    # Engineer features
    feature_engineer = MLFeatureEngineer(
        collector=predictor.collector,
        calculator=predictor.calculator
    )

    for record in training_data:
        game_id = record['game_id']

        # Get team IDs from database
        home_team_id = record.get('home_team_id')
        away_team_id = record.get('away_team_id')

        if home_team_id is None or away_team_id is None:
            continue

        # Get UKF states
        home_state = predictor.ukf.get_team_state(home_team_id)
        away_state = predictor.ukf.get_team_state(away_team_id)
        home_ukf = predictor.ukf.get_team_ukf(home_team_id)
        away_ukf = predictor.ukf.get_team_ukf(away_team_id)
        home_uncertainty = home_ukf.get_uncertainty()
        away_uncertainty = away_ukf.get_uncertainty()

        # Get game date from database
        game_date = record.get('game_date')
        if game_date is None:
            continue

        # Parse game_date if it's a string
        if isinstance(game_date, str):
            try:
                game_date = datetime.fromisoformat(game_date.replace('Z', '+00:00'))
            except:
                continue

        # Create game object from database record (no API needed)
        game = {
            'GameID': game_id,
            'DateTime': game_date.isoformat() if isinstance(game_date, datetime) else str(game_date),
            'HomeTeam': 'Unknown',
            'AwayTeam': 'Unknown'
        }

        try:
            features_array, _ = feature_engineer.engineer_features(
                home_state, away_state,
                home_uncertainty, away_uncertainty,
                game, home_team_id, away_team_id,
                game_date, all_games
            )
            feature_arrays.append(features_array)
        except Exception as e:
            print(f"Failed to engineer features for game {game_id}: {e}")
            continue

    return feature_arrays


def train_model(season: Optional[int] = None, limit: Optional[int] = None,
                epochs: int = None, batch_size: int = None) -> Dict:
    """
    Train the neural network model.
    
    Args:
        season: Season to train on (None for all available)
        limit: Limit number of training examples
        epochs: Number of training epochs (None to use config default)
        batch_size: Batch size (None to use config default)
    
    Returns:
        Dictionary with training results
    """
    print("Starting model training...")
    
    # Initialize components
    database = get_database()
    predictor = Predictor()
    predictor.initialize()
    
    # Load training data from database
    print("Loading training data from database...")
    training_data = database.get_training_data(season=season, limit=limit)
    
    if len(training_data) < 100:
        raise ValueError(f"Insufficient training data: {len(training_data)} records. Need at least 100.")
    
    print(f"Loaded {len(training_data)} training records")
    
    # Recompute features (in case they weren't stored properly)
    print("Engineering features...")
    feature_engineer = MLFeatureEngineer(
        collector=predictor.collector,
        calculator=predictor.calculator
    )

    # Fetch completed games ONCE before the loop
    print("Loading completed games for context...")
    all_games = predictor.collector.get_completed_games()
    print(f"Loaded {len(all_games)} completed games")

    features_list = []
    margins = []
    totals = []

    for i, record in enumerate(training_data):
        if (i + 1) % 50 == 0:
            print(f"  Processing example {i+1}/{len(training_data)}...")
        
        game_id = record['game_id']

        # Get team IDs from stored data
        home_team_id = record.get('home_team_id')
        away_team_id = record.get('away_team_id')

        # Skip if database is missing team IDs (shouldn't happen in production)
        if home_team_id is None or away_team_id is None:
            if i < 5:  # Log first few errors only
                print(f"  Skipping game {game_id}: missing team IDs in database")
            continue
        
        # Get UKF states
        home_state = predictor.ukf.get_team_state(home_team_id)
        away_state = predictor.ukf.get_team_state(away_team_id)
        home_ukf = predictor.ukf.get_team_ukf(home_team_id)
        away_ukf = predictor.ukf.get_team_ukf(away_team_id)
        home_uncertainty = home_ukf.get_uncertainty()
        away_uncertainty = away_ukf.get_uncertainty()

        # Get game date from database
        game_date = record.get('game_date')
        if game_date is None:
            if i < 5:
                print(f"  Skipping game {game_id}: missing game_date in database")
            continue

        # Parse game_date if it's a string
        if isinstance(game_date, str):
            try:
                game_date = datetime.fromisoformat(game_date.replace('Z', '+00:00'))
            except:
                continue

        # Always create game object from database record (no API needed)
        game = {
            'GameID': game_id,
            'DateTime': game_date.isoformat() if isinstance(game_date, datetime) else str(game_date),
            'HomeTeam': 'Unknown',  # Not used in feature engineering
            'AwayTeam': 'Unknown'   # Not used in feature engineering
        }
        # Note: PointSpread and OverUnder removed - not used in ML features
        
        try:
            features_array, _ = feature_engineer.engineer_features(
                home_state, away_state,
                home_uncertainty, away_uncertainty,
                game, home_team_id, away_team_id,
                game_date, all_games
            )
            
            features_list.append(features_array)
            margins.append(float(record['actual_margin']))
            totals.append(float(record['actual_total']))
        except Exception as e:
            if i < 5:  # Only print first few errors
                print(f"  Failed to process game {game_id}: {e}")
            continue
    
    if len(features_list) < 50:
        raise ValueError(f"Insufficient valid training examples: {len(features_list)}")
    
    print(f"Prepared {len(features_list)} training examples")
    
    # Prepare training data
    X, y = prepare_training_data(features_list, margins, totals)
    
    # Fit scaler on all features
    print("Fitting feature scaler...")
    feature_engineer.fit_scaler(features_list)
    
    # Transform features
    X_scaled = np.array([feature_engineer.transform_features(f) for f in features_list])
    
    # Determine input dimension
    input_dim = X_scaled.shape[1]
    print(f"Input dimension: {input_dim}")
    
    # Create and train model
    print("Building model...")
    model = SpreadPredictionModel(
        input_dim=input_dim,
        hidden_layers=config.NN_HIDDEN_LAYERS,
        dropout_rate=config.NN_DROPOUT_RATE,
        learning_rate=config.NN_LEARNING_RATE
    )
    model.build_model()
    
    print("Training model...")
    epochs = epochs or config.NN_EPOCHS
    batch_size = batch_size or config.NN_BATCH_SIZE
    
    history = model.train(
        X_scaled, y,
        validation_split=config.NN_VALIDATION_SPLIT,
        epochs=epochs,
        batch_size=batch_size,
        verbose=1
    )
    
    # Evaluate on validation set
    from sklearn.model_selection import train_test_split
    X_train, X_val, y_train, y_val = train_test_split(
        X_scaled, y, test_size=config.NN_VALIDATION_SPLIT, random_state=42
    )
    
    print("Evaluating model...")
    metrics = model.evaluate(X_val, y_val)
    print(f"Validation metrics: {metrics}")
    
    # Save model
    os.makedirs(config.MODEL_PATH, exist_ok=True)
    
    # Determine next version number
    session = database.get_session()
    try:
        from src.database import ModelVersion
        existing_versions = session.query(ModelVersion).order_by(
            ModelVersion.version_number.desc()
        ).all()
        next_version = existing_versions[0].version_number + 1 if existing_versions else 1
    except:
        next_version = 1
    finally:
        session.close()
    
    model_filename = f"model_v{next_version}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.keras"
    model_path = os.path.join(config.MODEL_PATH, model_filename)
    
    scaler_filename = f"scaler_v{next_version}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pkl"
    scaler_path = os.path.join(config.MODEL_PATH, scaler_filename)
    
    print(f"Saving model to {model_path}...")
    model.save_model(model_path, scaler_path)
    feature_engineer.save_scaler(scaler_path)
    
    # Save to database
    hyperparameters = model.get_hyperparameters()
    hyperparameters['epochs'] = epochs
    hyperparameters['batch_size'] = batch_size
    hyperparameters['scaler_path'] = scaler_path
    
    # Deactivate old models and activate new one
    version_id = database.save_model_version(
        version_number=next_version,
        model_path=model_path,
        training_games_count=len(features_list),
        validation_accuracy=metrics.get('margin_rmse'),  # Using margin RMSE as validation metric
        hyperparameters=hyperparameters,
        is_active=True
    )
    
    print(f"Model saved as version {next_version} (ID: {version_id})")
    
    return {
        'version_id': version_id,
        'version_number': next_version,
        'model_path': model_path,
        'scaler_path': scaler_path,
        'training_examples': len(features_list),
        'validation_metrics': metrics,
        'hyperparameters': hyperparameters
    }


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Train neural network model for spread prediction")
    parser.add_argument("--season", type=int, help="Season to train on (default: all)")
    parser.add_argument("--limit", type=int, help="Limit number of training examples")
    parser.add_argument("--epochs", type=int, help="Number of epochs (default: from config)")
    parser.add_argument("--batch-size", type=int, help="Batch size (default: from config)")
    
    args = parser.parse_args()
    
    try:
        results = train_model(
            season=args.season,
            limit=args.limit,
            epochs=args.epochs,
            batch_size=getattr(args, 'batch_size')
        )
        print("\nTraining completed successfully!")
        print(f"Model version: {results['version_number']}")
        print(f"Validation RMSE (margin): {results['validation_metrics']['margin_rmse']:.2f}")
        print(f"Validation RMSE (total): {results['validation_metrics']['total_rmse']:.2f}")
    except Exception as e:
        print(f"\nTraining failed: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)

