"""
Shared utility helpers.
"""
from typing import Optional, Any, Dict


def normalize_team_id(team_id_or_name: Optional[Any]) -> Optional[int]:
    """Normalize team identifier to integer ID."""
    if team_id_or_name is None:
        return None

    if isinstance(team_id_or_name, int):
        return team_id_or_name

    if isinstance(team_id_or_name, str):
        try:
            return int(team_id_or_name)
        except ValueError:
            # Use hash for string names
            return abs(hash(team_id_or_name)) % 100000

    return None


def is_neutral_court(game: Dict) -> bool:
    """
    Detect if a game is played on a neutral court.

    Checks for:
    - Explicit neutral court flag
    - Tournament/classic keywords in game name
    - Location mismatch (home team playing away from home location)

    Args:
        game: Game dictionary

    Returns:
        True if neutral court, False otherwise
    """
    # Check explicit neutral flag
    if game.get('NeutralCourt') or game.get('neutral_site'):
        return True

    # Check for explicit false flag
    neutral_flag = game.get('NeutralCourt')
    if neutral_flag is False:  # Explicitly False
        return False

    # Tournament/event keywords indicating neutral court
    tournament_keywords = [
        'tournament', 'classic', 'invitational', 'championship',
        'bracket', 'showcase', 'challenge', 'shootout',
        'ncaa tournament', 'march madness', 'sweet 16',
        'elite 8', 'final four', 'finals'
    ]

    # Check game name/title
    game_name = str(game.get('name', '')).lower()
    if any(keyword in game_name for keyword in tournament_keywords):
        return True

    # Check event/tournament field
    event = str(game.get('event', '')).lower()
    tournament = str(game.get('tournament', '')).lower()
    if any(keyword in event for keyword in tournament_keywords):
        return True
    if any(keyword in tournament for keyword in tournament_keywords):
        return True

    # Check location mismatch
    # If home team name not in venue/location, likely neutral
    home_team = str(game.get('HomeTeam', '')).lower()
    location = str(game.get('location', '')).lower()
    venue = str(game.get('venue', '')).lower()

    if home_team and location:
        # Remove common suffixes for matching
        home_clean = home_team.replace(' university', '').replace(' college', '').strip()
        # Check if home team city/name appears in location
        if home_clean and home_clean not in location and home_clean not in venue:
            # Likely neutral site (e.g., Duke playing "home" game at MSG)
            return True

    return False

