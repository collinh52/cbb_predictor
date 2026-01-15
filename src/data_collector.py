"""
Data collection module for fetching college basketball game data from APIs.
"""
import os
import json
import time
import csv
import re
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
        self._kenpom_cache: Dict[int, Dict[str, Dict]] = {}
        
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

    def _normalize_team_name(self, team_name: Optional[str]) -> str:
        """Normalize team name for matching across datasets."""
        if not team_name:
            return ""
        normalized = team_name.lower().strip()
        normalized = normalized.replace("&", "and")
        normalized = normalized.replace("st.", "saint")
        normalized = normalized.replace("st ", "saint ")
        normalized = re.sub(r"[^a-z0-9\s]", "", normalized)
        normalized = re.sub(r"\s+", " ", normalized).strip()
        return normalized

    def _parse_float(self, value: Optional[Any]) -> Optional[float]:
        """Parse a float value that may include rankings or extra text."""
        if value is None:
            return None
        if isinstance(value, (int, float)):
            return float(value)
        match = re.search(r"-?\d+(?:\.\d+)?", str(value))
        return float(match.group(0)) if match else None

    def _default_kenpom_rating(self) -> Dict[str, float]:
        """Default KenPom ratings when data is missing."""
        return {
            'adj_em': float(config.KENPOM_DEFAULT_ADJ_EM),
            'adj_o': float(config.KENPOM_DEFAULT_ADJ_O),
            'adj_d': float(config.KENPOM_DEFAULT_ADJ_D),
            'adj_t': float(config.KENPOM_DEFAULT_ADJ_T)
        }

    def _get_kenpom_summary_paths(self, season: int) -> List[Path]:
        """Get candidate KenPom summary file paths for a season."""
        season_short = f"{season % 100:02d}"
        candidates = []
        candidates.append(Path(config.DATA_DIR) / config.KENPOM_SUMMARY_PATTERN.format(season=season))
        candidates.append(Path(config.DATA_DIR) / f"summary{season_short}.csv")
        return candidates

    def _build_kenpom_url(self, season: int) -> Optional[str]:
        """Build a KenPom download URL for a season."""
        base_url = os.getenv("KENPOM_SUMMARY_URL")
        if not base_url:
            return None
        season_short = f"{season % 100:02d}"
        if "{season_short}" in base_url:
            return base_url.replace("{season_short}", season_short)
        if "{season}" in base_url:
            return base_url.replace("{season}", season_short)
        return re.sub(r"summary\d+", f"summary{season_short}", base_url)

    def _get_kenpom_cookie(self) -> Optional[str]:
        """Get a KenPom cookie from env or by logging in with Playwright."""
        kenpom_cookie = os.getenv("KENPOM_COOKIE")
        if kenpom_cookie:
            return kenpom_cookie

        username = os.getenv("KENPOM_USERNAME")
        password = os.getenv("KENPOM_PASSWORD")
        if not username or not password:
            return None

        try:
            from playwright.sync_api import sync_playwright
        except Exception:
            print("Playwright not available; cannot log in to KenPom.")
            return None

        def _fill_first(page, selectors: List[str], value: str) -> bool:
            for selector in selectors:
                locator = page.locator(selector)
                if locator.count() > 0:
                    locator.first.fill(value)
                    return True
            return False

        try:
            with sync_playwright() as p:
                browser = p.chromium.launch(headless=True)
                context = browser.new_context()
                page = context.new_page()
                page.goto("https://kenpom.com/login.php", wait_until="domcontentloaded")

                if not _fill_first(page, ["input[name='email']", "input[name='username']",
                                          "input[name='user']", "input[type='email']"], username):
                    print("Could not find KenPom username field.")
                    return None
                if not _fill_first(page, ["input[name='password']", "input[type='password']"], password):
                    print("Could not find KenPom password field.")
                    return None

                submitted = False
                for selector in ["input[type='submit']", "button[type='submit']",
                                 "input[value*='Login']", "button:has-text('Login')"]:
                    locator = page.locator(selector)
                    if locator.count() > 0:
                        locator.first.click()
                        submitted = True
                        break
                if not submitted:
                    page.keyboard.press("Enter")

                try:
                    page.wait_for_load_state("networkidle", timeout=15000)
                except Exception:
                    pass

                cookies = context.cookies("https://kenpom.com/")
                cookie_str = "; ".join([f"{cookie['name']}={cookie['value']}" for cookie in cookies])
                browser.close()
                return cookie_str or None
        except Exception as exc:
            print(f"KenPom login failed: {exc}")
            return None

    def _download_kenpom_summary(self, season: int, target_paths: List[Path]) -> bool:
        """Download KenPom summary CSV for a season."""
        url = self._build_kenpom_url(season)
        if not url:
            return False

        headers = {
            "User-Agent": "Mozilla/5.0",
            "Referer": "https://kenpom.com/",
        }
        kenpom_cookie = self._get_kenpom_cookie()
        if kenpom_cookie:
            headers["Cookie"] = kenpom_cookie

        try:
            response = requests.get(url, headers=headers, timeout=20)
            response.raise_for_status()
        except requests.exceptions.RequestException:
            return False

        for path in target_paths:
            path.parent.mkdir(parents=True, exist_ok=True)
            with open(path, "wb") as f:
                f.write(response.content)
        return True

    def get_kenpom_ratings(self, season: Optional[int] = None) -> Dict[str, Dict[str, float]]:
        """
        Load KenPom ratings from local summary CSV.
        
        Returns a dict keyed by normalized team name.
        """
        season = season or config.CURRENT_SEASON
        if season in self._kenpom_cache:
            return self._kenpom_cache[season]['normalized']

        summary_paths = self._get_kenpom_summary_paths(season)
        summary_path = next((path for path in summary_paths if path.exists()), None)
        if summary_path is None:
            if self._download_kenpom_summary(season, summary_paths):
                summary_path = next((path for path in summary_paths if path.exists()), None)
        if summary_path is None:
            self._kenpom_cache[season] = {'normalized': {}, 'original': {}}
            return {}

        ratings_by_normalized: Dict[str, Dict[str, float]] = {}
        ratings_by_original: Dict[str, Dict[str, float]] = {}

        try:
            with open(summary_path, 'r', newline='') as f:
                reader = csv.DictReader(f)
                if not reader.fieldnames:
                    self._kenpom_cache[season] = {'normalized': {}, 'original': {}}
                    return {}

                field_map = {field.lower(): field for field in reader.fieldnames}

                def _find_field(candidates: List[str]) -> Optional[str]:
                    for candidate in candidates:
                        field = field_map.get(candidate.lower())
                        if field:
                            return field
                    return None

                team_field = _find_field(['Team', 'TeamName', 'School', 'TEAM'])
                adj_em_field = _find_field(['AdjEM', 'AdjE', 'AdjEffMargin'])
                adj_o_field = _find_field(['AdjO', 'AdjOE', 'AdjOff'])
                adj_d_field = _find_field(['AdjD', 'AdjDE', 'AdjDef'])
                adj_t_field = _find_field(['AdjT', 'AdjTempo', 'AdjT.'])

                if not team_field:
                    self._kenpom_cache[season] = {'normalized': {}, 'original': {}}
                    return {}

                for row in reader:
                    team_name = row.get(team_field)
                    if not team_name:
                        continue

                    adj_em = self._parse_float(row.get(adj_em_field)) if adj_em_field else None
                    adj_o = self._parse_float(row.get(adj_o_field)) if adj_o_field else None
                    adj_d = self._parse_float(row.get(adj_d_field)) if adj_d_field else None
                    adj_t = self._parse_float(row.get(adj_t_field)) if adj_t_field else None

                    if adj_em is None and adj_o is not None and adj_d is not None:
                        adj_em = adj_o - adj_d

                    rating = {
                        'adj_em': float(adj_em) if adj_em is not None else float(config.KENPOM_DEFAULT_ADJ_EM),
                        'adj_o': float(adj_o) if adj_o is not None else float(config.KENPOM_DEFAULT_ADJ_O),
                        'adj_d': float(adj_d) if adj_d is not None else float(config.KENPOM_DEFAULT_ADJ_D),
                        'adj_t': float(adj_t) if adj_t is not None else float(config.KENPOM_DEFAULT_ADJ_T)
                    }

                    normalized_name = self._normalize_team_name(team_name)
                    ratings_by_normalized[normalized_name] = rating
                    ratings_by_original[team_name] = rating
        except Exception:
            self._kenpom_cache[season] = {'normalized': {}, 'original': {}}
            return {}

        self._kenpom_cache[season] = {
            'normalized': ratings_by_normalized,
            'original': ratings_by_original
        }
        return ratings_by_normalized

    def get_kenpom_team_rating(self, team_name: Optional[str], season: Optional[int] = None) -> Dict[str, float]:
        """Get KenPom ratings for a single team."""
        season = season or config.CURRENT_SEASON
        ratings_by_normalized = self.get_kenpom_ratings(season)
        if not team_name:
            return self._default_kenpom_rating()

        normalized_name = self._normalize_team_name(team_name)
        rating = ratings_by_normalized.get(normalized_name)
        if rating:
            return rating

        cached_original = self._kenpom_cache.get(season, {}).get('original', {})
        if cached_original:
            from src.team_name_mapping import fuzzy_match_team
            match = fuzzy_match_team(team_name, list(cached_original.keys()),
                                     threshold=config.KENPOM_FUZZY_MATCH_THRESHOLD)
            if match:
                return cached_original.get(match, self._default_kenpom_rating())

        return self._default_kenpom_rating()
    
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
            # Use the more comprehensive team schedule method
            games = espn.get_all_games_via_team_schedules(season=season)
            completed = []
            for g in games:
                status = str(g.get('Status', '')).upper()
                has_scores = g.get('HomeTeamScore') is not None and g.get('AwayTeamScore') is not None
                is_final_status = status.endswith('FINAL') or status == 'STATUS_FINAL'
                if g.get('IsClosed') or is_final_status or has_scores:
                    if has_scores:
                        completed.append(g)
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

