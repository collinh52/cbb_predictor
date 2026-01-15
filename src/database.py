"""
Database module for storing predictions, results, and model metrics.
Uses SQLAlchemy ORM with PostgreSQL.
"""
import os
from datetime import datetime, date
from typing import List, Dict, Optional, Tuple
from sqlalchemy import create_engine, Column, Integer, Float, Boolean, String, Text, Date, DateTime, ForeignKey, Enum as SQLEnum, JSON as SQLJSON
from sqlalchemy.dialects.sqlite import JSON as SQLiteJSON
import json
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, relationship
from sqlalchemy.sql import func
import json
import enum

import config

Base = declarative_base()


class PredictionSource(enum.Enum):
    UKF = "ukf"
    ML = "ml"
    HYBRID = "hybrid"


class ModelType(enum.Enum):
    NEURAL_NETWORK = "neural_network"


class Prediction(Base):
    """Table for storing game predictions."""
    __tablename__ = "predictions"
    
    prediction_id = Column(Integer, primary_key=True, autoincrement=True)
    game_id = Column(Integer, nullable=False, index=True)
    game_date = Column(DateTime, nullable=False, index=True)
    home_team_id = Column(Integer, nullable=False)
    away_team_id = Column(Integer, nullable=False)
    pregame_spread = Column(Float, nullable=True)
    pregame_total = Column(Float, nullable=True)
    ukf_predicted_margin = Column(Float, nullable=True)
    ukf_predicted_total = Column(Float, nullable=True)
    ml_predicted_margin = Column(Float, nullable=True)
    ml_predicted_total = Column(Float, nullable=True)
    hybrid_predicted_margin = Column(Float, nullable=True)
    hybrid_predicted_total = Column(Float, nullable=True)
    home_covers_probability = Column(Float, nullable=True)
    over_probability = Column(Float, nullable=True)
    prediction_confidence = Column(Float, nullable=True)
    ukf_features_json = Column(Text, nullable=True)  # Store as JSON string for SQLite compatibility
    ml_features_json = Column(Text, nullable=True)  # Store as JSON string for SQLite compatibility
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    prediction_source = Column(String(20), nullable=False, default="hybrid")
    
    # Relationship to game results
    result = relationship("GameResult", back_populates="prediction", uselist=False)


class GameResult(Base):
    """Table for storing game results."""
    __tablename__ = "game_results"
    
    result_id = Column(Integer, primary_key=True, autoincrement=True)
    game_id = Column(Integer, ForeignKey("predictions.game_id"), nullable=False, unique=True, index=True)
    home_score = Column(Integer, nullable=False)
    away_score = Column(Integer, nullable=False)
    actual_margin = Column(Integer, nullable=False)  # home - away
    actual_total = Column(Integer, nullable=False)
    home_covered = Column(Boolean, nullable=True)  # True if home team covered spread
    over_hit = Column(Boolean, nullable=True)  # True if total went over
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationship to prediction
    prediction = relationship("Prediction", back_populates="result")


class ModelAccuracy(Base):
    """Table for storing daily accuracy metrics."""
    __tablename__ = "model_accuracy"
    
    accuracy_id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date, nullable=False, unique=True, index=True)
    total_predictions = Column(Integer, nullable=False, default=0)
    spread_accuracy = Column(Float, nullable=True)  # Percentage correct
    total_accuracy = Column(Float, nullable=True)  # Percentage correct
    rmse_spread = Column(Float, nullable=True)  # Root Mean Squared Error
    rmse_total = Column(Float, nullable=True)
    brier_score_spread = Column(Float, nullable=True)
    brier_score_total = Column(Float, nullable=True)


class ModelVersion(Base):
    """Table for storing model versions and metadata."""
    __tablename__ = "model_versions"
    
    version_id = Column(Integer, primary_key=True, autoincrement=True)
    model_type = Column(String(50), nullable=False, default="neural_network")
    version_number = Column(Integer, nullable=False, index=True)
    trained_on_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    training_games_count = Column(Integer, nullable=False, default=0)
    validation_accuracy = Column(Float, nullable=True)
    model_path = Column(Text, nullable=False)
    hyperparameters_json = Column(Text, nullable=True)  # Store as JSON string for SQLite compatibility
    is_active = Column(Boolean, nullable=False, default=False, index=True)


