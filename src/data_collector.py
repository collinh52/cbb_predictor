"""
Data collection module for fetching college basketball game data from APIs.
"""
import os
import json
import time
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Any
import requests
from pathlib import Path

import config


class DataCollector:
    """Collects college basketball game data from APIs."""
    
    def __init__(self):
        self.api_key = config.API_KEY
        self.base_url = config.API_BASE_URL
        self.cache_dir = Path(config.CACHE_DIR)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.cache_expiry = timedelta(minutes=config.CACHE_EXPIRY_MINUTES)
        
    def _get_cache_path(self, cache_key: str) -> Path:
        """Get path for cached data."""
        return self.cache_dir / f"{cache_key}.json"
    
    def _load_from_cache(self, cache_key: str) -> Optional[Dict]:
        """Load data from cache if not expired."""
        cache_path = self._get_cache_path(cache_key)
        if not cache_path.exists():
            return None
        
        try:
            with open(cache_path, 'r') as f:
                cached_data = json.load(f)
            
            # Check if cache is expired
            cache_time = datetime.fromisoformat(cached_data.get('timestamp', ''))
            if datetime.now() - cache_time > self.cache_expiry:
                return None
            
            return cached_data.get('data')
        except Exception:
            return None
    
    def _save_to_cache(self, cache_key: str, data: Dict):
        """Save data to cache."""
        cache_path = self._get_cache_path(cache_key)
        cache_data = {
            'timestamp': datetime.now().isoformat(),
            'data': data
        }
        with open(cache_path, 'w') as f:
            json.dump(cache_data, f, indent=2)
    
    def _make_api_request(self, endpoint: str, params: Optional[Dict] = None) -> Dict:
        """Make API request with error handling and rate limiting."""
        url = f"{self.base_url}/{endpoint}"
        headers = {}
        
        if self.api_key:
            headers['Ocp-Apim-Subscription-Key'] = self.api_key
        
        try:
            response = requests.get(url, headers=headers, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            if response.status_code == 401:
                error_data = response.json() if response.text else {}
                error_msg = error_data.get('Description', response.text)
                print(f"API authentication error: {error_msg}")
                if 'Unauthorized Season' in error_msg:
                    print(f"  Hint: Free trial may not have access to this season. Try updating CURRENT_SEASON in config.py")
            else:
                print(f"API request failed ({response.status_code}): {response.text[:200]}")
            # Return mock data structure for development
            return self._get_mock_data(endpoint)
        except requests.exceptions.RequestException as e:
            print(f"API request failed: {e}")
            # Return mock data structure for development
            return self._get_mock_data(endpoint)
    
    def _get_mock_data(self, endpoint: str) -> Dict:
        """Return mock data for development when API is unavailable."""
        # This allows development without API access
        if 'games' in endpoint.lower():
            return self._generate_mock_games()
        elif 'teams' in endpoint.lower():
            return self._generate_mock_teams()
        elif 'injuries' in endpoint.lower() or 'players' in endpoint.lower():
            return []
        else:
            return {}
    
    def _generate_mock_games(self) -> List[Dict]:
        """Generate mock game data for testing."""
        teams = ['Duke', 'North Carolina', 'Kentucky', 'Kansas', 'UCLA', 'Michigan State']
        games = []
        today = datetime.now()
        
        # Generate some completed games
        for i in range(20):
            game_date = today - timedelta(days=i % 7)
            home_team = teams[i % len(teams)]
            away_team = teams[(i + 1) % len(teams)]
            
            home_score = 70 + (i * 3) % 30
            away_score = 65 + (i * 5) % 30
            
            games.append({
                'GameID': 1000 + i,
                'DateTime': game_date.isoformat(),
                'HomeTeam': home_team,
                'AwayTeam': away_team,
                'HomeTeamScore': home_score,
                'AwayTeamScore': away_score,
                'Status': 'Final',
                'IsClosed': True,
                'Updated': game_date.isoformat()
            })
        
        # Generate today's games
        for i in range(5):
            home_team = teams[i % len(teams)]
            away_team = teams[(i + 2) % len(teams)]
            
            games.append({
                'GameID': 2000 + i,
                'DateTime': today.isoformat(),
                'HomeTeam': home_team,
                'AwayTeam': away_team,
                'HomeTeamScore': None,
                'AwayTeamScore': None,
                'Status': 'Scheduled',
                'IsClosed': False,
                'Updated': today.isoformat(),
                'PointSpread': -5.5 + (i * 2),
                'OverUnder': 140.0 + (i * 5)
            })
        
        return games
    
    def _generate_mock_teams(self) -> List[Dict]:
        """Generate mock team data."""
        teams = ['Duke', 'North Carolina', 'Kentucky', 'Kansas', 'UCLA', 'Michigan State']
        return [{'TeamID': i, 'Name': team, 'Key': team.upper().replace(' ', '')} 
                for i, team in enumerate(teams, 1)]
    
    def get_completed_games(self, season: Optional[int] = None) -> List[Dict]:
        """Fetch all completed games for the season."""
        season = season or config.CURRENT_SEASON
        cache_key = f"completed_games_{season}"
        
        # Try cache first
        cached = self._load_from_cache(cache_key)
        if cached:
            return cached
        
        # Use ESPN for historical data if configured (real data, not scrambled)
        if config.USE_ESPN_FOR_HISTORICAL:
            from src.espn_collector import get_espn_collector
            espn = get_espn_collector()
            print(f"Fetching completed games from ESPN for season {season}...")
            games = espn.get_games_for_season(year=season, limit=500)  # Limit to 500 for faster initialization
            completed = [g for g in games if g.get('IsClosed') and g.get('HomeTeamScore') is not None]
            self._save_to_cache(cache_key, completed)
            return completed
        
        # Fallback to SportsDataIO (scrambled data on free trial)
        endpoint = f"scores/json/Games/{season}"
        games = self._make_api_request(endpoint)
        
        if isinstance(games, list):
            # Filter for completed games
            completed = [g for g in games if g.get('Status') == 'Final' or g.get('IsClosed', False)]
            self._save_to_cache(cache_key, completed)
            return completed
        
        return []
    
    def get_upcoming_games(self, days_ahead: int = 7, use_odds_api: bool = True) -> List[Dict]:
        """
        Fetch upcoming games with pregame lines (PointSpread, OverUnder).
        
        Args:
            days_ahead: Number of days to look ahead
            use_odds_api: If True, fetch real betting lines from The Odds API
        """
        cache_key = f"upcoming_games_{days_ahead}"
        
        # Try cache first (shorter cache for lines that change)
        cached = self._load_from_cache(cache_key)
        if cached:
            upcoming = cached
        else:
            # Fetch from API
            endpoint = f"scores/json/Games/{config.CURRENT_SEASON}"
            all_games = self._make_api_request(endpoint)
            
            if isinstance(all_games, list):
                today = datetime.now().date()
                end_date = today + timedelta(days=days_ahead)
                
                upcoming = []
                for game in all_games:
                    game_date_str = game.get('DateTime', '')
                    if not game_date_str:
                        continue
                    
                    try:
                        game_date = datetime.fromisoformat(game_date_str.replace('Z', '+00:00')).date()
                        if today <= game_date <= end_date and game.get('Status') != 'Final':
                            # Ensure PointSpread and OverUnder are included (may be None if not available yet)
                            if 'PointSpread' not in game:
                                game['PointSpread'] = None
                            if 'OverUnder' not in game:
                                game['OverUnder'] = None
                            upcoming.append(game)
                    except:
                        continue
                
                # Cache with shorter expiry for pregame lines (15 minutes)
                self._save_to_cache(cache_key, upcoming)
            else:
                upcoming = []
        
        # Enhance with real odds from The Odds API if enabled
        if use_odds_api and upcoming:
            try:
                from src.odds_collector import get_odds_collector
                odds_collector = get_odds_collector()
                upcoming = odds_collector.match_odds_to_games(upcoming)
            except Exception as e:
                print(f"Warning: Could not fetch odds from The Odds API: {e}")
        
        return upcoming
    
    def get_pregame_lines(self, game_id: int) -> Dict:
        """Get pregame betting lines for a specific game."""
        game = self.get_game_details(game_id)
        if game:
            return {
                'spread': game.get('PointSpread'),
                'total': game.get('OverUnder'),
                'home_team_moneyline': game.get('HomeTeamMoneyLine'),
                'away_team_moneyline': game.get('AwayTeamMoneyLine')
            }
        return {'spread': None, 'total': None, 'home_team_moneyline': None, 'away_team_moneyline': None}
    
    def get_todays_games(self, use_odds_api: bool = True) -> List[Dict]:
        """
        Fetch today's games.
        
        Args:
            use_odds_api: If True, fetch real betting lines from The Odds API
        """
        cache_key = "todays_games"
        
        # Try cache first (shorter expiry for today's games)
        cached = self._load_from_cache(cache_key)
        if cached:
            todays_games = cached
        else:
            upcoming = self.get_upcoming_games(days_ahead=1, use_odds_api=False)  # Don't fetch odds twice
            today = datetime.now().date()
            
            todays_games = []
            for game in upcoming:
                game_date_str = game.get('DateTime', '')
                if not game_date_str:
                    continue
                
                try:
                    game_date = datetime.fromisoformat(game_date_str.replace('Z', '+00:00')).date()
                    if game_date == today:
                        todays_games.append(game)
                except:
                    continue
            
            self._save_to_cache(cache_key, todays_games)
        
        # Enhance with real odds from The Odds API if enabled
        if use_odds_api and todays_games:
            try:
                from src.odds_collector import get_odds_collector
                odds_collector = get_odds_collector()
                todays_games = odds_collector.match_odds_to_games(todays_games)
            except Exception as e:
                print(f"Warning: Could not fetch odds from The Odds API: {e}")
        
        return todays_games
    
    def get_team_stats(self, team_id: int, season: Optional[int] = None) -> Dict:
        """Fetch team statistics including pace."""
        season = season or config.CURRENT_SEASON
        cache_key = f"team_stats_{team_id}_{season}"
        
        # Try cache first
        cached = self._load_from_cache(cache_key)
        if cached:
            return cached
        
        # Fetch from API
        endpoint = f"stats/json/TeamSeasonStats/{season}"
        all_stats = self._make_api_request(endpoint)
        
        if isinstance(all_stats, list):
            team_stats = next((s for s in all_stats if s.get('TeamID') == team_id), {})
            if team_stats:
                self._save_to_cache(cache_key, team_stats)
            return team_stats
        
        # Return mock stats
        return {
            'TeamID': team_id,
            'Possessions': 70.0,  # Default pace
            'Points': 75.0,
            'OpponentPoints': 68.0
        }
    
    def get_player_injuries(self, team_id: Optional[int] = None) -> List[Dict]:
        """Fetch player injury data."""
        cache_key = f"injuries_{team_id or 'all'}"
        
        # Try cache first
        cached = self._load_from_cache(cache_key)
        if cached:
            return cached
        
        # Fetch from API
        endpoint = "scores/json/Injuries"
        injuries = self._make_api_request(endpoint)
        
        if isinstance(injuries, list):
            if team_id:
                injuries = [i for i in injuries if i.get('TeamID') == team_id]
            self._save_to_cache(cache_key, injuries)
            return injuries
        
        return []
    
    def get_game_details(self, game_id: int) -> Dict:
        """Fetch detailed information about a specific game."""
        cache_key = f"game_{game_id}"
        
        # Try cache first
        cached = self._load_from_cache(cache_key)
        if cached:
            return cached
        
        # Fetch from API
        endpoint = f"scores/json/Game/{game_id}"
        game = self._make_api_request(endpoint)
        
        if isinstance(game, dict):
            self._save_to_cache(cache_key, game)
            return game
        
        return {}
    
    def get_team_schedule(self, team_id: int, season: Optional[int] = None) -> List[Dict]:
        """Get team's schedule for calculating momentum and fatigue."""
        season = season or config.CURRENT_SEASON
        cache_key = f"schedule_{team_id}_{season}"
        
        # Try cache first
        cached = self._load_from_cache(cache_key)
        if cached:
            return cached
        
        # Fetch from API
        endpoint = f"scores/json/TeamGameStats/{season}/{team_id}"
        games = self._make_api_request(endpoint)
        
        if isinstance(games, list):
            self._save_to_cache(cache_key, games)
            return games
        
        return []


# Convenience function
def get_collector() -> DataCollector:
    """Get a DataCollector instance."""
    return DataCollector()

