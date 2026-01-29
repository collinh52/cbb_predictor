"""
ESPN API collector for real college basketball game data.
ESPN's hidden API is free and provides comprehensive game data.
"""
import requests
from datetime import datetime, timedelta
from typing import List, Dict, Optional
import time

from src.http_session import get_shared_session

class ESPNCollector:
    """Collects college basketball data from ESPN's hidden API."""

    def __init__(self):
        self.base_url = "https://site.api.espn.com/apis/site/v2/sports/basketball/mens-college-basketball"
        # Use shared session for connection pooling
        self.session = get_shared_session()
    
    def get_scoreboard(self, date: Optional[str] = None) -> Dict:
        """
        Get scoreboard for a specific date.
        
        Args:
            date: Date in YYYYMMDD format (e.g., '20260112'). Defaults to today.
        
        Returns:
            Scoreboard data including games, scores, and odds
        """
        if date is None:
            date = datetime.now().strftime('%Y%m%d')
        
        url = f"{self.base_url}/scoreboard"
        params = {'dates': date}
        
        try:
            response = self.session.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"ESPN API request failed: {e}")
            return {}
    
    def get_games_for_date(self, date: datetime) -> List[Dict]:
        """
        Get all games for a specific date.
        
        Args:
            date: datetime object for the target date
        
        Returns:
            List of game dictionaries
        """
        date_str = date.strftime('%Y%m%d')
        scoreboard = self.get_scoreboard(date_str)
        
        if not scoreboard or 'events' not in scoreboard:
            return []
        
        games = []
        for event in scoreboard.get('events', []):
            game = self._parse_event(event)
            if game:
                games.append(game)
        
        return games
    
    def get_games_for_season(self, year: int = 2026, start_date: Optional[datetime] = None, 
                            end_date: Optional[datetime] = None, limit: Optional[int] = None) -> List[Dict]:
        """
        Get games for a season range.
        
        Args:
            year: Season year (e.g., 2026)
            start_date: Start date (defaults to Nov 1)
            end_date: End date (defaults to Apr 15)
            limit: Maximum number of games to fetch
        
        Returns:
            List of game dictionaries
        """
        if start_date is None:
            start_date = datetime(year, 11, 1)
        if end_date is None:
            end_date = datetime(year + 1, 4, 15)
        
        # Limit to avoid too many requests
        if end_date > datetime.now():
            end_date = datetime.now()
        
        all_games = []
        current_date = start_date
        
        print(f"Fetching games from {start_date.date()} to {end_date.date()}...")
        
        while current_date <= end_date:
            if limit and len(all_games) >= limit:
                break
            
            # Fetch games for this date
            games = self.get_games_for_date(current_date)
            all_games.extend(games)
            
            # Progress update every 7 days
            if (current_date - start_date).days % 7 == 0:
                print(f"  {current_date.date()}: Found {len(all_games)} games so far...")
            
            # Move to next day
            current_date += timedelta(days=1)
            
            # Rate limiting - be nice to ESPN
            time.sleep(0.1)
        
        print(f"✓ Total games found: {len(all_games)}")
        return all_games[:limit] if limit else all_games
    
    def _parse_event(self, event: Dict) -> Optional[Dict]:
        """Parse an ESPN event into our game format."""
        try:
            # Get basic info
            game_id = int(event.get('id', 0))
            game_date = event.get('date', '')
            status_type = event.get('status', {}).get('type', {})
            status = status_type.get('name', '')
            status_state = status_type.get('state', '')
            status_completed = status_type.get('completed', False)
            
            # Get competitions (usually just 1)
            competitions = event.get('competitions', [])
            if not competitions:
                return None
            
            comp = competitions[0]
            
            # Get teams
            competitors = comp.get('competitors', [])
            if len(competitors) != 2:
                return None
            
            # ESPN format: competitors[0] is usually home, competitors[1] is away
            home_comp = competitors[0] if competitors[0].get('homeAway') == 'home' else competitors[1]
            away_comp = competitors[1] if competitors[0].get('homeAway') == 'home' else competitors[0]
            
            # Get team info
            home_team = home_comp.get('team', {})
            away_team = away_comp.get('team', {})
            
            home_id = int(home_team.get('id', 0))
            away_id = int(away_team.get('id', 0))
            home_name = home_team.get('displayName', '')
            away_name = away_team.get('displayName', '')
            home_abbr = home_team.get('abbreviation', '')
            away_abbr = away_team.get('abbreviation', '')
            
            # Get scores (handle both dict and direct value formats)
            home_score_raw = home_comp.get('score')
            away_score_raw = away_comp.get('score')
            
            # Parse scores - can be dict with 'value' key or direct value
            home_score = None
            away_score = None
            
            if home_score_raw is not None:
                if isinstance(home_score_raw, dict):
                    home_score = int(float(home_score_raw.get('value', 0)))
                else:
                    try:
                        home_score = int(home_score_raw)
                    except (ValueError, TypeError):
                        pass
            
            if away_score_raw is not None:
                if isinstance(away_score_raw, dict):
                    away_score = int(float(away_score_raw.get('value', 0)))
                else:
                    try:
                        away_score = int(away_score_raw)
                    except (ValueError, TypeError):
                        pass
            
            # Get odds if available
            odds = comp.get('odds', [])
            spread = None
            over_under = None
            
            if odds:
                spread = odds[0].get('spread')
                over_under = odds[0].get('overUnder')
            
            # Build game dictionary
            status_upper = str(status).upper()
            is_closed = bool(status_completed) or status_state == 'post' or status_upper.endswith('FINAL')
            game = {
                'GameID': game_id,
                'DateTime': game_date,
                'Season': self._get_season_from_date(game_date),
                'SeasonType': 1,  # Regular season
                'Status': status,
                'HomeTeamID': home_id,
                'AwayTeamID': away_id,
                'HomeTeam': home_abbr,
                'AwayTeam': away_abbr,
                'HomeTeamName': home_name,
                'AwayTeamName': away_name,
                'HomeTeamScore': home_score,
                'AwayTeamScore': away_score,
                'PointSpread': spread,
                'OverUnder': over_under,
                'IsClosed': is_closed,
                'Updated': game_date
            }
            
            return game
            
        except Exception as e:
            print(f"Error parsing event: {e}")
            return None
    
    def _get_season_from_date(self, date_str: str) -> int:
        """Determine season year from date."""
        try:
            dt = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
            # Season year is the year of the spring semester
            # Nov-Dec games belong to next year's season
            if dt.month >= 11:
                return dt.year + 1
            else:
                return dt.year
        except:
            return datetime.now().year
    
    def get_all_teams(self) -> List[Dict]:
        """
        Get list of all college basketball teams.
        
        Returns:
            List of team dictionaries with id, name, etc.
        """
        url = f"{self.base_url}/teams"
        params = {'limit': 500}  # Get all teams
        
        try:
            response = self.session.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            # Navigate the nested structure
            sports = data.get('sports', [])
            if not sports:
                return []
            
            leagues = sports[0].get('leagues', [])
            if not leagues:
                return []
            
            teams_data = leagues[0].get('teams', [])
            
            teams = []
            for team_data in teams_data:
                team = team_data.get('team', {})
                teams.append({
                    'id': int(team.get('id', 0)),
                    'name': team.get('displayName', ''),
                    'abbreviation': team.get('abbreviation', ''),
                    'location': team.get('location', '')
                })
            
            return teams
        except requests.exceptions.RequestException as e:
            print(f"ESPN teams request failed: {e}")
            return []
    
    def get_team_schedule(self, team_id: int, season: int = 2026) -> List[Dict]:
        """
        Get schedule for a specific team.
        
        Args:
            team_id: ESPN team ID
            season: Season year
        
        Returns:
            List of games for the team
        """
        url = f"{self.base_url}/teams/{team_id}/schedule"
        params = {'season': season}
        
        try:
            response = self.session.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            games = []
            for event in data.get('events', []):
                game = self._parse_event(event)
                if game:
                    games.append(game)
            
            return games
        except requests.exceptions.RequestException as e:
            # Suppress 404s which are expected for invalid/inactive teams
            if hasattr(e, 'response') and e.response is not None and e.response.status_code == 404:
                # Silently ignore 404s (team doesn't exist or no schedule available)
                pass
            else:
                print(f"ESPN team schedule request failed for team {team_id}: {e}")
            return []
    
    def get_all_games_via_team_schedules(self, season: int = 2026) -> List[Dict]:
        """
        Get ALL games by fetching each team's schedule.
        This is more comprehensive than the scoreboard endpoint.
        
        Args:
            season: Season year (e.g., 2026)
        
        Returns:
            List of all unique games
        """
        print(f"Fetching all teams for {season} season...")
        teams = self.get_all_teams()
        print(f"✓ Found {len(teams)} teams")
        
        print(f"\nFetching schedules for all teams (this will take a few minutes)...")
        
        all_games = {}  # Use dict to deduplicate by GameID
        teams_processed = 0
        
        for i, team in enumerate(teams, 1):
            team_id = team['id']
            team_name = team['name']
            
            # Fetch this team's schedule
            games = self.get_team_schedule(team_id, season)
            
            # Add games to our collection (deduplicate by GameID)
            for game in games:
                game_id = game.get('GameID')
                if game_id and game_id not in all_games:
                    all_games[game_id] = game
            
            teams_processed += 1
            
            # Progress update every 50 teams
            if teams_processed % 50 == 0:
                print(f"  Processed {teams_processed}/{len(teams)} teams - {len(all_games)} unique games found")
            
            # Rate limiting - be nice to ESPN
            time.sleep(0.15)
        
        print(f"✓ Processed {teams_processed} teams")
        print(f"✓ Total unique games found: {len(all_games)}")
        
        return list(all_games.values())


# Singleton
_espn_collector: Optional[ESPNCollector] = None

def get_espn_collector() -> ESPNCollector:
    """Get or create the ESPN collector singleton."""
    global _espn_collector
    if _espn_collector is None:
        _espn_collector = ESPNCollector()
    return _espn_collector

