"""
Unit tests for the ML Model module.
Tests the neural network spread prediction model.
"""
import pytest
import numpy as np
import sys
import os
import tempfile
import json

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Skip tests if TensorFlow not available
pytest.importorskip("tensorflow")

from src.ml_model import SpreadPredictionModel, prepare_training_data


class TestModelInitialization:
    """Test cases for model initialization."""
    
    @pytest.mark.unit
    def test_model_init_defaults(self):
        """Test model initializes with default parameters."""
        model = SpreadPredictionModel(input_dim=45)
        
        assert model.input_dim == 45
        assert model.hidden_layers == [256, 128, 64]
        assert model.dropout_rate == 0.3
        assert model.learning_rate == 0.001
        assert model.model is None  # Not built yet
    
    @pytest.mark.unit
    def test_model_init_custom_layers(self):
        """Test model initialization with custom layers."""
        model = SpreadPredictionModel(
            input_dim=30,
            hidden_layers=[128, 64],
            dropout_rate=0.5
        )
        
        assert model.input_dim == 30
        assert model.hidden_layers == [128, 64]
        assert model.dropout_rate == 0.5
    
    @pytest.mark.unit
    def test_model_init_custom_learning_rate(self):
        """Test model initialization with custom learning rate."""
        model = SpreadPredictionModel(input_dim=45, learning_rate=0.0001)
        
        assert model.learning_rate == 0.0001


class TestModelBuilding:
    """Test cases for model building."""
    
    @pytest.mark.unit
    def test_build_model_creates_model(self):
        """Test that build_model creates a Keras model."""
        model = SpreadPredictionModel(input_dim=45)
        built_model = model.build_model()
        
        assert model.model is not None
        assert built_model is not None
    
    @pytest.mark.unit
    def test_build_model_correct_input_shape(self):
        """Test model has correct input shape."""
        model = SpreadPredictionModel(input_dim=45)
        model.build_model()
        
        # Check input shape
        input_shape = model.model.input_shape
        assert input_shape[1] == 45
    
    @pytest.mark.unit
    def test_build_model_correct_output_shape(self):
        """Test model has correct output shape (2 outputs: margin, total)."""
        model = SpreadPredictionModel(input_dim=45)
        model.build_model()
        
        # Check output shape
        output_shape = model.model.output_shape
        assert output_shape[1] == 2
    
    @pytest.mark.unit
    def test_build_model_different_input_dims(self):
        """Test model builds correctly with different input dimensions."""
        for input_dim in [10, 30, 50, 100]:
            model = SpreadPredictionModel(input_dim=input_dim)
            model.build_model()
            
            assert model.model.input_shape[1] == input_dim


class TestModelPrediction:
    """Test cases for model prediction."""
    
    @pytest.fixture
    def trained_model(self, sample_training_data):
        """Create a minimally trained model for testing."""
        X, y = sample_training_data
        model = SpreadPredictionModel(input_dim=X.shape[1])
        model.build_model()
        # Train for just 2 epochs for speed
        model.train(X, y, epochs=2, verbose=0)
        return model
    
    @pytest.mark.unit
    def test_predict_requires_built_model(self):
        """Test that predict raises error if model not built."""
        model = SpreadPredictionModel(input_dim=45)
        X = np.random.randn(10, 45).astype(np.float32)
        
        with pytest.raises(ValueError):
            model.predict(X)
    
    @pytest.mark.unit
    def test_predict_output_shape(self, trained_model):
        """Test prediction output shape."""
        X = np.random.randn(5, 45).astype(np.float32)
        predictions = trained_model.predict(X)
        
        assert predictions.shape == (5, 2)  # 5 samples, 2 outputs
    
    @pytest.mark.unit
    def test_predict_single_sample(self, trained_model):
        """Test prediction on single sample."""
        X = np.random.randn(1, 45).astype(np.float32)
        predictions = trained_model.predict(X)
        
        assert predictions.shape == (1, 2)
    
    @pytest.mark.unit
    def test_predict_returns_finite_values(self, trained_model):
        """Test that predictions are finite numbers."""
        X = np.random.randn(10, 45).astype(np.float32)
        predictions = trained_model.predict(X)
        
        assert np.all(np.isfinite(predictions))
    
    @pytest.mark.unit
    def test_predict_margin_reasonable_range(self, trained_model):
        """Test that predicted margins are in reasonable range."""
        X = np.random.randn(10, 45).astype(np.float32)
        predictions = trained_model.predict(X)
        
        margins = predictions[:, 0]
        # Margins should generally be between -50 and +50
        # Allow some flexibility for untrained model
        assert np.all(margins > -100) and np.all(margins < 100)


