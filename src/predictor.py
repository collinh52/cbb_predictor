"""
Prediction engine that processes games and generates predictions.
"""
from datetime import datetime
from typing import List, Dict, Optional, Tuple
import numpy as np
from scipy.stats import norm

from src.data_collector import DataCollector
from src.feature_calculator import FeatureCalculator
from src.ukf_model import MultiTeamUKF, TeamUKF
from src.utils import normalize_team_id
import config


class Predictor:
    """Main prediction engine."""
    
    def __init__(self):
        self.collector = DataCollector()
        self.calculator = FeatureCalculator(self.collector)
        self.ukf = MultiTeamUKF()
        self.initialized = False
        self._completed_games_cache: Optional[List[Dict]] = None
    
    def initialize(self, season: Optional[int] = None):
        """Initialize by processing all historical games."""
        if self.initialized:
            return
        
        season = season or config.CURRENT_SEASON
        games = self.collector.get_completed_games(season)
        self._completed_games_cache = games
        
        # Sort games by date
        games.sort(key=lambda g: g.get('DateTime', ''))
        
        # Process each game
        for idx, game in enumerate(games):
            self._process_completed_game(game, games, idx)
        
        self.initialized = True
    
    def _process_completed_game(
        self,
        game: Dict,
        all_games: Optional[List[Dict]] = None,
        game_index: Optional[int] = None,
    ):
        """Process a completed game to update team states."""
        if all_games is None or game_index is None:
            all_games = [game]
            game_index = 0

        home_team_id = self._get_team_id(game, 'HomeTeam', 'HomeTeamID')
        away_team_id = self._get_team_id(game, 'AwayTeam', 'AwayTeamID')
        home_score = game.get('HomeTeamScore')
        away_score = game.get('AwayTeamScore')
        
        if home_team_id is None or away_team_id is None:
            return
        
        if home_score is None or away_score is None:
            return
        
        # Get game date
        game_date_str = game.get('DateTime', '')
        if not game_date_str:
            return
        
        try:
            game_date = datetime.fromisoformat(game_date_str.replace('Z', '+00:00'))
        except:
            return
        
        # Get all games up to this point for feature calculation
        games_before = all_games[:game_index]
        
        # Calculate features for both teams
        home_features = self.calculator.get_game_features(
            game, home_team_id, is_home=True,
            all_games=games_before, current_date=game_date,
            team_name=game.get('HomeTeam') or game.get('HomeTeamName')
        )
        
        away_features = self.calculator.get_game_features(
            game, away_team_id, is_home=False,
            all_games=games_before, current_date=game_date,
            team_name=game.get('AwayTeam') or game.get('AwayTeamName')
        )
        
        # Estimate actual pace (simplified - would need possession data)
        # Typical college basketball pace is 65-75 possessions per game
        # We estimate based on total points: pace ≈ total_points / (avg_off_rating/100)
        # For a rough estimate, use a fixed pace around 70 possessions
        total_points = home_score + away_score
        # Rough estimate: pace correlates with total points, but is relatively stable
        # Use average of team paces from features, or default to 70
        avg_feature_pace = (home_features.get('pace', 70) + away_features.get('pace', 70)) / 2.0
        estimated_pace = max(60.0, min(80.0, avg_feature_pace))  # Clamp to reasonable range
        
        # Update UKF
        self.ukf.update_from_game(
            home_team_id, away_team_id,
            home_score, away_score,
            estimated_pace,
            home_features, away_features
        )
    
    def _get_team_id(self, game: Dict, name_key: str, id_key: str) -> Optional[int]:
        """Extract team ID from game data."""
        team_id = game.get(id_key)
        normalized_id = self._normalize_team_id(team_id)
        if normalized_id is not None:
            return normalized_id
        
        # Fallback: use team name as hash (consistent)
        team_name = game.get(name_key)
        if team_name:
            return self._normalize_team_id(str(team_name))
        
        return None

    def _normalize_team_id(self, team_id_or_name) -> Optional[int]:
        """Normalize a team identifier or name to an integer ID."""
        return normalize_team_id(team_id_or_name)

    @staticmethod
    def _coerce_float(value, default: float) -> float:
        try:
            if value is None:
                return default
            return float(value)
        except (TypeError, ValueError):
            return default

    def _sanitize_kenpom_rating(self, rating) -> Dict[str, float]:
        defaults = {
            'adj_em': float(config.KENPOM_DEFAULT_ADJ_EM),
            'adj_o': float(config.KENPOM_DEFAULT_ADJ_O),
            'adj_d': float(config.KENPOM_DEFAULT_ADJ_D),
            'adj_t': float(config.KENPOM_DEFAULT_ADJ_T),
        }
        if not isinstance(rating, dict):
            return defaults

        return {
            key: self._coerce_float(rating.get(key), defaults[key])
            for key in defaults
        }
    
    def predict_game(self, game: Dict) -> Dict:
        """
        Predict outcome for a game.
        
        Returns dictionary with predictions and confidence scores.
        """
        home_team_id = self._get_team_id(game, 'HomeTeam', 'HomeTeamID')
        away_team_id = self._get_team_id(game, 'AwayTeam', 'AwayTeamID')
        
        if home_team_id is None or away_team_id is None:
            return self._empty_prediction()
        
        # Get current states
        home_state = self.ukf.get_team_state(home_team_id)
        away_state = self.ukf.get_team_state(away_team_id)
        
        # Get current features
        all_games = self._get_completed_games_cached()
        game_date = datetime.now()
        
        home_features = self.calculator.get_game_features(
            game, home_team_id, is_home=True,
            all_games=all_games, current_date=game_date,
            team_name=game.get('HomeTeam') or game.get('HomeTeamName')
        )
        
        away_features = self.calculator.get_game_features(
            game, away_team_id, is_home=False,
            all_games=all_games, current_date=game_date,
            team_name=game.get('AwayTeam') or game.get('AwayTeamName')
        )
        
        # Get uncertainties
        home_ukf = self.ukf.get_team_ukf(home_team_id)
        away_ukf = self.ukf.get_team_ukf(away_team_id)
        home_uncertainty = home_ukf.get_uncertainty()
        away_uncertainty = away_ukf.get_uncertainty()
        
        # Predict point differential
        home_off = home_state[TeamUKF.OFF_RATING]
        home_def = home_state[TeamUKF.DEF_RATING]
        away_off = away_state[TeamUKF.OFF_RATING]
        away_def = away_state[TeamUKF.DEF_RATING]
        home_adv = home_state[TeamUKF.HOME_ADV]
        
        # Base prediction
        predicted_margin = (home_off - away_def) - (away_off - home_def) + home_adv
        
        # Apply feature impacts
        health_impact = (home_features['health_status'] - away_features['health_status']) * 5.0
        momentum_impact = (home_features['momentum'] - away_features['momentum']) * 3.0
        fatigue_impact = (away_features['fatigue'] - home_features['fatigue']) * 2.0
        
        predicted_margin += health_impact + momentum_impact + fatigue_impact

        # KenPom adjustment (scaled to game pace)
        kenpom_home = self._sanitize_kenpom_rating(self.collector.get_kenpom_team_rating(
            game.get('HomeTeam') or game.get('HomeTeamName')
        ))
        kenpom_away = self._sanitize_kenpom_rating(self.collector.get_kenpom_team_rating(
            game.get('AwayTeam') or game.get('AwayTeamName')
        ))
        kenpom_pace = (kenpom_home['adj_t'] + kenpom_away['adj_t']) / 2.0
        kenpom_margin = (kenpom_home['adj_em'] - kenpom_away['adj_em']) * (kenpom_pace / 100.0)
        predicted_margin += kenpom_margin * config.KENPOM_MARGIN_WEIGHT
        
        # Predict total points
        # Offensive ratings represent points per 100 possessions
        avg_pace = (home_features['pace'] + away_features['pace']) / 2.0
        if config.KENPOM_PACE_WEIGHT > 0:
            avg_pace = (1.0 - config.KENPOM_PACE_WEIGHT) * avg_pace + config.KENPOM_PACE_WEIGHT * kenpom_pace
        # Clamp pace to reasonable range (60-80 possessions per game)
        avg_pace = max(60.0, min(80.0, avg_pace))
        
        # Calculate expected points for each team: (offensive_rating / 100) * pace
        # With ratings ~90 and pace ~70: (90/100)*70 = 63 points per team = 126 total
        # Typical college basketball totals are 140-150, so scale factor ~1.15-1.20
        home_expected_points = (home_off / 100.0) * avg_pace
        away_expected_points = (away_off / 100.0) * avg_pace
        predicted_total = (home_expected_points + away_expected_points) * 1.15
        
        # Apply health adjustment (health_status is 0-1, adjusts down if teams unhealthy)
        health_factor = (home_features['health_status'] + away_features['health_status']) / 2.0
        predicted_total *= health_factor
        
        # Calculate uncertainty in predictions
        margin_uncertainty = np.sqrt(
            home_uncertainty[TeamUKF.OFF_RATING]**2 +
            home_uncertainty[TeamUKF.DEF_RATING]**2 +
            away_uncertainty[TeamUKF.OFF_RATING]**2 +
            away_uncertainty[TeamUKF.DEF_RATING]**2 +
            config.MEASUREMENT_NOISE['score_differential']**2
        )
        
        total_uncertainty = np.sqrt(
            home_uncertainty[TeamUKF.OFF_RATING]**2 +
            away_uncertainty[TeamUKF.OFF_RATING]**2 +
            config.MEASUREMENT_NOISE['total_points']**2
        )
        
        # Get spread and total from game
        spread = game.get('PointSpread')
        total_line = game.get('OverUnder')
        
        predictions = {
            'predicted_margin': float(predicted_margin),
            'predicted_total': float(predicted_total),
            'margin_uncertainty': float(margin_uncertainty),
            'total_uncertainty': float(total_uncertainty),
            'predicted_winner': 'home' if predicted_margin > 0 else 'away',
            'home_team_id': home_team_id,
            'away_team_id': away_team_id
        }
        
        # Calculate spread coverage probability
        if spread is not None:
            # Home team covers if: home_score - away_score > spread
            # Which means: predicted_margin > spread
            prob_home_covers = 1.0 - norm.cdf(spread, predicted_margin, margin_uncertainty)
            predictions['spread'] = float(spread)
            predictions['home_covers_probability'] = float(prob_home_covers)
            predictions['away_covers_probability'] = float(1.0 - prob_home_covers)
            predictions['home_covers_confidence'] = float(abs(prob_home_covers - 0.5) * 200)  # 0-100%
        else:
            predictions['spread'] = None
            predictions['home_covers_probability'] = None
            predictions['away_covers_probability'] = None
            predictions['home_covers_confidence'] = None
        
        # Calculate over/under probability
        if total_line is not None:
            prob_over = 1.0 - norm.cdf(total_line, predicted_total, total_uncertainty)
            predictions['total_line'] = float(total_line)
            predictions['over_probability'] = float(prob_over)
            predictions['under_probability'] = float(1.0 - prob_over)
            predictions['over_confidence'] = float(abs(prob_over - 0.5) * 200)  # 0-100%
        else:
            predictions['total_line'] = None
            predictions['over_probability'] = None
            predictions['under_probability'] = None
            predictions['over_confidence'] = None
        
        # Overall confidence (average of available confidences)
        confidences = []
        if predictions['home_covers_confidence'] is not None:
            confidences.append(predictions['home_covers_confidence'])
        if predictions['over_confidence'] is not None:
            confidences.append(predictions['over_confidence'])
        
        predictions['overall_confidence'] = float(np.mean(confidences)) if confidences else 50.0
        
        return predictions
    
    def _empty_prediction(self) -> Dict:
        """Return empty prediction structure."""
        return {
            'predicted_margin': 0.0,
            'predicted_total': 0.0,
            'margin_uncertainty': 0.0,
            'total_uncertainty': 0.0,
            'predicted_winner': None,
            'spread': None,
            'total_line': None,
            'home_covers_probability': None,
            'away_covers_probability': None,
            'over_probability': None,
            'under_probability': None,
            'home_covers_confidence': None,
            'over_confidence': None,
            'overall_confidence': 0.0
        }
    
    def get_team_ratings(self) -> Dict[int, Dict]:
        """Get current ratings for all teams."""
        ratings = {}
        for team_id, state in self.ukf.get_all_states().items():
            ratings[team_id] = {
                'offensive_rating': float(state[TeamUKF.OFF_RATING]),
                'defensive_rating': float(state[TeamUKF.DEF_RATING]),
                'home_advantage': float(state[TeamUKF.HOME_ADV]),
                'health_status': float(state[TeamUKF.HEALTH]),
                'momentum': float(state[TeamUKF.MOMENTUM]),
                'fatigue': float(state[TeamUKF.FATIGUE]),
                'pace': float(state[TeamUKF.PACE])
            }
        return ratings

    def _get_completed_games_cached(self) -> List[Dict]:
        """Return cached completed games to avoid repeated disk reads."""
        if self._completed_games_cache is None:
            self._completed_games_cache = self.collector.get_completed_games()
        return self._completed_games_cache
    
    def predict_games(self, games: List[Dict]) -> List[Dict]:
        """Predict outcomes for multiple games."""
        if not self.initialized:
            self.initialize()
        
        results = []
        for game in games:
            prediction = self.predict_game(game)
            results.append({
                'game': game,
                'prediction': prediction
            })
        
        return results


# Global predictor instances
_predictor: Optional[Predictor] = None
_hybrid_predictor: Optional['HybridPredictor'] = None


def get_predictor() -> Predictor:
    """Get or create global predictor instance."""
    global _predictor
    if _predictor is None:
        _predictor = Predictor()
        _predictor.initialize()
    return _predictor


def get_hybrid_predictor() -> 'HybridPredictor':
    """Get or create global hybrid predictor instance."""
    global _hybrid_predictor
    if _hybrid_predictor is None:
        from src.hybrid_predictor import HybridPredictor
        _hybrid_predictor = HybridPredictor(get_predictor())
    return _hybrid_predictor

