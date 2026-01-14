"""
Prediction tracking system for storing and validating spread/total predictions.
"""
import json
import os
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any
from src.espn_collector import get_espn_collector
import config


class PredictionTracker:
    """Handles storing predictions and tracking accuracy over time."""

    def __init__(self, data_dir: str = "data"):
        self.data_dir = data_dir
        self.predictions_file = os.path.join(data_dir, "predictions.json")
        self.results_file = os.path.join(data_dir, "results.json")

        # Ensure data directory exists
        os.makedirs(data_dir, exist_ok=True)

        # Load existing data
        self.predictions = self._load_predictions()
        self.results = self._load_results()

    def _load_predictions(self) -> Dict:
        """Load stored predictions."""
        if os.path.exists(self.predictions_file):
            try:
                with open(self.predictions_file, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                print("Warning: Could not load predictions file, starting fresh")
                return {}
        return {}

    def _load_results(self) -> Dict:
        """Load stored results."""
        if os.path.exists(self.results_file):
            try:
                with open(self.results_file, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                print("Warning: Could not load results file, starting fresh")
                return {}
        return {}

    def _save_predictions(self):
        """Save predictions to file."""
        with open(self.predictions_file, 'w') as f:
            json.dump(self.predictions, f, indent=2, default=str)

    def _save_results(self):
        """Save results to file."""
        with open(self.results_file, 'w') as f:
            json.dump(self.results, f, indent=2, default=str)

    def store_prediction(self, game_info: Dict, prediction: Dict):
        """
        Store a prediction for a game.

        Args:
            game_info: Game details (teams, date, spread, total)
            prediction: Model prediction (spread_pick, total_pick, confidence, etc.)
        """
        game_key = self._get_game_key(game_info)

        prediction_entry = {
            'timestamp': datetime.now().isoformat(),
            'game_info': game_info,
            'prediction': prediction,
            'result_checked': False
        }

        # Store by date for easy retrieval
        date_key = datetime.now().strftime('%Y-%m-%d')
        if date_key not in self.predictions:
            self.predictions[date_key] = {}

        self.predictions[date_key][game_key] = prediction_entry
        self._save_predictions()

    def _get_game_key(self, game_info: Dict) -> str:
        """Generate a unique key for a game."""
        home_team = game_info.get('home_team', '')
        away_team = game_info.get('away_team', '')
        game_date = game_info.get('date', datetime.now().strftime('%Y-%m-%d'))

        # Use team abbreviations for key
        return f"{away_team}_at_{home_team}_{game_date}"

    def check_results_for_date(self, target_date: str) -> Dict:
        """
        Check results for predictions made on a specific date.

        Args:
            target_date: Date string in YYYY-MM-DD format

        Returns:
            Dict with accuracy statistics
        """
        if target_date not in self.predictions:
            return {'error': f'No predictions found for {target_date}'}

        date_predictions = self.predictions[target_date]
        results = []

        # Get actual results from ESPN
        espn = get_espn_collector()
        completed_games = []

        # Fetch games for the target date and a few days after (in case of postponements)
        for days_ahead in range(7):
            check_date = (datetime.strptime(target_date, '%Y-%m-%d') + timedelta(days=days_ahead)).strftime('%Y%m%d')
            try:
                day_games = espn.get_games_for_date(check_date)
                completed_games.extend([g for g in day_games if g.get('HomeTeamScore') is not None])
            except Exception as e:
                continue

        print(f"Found {len(completed_games)} completed games to check against {len(date_predictions)} predictions")

        for game_key, pred_entry in date_predictions.items():
            if pred_entry.get('result_checked', False):
                continue  # Already checked

            game_info = pred_entry['game_info']
            prediction = pred_entry['prediction']

            # Find matching completed game
            actual_result = self._find_actual_result(game_info, completed_games)

            if actual_result:
                accuracy_result = self._calculate_accuracy(game_info, prediction, actual_result)

                # Store result
                if target_date not in self.results:
                    self.results[target_date] = {}

                self.results[target_date][game_key] = {
                    'prediction': pred_entry,
                    'actual_result': actual_result,
                    'accuracy': accuracy_result,
                    'checked_at': datetime.now().isoformat()
                }

                # Mark as checked
                pred_entry['result_checked'] = True
                results.append(accuracy_result)

        self._save_predictions()
        self._save_results()

        return self._summarize_accuracy(results)

    def _find_actual_result(self, game_info: Dict, completed_games: List) -> Optional[Dict]:
        """Find the actual result for a predicted game."""
        home_team = game_info.get('home_team', '').lower()
        away_team = game_info.get('away_team', '').lower()

        for game in completed_games:
            espn_home = game.get('HomeTeam', '').lower()
            espn_away = game.get('AwayTeam', '').lower()

            # Check for team name matches (could be improved with team mapping)
            if (home_team in espn_home or espn_home in home_team) and \
               (away_team in espn_away or espn_away in away_team):
                return {
                    'home_team': game.get('HomeTeam'),
                    'away_team': game.get('AwayTeam'),
                    'home_score': game.get('HomeTeamScore'),
                    'away_score': game.get('AwayTeamScore'),
                    'game_date': game.get('Date')
                }

        return None

    def _calculate_accuracy(self, game_info: Dict, prediction: Dict, actual_result: Dict) -> Dict:
        """Calculate if predictions were correct."""
        actual_home_score = actual_result['home_score']
        actual_away_score = actual_result['away_score']
        actual_margin = actual_home_score - actual_away_score
        actual_total = actual_home_score + actual_away_score

        spread_line = game_info.get('spread', 0)
        total_line = game_info.get('total', 0)

        # Spread accuracy
        spread_pick = prediction.get('covers_pick', '')
        home_favored = spread_line < 0  # Negative spread means home is favorite

        # Calculate if home team covered the spread
        actual_home_cover = actual_margin > abs(spread_line) if home_favored else actual_margin < -abs(spread_line)

        spread_correct = False
        if spread_pick == 'HOME':
            spread_correct = actual_home_cover
        elif spread_pick == 'AWAY':
            spread_correct = not actual_home_cover

        # Total accuracy
        total_pick = prediction.get('total_pick', '')
        total_correct = False
        if total_pick == 'OVER':
            total_correct = actual_total > total_line
        elif total_pick == 'UNDER':
            total_correct = actual_total < total_line

        return {
            'game': f"{actual_result['away_team']} @ {actual_result['home_team']}",
            'actual_score': f"{actual_away_score}-{actual_home_score}",
            'actual_total': actual_total,
            'spread_pick': spread_pick,
            'spread_correct': spread_correct,
            'spread_confidence': prediction.get('covers_conf', 0),
            'total_pick': total_pick,
            'total_correct': total_correct,
            'total_confidence': prediction.get('total_conf', 0),
            'spread_line': spread_line,
            'total_line': total_line
        }

    def _summarize_accuracy(self, results: List[Dict]) -> Dict:
        """Calculate overall accuracy statistics."""
        if not results:
            return {'error': 'No results to analyze'}

        spread_correct = [r for r in results if r.get('spread_correct')]
        total_correct = [r for r in results if r.get('total_correct')]

        spread_accuracy = len(spread_correct) / len(results) if results else 0
        total_accuracy = len(total_correct) / len(results) if results else 0

        # Confidence-weighted accuracy
        spread_weighted_correct = sum(r.get('spread_confidence', 0) for r in spread_correct)
        spread_weighted_total = sum(r.get('spread_confidence', 0) for r in results)
        spread_weighted_accuracy = spread_weighted_correct / spread_weighted_total if spread_weighted_total > 0 else 0

        total_weighted_correct = sum(r.get('total_confidence', 0) for r in total_correct)
        total_weighted_total = sum(r.get('total_confidence', 0) for r in results)
        total_weighted_accuracy = total_weighted_correct / total_weighted_total if total_weighted_total > 0 else 0

        return {
            'total_games': len(results),
            'spread_accuracy': spread_accuracy,
            'total_accuracy': total_accuracy,
            'spread_weighted_accuracy': spread_weighted_accuracy,
            'total_weighted_accuracy': total_weighted_accuracy,
            'results': results
        }

    def get_accuracy_report(self, days_back: int = 7) -> Dict:
        """Get accuracy report for recent predictions."""
        all_results = []
        end_date = datetime.now()

        for i in range(days_back):
            check_date = (end_date - timedelta(days=i)).strftime('%Y-%m-%d')
            if check_date in self.results:
                day_results = self.results[check_date]
                for game_key, result_data in day_results.items():
                    all_results.append(result_data['accuracy'])

        return self._summarize_accuracy(all_results)

    def list_unchecked_predictions(self) -> List[Dict]:
        """Get list of predictions that haven't been checked yet."""
        unchecked = []

        for date_key, date_predictions in self.predictions.items():
            for game_key, pred_entry in date_predictions.items():
                if not pred_entry.get('result_checked', False):
                    unchecked.append({
                        'date': date_key,
                        'game_key': game_key,
                        'game_info': pred_entry['game_info'],
                        'prediction': pred_entry['prediction']
                    })

        return unchecked
