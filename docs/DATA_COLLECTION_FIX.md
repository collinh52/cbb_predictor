# Data Collection Fix - Complete Season Coverage

## Problem Identified
The original ESPN data collection was using the **scoreboard endpoint**, which only returns ~9 featured games per day. This resulted in:
- Only **513 games** collected (vs 3,334+ actual games)
- Only **40 teams** with sufficient data
- Missing most D1 games

## Root Cause
ESPN's scoreboard API (`/scoreboard?dates=YYYYMMDD`) is designed for displaying daily highlights, not comprehensive data collection.

## Solution Implemented
Switched to using ESPN's **team schedule endpoint** to get complete coverage:

### New Approach
1. **Get all teams** via `/teams` endpoint → 362 D1 teams
2. **Fetch each team's schedule** via `/teams/{team_id}/schedule?season=2026`
3. **Deduplicate games** by GameID (since each game appears in both teams' schedules)

### Code Changes

#### `src/espn_collector.py`
Added three new methods:
- `get_all_teams()` - Fetches list of all 362 D1 teams
- `get_team_schedule(team_id, season)` - Gets full schedule for one team
- `get_all_games_via_team_schedules(season)` - Orchestrates collection from all teams

Also fixed score parsing:
- ESPN returns scores as dicts: `{'value': 75.0, 'displayValue': '75'}`
- Updated parser to handle both dict and direct value formats

#### `show_team_ratings.py`
Changed from:
```python
historical_games = espn.get_games_for_season(year=2025, start_date=..., end_date=...)
```

To:
```python
historical_games = espn.get_all_games_via_team_schedules(season=2026)
```

#### `predict_today.py`
Same change as above.

## Results

### Before Fix
- **513 games** collected
- **40 teams** with 5+ games
- Missing most games for major programs

### After Fix
- **5,889 total games** found (3,334 completed)
- **372 teams** with 5+ games
- Complete coverage of all D1 games

### Performance
- Takes ~1-2 minutes to fetch all data
- Rate limited to 0.15s per team (362 teams × 0.15s ≈ 54 seconds)
- Deduplicates automatically by GameID

## Validation
Top teams now correctly show:
1. Michigan (14-1)
2. High Point (16-3)
3. Saint Louis (15-1)
4. Iowa State (16-0) - undefeated!
5. Gonzaga (17-1)
6. Arizona (16-0) - undefeated!

All major programs have correct 15-17 game records, matching real season progress.

## API Endpoints Used

### Teams List
```
GET https://site.api.espn.com/apis/site/v2/sports/basketball/mens-college-basketball/teams?limit=500
```

Returns:
```json
{
  "sports": [{
    "leagues": [{
      "teams": [
        {"team": {"id": 150, "displayName": "Duke Blue Devils", ...}},
        ...
      ]
    }]
  }]
}
```

### Team Schedule
```
GET https://site.api.espn.com/apis/site/v2/sports/basketball/mens-college-basketball/teams/{team_id}/schedule?season=2026
```

Returns:
```json
{
  "events": [
    {
      "id": "401817228",
      "name": "Texas Longhorns at Duke Blue Devils",
      "date": "2025-11-05T01:45Z",
      "competitions": [{
        "competitors": [
          {"team": {...}, "score": {"value": 75.0, "displayValue": "75"}},
          {"team": {...}, "score": {"value": 60.0, "displayValue": "60"}}
        ]
      }]
    },
    ...
  ]
}
```

## Future Improvements
- Cache team schedules to avoid re-fetching
- Implement incremental updates (only fetch new games)
- Add parallel requests for faster collection (with rate limiting)

