"""
Unscented Kalman Filter implementation for tracking team states.
"""
import numpy as np
from typing import Dict, List, Optional, Tuple
from filterpy.kalman import UnscentedKalmanFilter as UKF
from filterpy.kalman import MerweScaledSigmaPoints
from scipy.linalg import block_diag

import config


class TeamUKF:
    """UKF for tracking a single team's state."""
    
    # State indices
    OFF_RATING = 0
    DEF_RATING = 1
    HOME_ADV = 2
    HEALTH = 3
    MOMENTUM = 4
    FATIGUE = 5
    PACE = 6
    
    STATE_DIM = 7
    
    def __init__(self, team_id: int, initial_state: Optional[np.ndarray] = None):
        self.team_id = team_id
        
        # Initialize state
        if initial_state is None:
            initial_state = np.array([
                100.0,  # offensive_rating (average)
                100.0,  # defensive_rating (average)
                config.DEFAULT_HOME_ADVANTAGE,  # home_advantage
                config.DEFAULT_HEALTH_STATUS,  # health_status
                0.0,    # momentum (neutral)
                0.0,    # fatigue (no fatigue)
                config.DEFAULT_PACE  # pace
            ])
        
        self.state = initial_state.copy()
        
        # Initialize UKF
        self._setup_ukf()
    
    def _setup_ukf(self):
        """Set up the Unscented Kalman Filter."""
        # Process noise covariance
        Q = np.diag([
            config.PROCESS_NOISE['offensive_rating'] ** 2,
            config.PROCESS_NOISE['defensive_rating'] ** 2,
            config.PROCESS_NOISE['home_advantage'] ** 2,
            config.PROCESS_NOISE['health_status'] ** 2,
            config.PROCESS_NOISE['momentum'] ** 2,
            config.PROCESS_NOISE['fatigue'] ** 2,
            config.PROCESS_NOISE['pace'] ** 2
        ])
        
        # Measurement noise covariance (for score differential and total)
        R = np.diag([
            config.MEASUREMENT_NOISE['score_differential'] ** 2,
            config.MEASUREMENT_NOISE['total_points'] ** 2,
            config.MEASUREMENT_NOISE['pace'] ** 2
        ])
        
        # Initial covariance (uncertainty in initial state)
        P = np.eye(self.STATE_DIM) * 10.0
        
        # Create sigma points
        points = MerweScaledSigmaPoints(n=self.STATE_DIM, alpha=0.001, beta=2, kappa=0)
        
        # Create UKF
        self.ukf = UKF(dim_x=self.STATE_DIM, dim_z=3, dt=1.0, 
                       fx=self._process_model, hx=self._measurement_model,
                       points=points)
        
        self.ukf.x = self.state.copy()
        self.ukf.P = P
        self.ukf.Q = Q
        self.ukf.R = R
    
    def _process_model(self, x: np.ndarray, dt: float) -> np.ndarray:
        """
        Process model: how state evolves over time.
        Most components follow random walk, but some have specific dynamics.
        """
        x_new = x.copy()
        
        # Ratings: random walk
        # (already handled by Q matrix, but we can add constraints)
        
        # Home advantage: slow drift (already in Q)
        
        # Health: can change quickly (handled by Q)
        
        # Momentum: exponential decay
        x_new[self.MOMENTUM] *= config.MOMENTUM_DECAY
        
        # Fatigue: decays with time (if no new games)
        x_new[self.FATIGUE] *= 0.95  # Slight decay per time step
        
        # Pace: relatively stable (random walk in Q)
        
        # Clamp values to reasonable ranges
        x_new[self.OFF_RATING] = np.clip(x_new[self.OFF_RATING], 50, 150)
        x_new[self.DEF_RATING] = np.clip(x_new[self.DEF_RATING], 50, 150)
        x_new[self.HOME_ADV] = np.clip(x_new[self.HOME_ADV], 0, 10)
        x_new[self.HEALTH] = np.clip(x_new[self.HEALTH], 0, 1)
        x_new[self.MOMENTUM] = np.clip(x_new[self.MOMENTUM], -1, 1)
        x_new[self.FATIGUE] = np.clip(x_new[self.FATIGUE], 0, 1)
        x_new[self.PACE] = np.clip(x_new[self.PACE], 60, 80)
        
        return x_new
    
    def _measurement_model(self, x: np.ndarray) -> np.ndarray:
        """
        Measurement model: predicts what we observe (score differential, total, pace)
        given the state.
        
        Note: This is a simplified model. In practice, we'd need opponent's state too.
        """
        # This is a placeholder - actual measurement requires opponent state
        # For now, return zeros (will be updated in game context)
        return np.array([0.0, 0.0, x[self.PACE]])
    
    def predict(self):
        """Predict state forward one time step."""
        self.ukf.predict()
        self.state = self.ukf.x.copy()
    
    def update_from_game(self, opponent_state: np.ndarray, score_diff: float, 
                        total_points: float, actual_pace: float, 
                        is_home: bool, features: Dict):
        """
        Update state based on game result.
        
        Args:
            opponent_state: Opponent's state vector
            score_diff: Score differential (positive if we won)
            total_points: Total points in game
            actual_pace: Actual pace of the game
            is_home: Whether this team was home
            features: Current feature values (health, momentum, fatigue, etc.)
        """
        # Update features that can be directly observed
        self.ukf.x[self.HEALTH] = features.get('health_status', self.ukf.x[self.HEALTH])
        self.ukf.x[self.MOMENTUM] = features.get('momentum', self.ukf.x[self.MOMENTUM])
        self.ukf.x[self.FATIGUE] = features.get('fatigue', self.ukf.x[self.FATIGUE])
        # Update pace with clamping to reasonable range (60-80 possessions)
        actual_pace_clamped = max(60.0, min(80.0, actual_pace))
        self.ukf.x[self.PACE] = 0.9 * self.ukf.x[self.PACE] + 0.1 * actual_pace_clamped
        
        if is_home:
            # Update home advantage based on performance
            expected_advantage = self.ukf.x[self.HOME_ADV]
            # Slight update based on home performance
            self.ukf.x[self.HOME_ADV] = 0.95 * expected_advantage + 0.05 * max(0, score_diff / 2)
        
        # Predict expected score differential and total
        opp_off = opponent_state[TeamUKF.OFF_RATING]
        opp_def = opponent_state[TeamUKF.DEF_RATING]
        our_off = self.ukf.x[self.OFF_RATING]
        our_def = self.ukf.x[self.DEF_RATING]
        
        # Expected score differential
        expected_diff = (our_off - opp_def) - (opp_off - our_def)
        if is_home:
            expected_diff += self.ukf.x[self.HOME_ADV]
        
        # Apply feature impacts
        health_impact = (features.get('health_status', 1.0) - 1.0) * 5.0
        momentum_impact = features.get('momentum', 0.0) * 3.0
        fatigue_impact = features.get('fatigue', 0.0) * 2.0
        
        expected_diff += health_impact + momentum_impact - fatigue_impact
        
        # Expected total - ratings are points per 100 possessions
        # Expected score = (team_offense - opponent_defense + baseline) * pace
        actual_pace_clamped = max(60.0, min(80.0, actual_pace))
        our_expected = ((our_off - opp_def + 100.0) / 100.0) * actual_pace_clamped
        opp_expected = ((opp_off - our_def + 100.0) / 100.0) * actual_pace_clamped
        expected_total = our_expected + opp_expected
        expected_total *= features.get('health_status', 1.0)
        
        # Measurement vector
        z = np.array([score_diff, total_points, actual_pace])
        z_pred = np.array([expected_diff, expected_total, actual_pace])
        
        # Update UKF
        self.ukf.update(z, hx=lambda x: self._measurement_model_with_opponent(x, opponent_state, is_home, features))
        
        # Update ratings based on residual
        residual_diff = score_diff - expected_diff
        residual_total = total_points - expected_total
        
        # Update offensive rating based on scoring
        # Use consistent formula with measurement model: expected = ((off - def + 100) / 100) * pace
        our_score = (total_points + score_diff) / 2.0 if score_diff > 0 else (total_points - score_diff) / 2.0
        opp_score = total_points - our_score
        expected_our_score = ((our_off - opp_def + 100.0) / 100.0) * actual_pace_clamped
        offensive_update = (our_score - expected_our_score) * 0.1
        self.ukf.x[self.OFF_RATING] += offensive_update

        # Update defensive rating based on opponent scoring
        expected_opp_score = ((opp_off - our_def + 100.0) / 100.0) * actual_pace_clamped
        defensive_update = (expected_opp_score - opp_score) * 0.1
        self.ukf.x[self.DEF_RATING] += defensive_update
        
        # Clamp values
        self.ukf.x[self.OFF_RATING] = np.clip(self.ukf.x[self.OFF_RATING], 50, 150)
        self.ukf.x[self.DEF_RATING] = np.clip(self.ukf.x[self.DEF_RATING], 50, 150)
        
        self.state = self.ukf.x.copy()
    
    def _measurement_model_with_opponent(self, x: np.ndarray, opponent_state: np.ndarray,
                                        is_home: bool, features: Dict) -> np.ndarray:
        """Measurement model that includes opponent state."""
        opp_off = opponent_state[TeamUKF.OFF_RATING]
        opp_def = opponent_state[TeamUKF.DEF_RATING]
        our_off = x[self.OFF_RATING]
        our_def = x[self.DEF_RATING]
        
        # Expected score differential
        expected_diff = (our_off - opp_def) - (opp_off - our_def)
        if is_home:
            expected_diff += x[self.HOME_ADV]
        
        # Apply feature impacts
        health_impact = (features.get('health_status', 1.0) - 1.0) * 5.0
        momentum_impact = features.get('momentum', 0.0) * 3.0
        fatigue_impact = features.get('fatigue', 0.0) * 2.0
        
        expected_diff += health_impact + momentum_impact - fatigue_impact
        
        # Expected total - use same formula as predictor
        # Expected score = (team_offense - opponent_defense + baseline) * pace
        pace = max(60.0, min(80.0, x[self.PACE]))
        our_expected = ((our_off - opp_def + 100.0) / 100.0) * pace
        opp_expected = ((opp_off - our_def + 100.0) / 100.0) * pace
        expected_total = our_expected + opp_expected
        expected_total *= features.get('health_status', 1.0)
        
        return np.array([expected_diff, expected_total, pace])
    
    def get_state(self) -> np.ndarray:
        """Get current state estimate."""
        return self.state.copy()
    
    def get_uncertainty(self) -> np.ndarray:
        """Get uncertainty (standard deviation) for each state component."""
        return np.sqrt(np.diag(self.ukf.P))


