"""
Feature calculation module for computing momentum, fatigue, health status, and home advantage.
"""
from datetime import datetime, timedelta
from typing import List, Dict, Optional
import numpy as np

import config
from src.data_collector import DataCollector


class FeatureCalculator:
    """Calculates derived features from game data."""
    
    def __init__(self, collector: Optional[DataCollector] = None):
        self.collector = collector or DataCollector()
    
    def _normalize_team_id(self, team_id_or_name) -> Optional[int]:
        """Normalize team identifier to integer ID."""
        if team_id_or_name is None:
            return None
        
        if isinstance(team_id_or_name, int):
            return team_id_or_name
        
        if isinstance(team_id_or_name, str):
            try:
                # Try to parse as int first
                return int(team_id_or_name)
            except ValueError:
                # Use hash for string names
                return abs(hash(team_id_or_name)) % 100000
        
        return None
    
    def calculate_momentum(self, team_id: int, games: List[Dict], current_date: datetime) -> float:
        """
        Calculate team momentum based on recent win/loss record and point differential.
        
        Returns normalized momentum score (-1 to 1, where 1 is best).
        """
        # Get recent games within the momentum window
        recent_games = []
        cutoff_date = current_date - timedelta(days=30)  # Look back 30 days
        
        for game in games:
            game_date_str = game.get('DateTime', '')
            if not game_date_str:
                continue
            
            try:
                game_date = datetime.fromisoformat(game_date_str.replace('Z', '+00:00'))
                if game_date < current_date and game_date >= cutoff_date:
                    recent_games.append(game)
            except:
                continue
        
        if len(recent_games) < 2:
            return 0.0  # Neutral momentum if not enough data
        
        # Sort by date (most recent first)
        recent_games.sort(key=lambda g: g.get('DateTime', ''), reverse=True)
        recent_games = recent_games[:config.MOMENTUM_WINDOW]
        
        # Calculate win/loss record
        wins = 0
        point_differential_sum = 0.0
        
        for game in recent_games:
            home_team_id = self._normalize_team_id(game.get('HomeTeamID') or game.get('HomeTeam'))
            away_team_id = self._normalize_team_id(game.get('AwayTeamID') or game.get('AwayTeam'))
            team_id_norm = self._normalize_team_id(team_id)
            home_score = game.get('HomeTeamScore')
            away_score = game.get('AwayTeamScore')
            
            if home_score is None or away_score is None:
                continue
            
            if home_team_id == team_id_norm:
                point_diff = home_score - away_score
                if point_diff > 0:
                    wins += 1
            elif away_team_id == team_id_norm:
                point_diff = away_score - home_score
                if point_diff > 0:
                    wins += 1
            else:
                continue
            
            point_differential_sum += point_diff
        
        if len(recent_games) == 0:
            return 0.0
        
        # Win percentage
        win_pct = wins / len(recent_games)
        
        # Average point differential (normalized)
        avg_point_diff = point_differential_sum / len(recent_games) if recent_games else 0.0
        normalized_diff = np.tanh(avg_point_diff / 20.0)  # Normalize to [-1, 1]
        
        # Combine win percentage and point differential
        momentum = (win_pct * 0.6 + normalized_diff * 0.4)
        
        # Apply exponential decay for older games
        momentum *= config.MOMENTUM_DECAY
        
        return float(np.clip(momentum, -1.0, 1.0))
    
    def calculate_fatigue(self, team_id: int, games: List[Dict], current_date: datetime) -> float:
        """
        Calculate team fatigue based on games played recently and travel.
        
        Returns fatigue factor (0 to 1, where 1 is most fatigued).
        """
        fatigue = 0.0
        cutoff_date = current_date - timedelta(days=config.FATIGUE_WINDOW_DAYS)
        
        # Get recent games
        recent_games = []
        for game in games:
            game_date_str = game.get('DateTime', '')
            if not game_date_str:
                continue
            
            try:
                game_date = datetime.fromisoformat(game_date_str.replace('Z', '+00:00'))
                if game_date < current_date and game_date >= cutoff_date:
                    recent_games.append(game)
            except:
                continue
        
        # Count games in fatigue window
        game_count = len(recent_games)
        fatigue += game_count * config.FATIGUE_GAME_WEIGHT
        
        # Calculate rest days since last game
        if recent_games:
            last_game_date = max(
                datetime.fromisoformat(g.get('DateTime', '').replace('Z', '+00:00'))
                for g in recent_games if g.get('DateTime')
            )
            rest_days = (current_date.date() - last_game_date.date()).days
            # Reduce fatigue based on rest
            fatigue -= rest_days * config.REST_DECAY
        
        # Travel distance (simplified - would need venue data for accurate calculation)
        # For now, assume away games add travel fatigue
        away_games = sum(1 for g in recent_games 
                        if (g.get('AwayTeamID') == team_id or g.get('AwayTeam') == team_id))
        fatigue += away_games * config.FATIGUE_TRAVEL_WEIGHT
        
        return float(np.clip(fatigue, 0.0, 1.0))
    
    def calculate_health_status(self, team_id: int) -> float:
        """
        Calculate aggregate team health status based on player injuries.
        
        Returns health score (0 to 1, where 1 is fully healthy).
        """
        injuries = self.collector.get_player_injuries(team_id)
        
        if not injuries:
            return config.DEFAULT_HEALTH_STATUS
        
        # Count active injuries
        active_injuries = [i for i in injuries 
                          if i.get('Status') not in ['Active', 'Healthy', None]]
        
        # Simple model: reduce health based on number of injuries
        # More sophisticated model would weight by player importance
        injury_penalty = min(len(active_injuries) * 0.1, 0.5)  # Max 50% reduction
        
        health = 1.0 - injury_penalty
        return float(np.clip(health, 0.0, 1.0))
    
    def calculate_home_advantage(self, team_id: int, games: List[Dict]) -> float:
        """
        Calculate team-specific home court advantage.
        
        Returns home advantage in points.
        """
        home_games = []
        away_games = []
        
        team_id_norm = self._normalize_team_id(team_id)
        for game in games:
            home_team_id = self._normalize_team_id(game.get('HomeTeamID') or game.get('HomeTeam'))
            away_team_id = self._normalize_team_id(game.get('AwayTeamID') or game.get('AwayTeam'))
            home_score = game.get('HomeTeamScore')
            away_score = game.get('AwayTeamScore')
            
            if home_score is None or away_score is None:
                continue
            
            if home_team_id == team_id_norm:
                home_games.append(home_score - away_score)
            elif away_team_id == team_id_norm:
                away_games.append(away_score - home_score)
        
        if len(home_games) < 5 or len(away_games) < 5:
            return config.DEFAULT_HOME_ADVANTAGE
        
        # Calculate average point differential at home vs away
        avg_home_diff = np.mean(home_games)
        avg_away_diff = np.mean(away_games)
        
        home_advantage = avg_home_diff - avg_away_diff
        
        # Clamp to reasonable range
        return float(np.clip(home_advantage, 0.0, 10.0))
    
    def calculate_pace(self, team_id: int, games: List[Dict]) -> float:
        """
        Calculate team's preferred pace (possessions per game).
        
        Returns average possessions per game.
        """
        # Try to get from team stats first
        team_stats = self.collector.get_team_stats(team_id)
        if team_stats and 'Possessions' in team_stats:
            return float(team_stats['Possessions'])
        
        # Fallback: estimate from scores (simplified)
        # In reality, would need possession data
        total_points = []
        team_id_norm = self._normalize_team_id(team_id)
        for game in games:
            home_team_id = self._normalize_team_id(game.get('HomeTeamID') or game.get('HomeTeam'))
            away_team_id = self._normalize_team_id(game.get('AwayTeamID') or game.get('AwayTeam'))
            home_score = game.get('HomeTeamScore')
            away_score = game.get('AwayTeamScore')
            
            if home_score is None or away_score is None:
                continue
            
            if home_team_id == team_id_norm or away_team_id == team_id_norm:
                total_points.append(home_score + away_score)
        
        if total_points:
            # Rough estimate: pace ≈ total_points / 2 (very simplified)
            avg_total = np.mean(total_points)
            estimated_pace = avg_total / 2.0
            return float(np.clip(estimated_pace, 60.0, 80.0))
        
        return config.DEFAULT_PACE
    
    def get_game_features(self, game: Dict, team_id: int, is_home: bool, 
                         all_games: List[Dict], current_date: datetime) -> Dict:
        """
        Get all features for a team in a specific game context.
        
        Returns dictionary with all feature values.
        """
        return {
            'momentum': self.calculate_momentum(team_id, all_games, current_date),
            'fatigue': self.calculate_fatigue(team_id, all_games, current_date),
            'health_status': self.calculate_health_status(team_id),
            'home_advantage': self.calculate_home_advantage(team_id, all_games) if is_home else 0.0,
            'pace': self.calculate_pace(team_id, all_games)
        }


# Convenience function
def get_calculator(collector: Optional[DataCollector] = None) -> FeatureCalculator:
    """Get a FeatureCalculator instance."""
    return FeatureCalculator(collector)

