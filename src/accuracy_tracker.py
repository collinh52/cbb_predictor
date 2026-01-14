"""
Accuracy tracking module for monitoring prediction performance over time.
"""
from datetime import datetime, date, timedelta
from typing import List, Dict, Optional, Tuple
from sqlalchemy import func, extract
from sqlalchemy.orm import Session

from src.database import get_database, Prediction, GameResult, ModelAccuracy


class AccuracyTracker:
    """Tracks prediction accuracy over time."""
    
    def __init__(self):
        self.db = get_database()
    
    def calculate_daily_accuracy(self, target_date: date) -> Dict:
        """Calculate accuracy metrics for a specific date."""
        session = self.db.get_session()
        try:
            query = session.query(Prediction, GameResult).join(
                GameResult, Prediction.game_id == GameResult.game_id
            ).filter(
                func.date(Prediction.game_date) == target_date
            )
            
            predictions_with_results = query.all()
            
            if not predictions_with_results:
                return {
                    'date': target_date.isoformat(),
                    'total_predictions': 0,
                    'spread_accuracy': 0.0,
                    'total_accuracy': 0.0,
                    'rmse_spread': 0.0,
                    'rmse_total': 0.0,
                    'brier_score_spread': 0.0,
                    'brier_score_total': 0.0
                }
            
            return self._calculate_metrics(predictions_with_results, target_date)
        finally:
            session.close()
    
    def calculate_weekly_accuracy(self, start_date: date, end_date: date) -> Dict:
        """Calculate accuracy metrics for a date range."""
        session = self.db.get_session()
        try:
            query = session.query(Prediction, GameResult).join(
                GameResult, Prediction.game_id == GameResult.game_id
            ).filter(
                func.date(Prediction.game_date) >= start_date,
                func.date(Prediction.game_date) <= end_date
            )
            
            predictions_with_results = query.all()
            
            if not predictions_with_results:
                return {
                    'start_date': start_date.isoformat(),
                    'end_date': end_date.isoformat(),
                    'total_predictions': 0,
                    'spread_accuracy': 0.0,
                    'total_accuracy': 0.0,
                    'rmse_spread': 0.0,
                    'rmse_total': 0.0,
                    'brier_score_spread': 0.0,
                    'brier_score_total': 0.0
                }
            
            return self._calculate_metrics(predictions_with_results, start_date, end_date)
        finally:
            session.close()
    
    def get_accuracy_by_week(self, season_start: Optional[date] = None) -> List[Dict]:
        """Get accuracy metrics grouped by week."""
        session = self.db.get_session()
        try:
            if season_start is None:
                # Get earliest game date
                earliest = session.query(func.min(Prediction.game_date)).scalar()
                if earliest:
                    season_start = earliest.date()
                else:
                    return []
            
            # Get all predictions with results
            query = session.query(
                Prediction,
                GameResult,
                func.date(Prediction.game_date).label('game_date_only')
            ).join(
                GameResult, Prediction.game_id == GameResult.game_id
            ).filter(
                func.date(Prediction.game_date) >= season_start
            ).order_by('game_date_only')
            
            results = query.all()
            
            # Group by week
            weekly_data = {}
            for pred, result, game_date_only in results:
                # Ensure game_date_only is a date object
                if isinstance(game_date_only, str):
                    game_date_only = datetime.fromisoformat(game_date_only).date()
                elif isinstance(game_date_only, datetime):
                    game_date_only = game_date_only.date()
                
                # Calculate week number from season start
                days_diff = (game_date_only - season_start).days
                week_num = days_diff // 7
                week_start = season_start + timedelta(days=week_num * 7)
                
                if week_start not in weekly_data:
                    weekly_data[week_start] = []
                
                weekly_data[week_start].append((pred, result))
            
            # Calculate metrics for each week
            weekly_accuracy = []
            for week_start, preds_results in sorted(weekly_data.items()):
                week_end = week_start + timedelta(days=6)
                metrics = self._calculate_metrics(preds_results, week_start, week_end)
                metrics['week_start'] = week_start.isoformat()
                metrics['week_end'] = week_end.isoformat()
                weekly_accuracy.append(metrics)
            
            return weekly_accuracy
        finally:
            session.close()
    
    def get_accuracy_by_month(self, season_start: Optional[date] = None) -> List[Dict]:
        """Get accuracy metrics grouped by month."""
        session = self.db.get_session()
        try:
            if season_start is None:
                earliest = session.query(func.min(Prediction.game_date)).scalar()
                if earliest:
                    season_start = earliest.date()
                else:
                    return []
            
            # Group by year-month
            query = session.query(
                Prediction,
                GameResult,
                extract('year', Prediction.game_date).label('year'),
                extract('month', Prediction.game_date).label('month')
            ).join(
                GameResult, Prediction.game_id == GameResult.game_id
            ).filter(
                func.date(Prediction.game_date) >= season_start
            ).order_by('year', 'month')
            
            results = query.all()
            
            # Group by month
            monthly_data = {}
            for pred, result, year, month in results:
                month_key = f"{int(year)}-{int(month):02d}"
                if month_key not in monthly_data:
                    monthly_data[month_key] = []
                monthly_data[month_key].append((pred, result))
            
            # Calculate metrics for each month
            monthly_accuracy = []
            for month_key, preds_results in sorted(monthly_data.items()):
                metrics = self._calculate_metrics(preds_results)
                metrics['month'] = month_key
                monthly_accuracy.append(metrics)
            
            return monthly_accuracy
        finally:
            session.close()
    
    def get_rolling_accuracy(self, window_days: int = 30, end_date: Optional[date] = None) -> List[Dict]:
        """Get rolling accuracy over a sliding window."""
        session = self.db.get_session()
        try:
            if end_date is None:
                end_date = date.today()
            
            start_date = end_date - timedelta(days=window_days)
            
            # Get all dates in range
            query = session.query(
                func.date(Prediction.game_date).label('game_date_only')
            ).join(
                GameResult, Prediction.game_id == GameResult.game_id
            ).filter(
                func.date(Prediction.game_date) >= start_date,
                func.date(Prediction.game_date) <= end_date
            ).distinct().order_by('game_date_only')
            
            dates = [row[0] for row in query.all()]
            
            rolling_accuracy = []
            for i in range(len(dates)):
                window_start = dates[max(0, i - window_days + 1)]
                window_end = dates[i]
                
                window_query = session.query(Prediction, GameResult).join(
                    GameResult, Prediction.game_id == GameResult.game_id
                ).filter(
                    func.date(Prediction.game_date) >= window_start,
                    func.date(Prediction.game_date) <= window_end
                )
                
                preds_results = window_query.all()
                if preds_results:
                    metrics = self._calculate_metrics(preds_results)
                    metrics['date'] = window_end.isoformat()
                    metrics['window_start'] = window_start.isoformat()
                    rolling_accuracy.append(metrics)
            
            return rolling_accuracy
        finally:
            session.close()
    
    def _calculate_metrics(self, predictions_with_results: List[Tuple], 
                          start_date: Optional[date] = None,
                          end_date: Optional[date] = None) -> Dict:
        """Calculate accuracy metrics from predictions and results."""
        if not predictions_with_results:
            return {
                'total_predictions': 0,
                'spread_accuracy': 0.0,
                'total_accuracy': 0.0,
                'rmse_spread': 0.0,
                'rmse_total': 0.0,
                'brier_score_spread': 0.0,
                'brier_score_total': 0.0
            }
        
        correct_spread = 0
        correct_total = 0
        squared_errors_spread = []
        squared_errors_total = []
        brier_scores_spread = []
        brier_scores_total = []
        
        for pred, result in predictions_with_results:
            # Spread accuracy
            if pred.pregame_spread is not None and result.actual_margin is not None:
                predicted_cover = pred.hybrid_predicted_margin > pred.pregame_spread
                actual_cover = result.actual_margin > pred.pregame_spread
                if predicted_cover == actual_cover:
                    correct_spread += 1
                
                # Brier Score for spread
                if pred.home_covers_probability is not None:
                    brier_scores_spread.append(
                        (pred.home_covers_probability - (1.0 if actual_cover else 0.0))**2
                    )
            
            # Total accuracy
            if pred.pregame_total is not None and result.actual_total is not None:
                predicted_over = pred.hybrid_predicted_total > pred.pregame_total
                actual_over = result.actual_total > pred.pregame_total
                if predicted_over == actual_over:
                    correct_total += 1
                
                # Brier Score for total
                if pred.over_probability is not None:
                    brier_scores_total.append(
                        (pred.over_probability - (1.0 if actual_over else 0.0))**2
                    )
            
            # RMSE
            if pred.hybrid_predicted_margin is not None and result.actual_margin is not None:
                squared_errors_spread.append(
                    (pred.hybrid_predicted_margin - result.actual_margin)**2
                )
            if pred.hybrid_predicted_total is not None and result.actual_total is not None:
                squared_errors_total.append(
                    (pred.hybrid_predicted_total - result.actual_total)**2
                )
        
        total_count = len(predictions_with_results)
        spread_accuracy = correct_spread / total_count if total_count > 0 else 0.0
        total_accuracy = correct_total / total_count if total_count > 0 else 0.0
        rmse_spread = (sum(squared_errors_spread) / len(squared_errors_spread))**0.5 if squared_errors_spread else 0.0
        rmse_total = (sum(squared_errors_total) / len(squared_errors_total))**0.5 if squared_errors_total else 0.0
        brier_score_spread = sum(brier_scores_spread) / len(brier_scores_spread) if brier_scores_spread else 0.0
        brier_score_total = sum(brier_scores_total) / len(brier_scores_total) if brier_scores_total else 0.0
        
        result = {
            'total_predictions': total_count,
            'spread_accuracy': spread_accuracy,
            'total_accuracy': total_accuracy,
            'rmse_spread': rmse_spread,
            'rmse_total': rmse_total,
            'brier_score_spread': brier_score_spread,
            'brier_score_total': brier_score_total
        }
        
        if start_date:
            if isinstance(start_date, date):
                result['start_date'] = start_date.isoformat()
            else:
                result['start_date'] = str(start_date)
        if end_date:
            if isinstance(end_date, date):
                result['end_date'] = end_date.isoformat()
            else:
                result['end_date'] = str(end_date)
        
        return result
    
    def update_daily_accuracy(self, target_date: date):
        """Update or create daily accuracy record."""
        # Ensure target_date is a date object
        if isinstance(target_date, str):
            from datetime import datetime
            target_date = datetime.fromisoformat(target_date).date()
        
        session = self.db.get_session()
        try:
            accuracy = self.calculate_daily_accuracy(target_date)
            
            existing = session.query(ModelAccuracy).filter_by(date=target_date).first()
            if existing:
                existing.total_predictions = accuracy['total_predictions']
                existing.spread_accuracy = accuracy['spread_accuracy']
                existing.total_accuracy = accuracy['total_accuracy']
                existing.rmse_spread = accuracy['rmse_spread']
                existing.rmse_total = accuracy['rmse_total']
                existing.brier_score_spread = accuracy['brier_score_spread']
                existing.brier_score_total = accuracy['brier_score_total']
            else:
                accuracy_record = ModelAccuracy(
                    date=target_date,  # Already a date object
                    total_predictions=accuracy['total_predictions'],
                    spread_accuracy=accuracy['spread_accuracy'],
                    total_accuracy=accuracy['total_accuracy'],
                    rmse_spread=accuracy['rmse_spread'],
                    rmse_total=accuracy['rmse_total'],
                    brier_score_spread=accuracy['brier_score_spread'],
                    brier_score_total=accuracy['brier_score_total']
                )
                session.add(accuracy_record)
            
            session.commit()
        finally:
            session.close()
    
    def update_all_daily_accuracy(self):
        """Update accuracy records for all dates with predictions."""
        session = self.db.get_session()
        try:
            # Get all unique dates
            dates = session.query(
                func.date(Prediction.game_date).label('game_date_only')
            ).join(
                GameResult, Prediction.game_id == GameResult.game_id
            ).distinct().order_by('game_date_only')
            
            date_list = [row[0] for row in dates.all()]
            
            print(f"Updating accuracy for {len(date_list)} dates...")
            for i, target_date in enumerate(date_list):
                if (i + 1) % 10 == 0:
                    print(f"  Processing date {i+1}/{len(date_list)}...")
                self.update_daily_accuracy(target_date)
            
            print(f"✓ Updated accuracy records for {len(date_list)} dates")
        finally:
            session.close()

