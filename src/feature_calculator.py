"""
Feature calculation module for computing momentum, fatigue, health status, and home advantage.
"""
from datetime import datetime, timedelta
from typing import List, Dict, Optional
import numpy as np

import config
from src.data_collector import DataCollector
from src.utils import normalize_team_id


class FeatureCalculator:
    """Calculates derived features from game data."""

    def __init__(self, collector: Optional[DataCollector] = None):
        self.collector = collector or DataCollector()
        # Feature cache: {team_id: {'features': dict, 'valid_until': datetime, 'last_game_count': int}}
        self._feature_cache: Dict[int, Dict] = {}
        self._cache_hits = 0
        self._cache_misses = 0
    
    def _normalize_team_id(self, team_id_or_name) -> Optional[int]:
        """Normalize team identifier to integer ID."""
        return normalize_team_id(team_id_or_name)
    
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

        # Calculate weighted momentum with exponential decay per game
        # More recent games get higher weight
        team_id_norm = self._normalize_team_id(team_id)
        weighted_wins = 0.0
        weighted_point_diff = 0.0
        total_weight = 0.0

        for i, game in enumerate(recent_games):
            # Exponential decay: most recent = 1.0, then 0.85, 0.7225, etc.
            weight = config.MOMENTUM_DECAY ** i

            home_team_id = self._normalize_team_id(game.get('HomeTeamID') or game.get('HomeTeam'))
            away_team_id = self._normalize_team_id(game.get('AwayTeamID') or game.get('AwayTeam'))
            home_score = game.get('HomeTeamScore')
            away_score = game.get('AwayTeamScore')

            if home_score is None or away_score is None:
                continue

            if home_team_id == team_id_norm:
                point_diff = home_score - away_score
                won = 1.0 if point_diff > 0 else 0.0
            elif away_team_id == team_id_norm:
                point_diff = away_score - home_score
                won = 1.0 if point_diff > 0 else 0.0
            else:
                continue

            weighted_wins += won * weight
            weighted_point_diff += point_diff * weight
            total_weight += weight

        if total_weight == 0.0:
            return 0.0

        # Calculate weighted averages
        win_pct = weighted_wins / total_weight
        avg_point_diff = weighted_point_diff / total_weight
        normalized_diff = np.tanh(avg_point_diff / 20.0)  # Normalize to [-1, 1]

        # Combine win percentage and point differential
        momentum = (win_pct * 0.6 + normalized_diff * 0.4)
        
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

        # Try to get from KenPom (most reliable source)
        kenpom_data = self.collector.get_kenpom_ratings()
        team_id_norm = self._normalize_team_id(team_id)
        if team_id_norm in kenpom_data:
            adj_t = kenpom_data[team_id_norm].get('adj_t')
            # Only use if it's not the default value (70.0)
            if adj_t is not None and adj_t != config.KENPOM_DEFAULT_ADJ_T:
                return float(np.clip(adj_t, 60.0, 80.0))

        # Fallback: estimate from team's average scoring
        # This is a rough approximation assuming ~1.0 points per possession
        team_points = []
        for game in games:
            home_team_id = self._normalize_team_id(game.get('HomeTeamID') or game.get('HomeTeam'))
            away_team_id = self._normalize_team_id(game.get('AwayTeamID') or game.get('AwayTeam'))
            home_score = game.get('HomeTeamScore')
            away_score = game.get('AwayTeamScore')

            if home_score is None or away_score is None:
                continue

            # Only collect the team's own scores
            if home_team_id == team_id_norm:
                team_points.append(home_score)
            elif away_team_id == team_id_norm:
                team_points.append(away_score)

        if team_points and len(team_points) >= 3:
            # Estimate pace as: team's average points / estimated efficiency
            # College basketball efficiency ~0.95-1.05 PPP, assume 1.0 for neutral estimate
            avg_points = np.mean(team_points)
            ASSUMED_EFFICIENCY = 1.0  # points per possession
            estimated_pace = avg_points / ASSUMED_EFFICIENCY
            return float(np.clip(estimated_pace, 60.0, 80.0))

        return config.DEFAULT_PACE

    def calculate_sos(self, team_id: int, games: List[Dict],
                     team_ratings: Optional[Dict[int, float]] = None) -> float:
        """
        Calculate Strength of Schedule (SOS) for a team.

        SOS is the average rating of all opponents faced.
        Positive SOS = tough schedule, Negative SOS = weak schedule.

        Args:
            team_id: Team to calculate SOS for
            games: All games to analyze
            team_ratings: Dict mapping team_id to rating (offensive - defensive)

        Returns:
            Average opponent rating (0.0 if no data)
        """
        if not team_ratings:
            return 0.0

        team_id_norm = self._normalize_team_id(team_id)
        opponent_ratings = []

        for game in games:
            if game.get('Status') != 'Final':
                continue

            home_id = self._normalize_team_id(game.get('HomeTeamID') or game.get('HomeTeam'))
            away_id = self._normalize_team_id(game.get('AwayTeamID') or game.get('AwayTeam'))

            # Identify opponent
            opponent_id = None
            if home_id == team_id_norm:
                opponent_id = away_id
            elif away_id == team_id_norm:
                opponent_id = home_id
            else:
                continue

            # Get opponent rating
            if opponent_id and opponent_id in team_ratings:
                opponent_ratings.append(team_ratings[opponent_id])

        if opponent_ratings:
            return float(np.mean(opponent_ratings))

        return 0.0

    def get_game_features(self, game: Dict, team_id: int, is_home: bool,
                         all_games: List[Dict], current_date: datetime,
                         team_name: Optional[str] = None,
                         team_ratings: Optional[Dict[int, float]] = None) -> Dict:
        """
        Get all features for a team in a specific game context.
        Uses caching to avoid recalculating features unnecessarily.

        Args:
            game: Game dictionary
            team_id: Team identifier
            is_home: Whether team is home
            all_games: All games for context
            current_date: Current date for time-based features
            team_name: Team name (optional)
            team_ratings: Dict of team_id -> rating for SOS calculation (optional)

        Returns dictionary with all feature values.
        """
        if team_name is None:
            team_name = (game.get('HomeTeam') or game.get('HomeTeamName')) if is_home else (
                game.get('AwayTeam') or game.get('AwayTeamName')
            )

        # Create cache key that includes game context
        team_id_norm = self._normalize_team_id(team_id)
        if team_id_norm is None:
            team_id_norm = team_id

        # Check cache validity
        cache_key = team_id_norm
        current_game_count = len(all_games)

        if cache_key in self._feature_cache:
            cached = self._feature_cache[cache_key]
            cached_game_count = cached.get('last_game_count', 0)
            cached_date = cached.get('valid_until')

            # Cache is valid if:
            # 1. Same or fewer games (no new results)
            # 2. Current date is before cached validity date
            if (cached_game_count == current_game_count and
                cached_date and current_date <= cached_date):
                self._cache_hits += 1
                # Return cached features, but update home_advantage for context
                features = cached['features'].copy()
                features['home_advantage'] = (self.calculate_home_advantage(team_id, all_games)
                                             if is_home else 0.0)
                return features

        # Cache miss - calculate features
        self._cache_misses += 1

        kenpom = self.collector.get_kenpom_team_rating(team_name)

        features = {
            'momentum': self.calculate_momentum(team_id, all_games, current_date),
            'fatigue': self.calculate_fatigue(team_id, all_games, current_date),
            'health_status': self.calculate_health_status(team_id),
            'home_advantage': self.calculate_home_advantage(team_id, all_games) if is_home else 0.0,
            'pace': self.calculate_pace(team_id, all_games),
            'kenpom_adj_em': kenpom['adj_em'],
            'kenpom_adj_o': kenpom['adj_o'],
            'kenpom_adj_d': kenpom['adj_d'],
            'kenpom_adj_t': kenpom['adj_t'],
            'sos': self.calculate_sos(team_id, all_games, team_ratings) if team_ratings else 0.0,
            # Four Factors from KenPom
            'efg_o': kenpom.get('efg_o', 50.0),
            'efg_d': kenpom.get('efg_d', 50.0),
            'tov_o': kenpom.get('tov_o', 20.0),
            'tov_d': kenpom.get('tov_d', 20.0),
            'oreb_pct': kenpom.get('oreb_pct', 30.0),
            'ft_rate': kenpom.get('ft_rate', 35.0)
        }

        # Cache the calculated features (valid until next game)
        self._feature_cache[cache_key] = {
            'features': features.copy(),
            'valid_until': current_date + timedelta(days=1),  # Valid for 1 day
            'last_game_count': current_game_count
        }

        return features

    def invalidate_cache(self, team_id: Optional[int] = None):
        """
        Invalidate feature cache for a specific team or all teams.

        Args:
            team_id: If provided, only invalidate this team. If None, clear all cache.
        """
        if team_id is None:
            self._feature_cache.clear()
        else:
            team_id_norm = self._normalize_team_id(team_id)
            if team_id_norm in self._feature_cache:
                del self._feature_cache[team_id_norm]

    def get_cache_stats(self) -> Dict[str, int]:
        """
        Get cache performance statistics.

        Returns:
            Dictionary with cache hits, misses, and hit rate.
        """
        total = self._cache_hits + self._cache_misses
        hit_rate = (self._cache_hits / total * 100) if total > 0 else 0.0

        return {
            'hits': self._cache_hits,
            'misses': self._cache_misses,
            'hit_rate': hit_rate,
            'cached_teams': len(self._feature_cache)
        }


# Convenience function
def get_calculator(collector: Optional[DataCollector] = None) -> FeatureCalculator:
    """Get a FeatureCalculator instance."""
    return FeatureCalculator(collector)

