"""
ATS (Against The Spread) Accuracy Tracking System.

Tracks prediction accuracy separately for:
- Games WITH Vegas spread data (true ATS tracking)
- Games WITHOUT spread data (implied spread from ratings)
"""
import json
import os
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, asdict
import numpy as np


@dataclass
class ATSRecord:
    """Record for a single ATS prediction."""
    game_id: str
    game_date: str
    home_team: str
    away_team: str
    home_team_id: int
    away_team_id: int
    
    # Prediction data
    predicted_margin: float  # Positive = home team favored
    predicted_total: float
    prediction_confidence: float
    
    # Spread data (None if not available)
    vegas_spread: Optional[float] = None  # Home team perspective (negative = home favored)
    vegas_total: Optional[float] = None
    has_vegas_line: bool = False
    
    # Prediction picks
    spread_pick: str = ""  # "HOME" or "AWAY"
    total_pick: str = ""   # "OVER" or "UNDER"
    
    # Results (filled in after game completes)
    home_score: Optional[int] = None
    away_score: Optional[int] = None
    actual_margin: Optional[int] = None
    actual_total: Optional[int] = None
    
    # Accuracy results
    spread_correct: Optional[bool] = None
    total_correct: Optional[bool] = None
    result_checked: bool = False
    checked_at: Optional[str] = None
    
    # Timestamps
    prediction_timestamp: str = ""
    odds_collected_at: Optional[str] = None


