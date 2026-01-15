"""
Feature engineering module for ML model.
Combines UKF state estimates with pregame lines and contextual features.
"""
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
import numpy as np
from sklearn.preprocessing import StandardScaler
import pickle
import os

from src.ukf_model import TeamUKF
from src.feature_calculator import FeatureCalculator
from src.data_collector import DataCollector
import config


class MLFeatureEngineer:
    """Engineer features for ML model from UKF states and game context."""
    
    def __init__(self, collector: Optional[DataCollector] = None, 
                 calculator: Optional[FeatureCalculator] = None):
        self.collector = collector or DataCollector()
        self.calculator = calculator or FeatureCalculator(self.collector)
        self.scaler = StandardScaler()
        self.scaler_fitted = False
        self.feature_names = []
    
    def extract_ukf_features(self, home_state: np.ndarray, away_state: np.ndarray,
                            home_uncertainty: np.ndarray, away_uncertainty: np.ndarray) -> Dict:
        """Extract UKF state features."""
        return {
            # Home team features
            'home_off_rating': float(home_state[TeamUKF.OFF_RATING]),
            'home_def_rating': float(home_state[TeamUKF.DEF_RATING]),
            'home_home_adv': float(home_state[TeamUKF.HOME_ADV]),
            'home_health': float(home_state[TeamUKF.HEALTH]),
            'home_momentum': float(home_state[TeamUKF.MOMENTUM]),
            'home_fatigue': float(home_state[TeamUKF.FATIGUE]),
            'home_pace': float(home_state[TeamUKF.PACE]),
            
            # Home team uncertainties
            'home_off_uncertainty': float(home_uncertainty[TeamUKF.OFF_RATING]),
            'home_def_uncertainty': float(home_uncertainty[TeamUKF.DEF_RATING]),
            'home_home_adv_uncertainty': float(home_uncertainty[TeamUKF.HOME_ADV]),
            
            # Away team features
            'away_off_rating': float(away_state[TeamUKF.OFF_RATING]),
            'away_def_rating': float(away_state[TeamUKF.DEF_RATING]),
            'away_health': float(away_state[TeamUKF.HEALTH]),
            'away_momentum': float(away_state[TeamUKF.MOMENTUM]),
            'away_fatigue': float(away_state[TeamUKF.FATIGUE]),
            'away_pace': float(away_state[TeamUKF.PACE]),
            
            # Away team uncertainties
            'away_off_uncertainty': float(away_uncertainty[TeamUKF.OFF_RATING]),
            'away_def_uncertainty': float(away_uncertainty[TeamUKF.DEF_RATING]),
            
            # Derived features
            'off_rating_diff': float(home_state[TeamUKF.OFF_RATING] - away_state[TeamUKF.OFF_RATING]),
            'def_rating_diff': float(home_state[TeamUKF.DEF_RATING] - away_state[TeamUKF.DEF_RATING]),
            'momentum_diff': float(home_state[TeamUKF.MOMENTUM] - away_state[TeamUKF.MOMENTUM]),
            'fatigue_diff': float(home_state[TeamUKF.FATIGUE] - away_state[TeamUKF.FATIGUE]),
            'pace_avg': float((home_state[TeamUKF.PACE] + away_state[TeamUKF.PACE]) / 2.0),
            'health_diff': float(home_state[TeamUKF.HEALTH] - away_state[TeamUKF.HEALTH]),
        }
    
    def extract_contextual_features(self, game: Dict, home_team_id: int, 
                                   away_team_id: int, game_date: datetime,
                                   all_games: List[Dict]) -> Dict:
        """Extract contextual features (rest days, recent form, etc.)."""
        features = {}
        home_team_name = game.get('HomeTeam') or game.get('HomeTeamName')
        away_team_name = game.get('AwayTeam') or game.get('AwayTeamName')
        
        # Pregame lines
        pregame_spread = game.get('PointSpread')
        pregame_total = game.get('OverUnder')
        features['pregame_spread'] = float(pregame_spread) if pregame_spread is not None else 0.0
        features['pregame_total'] = float(pregame_total) if pregame_total is not None else 0.0
        
        # Days of rest
        home_rest_days = self._calculate_rest_days(home_team_id, game_date, all_games)
        away_rest_days = self._calculate_rest_days(away_team_id, game_date, all_games)
        features['home_rest_days'] = float(home_rest_days)
        features['away_rest_days'] = float(away_rest_days)
        features['rest_days_diff'] = float(home_rest_days - away_rest_days)
        
        # Recent form (last 5 and 10 games)
        home_form_5 = self._calculate_recent_form(home_team_id, game_date, all_games, window=5)
        home_form_10 = self._calculate_recent_form(home_team_id, game_date, all_games, window=10)
        away_form_5 = self._calculate_recent_form(away_team_id, game_date, all_games, window=5)
        away_form_10 = self._calculate_recent_form(away_team_id, game_date, all_games, window=10)
        
        features['home_form_5'] = float(home_form_5)
        features['home_form_10'] = float(home_form_10)
        features['away_form_5'] = float(away_form_5)
        features['away_form_10'] = float(away_form_10)
        features['form_diff_5'] = float(home_form_5 - away_form_5)
        features['form_diff_10'] = float(home_form_10 - away_form_10)
        
        # Head-to-head history (simplified - could be enhanced)
        h2h_margin = self._get_head_to_head(home_team_id, away_team_id, game_date, all_games)
        features['h2h_margin'] = float(h2h_margin) if h2h_margin is not None else 0.0
        
        # Time of day (if available)
        game_time_str = game.get('DateTime', '')
        if game_time_str:
            try:
                game_dt = datetime.fromisoformat(game_time_str.replace('Z', '+00:00'))
                features['hour_of_day'] = float(game_dt.hour)
                features['day_of_week'] = float(game_dt.weekday())
            except:
                features['hour_of_day'] = 0.0
                features['day_of_week'] = 0.0
        else:
            features['hour_of_day'] = 0.0
            features['day_of_week'] = 0.0
        
        # Home/away record differences (simplified)
        home_record = self._calculate_record(home_team_id, game_date, all_games, is_home=True)
        away_record = self._calculate_record(away_team_id, game_date, all_games, is_home=False)
        features['home_home_win_pct'] = float(home_record)
        features['away_away_win_pct'] = float(away_record)

        # KenPom ratings
        home_kp = self.collector.get_kenpom_team_rating(home_team_name)
        away_kp = self.collector.get_kenpom_team_rating(away_team_name)
        features['home_kp_adj_em'] = float(home_kp['adj_em'])
        features['home_kp_adj_o'] = float(home_kp['adj_o'])
        features['home_kp_adj_d'] = float(home_kp['adj_d'])
        features['home_kp_adj_t'] = float(home_kp['adj_t'])
        features['away_kp_adj_em'] = float(away_kp['adj_em'])
        features['away_kp_adj_o'] = float(away_kp['adj_o'])
        features['away_kp_adj_d'] = float(away_kp['adj_d'])
        features['away_kp_adj_t'] = float(away_kp['adj_t'])
        features['kp_adj_em_diff'] = float(home_kp['adj_em'] - away_kp['adj_em'])
        features['kp_adj_o_diff'] = float(home_kp['adj_o'] - away_kp['adj_o'])
        features['kp_adj_d_diff'] = float(home_kp['adj_d'] - away_kp['adj_d'])
        features['kp_adj_t_diff'] = float(home_kp['adj_t'] - away_kp['adj_t'])
        
        return features
    
    def _calculate_rest_days(self, team_id: int, game_date: datetime, all_games: List[Dict]) -> int:
        """Calculate days of rest since last game."""
        team_games = []
        for game in all_games:
            if game.get('Status') != 'Final':
                continue
            home_id = self.calculator._normalize_team_id(game.get('HomeTeamID') or game.get('HomeTeam'))
            away_id = self.calculator._normalize_team_id(game.get('AwayTeamID') or game.get('AwayTeam'))
            team_norm = self.calculator._normalize_team_id(team_id)
            
            if home_id == team_norm or away_id == team_norm:
                game_date_str = game.get('DateTime', '')
                if game_date_str:
                    try:
                        g_date = datetime.fromisoformat(game_date_str.replace('Z', '+00:00'))
                        if g_date < game_date:
                            team_games.append(g_date)
                    except:
                        continue
        
        if team_games:
            last_game = max(team_games)
            rest_days = (game_date.date() - last_game.date()).days
            return max(0, rest_days)
        return 7  # Default if no previous games
    
    def _calculate_recent_form(self, team_id: int, game_date: datetime, 
                              all_games: List[Dict], window: int = 5) -> float:
        """Calculate recent form (average point differential in last N games)."""
        team_norm = self.calculator._normalize_team_id(team_id)
        recent_games = []
        
        for game in all_games:
            if game.get('Status') != 'Final':
                continue
            home_id = self.calculator._normalize_team_id(game.get('HomeTeamID') or game.get('HomeTeam'))
            away_id = self.calculator._normalize_team_id(game.get('AwayTeamID') or game.get('AwayTeam'))
            home_score = game.get('HomeTeamScore')
            away_score = game.get('AwayTeamScore')
            
            if home_score is None or away_score is None:
                continue
            
            game_date_str = game.get('DateTime', '')
            if not game_date_str:
                continue
            
            try:
                g_date = datetime.fromisoformat(game_date_str.replace('Z', '+00:00'))
                if g_date >= game_date:
                    continue
            except:
                continue
            
            if home_id == team_norm:
                point_diff = home_score - away_score
                recent_games.append((g_date, point_diff))
            elif away_id == team_norm:
                point_diff = away_score - home_score
                recent_games.append((g_date, point_diff))
        
        if recent_games:
            recent_games.sort(key=lambda x: x[0], reverse=True)
            recent_games = recent_games[:window]
            avg_diff = np.mean([g[1] for g in recent_games])
            return float(avg_diff)
        
        return 0.0
    
    def _get_head_to_head(self, home_team_id: int, away_team_id: int,
                          game_date: datetime, all_games: List[Dict]) -> Optional[float]:
        """Get average point differential from head-to-head matchups."""
        home_norm = self.calculator._normalize_team_id(home_team_id)
        away_norm = self.calculator._normalize_team_id(away_team_id)
        
        margins = []
        for game in all_games:
            if game.get('Status') != 'Final':
                continue
            game_home = self.calculator._normalize_team_id(game.get('HomeTeamID') or game.get('HomeTeam'))
            game_away = self.calculator._normalize_team_id(game.get('AwayTeamID') or game.get('AwayTeam'))
            home_score = game.get('HomeTeamScore')
            away_score = game.get('AwayTeamScore')
            
            if home_score is None or away_score is None:
                continue
            
            game_date_str = game.get('DateTime', '')
            if not game_date_str:
                continue
            
            try:
                g_date = datetime.fromisoformat(game_date_str.replace('Z', '+00:00'))
                if g_date >= game_date:
                    continue
            except:
                continue
            
            # Check if this is a matchup between these teams
            if (game_home == home_norm and game_away == away_norm):
                margins.append(float(home_score - away_score))
            elif (game_home == away_norm and game_away == home_norm):
                margins.append(float(away_score - home_score))
        
        if margins:
            return float(np.mean(margins))
        return None
    
    def _calculate_record(self, team_id: int, game_date: datetime,
                         all_games: List[Dict], is_home: bool) -> float:
        """Calculate win percentage at home (if is_home=True) or away (if False)."""
        team_norm = self.calculator._normalize_team_id(team_id)
        wins = 0
        total = 0
        
        for game in all_games:
            if game.get('Status') != 'Final':
                continue
            home_id = self.calculator._normalize_team_id(game.get('HomeTeamID') or game.get('HomeTeam'))
            away_id = self.calculator._normalize_team_id(game.get('AwayTeamID') or game.get('AwayTeam'))
            home_score = game.get('HomeTeamScore')
            away_score = game.get('AwayTeamScore')
            
            if home_score is None or away_score is None:
                continue
            
            game_date_str = game.get('DateTime', '')
            if not game_date_str:
                continue
            
            try:
                g_date = datetime.fromisoformat(game_date_str.replace('Z', '+00:00'))
                if g_date >= game_date:
                    continue
            except:
                continue
            
            if is_home and home_id == team_norm:
                total += 1
                if home_score > away_score:
                    wins += 1
            elif not is_home and away_id == team_norm:
                total += 1
                if away_score > home_score:
                    wins += 1
        
        return (wins / total) if total > 0 else 0.5
    
    def engineer_features(self, home_state: np.ndarray, away_state: np.ndarray,
                         home_uncertainty: np.ndarray, away_uncertainty: np.ndarray,
                         game: Dict, home_team_id: int, away_team_id: int,
                         game_date: datetime, all_games: List[Dict]) -> Tuple[np.ndarray, Dict]:
        """
        Engineer all features for ML model.
        
        Returns:
            features_array: numpy array of features (for model input)
            features_dict: dictionary with feature names and values (for storage)
        """
        # Extract UKF features
        ukf_features = self.extract_ukf_features(home_state, away_state, home_uncertainty, away_uncertainty)
        
        # Extract contextual features
        contextual_features = self.extract_contextual_features(
            game, home_team_id, away_team_id, game_date, all_games
        )
        
        # Combine all features
        all_features = {**ukf_features, **contextual_features}
        
        # Store feature names on first call
        if not self.feature_names:
            self.feature_names = sorted(all_features.keys())
        
        # Convert to array in consistent order
        features_array = np.array([all_features[name] for name in self.feature_names], dtype=np.float32)
        
        return features_array, all_features
    
    def fit_scaler(self, feature_arrays: List[np.ndarray]):
        """Fit the feature scaler on training data."""
        if not feature_arrays:
            return
        
        X = np.vstack(feature_arrays)
        self.scaler.fit(X)
        self.scaler_fitted = True
    
    def transform_features(self, features_array: np.ndarray) -> np.ndarray:
        """Transform features using fitted scaler."""
        if not self.scaler_fitted:
            # If scaler not fitted, return as-is (will be fitted during training)
            return features_array
        
        return self.scaler.transform(features_array.reshape(1, -1)).flatten()
    
    def save_scaler(self, path: str):
        """Save the fitted scaler."""
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'wb') as f:
            pickle.dump({
                'scaler': self.scaler,
                'feature_names': self.feature_names
            }, f)
    
    def load_scaler(self, path: str):
        """Load a fitted scaler."""
        with open(path, 'rb') as f:
            data = pickle.load(f)
            self.scaler = data['scaler']
            self.feature_names = data['feature_names']
            self.scaler_fitted = True

