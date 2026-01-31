"""
Hybrid predictor that combines UKF and ML model predictions.
"""
from datetime import datetime, date
from typing import Dict, Optional, Tuple
import numpy as np
from scipy.stats import norm
import os

from src.predictor import Predictor
from src.ukf_model import TeamUKF
from src.ml_model import SpreadPredictionModel
from src.ml_features import MLFeatureEngineer
from src.database import Database, get_database
import config


class HybridPredictor:
    """Combines UKF and ML predictions for improved accuracy."""
    
    def __init__(self, ukf_predictor: Optional[Predictor] = None):
        """
        Initialize hybrid predictor.
        
        Args:
            ukf_predictor: UKF-based predictor instance
        """
        self.ukf_predictor = ukf_predictor or Predictor()
        self.ml_model: Optional[SpreadPredictionModel] = None
        self.feature_engineer = MLFeatureEngineer(
            collector=self.ukf_predictor.collector,
            calculator=self.ukf_predictor.calculator
        )
        self.database = get_database()
        self._load_active_model()
    
    def _load_active_model(self):
        """Load the active ML model from database or fallback to latest model file."""
        active_model = self.database.get_active_model_version()
        model_path = active_model['model_path'] if active_model else None
        if active_model and (not model_path or not os.path.exists(model_path)):
            # Fallback: pick newest model file from model directory when DB entry exists
            try:
                from glob import glob
                candidates = glob(os.path.join(config.MODEL_PATH, "*.keras"))
                candidates.extend(glob(os.path.join(config.MODEL_PATH, "*.h5")))
                if candidates:
                    model_path = max(candidates, key=os.path.getmtime)
                    active_model = {'model_path': model_path, 'version_number': 'latest'}
            except Exception:
                model_path = None

        if model_path and os.path.exists(model_path):
            try:
                self.ml_model = SpreadPredictionModel(input_dim=1)  # Will be set correctly on load
                self.ml_model.load_model(model_path)
                
                # Load scaler if available
                scaler_path = active_model.get('scaler_path')
                if not scaler_path:
                    metadata_path = model_path.replace('.h5', '_metadata.json').replace('.keras', '_metadata.json')
                    if not metadata_path.endswith('_metadata.json'):
                        metadata_path = model_path + '_metadata.json'
                    if os.path.exists(metadata_path):
                        try:
                            import json
                            with open(metadata_path, 'r') as f:
                                metadata = json.load(f)
                                scaler_path = metadata.get('scaler_path')
                        except Exception:
                            scaler_path = None

                if scaler_path and os.path.exists(scaler_path):
                    self.feature_engineer.load_scaler(scaler_path)
                
                print(f"Loaded active ML model version {active_model['version_number']}")
            except Exception as e:
                print(f"Failed to load ML model: {e}")
                self.ml_model = None
        else:
            print("No active ML model found. Using UKF only.")
            self.ml_model = None
    
    def predict_game(self, game: Dict) -> Dict:
        """
        Generate hybrid prediction for a game.
        
        Args:
            game: Game dictionary with team info, date, etc.
        
        Returns:
            Dictionary with predictions including UKF, ML, and hybrid predictions
        """
        # Get UKF prediction
        ukf_prediction = self.ukf_predictor.predict_game(game)
        
        # Get game details
        home_team_id = self.ukf_predictor._get_team_id(game, 'HomeTeam', 'HomeTeamID')
        away_team_id = self.ukf_predictor._get_team_id(game, 'AwayTeam', 'AwayTeamID')
        
        if home_team_id is None or away_team_id is None:
            return ukf_prediction  # Return UKF prediction if teams not found
        
        # Get UKF states and uncertainties
        home_state = self.ukf_predictor.ukf.get_team_state(home_team_id)
        away_state = self.ukf_predictor.ukf.get_team_state(away_team_id)
        home_ukf = self.ukf_predictor.ukf.get_team_ukf(home_team_id)
        away_ukf = self.ukf_predictor.ukf.get_team_ukf(away_team_id)
        home_uncertainty = home_ukf.get_uncertainty()
        away_uncertainty = away_ukf.get_uncertainty()
        
        # Get game date
        game_date_str = game.get('DateTime', '')
        if not game_date_str:
            game_date = datetime.now()
        else:
            try:
                game_date = datetime.fromisoformat(game_date_str.replace('Z', '+00:00'))
            except:
                game_date = datetime.now()
        
        # Get all games for feature engineering
        all_games = self.ukf_predictor.collector.get_completed_games()

        # Engineer features for ML model
        try:
            features_array, features_dict = self.feature_engineer.engineer_features(
                home_state, away_state,
                home_uncertainty, away_uncertainty,
                game, home_team_id, away_team_id,
                game_date, all_games
            )

            # Transform features if scaler is fitted
            if self.feature_engineer.scaler_fitted:
                features_array = self.feature_engineer.transform_features(features_array)

                # Debug: Check for NaN or Inf values
                if np.any(np.isnan(features_array)) or np.any(np.isinf(features_array)):
                    print(f"   ⚠️  Warning: NaN or Inf values in features, using UKF only")
                    raise ValueError("Invalid feature values")

            # Get ML prediction if model is available
            ml_predicted_margin = None
            ml_predicted_total = None

            if self.ml_model is not None:
                try:
                    expected_dim = None
                    if self.ml_model.model is not None:
                        input_shape = self.ml_model.model.input_shape
                        if isinstance(input_shape, tuple) and len(input_shape) > 1:
                            expected_dim = input_shape[-1]

                    # Validate feature dimension
                    actual_dim = features_array.shape[0]
                    if expected_dim and actual_dim != expected_dim:
                        print(
                            f"   ⚠️  ML prediction skipped: feature count {actual_dim} "
                            f"does not match model input {expected_dim}. "
                            "Retrain the model to update feature alignment."
                        )
                        raise ValueError("ML feature/model shape mismatch")

                    # Make prediction
                    ml_predictions = self.ml_model.predict(features_array.reshape(1, -1), verbose=0)
                    ml_predicted_margin = float(ml_predictions[0, 0])
                    ml_predicted_total = float(ml_predictions[0, 1])

                    # Validate predictions are reasonable before using
                    if abs(ml_predicted_margin) > 100 or ml_predicted_total < 50 or ml_predicted_total > 300:
                        print(
                            f"   ⚠️  ML prediction out of reasonable range "
                            f"(margin={ml_predicted_margin:.1f}, total={ml_predicted_total:.1f}), "
                            "using UKF only"
                        )
                        raise ValueError("ML prediction out of range")

                except Exception as e:
                    if "ML prediction" not in str(e) and "feature count" not in str(e):
                        print(f"   ⚠️  ML prediction failed: {e}")
                    ml_predicted_margin = None
                    ml_predicted_total = None
        except Exception as e:
            print(f"Feature engineering failed: {e}")
            features_dict = {}
            ml_predicted_margin = None
            ml_predicted_total = None
        
        # Combine UKF and ML predictions
        ukf_margin = ukf_prediction.get('predicted_margin', 0.0)
        ukf_total = ukf_prediction.get('predicted_total', 0.0)
        
        # Sanity check UKF predictions - clamp to reasonable ranges
        # Margins should be between -60 and +60 (even blowouts rarely exceed this)
        # Totals should be between 80 and 220 (typical range for college basketball)
        ukf_margin = max(-60.0, min(60.0, ukf_margin))
        ukf_total = max(80.0, min(220.0, ukf_total))
        
        if ml_predicted_margin is not None and ml_predicted_total is not None:
            # Sanity check ML predictions - detect garbage output
            ml_margin_valid = -60.0 <= ml_predicted_margin <= 60.0
            ml_total_valid = 80.0 <= ml_predicted_total <= 220.0
            
            if ml_margin_valid and ml_total_valid:
                # ML predictions are reasonable - use weighted combination
                hybrid_margin = (config.HYBRID_WEIGHT_UKF * ukf_margin + 
                               config.HYBRID_WEIGHT_ML * ml_predicted_margin)
                hybrid_total = (config.HYBRID_WEIGHT_UKF * ukf_total + 
                              config.HYBRID_WEIGHT_ML * ml_predicted_total)
                prediction_source = 'hybrid'
            else:
                # ML predictions are garbage (likely due to unknown teams) - use UKF only
                print(f"   ⚠️  ML prediction out of range (margin={ml_predicted_margin:.1f}, total={ml_predicted_total:.1f}), using UKF only")
                hybrid_margin = ukf_margin
                hybrid_total = ukf_total
                prediction_source = 'ukf'
                ml_predicted_margin = None
                ml_predicted_total = None
        else:
            # Fallback to UKF only
            hybrid_margin = ukf_margin
            hybrid_total = ukf_total
            prediction_source = 'ukf'
        
        # Final sanity clamp on hybrid predictions
        hybrid_margin = max(-60.0, min(60.0, hybrid_margin))
        hybrid_total = max(80.0, min(220.0, hybrid_total))
        
        # Get pregame lines
        pregame_spread = game.get('PointSpread')
        pregame_total = game.get('OverUnder')
        
        # Calculate probabilities using hybrid predictions
        margin_uncertainty = ukf_prediction.get('margin_uncertainty', 10.0)
        total_uncertainty = ukf_prediction.get('total_uncertainty', 12.0)
        
        # Enforce minimum uncertainty to prevent overconfident predictions
        # College basketball games have inherent variance - minimum ~8 points for margin
        MIN_MARGIN_UNCERTAINTY = 8.0
        MIN_TOTAL_UNCERTAINTY = 10.0
        margin_uncertainty = max(MIN_MARGIN_UNCERTAINTY, margin_uncertainty)
        total_uncertainty = max(MIN_TOTAL_UNCERTAINTY, total_uncertainty)
        
        home_covers_probability = None
        over_probability = None
        
        if pregame_spread is not None:
            # Probability that home team covers: P(home_margin > spread)
            home_covers_probability = 1.0 - norm.cdf(pregame_spread, hybrid_margin, margin_uncertainty)
            # Clamp to prevent extreme probabilities (max ~95% confidence)
            home_covers_probability = max(0.025, min(0.975, home_covers_probability))
        
        if pregame_total is not None:
            # Probability that total goes over
            over_probability = 1.0 - norm.cdf(pregame_total, hybrid_total, total_uncertainty)
            # Clamp to prevent extreme probabilities
            over_probability = max(0.025, min(0.975, over_probability))
        
        # Build comprehensive prediction dictionary
        prediction = {
            'predicted_margin': float(hybrid_margin),
            'predicted_total': float(hybrid_total),
            'margin_uncertainty': float(margin_uncertainty),
            'total_uncertainty': float(total_uncertainty),
            'predicted_winner': 'home' if hybrid_margin > 0 else 'away',
            'home_team_id': home_team_id,
            'away_team_id': away_team_id,
            
            # UKF predictions
            'ukf_predicted_margin': float(ukf_margin),
            'ukf_predicted_total': float(ukf_total),
            
            # ML predictions
            'ml_predicted_margin': ml_predicted_margin,
            'ml_predicted_total': ml_predicted_total,
            
            # Hybrid combination
            'hybrid_predicted_margin': float(hybrid_margin),
            'hybrid_predicted_total': float(hybrid_total),
            'prediction_source': prediction_source,
            
            # Probabilities
            'spread': float(pregame_spread) if pregame_spread is not None else None,
            'total_line': float(pregame_total) if pregame_total is not None else None,
            'home_covers_probability': float(home_covers_probability) if home_covers_probability is not None else None,
            'away_covers_probability': float(1.0 - home_covers_probability) if home_covers_probability is not None else None,
            'over_probability': float(over_probability) if over_probability is not None else None,
            'under_probability': float(1.0 - over_probability) if over_probability is not None else None,
            
            # Confidence scores
            'home_covers_confidence': float(abs((home_covers_probability or 0.5) - 0.5) * 200) if home_covers_probability is not None else None,
            'over_confidence': float(abs((over_probability or 0.5) - 0.5) * 200) if over_probability is not None else None,
        }
        
        # Calculate overall confidence
        confidences = []
        if prediction['home_covers_confidence'] is not None:
            confidences.append(prediction['home_covers_confidence'])
        if prediction['over_confidence'] is not None:
            confidences.append(prediction['over_confidence'])
        prediction['overall_confidence'] = float(np.mean(confidences)) if confidences else 50.0
        prediction['prediction_confidence'] = prediction['overall_confidence']
        
        # Store features for later analysis
        prediction['ukf_features_json'] = {
            'home_state': [float(x) for x in home_state],
            'away_state': [float(x) for x in away_state],
            'home_uncertainty': [float(x) for x in home_uncertainty],
            'away_uncertainty': [float(x) for x in away_uncertainty]
        }
        prediction['ml_features_json'] = features_dict
        
        return prediction
    
    def save_prediction_to_database(self, game_id: int, game_date: datetime,
                                   home_team_id: int, away_team_id: int,
                                   prediction: Dict):
        """Save prediction to database."""
        import json

        # Convert feature dicts to JSON strings for database storage
        ukf_features = prediction.get('ukf_features_json')
        ml_features = prediction.get('ml_features_json')

        prediction_data = {
            'pregame_spread': prediction.get('spread'),
            'pregame_total': prediction.get('total_line'),
            'ukf_predicted_margin': prediction.get('ukf_predicted_margin'),
            'ukf_predicted_total': prediction.get('ukf_predicted_total'),
            'ml_predicted_margin': prediction.get('ml_predicted_margin'),
            'ml_predicted_total': prediction.get('ml_predicted_total'),
            'hybrid_predicted_margin': prediction.get('hybrid_predicted_margin'),
            'hybrid_predicted_total': prediction.get('hybrid_predicted_total'),
            'home_covers_probability': prediction.get('home_covers_probability'),
            'over_probability': prediction.get('over_probability'),
            'prediction_confidence': prediction.get('prediction_confidence'),
            'ukf_features_json': json.dumps(ukf_features) if ukf_features else None,
            'ml_features_json': json.dumps(ml_features) if ml_features else None,
            'prediction_source': prediction.get('prediction_source', 'hybrid')
        }

        self.database.save_prediction(
            game_id, game_date, home_team_id, away_team_id, prediction_data
        )
    
    def update_game_result(self, game_id: int, home_score: int, away_score: int):
        """Update game result in database and calculate accuracy."""
        # Get prediction to get pregame lines
        pred = self.database.get_prediction_by_game_id(game_id)
        pregame_spread = pred.get('pregame_spread') if pred else None
        pregame_total = pred.get('pregame_total') if pred else None
        
        # Save result
        self.database.save_result(game_id, home_score, away_score, 
                                 pregame_spread, pregame_total)
        
        # Update daily accuracy
        from datetime import date
        game_date = pred.get('game_date') if pred else datetime.now()
        if isinstance(game_date, datetime):
            self.database.update_daily_accuracy(game_date.date())
        elif isinstance(game_date, date):
            self.database.update_daily_accuracy(game_date)
    
    def get_prediction_accuracy(self, start_date: Optional[date] = None,
                               end_date: Optional[date] = None) -> Dict:
        """Get accuracy statistics."""
        return self.database.calculate_accuracy(start_date, end_date)