class ATSTracker:
    """
    Comprehensive ATS tracking system that maintains separate accuracy
    metrics for games with and without Vegas lines.
    """
    
    def __init__(self, data_dir: str = "data"):
        self.data_dir = data_dir
        self.ats_file = os.path.join(data_dir, "ats_tracking.json")
        self.accuracy_file = os.path.join(data_dir, "ats_accuracy.json")
        
        os.makedirs(data_dir, exist_ok=True)
        
        self.records: Dict[str, ATSRecord] = self._load_records()
        self.accuracy_history = self._load_accuracy_history()
    
    def _load_records(self) -> Dict[str, ATSRecord]:
        """Load ATS records from file."""
        if os.path.exists(self.ats_file):
            try:
                with open(self.ats_file, 'r') as f:
                    data = json.load(f)
                    return {k: ATSRecord(**v) for k, v in data.items()}
            except (json.JSONDecodeError, TypeError) as e:
                print(f"Warning: Could not load ATS records: {e}")
                return {}
        return {}
    
    def _load_accuracy_history(self) -> Dict:
        """Load accuracy history from file."""
        if os.path.exists(self.accuracy_file):
            try:
                with open(self.accuracy_file, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return self._empty_accuracy_history()
        return self._empty_accuracy_history()
    
    def _empty_accuracy_history(self) -> Dict:
        """Return empty accuracy history structure."""
        return {
            "with_vegas_lines": {
                "total_predictions": 0,
                "spread_correct": 0,
                "spread_accuracy": 0.0,
                "total_correct": 0,
                "total_accuracy": 0.0,
                "last_updated": None,
                "daily_breakdown": {}
            },
            "without_vegas_lines": {
                "total_predictions": 0,
                "implied_spread_correct": 0,
                "implied_spread_accuracy": 0.0,
                "total_correct": 0,
                "total_accuracy": 0.0,
                "last_updated": None,
                "daily_breakdown": {}
            },
            "combined": {
                "total_predictions": 0,
                "straight_up_correct": 0,
                "straight_up_accuracy": 0.0,
                "last_updated": None
            },
            "rolling_7_day": {
                "with_vegas": {"predictions": 0, "spread_correct": 0, "accuracy": 0.0},
                "without_vegas": {"predictions": 0, "correct": 0, "accuracy": 0.0}
            },
            "rolling_30_day": {
                "with_vegas": {"predictions": 0, "spread_correct": 0, "accuracy": 0.0},
                "without_vegas": {"predictions": 0, "correct": 0, "accuracy": 0.0}
            }
        }
    
    def _save_records(self):
        """Save ATS records to file."""
        with open(self.ats_file, 'w') as f:
            json.dump({k: asdict(v) for k, v in self.records.items()}, f, indent=2, default=str)
    
    def _save_accuracy_history(self):
        """Save accuracy history to file."""
        with open(self.accuracy_file, 'w') as f:
            json.dump(self.accuracy_history, f, indent=2, default=str)
    
    def store_prediction(
        self,
        game_id: str,
        game_date: str,
        home_team: str,
        away_team: str,
        home_team_id: int,
        away_team_id: int,
        predicted_margin: float,
        predicted_total: float,
        prediction_confidence: float,
        vegas_spread: Optional[float] = None,
        vegas_total: Optional[float] = None
    ) -> ATSRecord:
        """
        Store a new prediction with optional Vegas line data.
        
        Args:
            game_id: Unique game identifier
            game_date: Date of the game (YYYY-MM-DD)
            home_team: Home team name
            away_team: Away team name
            home_team_id: Home team ID
            away_team_id: Away team ID
            predicted_margin: Predicted margin (positive = home team wins by X)
            predicted_total: Predicted total points
            prediction_confidence: Confidence level (0-100)
            vegas_spread: Vegas spread if available (home team perspective)
            vegas_total: Vegas total if available
        
        Returns:
            ATSRecord for the stored prediction
        """
        has_vegas = vegas_spread is not None
        
        # Determine picks
        if has_vegas:
            # With Vegas line: pick based on predicted margin vs spread
            # If spread is -5 (home favored by 5) and predicted margin is 8,
            # then home should cover, so pick HOME
            spread_pick = "HOME" if predicted_margin > vegas_spread else "AWAY"
            # Only pick totals if we have a total line
            if vegas_total is not None:
                total_pick = "OVER" if predicted_total > vegas_total else "UNDER"
            else:
                total_pick = ""
        else:
            # Without Vegas line: use implied spread (predicted margin = 0 is the line)
            spread_pick = "HOME" if predicted_margin > 0 else "AWAY"
            total_pick = ""  # Can't pick totals without a line
        
        record = ATSRecord(
            game_id=game_id,
            game_date=game_date,
            home_team=home_team,
            away_team=away_team,
            home_team_id=home_team_id,
            away_team_id=away_team_id,
            predicted_margin=predicted_margin,
            predicted_total=predicted_total,
            prediction_confidence=prediction_confidence,
            vegas_spread=vegas_spread,
            vegas_total=vegas_total,
            has_vegas_line=has_vegas,
            spread_pick=spread_pick,
            total_pick=total_pick,
            prediction_timestamp=datetime.now().isoformat(),
            odds_collected_at=datetime.now().isoformat() if has_vegas else None
        )
        
        self.records[game_id] = record
        self._save_records()
        
        return record
    
    def update_odds(self, game_id: str, vegas_spread: float, vegas_total: float) -> bool:
        """
        Update odds for an existing prediction.
        Useful for collecting odds closer to game time.
        
        Returns True if successful, False if game not found.
        """
        if game_id not in self.records:
            return False
        
        record = self.records[game_id]
        record.vegas_spread = vegas_spread
        record.vegas_total = vegas_total
        record.has_vegas_line = True
        record.odds_collected_at = datetime.now().isoformat()
        
        # Recalculate picks with actual Vegas line
        record.spread_pick = "HOME" if record.predicted_margin > vegas_spread else "AWAY"
        record.total_pick = "OVER" if record.predicted_total > vegas_total else "UNDER"
        
        self._save_records()
        return True
    
    def record_result(
        self,
        game_id: str,
        home_score: int,
        away_score: int
    ) -> Optional[ATSRecord]:
        """
        Record the actual game result and calculate accuracy.
        
        Returns the updated record or None if game not found.
        """
        if game_id not in self.records:
            return None
        
        record = self.records[game_id]
        record.home_score = home_score
        record.away_score = away_score
        record.actual_margin = home_score - away_score
        record.actual_total = home_score + away_score
        
        # Calculate ATS accuracy
        if record.has_vegas_line and record.vegas_spread is not None:
            # True ATS: did we beat the spread?
            # Home covers if actual_margin > vegas_spread
            home_covered = record.actual_margin > record.vegas_spread
            record.spread_correct = (record.spread_pick == "HOME") == home_covered
            
            # Total accuracy
            if record.vegas_total is not None:
                went_over = record.actual_total > record.vegas_total
                record.total_correct = (record.total_pick == "OVER") == went_over
        else:
            # Implied spread: did we pick the winner correctly?
            home_won = record.actual_margin > 0
            record.spread_correct = (record.spread_pick == "HOME") == home_won
            record.total_correct = None  # Can't evaluate without a line
        
        record.result_checked = True
        record.checked_at = datetime.now().isoformat()
        
        self._save_records()
        self._update_accuracy_history(record)
        
        return record
    
    def _update_accuracy_history(self, record: ATSRecord):
        """Update accuracy history after a result is recorded."""
        date_key = record.game_date
        
        if record.has_vegas_line:
            # Update with-Vegas stats
            section = self.accuracy_history["with_vegas_lines"]
            section["total_predictions"] += 1
            if record.spread_correct:
                section["spread_correct"] += 1
            if record.total_correct:
                section["total_correct"] += 1
            
            section["spread_accuracy"] = section["spread_correct"] / section["total_predictions"]
            if section["total_predictions"] > 0:
                total_with_lines = sum(1 for r in self.records.values() 
                                      if r.has_vegas_line and r.vegas_total and r.result_checked)
                total_correct = sum(1 for r in self.records.values() 
                                   if r.has_vegas_line and r.total_correct)
                section["total_accuracy"] = total_correct / total_with_lines if total_with_lines > 0 else 0
            
            # Daily breakdown
            if date_key not in section["daily_breakdown"]:
                section["daily_breakdown"][date_key] = {"predictions": 0, "spread_correct": 0, "total_correct": 0}
            section["daily_breakdown"][date_key]["predictions"] += 1
            if record.spread_correct:
                section["daily_breakdown"][date_key]["spread_correct"] += 1
            if record.total_correct:
                section["daily_breakdown"][date_key]["total_correct"] += 1
        else:
            # Update without-Vegas stats
            section = self.accuracy_history["without_vegas_lines"]
            section["total_predictions"] += 1
            if record.spread_correct:
                section["implied_spread_correct"] += 1
            
            section["implied_spread_accuracy"] = section["implied_spread_correct"] / section["total_predictions"]
            
            # Daily breakdown
            if date_key not in section["daily_breakdown"]:
                section["daily_breakdown"][date_key] = {"predictions": 0, "correct": 0}
            section["daily_breakdown"][date_key]["predictions"] += 1
            if record.spread_correct:
                section["daily_breakdown"][date_key]["correct"] += 1
        
        # Update combined stats
        combined = self.accuracy_history["combined"]
        combined["total_predictions"] += 1
        if record.spread_correct:
            combined["straight_up_correct"] += 1
        combined["straight_up_accuracy"] = combined["straight_up_correct"] / combined["total_predictions"]
        combined["last_updated"] = datetime.now().isoformat()
        
        # Update rolling stats
        self._update_rolling_accuracy()
        
        self._save_accuracy_history()
    
    def _update_rolling_accuracy(self):
        """Update 7-day and 30-day rolling accuracy."""
        now = datetime.now()
        
        for days, key in [(7, "rolling_7_day"), (30, "rolling_30_day")]:
            cutoff = (now - timedelta(days=days)).strftime('%Y-%m-%d')
            
            # Filter records within window
            recent_records = [r for r in self.records.values() 
                           if r.result_checked and r.game_date >= cutoff]
            
            # With Vegas
            vegas_records = [r for r in recent_records if r.has_vegas_line]
            self.accuracy_history[key]["with_vegas"]["predictions"] = len(vegas_records)
            self.accuracy_history[key]["with_vegas"]["spread_correct"] = sum(1 for r in vegas_records if r.spread_correct)
            self.accuracy_history[key]["with_vegas"]["accuracy"] = (
                self.accuracy_history[key]["with_vegas"]["spread_correct"] / len(vegas_records)
                if vegas_records else 0.0
            )
            
            # Without Vegas
            no_vegas = [r for r in recent_records if not r.has_vegas_line]
            self.accuracy_history[key]["without_vegas"]["predictions"] = len(no_vegas)
            self.accuracy_history[key]["without_vegas"]["correct"] = sum(1 for r in no_vegas if r.spread_correct)
            self.accuracy_history[key]["without_vegas"]["accuracy"] = (
                self.accuracy_history[key]["without_vegas"]["correct"] / len(no_vegas)
                if no_vegas else 0.0
            )
    
    def get_unchecked_predictions(self, before_date: Optional[str] = None) -> List[ATSRecord]:
        """Get predictions that haven't had results recorded yet."""
        cutoff = before_date or datetime.now().strftime('%Y-%m-%d')
        return [r for r in self.records.values() 
                if not r.result_checked and r.game_date < cutoff]
    
    def _calculate_confidence_stats(self) -> Dict:
        """Calculate accuracy for different confidence tiers."""
        tiers = {
            "over_50": {"min": 50, "predictions": 0, "correct": 0, "accuracy": 0.0},
            "over_60": {"min": 60, "predictions": 0, "correct": 0, "accuracy": 0.0},
            "over_70": {"min": 70, "predictions": 0, "correct": 0, "accuracy": 0.0},
            "over_80": {"min": 80, "predictions": 0, "correct": 0, "accuracy": 0.0}
        }
        
        checked_records = [r for r in self.records.values() if r.result_checked and r.has_vegas_line]
        
        for record in checked_records:
            conf = record.prediction_confidence
            is_correct = record.spread_correct
            
            for key, tier in tiers.items():
                if conf >= tier["min"]:
                    tier["predictions"] += 1
                    if is_correct:
                        tier["correct"] += 1
        
        # Calculate percentages
        for tier in tiers.values():
            if tier["predictions"] > 0:
                tier["accuracy"] = tier["correct"] / tier["predictions"]
        
        return tiers

    def get_accuracy_summary(self) -> Dict:
        """Get complete accuracy summary for README/reporting."""
        self._update_rolling_accuracy()
        confidence_stats = self._calculate_confidence_stats()
        
        return {
            "all_time": {
                "with_vegas_spread_accuracy": self.accuracy_history["with_vegas_lines"]["spread_accuracy"],
                "with_vegas_total_accuracy": self.accuracy_history["with_vegas_lines"]["total_accuracy"],
                "with_vegas_predictions": self.accuracy_history["with_vegas_lines"]["total_predictions"],
                "without_vegas_accuracy": self.accuracy_history["without_vegas_lines"]["implied_spread_accuracy"],
                "without_vegas_predictions": self.accuracy_history["without_vegas_lines"]["total_predictions"],
                "combined_straight_up": self.accuracy_history["combined"]["straight_up_accuracy"],
                "combined_predictions": self.accuracy_history["combined"]["total_predictions"]
            },
            "rolling_7_day": self.accuracy_history["rolling_7_day"],
            "rolling_30_day": self.accuracy_history["rolling_30_day"],
            "confidence_tiers": confidence_stats,
            "last_updated": self.accuracy_history["combined"]["last_updated"]
        }
    
    def generate_daily_predictions_table(self, target_date: str = None) -> str:
        """Generate a markdown table of predictions for a specific date."""
        if target_date is None:
            target_date = datetime.now().strftime('%Y-%m-%d')
            
        # Get predictions for this date
        predictions = [r for r in self.records.values() if r.game_date == target_date]
        
        if not predictions:
            return "*No predictions available for today.*"
            
        lines = [
            f"#### 📅 Predictions for {target_date}",
            "",
            "| Matchup | Spread Pick | Total Pick | Confidence |",
            "|---------|-------------|------------|------------|"
        ]
        
        # Sort by spread edge/confidence (highest absolute difference between prediction and line)
        # This highlights the "best bets" for the spread
        def get_spread_edge(record):
            if record.vegas_spread is None:
                return -1.0 # Push to bottom if no line
            return abs(record.predicted_margin - record.vegas_spread)
            
        predictions.sort(key=get_spread_edge, reverse=True)
        
        for p in predictions:
            matchup = f"{p.away_team} @ {p.home_team}"
            
            # Spread Pick
            if p.spread_pick:
                spread_text = f"**{p.spread_pick}**"
                if p.vegas_spread is not None:
                    spread_text += f" ({p.vegas_spread:+.1f})"
            else:
                spread_text = "-"
                
            # Total Pick
            if p.total_pick:
                total_text = f"**{p.total_pick}**"
                if p.vegas_total is not None:
                    total_text += f" ({p.vegas_total:.1f})"
            else:
                total_text = "-"
            
            lines.append(f"| {matchup} | {spread_text} | {total_text} | {p.prediction_confidence:.0f}% |")
            
        return "\n".join(lines)

    def generate_readme_section(self) -> str:
        """Generate markdown section for README with accuracy stats."""
        summary = self.get_accuracy_summary()
        all_time = summary["all_time"]
        r7 = summary["rolling_7_day"]
        r30 = summary["rolling_30_day"]
        
        # Determine badge colors
        def get_badge_color(accuracy: float) -> str:
            if accuracy >= 0.55:
                return "brightgreen"
            elif accuracy >= 0.52:
                return "green"
            elif accuracy >= 0.50:
                return "yellow"
            else:
                return "red"
        
        vegas_color = get_badge_color(all_time["with_vegas_spread_accuracy"])
        
        r7_combined_predictions = r7["with_vegas"]["predictions"] + r7["without_vegas"]["predictions"]
        r7_combined_correct = r7["with_vegas"]["spread_correct"] + r7["without_vegas"]["correct"]
        r7_combined_accuracy = (r7_combined_correct / r7_combined_predictions) if r7_combined_predictions else 0.0

        r30_combined_predictions = r30["with_vegas"]["predictions"] + r30["without_vegas"]["predictions"]
        r30_combined_correct = r30["with_vegas"]["spread_correct"] + r30["without_vegas"]["correct"]
        r30_combined_accuracy = (r30_combined_correct / r30_combined_predictions) if r30_combined_predictions else 0.0

        lines = [
            "## 📊 ATS Prediction Accuracy",
            "",
            "<!-- ACCURACY_STATS_START -->",
            "",
            "### Live Tracking Results",
            "",
            f"**Last Updated**: {summary['last_updated'] or 'Never'}",
            "",
            "#### Against The Spread (With Vegas Lines)",
            "",
            f"![ATS Accuracy](https://img.shields.io/badge/ATS_Accuracy-{all_time['with_vegas_spread_accuracy']*100:.1f}%25-{vegas_color})",
            "",
            f"| Metric | Value |",
            f"|--------|-------|",
            f"| **All-Time ATS** | {all_time['with_vegas_spread_accuracy']*100:.1f}% ({int(all_time['with_vegas_predictions'] * all_time['with_vegas_spread_accuracy'])}/{all_time['with_vegas_predictions']}) |",
            f"| **All-Time Totals** | {all_time['with_vegas_total_accuracy']*100:.1f}% |",
            f"| **7-Day ATS** | {r7['with_vegas']['accuracy']*100:.1f}% ({r7['with_vegas']['spread_correct']}/{r7['with_vegas']['predictions']}) |",
            f"| **30-Day ATS** | {r30['with_vegas']['accuracy']*100:.1f}% ({r30['with_vegas']['spread_correct']}/{r30['with_vegas']['predictions']}) |",
            "",
            "#### Straight-Up Predictions (All Games)",
            "",
            f"| Metric | Value |",
            f"|--------|-------|",
            f"| **All-Time** | {all_time['combined_straight_up']*100:.1f}% ({int(all_time['combined_predictions'] * all_time['combined_straight_up'])}/{all_time['combined_predictions']}) |",
            f"| **7-Day** | {r7_combined_accuracy*100:.1f}% ({r7_combined_correct}/{r7_combined_predictions}) |",
            f"| **30-Day** | {r30_combined_accuracy*100:.1f}% ({r30_combined_correct}/{r30_combined_predictions}) |",
            "",
            "<!-- ACCURACY_STATS_END -->",
            ""
        ]
        
        return "\n".join(lines)


# Singleton
_ats_tracker: Optional[ATSTracker] = None


def get_ats_tracker() -> ATSTracker:
    """Get or create the ATS tracker singleton."""
    global _ats_tracker
    if _ats_tracker is None:
        _ats_tracker = ATSTracker()
    return _ats_tracker