class MultiTeamUKF:
    """Manages UKF for multiple teams."""
    
    def __init__(self):
        self.teams: Dict[int, TeamUKF] = {}
    
    def get_team_ukf(self, team_id: int) -> TeamUKF:
        """Get or create UKF for a team."""
        if team_id not in self.teams:
            self.teams[team_id] = TeamUKF(team_id)
        return self.teams[team_id]
    
    def update_from_game(self, home_team_id: int, away_team_id: int,
                        home_score: float, away_score: float,
                        actual_pace: float, home_features: Dict, away_features: Dict):
        """Update both teams' states from a game result."""
        home_ukf = self.get_team_ukf(home_team_id)
        away_ukf = self.get_team_ukf(away_team_id)
        
        score_diff = home_score - away_score
        
        # Update home team
        home_ukf.update_from_game(
            away_ukf.get_state(),
            score_diff,
            home_score + away_score,
            actual_pace,
            is_home=True,
            features=home_features
        )
        
        # Update away team
        away_ukf.update_from_game(
            home_ukf.get_state(),
            -score_diff,
            home_score + away_score,
            actual_pace,
            is_home=False,
            features=away_features
        )
    
    def get_team_state(self, team_id: int) -> np.ndarray:
        """Get current state for a team."""
        return self.get_team_ukf(team_id).get_state()
    
    def get_all_states(self) -> Dict[int, np.ndarray]:
        """Get states for all teams."""
        return {team_id: ukf.get_state() for team_id, ukf in self.teams.items()}

    def get_all_team_ratings(self) -> Dict[int, float]:
        """
        Get overall ratings for all teams (offensive - defensive).

        Returns:
            Dict mapping team_id to rating (higher is better)
        """
        ratings = {}
        for team_id, ukf in self.teams.items():
            state = ukf.get_state()
            # Rating = offensive - defensive (higher is better)
            rating = state[TeamUKF.OFF_RATING] - state[TeamUKF.DEF_RATING]
            ratings[team_id] = float(rating)
        return ratings