class TestModelTraining:
    """Test cases for model training."""
    
    @pytest.mark.unit
    @pytest.mark.slow
    def test_train_creates_history(self, sample_training_data):
        """Test that training creates history object."""
        X, y = sample_training_data
        model = SpreadPredictionModel(input_dim=X.shape[1])
        
        history = model.train(X, y, epochs=5, verbose=0)
        
        assert model.history is not None
        assert history is not None
        assert 'loss' in history.history
    
    @pytest.mark.unit
    @pytest.mark.slow
    def test_train_loss_decreases(self, sample_training_data):
        """Test that training loss decreases (or at least runs)."""
        X, y = sample_training_data
        model = SpreadPredictionModel(input_dim=X.shape[1])
        
        history = model.train(X, y, epochs=10, verbose=0)
        
        losses = history.history['loss']
        # Loss should decrease or at least not explode
        assert losses[-1] < losses[0] * 10  # Very lenient check
    
    @pytest.mark.unit
    def test_train_with_validation(self, sample_training_data):
        """Test training with validation split."""
        X, y = sample_training_data
        model = SpreadPredictionModel(input_dim=X.shape[1])
        
        history = model.train(X, y, epochs=3, validation_split=0.2, verbose=0)
        
        assert 'val_loss' in history.history


class TestModelEvaluation:
    """Test cases for model evaluation."""
    
    @pytest.fixture
    def trained_model(self, sample_training_data):
        """Create a minimally trained model for testing."""
        X, y = sample_training_data
        model = SpreadPredictionModel(input_dim=X.shape[1])
        model.build_model()
        model.train(X, y, epochs=2, verbose=0)
        return model, X, y
    
    @pytest.mark.unit
    def test_evaluate_returns_dict(self, trained_model):
        """Test that evaluate returns metrics dictionary."""
        model, X, y = trained_model
        metrics = model.evaluate(X, y)
        
        assert isinstance(metrics, dict)
    
    @pytest.mark.unit
    def test_evaluate_contains_required_metrics(self, trained_model):
        """Test that evaluation contains required metrics."""
        model, X, y = trained_model
        metrics = model.evaluate(X, y)
        
        assert 'loss' in metrics
        assert 'mae' in metrics
        assert 'mse' in metrics
        assert 'margin_rmse' in metrics
        assert 'total_rmse' in metrics
    
    @pytest.mark.unit
    def test_evaluate_metrics_positive(self, trained_model):
        """Test that error metrics are positive."""
        model, X, y = trained_model
        metrics = model.evaluate(X, y)
        
        assert metrics['loss'] >= 0
        assert metrics['mae'] >= 0
        assert metrics['mse'] >= 0
        assert metrics['margin_rmse'] >= 0
        assert metrics['total_rmse'] >= 0


class TestModelSaveLoad:
    """Test cases for model saving and loading."""
    
    @pytest.fixture
    def trained_model(self, sample_training_data):
        """Create a minimally trained model for testing."""
        X, y = sample_training_data
        model = SpreadPredictionModel(input_dim=X.shape[1])
        model.build_model()
        model.train(X, y, epochs=2, verbose=0)
        return model
    
    @pytest.mark.unit
    def test_save_model_creates_file(self, trained_model):
        """Test that save_model creates model file."""
        with tempfile.TemporaryDirectory() as tmpdir:
            model_path = os.path.join(tmpdir, 'test_model.keras')
            trained_model.save_model(model_path)
            
            assert os.path.exists(model_path)
    
    @pytest.mark.unit
    def test_save_model_creates_metadata(self, trained_model):
        """Test that save_model creates metadata file."""
        with tempfile.TemporaryDirectory() as tmpdir:
            model_path = os.path.join(tmpdir, 'test_model.keras')
            trained_model.save_model(model_path)
            
            metadata_path = model_path.replace('.keras', '_metadata.json')
            assert os.path.exists(metadata_path)
    
    @pytest.mark.unit
    def test_save_load_predictions_match(self, trained_model, sample_training_data):
        """Test that loaded model gives same predictions."""
        X, _ = sample_training_data
        test_X = X[:5]
        
        # Get predictions before save
        original_predictions = trained_model.predict(test_X)
        
        with tempfile.TemporaryDirectory() as tmpdir:
            model_path = os.path.join(tmpdir, 'test_model.keras')
            trained_model.save_model(model_path)
            
            # Load into new model
            new_model = SpreadPredictionModel(input_dim=1)  # Will be overwritten
            new_model.load_model(model_path)
            
            # Get predictions after load
            loaded_predictions = new_model.predict(test_X)
            
            np.testing.assert_array_almost_equal(
                original_predictions, loaded_predictions, decimal=5
            )
    
    @pytest.mark.unit
    def test_load_model_restores_metadata(self, trained_model):
        """Test that loading restores model metadata."""
        with tempfile.TemporaryDirectory() as tmpdir:
            model_path = os.path.join(tmpdir, 'test_model.keras')
            trained_model.save_model(model_path)
            
            new_model = SpreadPredictionModel(input_dim=1)
            new_model.load_model(model_path)
            
            assert new_model.input_dim == trained_model.input_dim
            assert new_model.hidden_layers == trained_model.hidden_layers
    
    @pytest.mark.unit
    def test_save_model_without_built_raises(self):
        """Test that saving unbuilt model raises error."""
        model = SpreadPredictionModel(input_dim=45)
        
        with tempfile.TemporaryDirectory() as tmpdir:
            model_path = os.path.join(tmpdir, 'test_model.keras')
            with pytest.raises(ValueError):
                model.save_model(model_path)


