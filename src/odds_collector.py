"""
Collector for betting odds data from The Odds API.
"""
import requests
from datetime import datetime, timedelta
from typing import List, Dict, Optional
import json
from pathlib import Path

import config


class OddsCollector:
    """Collects betting odds from The Odds API."""
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or config.THE_ODDS_API_KEY
        self.base_url = config.THE_ODDS_API_BASE_URL
        self.sport = "basketball_ncaab"
        
        if not self.api_key:
            print("Warning: THE_ODDS_API_KEY not set. Odds data will not be available.")
    
    def get_ncaab_odds(self, regions: str = "us", markets: str = "spreads,totals") -> List[Dict]:
        """
        Fetch current NCAAB betting odds.
        
        Args:
            regions: Comma-separated regions (e.g., 'us', 'uk', 'eu')
            markets: Comma-separated markets (e.g., 'spreads', 'totals', 'h2h')
        
        Returns:
            List of games with odds data
        """
        if not self.api_key:
            print("THE_ODDS_API_KEY not configured. Cannot fetch odds.")
            return []
        
        endpoint = f"{self.base_url}/sports/{self.sport}/odds"
        params = {
            'apiKey': self.api_key,
            'regions': regions,
            'markets': markets,
            'oddsFormat': 'american',
            'dateFormat': 'iso'
        }
        
        try:
            response = requests.get(endpoint, params=params, timeout=10)
            response.raise_for_status()
            
            # Check remaining quota
            remaining = response.headers.get('x-requests-remaining')
            used = response.headers.get('x-requests-used')
            if remaining:
                print(f"The Odds API - Requests remaining: {remaining}, used: {used}")
            
            return response.json()
        except requests.exceptions.HTTPError as e:
            print(f"The Odds API request failed: {e.response.status_code} - {e.response.reason}")
            if e.response.status_code == 401:
                print("Unauthorized: Check your THE_ODDS_API_KEY")
            elif e.response.status_code == 429:
                print("Rate limit exceeded. Check your quota at https://the-odds-api.com/")
            return []
        except requests.exceptions.RequestException as e:
            print(f"The Odds API request failed: {e}")
            return []
    
    def get_game_odds(self, home_team: str, away_team: str, all_odds: Optional[List[Dict]] = None) -> Dict:
        """
        Get odds for a specific game by team names.
        
        Args:
            home_team: Home team name or abbreviation
            away_team: Away team name or abbreviation
            all_odds: Pre-fetched odds data (optional, will fetch if not provided)
        
        Returns:
            Dictionary with spread and total, or None values if not found
        """
        if all_odds is None:
            all_odds = self.get_ncaab_odds()
        
        # Try to find the game by team names
        for game in all_odds:
            home = game.get('home_team', '')
            away = game.get('away_team', '')
            
            # Flexible matching (case-insensitive, partial match)
            if (home_team.lower() in home.lower() or home.lower() in home_team.lower()) and \
               (away_team.lower() in away.lower() or away.lower() in away_team.lower()):
                
                # Extract spread and total from bookmakers
                spread = self._extract_spread(game, home_team)
                total = self._extract_total(game)
                
                return {
                    'spread': spread,
                    'total': total,
                    'home_team': home,
                    'away_team': away,
                    'commence_time': game.get('commence_time')
                }
        
        return {'spread': None, 'total': None}
    
    def _extract_spread(self, game: Dict, home_team: str) -> Optional[float]:
        """Extract spread from bookmakers data (home team perspective)."""
        bookmakers = game.get('bookmakers', [])
        
        if not bookmakers:
            return None
        
        # Use first available bookmaker
        for bookmaker in bookmakers:
            markets = bookmaker.get('markets', [])
            for market in markets:
                if market.get('key') == 'spreads':
                    outcomes = market.get('outcomes', [])
                    for outcome in outcomes:
                        # Find home team spread
                        if outcome.get('name', '').lower() in home_team.lower() or \
                           home_team.lower() in outcome.get('name', '').lower():
                            return float(outcome.get('point', 0))
        
        return None
    
    def _extract_total(self, game: Dict) -> Optional[float]:
        """Extract total (over/under) from bookmakers data."""
        bookmakers = game.get('bookmakers', [])
        
        if not bookmakers:
            return None
        
        # Use first available bookmaker
        for bookmaker in bookmakers:
            markets = bookmaker.get('markets', [])
            for market in markets:
                if market.get('key') == 'totals':
                    outcomes = market.get('outcomes', [])
                    # Get the Over line (they're the same for Over/Under)
                    for outcome in outcomes:
                        if outcome.get('name') == 'Over':
                            return float(outcome.get('point', 0))
        
        return None
    
    def match_odds_to_games(self, games: List[Dict]) -> List[Dict]:
        """
        Match odds data to a list of games and add spread/total to each game.
        
        Args:
            games: List of game dictionaries (from SportsDataIO or other source)
        
        Returns:
            List of games with odds data added
        """
        if not self.api_key:
            print("Warning: No Odds API key. Games will not have updated odds.")
            return games
        
        # Fetch all current odds
        all_odds = self.get_ncaab_odds()
        
        if not all_odds:
            print("Warning: Could not fetch odds data. Using existing game data.")
            return games
        
        # Import mapping
        from src.team_name_mapping import get_odds_api_name
        
        # Match odds to games
        matched_count = 0
        for game in games:
            # Get team abbreviations from SportsDataIO
            home_abbr = game.get('HomeTeam', '')
            away_abbr = game.get('AwayTeam', '')
            
            if not home_abbr or not away_abbr:
                continue
            
            # Convert to Odds API names using mapping
            home_odds_name = get_odds_api_name(home_abbr)
            away_odds_name = get_odds_api_name(away_abbr)
            
            # Try to find matching game in odds data
            odds = self.get_game_odds(home_odds_name, away_odds_name, all_odds)
            
            if odds['spread'] is not None:
                game['PointSpread'] = odds['spread']
                matched_count += 1
            
            if odds['total'] is not None:
                game['OverUnder'] = odds['total']
        
        print(f"Matched odds for {matched_count}/{len(games)} games from The Odds API")
        return games
    
    def get_sports_list(self) -> List[Dict]:
        """Get list of available sports (for testing/debugging)."""
        if not self.api_key:
            return []
        
        endpoint = f"{self.base_url}/sports"
        params = {'apiKey': self.api_key}
        
        try:
            response = requests.get(endpoint, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Failed to get sports list: {e}")
            return []


# Singleton pattern
_odds_collector: Optional[OddsCollector] = None

def get_odds_collector() -> OddsCollector:
    """Get or create the odds collector singleton."""
    global _odds_collector
    if _odds_collector is None:
        _odds_collector = OddsCollector()
    return _odds_collector

