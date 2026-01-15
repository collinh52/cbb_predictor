"""
Shared utility helpers.
"""
from typing import Optional, Any


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