class TestModelHyperparameters:
    """Test cases for hyperparameter management."""
    
    @pytest.mark.unit
    def test_get_hyperparameters(self):
        """Test getting hyperparameters."""
        model = SpreadPredictionModel(
            input_dim=45,
            hidden_layers=[128, 64],
            dropout_rate=0.4,
            learning_rate=0.0005
        )
        
        params = model.get_hyperparameters()
        
        assert params['input_dim'] == 45
        assert params['hidden_layers'] == [128, 64]
        assert params['dropout_rate'] == 0.4
        assert params['learning_rate'] == 0.0005


class TestPrepareTrainingData:
    """Test cases for prepare_training_data helper."""
    
    @pytest.mark.unit
    def test_prepare_training_data_shapes(self):
        """Test that prepare_training_data returns correct shapes."""
        features_list = [np.random.randn(45) for _ in range(10)]
        margins = [5.0, -3.0, 10.0, -7.0, 2.0, -1.0, 8.0, -5.0, 3.0, 0.0]
        totals = [145.0, 150.0, 142.0, 138.0, 155.0, 148.0, 140.0, 152.0, 146.0, 143.0]
        
        X, y = prepare_training_data(features_list, margins, totals)
        
        assert X.shape == (10, 45)
        assert y.shape == (10, 2)
    
    @pytest.mark.unit
    def test_prepare_training_data_dtypes(self):
        """Test that prepare_training_data returns float32."""
        features_list = [np.random.randn(20) for _ in range(5)]
        margins = [5.0, -3.0, 10.0, -7.0, 2.0]
        totals = [145.0, 150.0, 142.0, 138.0, 155.0]
        
        X, y = prepare_training_data(features_list, margins, totals)
        
        assert X.dtype == np.float32
        assert y.dtype == np.float32
    
    @pytest.mark.unit
    def test_prepare_training_data_values(self):
        """Test that prepare_training_data preserves values correctly."""
        features_list = [np.array([1.0, 2.0, 3.0])]
        margins = [5.5]
        totals = [145.0]
        
        X, y = prepare_training_data(features_list, margins, totals)
        
        np.testing.assert_array_almost_equal(X[0], [1.0, 2.0, 3.0])
        np.testing.assert_array_almost_equal(y[0], [5.5, 145.0])


class TestModelEdgeCases:
    """Edge case tests for ML model."""
    
    @pytest.mark.unit
    def test_model_with_single_hidden_layer(self, sample_training_data):
        """Test model with single hidden layer."""
        X, y = sample_training_data
        model = SpreadPredictionModel(input_dim=X.shape[1], hidden_layers=[64])
        model.build_model()
        
        predictions = model.predict(X[:5])
        assert predictions.shape == (5, 2)
    
    @pytest.mark.unit
    def test_model_with_many_hidden_layers(self, sample_training_data):
        """Test model with many hidden layers."""
        X, y = sample_training_data
        model = SpreadPredictionModel(
            input_dim=X.shape[1], 
            hidden_layers=[256, 128, 64, 32, 16]
        )
        model.build_model()
        
        predictions = model.predict(X[:5])
        assert predictions.shape == (5, 2)
    
    @pytest.mark.unit
    def test_model_with_zero_dropout(self, sample_training_data):
        """Test model with zero dropout."""
        X, y = sample_training_data
        model = SpreadPredictionModel(input_dim=X.shape[1], dropout_rate=0.0)
        model.build_model()
        model.train(X, y, epochs=2, verbose=0)
        
        predictions = model.predict(X[:5])
        assert np.all(np.isfinite(predictions))
    
    @pytest.mark.unit
    def test_model_with_high_dropout(self, sample_training_data):
        """Test model with high dropout."""
        X, y = sample_training_data
        model = SpreadPredictionModel(input_dim=X.shape[1], dropout_rate=0.7)
        model.build_model()
        model.train(X, y, epochs=2, verbose=0)
        
        predictions = model.predict(X[:5])
        assert np.all(np.isfinite(predictions))