class Database:
    """Database interface for predictions and results."""
    
    def __init__(self, database_url: Optional[str] = None):
        """Initialize database connection."""
        self.database_url = database_url or config.DATABASE_URL
        if not self.database_url:
            raise ValueError("DATABASE_URL must be set in config or environment")
        
        self.engine = create_engine(self.database_url, pool_pre_ping=True)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
    
    def init_database(self):
        """Create all tables if they don't exist."""
        Base.metadata.create_all(bind=self.engine)
    
    def get_session(self) -> Session:
        """Get a database session."""
        return self.SessionLocal()
    
    def save_prediction(self, game_id: int, game_date: datetime, home_team_id: int, 
                       away_team_id: int, prediction_data: Dict, session: Optional[Session] = None) -> int:
        """Save a prediction to the database."""
        close_session = session is None
        if session is None:
            session = self.get_session()
        
        try:
            # Check if prediction already exists
            existing = session.query(Prediction).filter_by(game_id=game_id).first()
            if existing:
                # Update existing prediction
                for key, value in prediction_data.items():
                    if hasattr(existing, key):
                        setattr(existing, key, value)
                prediction_id = existing.prediction_id
            else:
                # Create new prediction
                prediction = Prediction(
                    game_id=game_id,
                    game_date=game_date,
                    home_team_id=home_team_id,
                    away_team_id=away_team_id,
                    **prediction_data
                )
                session.add(prediction)
                session.commit()
                session.refresh(prediction)
                prediction_id = prediction.prediction_id
            
            return prediction_id
        except Exception as e:
            session.rollback()
            raise e
        finally:
            if close_session:
                session.close()
    
    def save_result(self, game_id: int, home_score: int, away_score: int, 
                   pregame_spread: Optional[float] = None, pregame_total: Optional[float] = None,
                   session: Optional[Session] = None) -> int:
        """Save a game result and link it to the prediction."""
        close_session = session is None
        if session is None:
            session = self.get_session()
        
        try:
            actual_margin = home_score - away_score
            actual_total = home_score + away_score
            
            # Calculate whether home covered and over hit
            home_covered = None
            over_hit = None
            
            if pregame_spread is not None:
                home_covered = actual_margin > pregame_spread
            
            if pregame_total is not None:
                over_hit = actual_total > pregame_total
            
            # Check if result already exists
            existing = session.query(GameResult).filter_by(game_id=game_id).first()
            if existing:
                existing.home_score = home_score
                existing.away_score = away_score
                existing.actual_margin = actual_margin
                existing.actual_total = actual_total
                existing.home_covered = home_covered
                existing.over_hit = over_hit
                existing.updated_at = datetime.utcnow()
                result_id = existing.result_id
            else:
                result = GameResult(
                    game_id=game_id,
                    home_score=home_score,
                    away_score=away_score,
                    actual_margin=actual_margin,
                    actual_total=actual_total,
                    home_covered=home_covered,
                    over_hit=over_hit
                )
                session.add(result)
                session.commit()
                session.refresh(result)
                result_id = result.result_id
            
            return result_id
        except Exception as e:
            session.rollback()
            raise e
        finally:
            if close_session:
                session.close()
    
    def get_training_data(self, season: Optional[int] = None, limit: Optional[int] = None) -> List[Dict]:
        """Retrieve predictions with results for training."""
        session = self.get_session()
        try:
            query = session.query(Prediction, GameResult).join(
                GameResult, Prediction.game_id == GameResult.game_id
            )
            
            if season:
                year_start = datetime(season, 11, 1)  # College basketball season starts Nov
                year_end = datetime(season + 1, 4, 15)  # Ends in April
                query = query.filter(
                    Prediction.game_date >= year_start,
                    Prediction.game_date <= year_end
                )
            
            if limit:
                query = query.limit(limit)
            
            results = query.all()
            
            training_data = []
            for pred, result in results:
                # Parse JSON strings if stored as Text
                ukf_features = {}
                ml_features = {}
                if pred.ukf_features_json:
                    if isinstance(pred.ukf_features_json, str):
                        try:
                            ukf_features = json.loads(pred.ukf_features_json)
                        except:
                            ukf_features = {}
                    else:
                        ukf_features = pred.ukf_features_json
                
                if pred.ml_features_json:
                    if isinstance(pred.ml_features_json, str):
                        try:
                            ml_features = json.loads(pred.ml_features_json)
                        except:
                            ml_features = {}
                    else:
                        ml_features = pred.ml_features_json
                
                training_data.append({
                    'prediction_id': pred.prediction_id,
                    'game_id': pred.game_id,
                    'game_date': pred.game_date,
                    'home_team_id': pred.home_team_id,
                    'away_team_id': pred.away_team_id,
                    'pregame_spread': pred.pregame_spread,
                    'pregame_total': pred.pregame_total,
                    'ukf_features': ukf_features,
                    'ml_features': ml_features,
                    'ukf_predicted_margin': pred.ukf_predicted_margin,
                    'ukf_predicted_total': pred.ukf_predicted_total,
                    'ml_predicted_margin': pred.ml_predicted_margin,
                    'ml_predicted_total': pred.ml_predicted_total,
                    'hybrid_predicted_margin': pred.hybrid_predicted_margin,
                    'hybrid_predicted_total': pred.hybrid_predicted_total,
                    'actual_margin': result.actual_margin,
                    'actual_total': result.actual_total,
                    'home_covered': result.home_covered,
                    'over_hit': result.over_hit
                })
            
            return training_data
        finally:
            session.close()
    
    def calculate_accuracy(self, start_date: Optional[date] = None, 
                          end_date: Optional[date] = None) -> Dict:
        """Calculate accuracy metrics for predictions with results."""
        session = self.get_session()
        try:
            query = session.query(Prediction, GameResult).join(
                GameResult, Prediction.game_id == GameResult.game_id
            )
            
            if start_date:
                query = query.filter(Prediction.game_date >= start_date)
            if end_date:
                query = query.filter(Prediction.game_date <= end_date)
            
            results = query.all()
            
            if not results:
                return {
                    'total_predictions': 0,
                    'spread_accuracy': None,
                    'total_accuracy': None,
                    'rmse_spread': None,
                    'rmse_total': None,
                    'brier_score_spread': None,
                    'brier_score_total': None
                }
            
            # Calculate metrics
            spread_errors = []
            total_errors = []
            spread_correct = 0
            total_correct = 0
            spread_brier_scores = []
            total_brier_scores = []
            
            for pred, result in results:
                if pred.pregame_spread is not None:
                    predicted_cover = pred.hybrid_predicted_margin > pred.pregame_spread if pred.hybrid_predicted_margin is not None else None
                    if predicted_cover is not None and result.home_covered is not None:
                        if predicted_cover == result.home_covered:
                            spread_correct += 1
                        # Brier score: (probability - outcome)^2
                        prob = pred.home_covers_probability or 0.5
                        outcome = 1.0 if result.home_covered else 0.0
                        spread_brier_scores.append((prob - outcome) ** 2)
                    
                    if pred.hybrid_predicted_margin is not None:
                        error = pred.hybrid_predicted_margin - result.actual_margin
                        spread_errors.append(error ** 2)
                
                if pred.pregame_total is not None:
                    predicted_over = pred.hybrid_predicted_total > pred.pregame_total if pred.hybrid_predicted_total is not None else None
                    if predicted_over is not None and result.over_hit is not None:
                        if predicted_over == result.over_hit:
                            total_correct += 1
                        # Brier score
                        prob = pred.over_probability or 0.5
                        outcome = 1.0 if result.over_hit else 0.0
                        total_brier_scores.append((prob - outcome) ** 2)
                    
                    if pred.hybrid_predicted_total is not None:
                        error = pred.hybrid_predicted_total - result.actual_total
                        total_errors.append(error ** 2)
            
            total_predictions = len(results)
            spread_count = sum(1 for _, r in results if r.home_covered is not None)
            total_count = sum(1 for _, r in results if r.over_hit is not None)
            
            accuracy = {
                'total_predictions': total_predictions,
                'spread_accuracy': (spread_correct / spread_count) if spread_count > 0 else None,  # As decimal, not percentage
                'total_accuracy': (total_correct / total_count) if total_count > 0 else None,  # As decimal, not percentage
                'rmse_spread': (sum(spread_errors) / len(spread_errors)) ** 0.5 if spread_errors else None,
                'rmse_total': (sum(total_errors) / len(total_errors)) ** 0.5 if total_errors else None,
                'brier_score_spread': sum(spread_brier_scores) / len(spread_brier_scores) if spread_brier_scores else None,
                'brier_score_total': sum(total_brier_scores) / len(total_brier_scores) if total_brier_scores else None
            }
            
            return accuracy
        finally:
            session.close()
    
    def update_daily_accuracy(self, target_date: date, session: Optional[Session] = None):
        """Update or create daily accuracy record."""
        close_session = session is None
        if session is None:
            session = self.get_session()
        
        try:
            accuracy = self.calculate_accuracy(start_date=target_date, end_date=target_date)
            
            existing = session.query(ModelAccuracy).filter_by(date=target_date).first()
            if existing:
                for key, value in accuracy.items():
                    if hasattr(existing, key):
                        setattr(existing, key, value)
            else:
                accuracy_record = ModelAccuracy(date=target_date, **accuracy)
                session.add(accuracy_record)
            
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            if close_session:
                session.close()
    
    def get_active_model_version(self) -> Optional[Dict]:
        """Get the currently active model version."""
        session = self.get_session()
        try:
            model = session.query(ModelVersion).filter_by(is_active=True).first()
            if model:
                hyperparameters = {}
                if model.hyperparameters_json:
                    try:
                        hyperparameters = json.loads(model.hyperparameters_json)
                    except json.JSONDecodeError:
                        hyperparameters = {}
                return {
                    'version_id': model.version_id,
                    'model_type': model.model_type,
                    'version_number': model.version_number,
                    'trained_on_date': model.trained_on_date,
                    'training_games_count': model.training_games_count,
                    'validation_accuracy': model.validation_accuracy,
                    'model_path': model.model_path,
                    'hyperparameters': hyperparameters,
                    'scaler_path': hyperparameters.get('scaler_path')
                }
            return None
        finally:
            session.close()
    
    def save_model_version(self, version_number: int, model_path: str, 
                          training_games_count: int, validation_accuracy: Optional[float],
                          hyperparameters: Dict, is_active: bool = False,
                          session: Optional[Session] = None) -> int:
        """Save a new model version."""
        close_session = session is None
        if session is None:
            session = self.get_session()
        
        try:
            # Deactivate other models if this one is active
            if is_active:
                session.query(ModelVersion).update({ModelVersion.is_active: False})
            
            # Convert hyperparameters dict to JSON string for SQLite
            hyperparams_json_str = json.dumps(hyperparameters) if hyperparameters else None
            
            model_version = ModelVersion(
                model_type="neural_network",
                version_number=version_number,
                model_path=model_path,
                training_games_count=training_games_count,
                validation_accuracy=validation_accuracy,
                hyperparameters_json=hyperparams_json_str,
                is_active=is_active
            )
            session.add(model_version)
            session.commit()
            session.refresh(model_version)
            return model_version.version_id
        except Exception as e:
            session.rollback()
            raise e
        finally:
            if close_session:
                session.close()
    
    def get_prediction_by_game_id(self, game_id: int) -> Optional[Dict]:
        """Get prediction for a specific game."""
        session = self.get_session()
        try:
            pred = session.query(Prediction).filter_by(game_id=game_id).first()
            if pred:
                return {
                    'prediction_id': pred.prediction_id,
                    'game_id': pred.game_id,
                    'game_date': pred.game_date,
                    'pregame_spread': pred.pregame_spread,
                    'pregame_total': pred.pregame_total,
                    'hybrid_predicted_margin': pred.hybrid_predicted_margin,
                    'hybrid_predicted_total': pred.hybrid_predicted_total,
                    'home_covers_probability': pred.home_covers_probability,
                    'over_probability': pred.over_probability,
                    'prediction_source': pred.prediction_source
                }
            return None
        finally:
            session.close()


# Global database instance
_db: Optional[Database] = None


def get_database() -> Database:
    """Get or create global database instance."""
    global _db
    if _db is None:
        _db = Database()
        _db.init_database()  # Ensure tables exist
    return _db

