"""
Neural Network model for spread and total prediction.
Uses TensorFlow/Keras for implementation.
"""
import os
import numpy as np
from typing import Tuple, Optional, Dict, List
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, callbacks
from sklearn.model_selection import train_test_split
import json

import config


class SpreadPredictionModel:
    """Neural network model for predicting game spreads and totals."""
    
    def __init__(self, input_dim: int, hidden_layers: Optional[List[int]] = None,
                 dropout_rate: float = 0.3, learning_rate: float = 0.001):
        """
        Initialize the model.
        
        Args:
            input_dim: Number of input features
            hidden_layers: List of hidden layer sizes (default: [256, 128, 64])
            dropout_rate: Dropout rate for regularization
            learning_rate: Learning rate for optimizer
        """
        self.input_dim = input_dim
        self.hidden_layers = hidden_layers or config.NN_HIDDEN_LAYERS
        self.dropout_rate = dropout_rate
        self.learning_rate = learning_rate
        self.model = None
        self.history = None
        
    def build_model(self):
        """Build the neural network architecture."""
        inputs = keras.Input(shape=(self.input_dim,))
        x = inputs
        
        # Hidden layers with batch normalization and dropout
        for i, units in enumerate(self.hidden_layers):
            x = layers.Dense(units, activation='relu')(x)
            x = layers.BatchNormalization()(x)
            if i < len(self.hidden_layers) - 1:  # Don't apply dropout to last hidden layer
                x = layers.Dropout(self.dropout_rate)(x)
        
        # Output layer: 2 outputs (predicted margin, predicted total)
        outputs = layers.Dense(2, activation='linear', name='predictions')(x)
        
        # Create model
        self.model = keras.Model(inputs=inputs, outputs=outputs)
        
        # Compile model
        self.model.compile(
            optimizer=keras.optimizers.Adam(learning_rate=self.learning_rate),
            loss='mse',  # Mean Squared Error for regression
            metrics=['mae', 'mse']  # Mean Absolute Error, Mean Squared Error
        )
        
        return self.model
    
    def train(self, X: np.ndarray, y: np.ndarray, 
              validation_split: float = 0.2, epochs: int = 100,
              batch_size: int = 32, verbose: int = 1) -> keras.callbacks.History:
        """
        Train the model.
        
        Args:
            X: Feature matrix (n_samples, n_features)
            y: Target matrix (n_samples, 2) - [margin, total]
            validation_split: Fraction of data to use for validation
            epochs: Number of training epochs
            batch_size: Batch size
            verbose: Verbosity level
        
        Returns:
            Training history
        """
        if self.model is None:
            self.build_model()
        
        # Split into train/validation
        X_train, X_val, y_train, y_val = train_test_split(
            X, y, test_size=validation_split, random_state=42
        )
        
        # Callbacks
        early_stopping = callbacks.EarlyStopping(
            monitor='val_loss',
            patience=15,
            restore_best_weights=True,
            verbose=1
        )
        
        reduce_lr = callbacks.ReduceLROnPlateau(
            monitor='val_loss',
            factor=0.5,
            patience=5,
            min_lr=1e-6,
            verbose=1
        )
        
        # Train model
        self.history = self.model.fit(
            X_train, y_train,
            validation_data=(X_val, y_val),
            epochs=epochs,
            batch_size=batch_size,
            callbacks=[early_stopping, reduce_lr],
            verbose=verbose
        )
        
        return self.history
    
    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Make predictions.
        
        Args:
            X: Feature matrix (n_samples, n_features)
        
        Returns:
            Predictions (n_samples, 2) - [margin, total]
        """
        if self.model is None:
            raise ValueError("Model not built or loaded. Call build_model() or load_model() first.")
        
        return self.model.predict(X, verbose=0)
    
    def evaluate(self, X: np.ndarray, y: np.ndarray) -> Dict[str, float]:
        """
        Evaluate model on test data.
        
        Args:
            X: Feature matrix
            y: Target matrix
        
        Returns:
            Dictionary of metrics
        """
        if self.model is None:
            raise ValueError("Model not built or loaded.")
        
        results = self.model.evaluate(X, y, verbose=0)
        metrics = {
            'loss': float(results[0]),
            'mae': float(results[1]),
            'mse': float(results[2])
        }
        
        # Calculate RMSE for margin and total separately
        predictions = self.predict(X)
        margin_rmse = np.sqrt(np.mean((predictions[:, 0] - y[:, 0]) ** 2))
        total_rmse = np.sqrt(np.mean((predictions[:, 1] - y[:, 1]) ** 2))
        
        metrics['margin_rmse'] = float(margin_rmse)
        metrics['total_rmse'] = float(total_rmse)
        
        return metrics
    
    def save_model(self, model_path: str, scaler_path: Optional[str] = None):
        """
        Save model and optional scaler.
        
        Args:
            model_path: Path to save the model
            scaler_path: Path to save the scaler (if provided)
        """
        if self.model is None:
            raise ValueError("No model to save.")
        
        os.makedirs(os.path.dirname(model_path), exist_ok=True)
        self.model.save(model_path)
        
        # Save model metadata
        metadata = {
            'input_dim': self.input_dim,
            'hidden_layers': self.hidden_layers,
            'dropout_rate': self.dropout_rate,
            'learning_rate': self.learning_rate,
            'model_path': model_path,
            'scaler_path': scaler_path
        }
        
        metadata_path = model_path.replace('.h5', '_metadata.json').replace('.keras', '_metadata.json')
        if not metadata_path.endswith('_metadata.json'):
            metadata_path = model_path + '_metadata.json'
        
        with open(metadata_path, 'w') as f:
            json.dump(metadata, f, indent=2)
    
    def load_model(self, model_path: str):
        """
        Load a saved model.
        
        Args:
            model_path: Path to the saved model
        """
        self.model = keras.models.load_model(model_path)
        
        # Try to load metadata
        metadata_path = model_path.replace('.h5', '_metadata.json').replace('.keras', '_metadata.json')
        if not metadata_path.endswith('_metadata.json'):
            metadata_path = model_path + '_metadata.json'
        
        if os.path.exists(metadata_path):
            with open(metadata_path, 'r') as f:
                metadata = json.load(f)
                self.input_dim = metadata.get('input_dim', self.input_dim)
                self.hidden_layers = metadata.get('hidden_layers', self.hidden_layers)
                self.dropout_rate = metadata.get('dropout_rate', self.dropout_rate)
                self.learning_rate = metadata.get('learning_rate', self.learning_rate)
    
    def get_hyperparameters(self) -> Dict:
        """Get model hyperparameters."""
        return {
            'input_dim': self.input_dim,
            'hidden_layers': self.hidden_layers,
            'dropout_rate': self.dropout_rate,
            'learning_rate': self.learning_rate
        }
    
    def summary(self):
        """Print model summary."""
        if self.model is None:
            print("Model not built yet.")
        else:
            self.model.summary()


def prepare_training_data(features_list: List[np.ndarray], 
                         margins: List[float], totals: List[float]) -> Tuple[np.ndarray, np.ndarray]:
    """
    Prepare training data from lists of features and targets.
    
    Args:
        features_list: List of feature arrays
        margins: List of actual margins
        totals: List of actual totals
    
    Returns:
        X: Feature matrix
        y: Target matrix
    """
    X = np.vstack(features_list)
    y = np.column_stack([margins, totals])
    return X.astype(np.float32), y.astype(np.float32)

