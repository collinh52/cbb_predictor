# API Quota Workaround Solutions

## Problem

When running `python scripts/predict_today.py`, you're hitting Sports Data IO API quota limits. The predictor fetches all completed games from ESPN (5894+ games across 362 teams), which requires many API calls.

## Root Cause

The data collector (`src/data_collector.py`) caches completed games but the cache expires after 60 minutes (config.py:58). When the cache expires, it refetches ALL games by calling ESPN's API 362 times (once per team).

---

## Solution 1: Increase Cache Expiry (EASIEST)

Completed games don't change, so you can cache them for much longer.

### Edit `config.py`

Change line 58:
```python
# OLD:
CACHE_EXPIRY_MINUTES: int = 60  # Cache game data for 1 hour

# NEW:
CACHE_EXPIRY_MINUTES: int = 1440  # Cache game data for 24 hours (1 day)
```

**Or even longer:**
```python
CACHE_EXPIRY_MINUTES: int = 10080  # Cache game data for 7 days (1 week)
```

**Why this works:**
- Completed games are immutable (final scores don't change)
- Only new games need to be fetched
- You can manually refresh the cache once a week by deleting the cache file

**Manual cache refresh (when needed):**
```bash
rm data/cache/completed_games_2026.json
python scripts/predict_today.py --days 1
```

---

## Solution 2: Use Only The Odds API (NO ESPN)

The Odds API provides all upcoming games with betting lines. You don't need ESPN for predictions.

### Edit `.env`

Comment out or remove the SportsDataIO key:
```bash
# BASKETBALL_API_KEY="ad95f949ce9543949364994b53a73b5f"  # DISABLED - quota exceeded
```

### Result

- Predictor will use cached historical data (still valid)
- No new API calls to ESPN
- Predictions will still work for upcoming games

---

## Solution 3: Disable ESPN API Completely

Force the system to use ONLY cached data, never make fresh API calls.

### Edit `config.py`

Add a new setting:
```python
# Near line 58, add:
USE_CACHED_DATA_ONLY: bool = True  # Never make API calls, use cache only
```

### Edit `src/data_collector.py` (line 500)

```python
# OLD (lines 500-503):
# Try cache first
cached = self._load_from_cache(cache_key)
if cached:
    return cached

# NEW:
# Try cache first
cached = self._load_from_cache(cache_key)
if cached:
    return cached

# If cache-only mode, return empty instead of making API calls
if getattr(config, 'USE_CACHED_DATA_ONLY', False):
    print(f"⚠️  Cache-only mode: No cached data for {cache_key}, returning empty")
    return []
```

**Caution:** This will only work if you have cached data. Make sure to run it once with API access to populate the cache first.

---

## Solution 4: Pre-populate Cache Once a Week (RECOMMENDED)

Instead of disabling the API, just refresh the cache less frequently.

### Weekly Cache Refresh Script

Create `scripts/refresh_cache.sh`:
```bash
#!/bin/bash
# Refresh historical game cache (run once a week)

echo "Deleting old cache..."
rm -f data/cache/completed_games_*.json

echo "Fetching fresh data from ESPN..."
python scripts/setup_and_train.py --populate 200 --train

echo "Cache refreshed! You can now run predictions for the week."
```

Make it executable:
```bash
chmod +x scripts/refresh_cache.sh
```

**Usage:**
```bash
# Run this once a week (or when you get quota errors)
./scripts/refresh_cache.sh

# Then run predictions as many times as you want (uses cache)
python scripts/predict_today.py --days 1
python scripts/predict_today.py --days 2
# ... etc
```

---

## Solution 5: Use ESPN Directly (FREE, NO API KEY)

ESPN's public API doesn't require authentication for most endpoints. You can use it directly without Sports Data IO.

### Already implemented!

Your code already uses ESPN via `src/espn_collector.py`. The issue is just the caching frequency.

**The Good News:**
- ESPN API is FREE and has no quota limits
- Your caching system already works
- You just need to cache longer (Solution 1)

**The Bad News:**
- ESPN can rate limit if you make too many requests too fast
- That's why there's a `time.sleep(0.15)` in the code (line 348 of espn_collector.py)

---

## Solution 6: Reduce Data Collection Frequency

Only fetch new games, not the entire season history.

### Current Behavior
- Fetches ALL 5894 games every time cache expires
- Uses 362 API calls (one per team)

### Better Approach

Modify the predictor to:
1. Load cached historical games
2. Only fetch games from the last 7 days
3. Merge new games into the cache

**This would require code changes to `src/data_collector.py`**

---

## Quick Fix Summary

**IMMEDIATE ACTION (choose one):**

### Option A: Extend cache to 7 days
Edit `config.py` line 58:
```python
CACHE_EXPIRY_MINUTES: int = 10080  # 7 days
```

### Option B: Use existing cache + update manually
```bash
# Check if cache exists and is recent
ls -lh data/cache/completed_games_2026.json

# If cache is less than a few days old, just use it
# Don't delete it, just run predictions
python scripts/predict_today.py --days 1
```

### Option C: Skip the problematic initialization
Create a lightweight prediction script that doesn't load all historical games:

**Create `scripts/predict_today_lite.py`:**
```python
#!/usr/bin/env python3
"""
Lightweight predictions using only The Odds API (no ESPN historical data).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.odds_collector import get_odds_collector
from src.ats_tracker import get_ats_tracker
from datetime import datetime

def main():
    odds_collector = get_odds_collector()
    ats_tracker = get_ats_tracker()

    print("🎰 Fetching games from The Odds API...")
    all_odds = odds_collector.get_ncaab_odds()

    if not all_odds:
        print("⚠️  No odds data available")
        return

    print(f"✓ Found {len(all_odds)} games with betting lines")

    # Just display the games and lines - no complex predictions
    for game in all_odds[:10]:  # Show first 10 games
        home = game.get('home_team', '')
        away = game.get('away_team', '')

        # Extract spread
        for bookmaker in game.get('bookmakers', []):
            for market in bookmaker.get('markets', []):
                if market.get('key') == 'spreads':
                    for outcome in market.get('outcomes', []):
                        if home.lower() in outcome.get('name', '').lower():
                            spread = outcome.get('point', 0)
                            print(f"{away} @ {home} | Line: {spread:+.1f}")
                            break
                    break
            break

if __name__ == "__main__":
    main()
```

Run it:
```bash
python scripts/predict_today_lite.py
```

This script ONLY uses The Odds API (which you have 276/500 requests remaining) and doesn't load ESPN data at all.

---

## Recommended Solution

**Best approach for your situation:**

1. **Extend cache to 1 week** (Solution 1)
   ```python
   # config.py line 58
   CACHE_EXPIRY_MINUTES: int = 10080
   ```

2. **Refresh cache weekly**
   ```bash
   # Every Sunday or Monday
   rm data/cache/completed_games_2026.json
   python scripts/setup_and_train.py --populate 200 --train
   ```

3. **Run predictions daily** (uses cache)
   ```bash
   python scripts/predict_today.py --days 1
   ```

This gives you:
- ✅ Full prediction accuracy (uses historical data)
- ✅ No daily API quota issues
- ✅ Weekly fresh data
- ✅ Simple to maintain

---

## Understanding Your APIs

### The Odds API (540557863d20eb2343252714e72300b9)
- **Quota:** 500 requests/month (you have 276 remaining)
- **Usage:** Fetching betting lines (spreads, totals)
- **Cost per call:** 1 request per call
- **Current usage:** ~224 calls this month
- **Status:** ✅ Plenty of quota remaining

### ESPN API (FREE)
- **Quota:** No official limit, but rate-limited
- **Usage:** Historical game scores, team schedules
- **Cost per call:** FREE but slow (362 calls to get all games)
- **Current issue:** Takes 5+ minutes to fetch all teams
- **Status:** ⚠️ Slow but functional

### Sports Data IO (BASKETBALL_API_KEY)
- **Quota:** Very limited on free tier
- **Usage:** Alternative to ESPN for game data
- **Status:** ❌ Quota exceeded (hence your error)
- **Solution:** Don't use it, use ESPN instead

---

## Testing Your Fix

After applying Solution 1 (extend cache):

```bash
# Check cache status
ls -lh data/cache/completed_games_2026.json

# Run prediction
python scripts/predict_today.py --days 1

# Should see:
# "✓ Retrieved 80 games with betting lines"  (The Odds API - no quota issue)
# No message about "Fetching completed games from ESPN" (using cache)

# If you see "Fetching schedules for all teams", the cache expired
# In that case, increase CACHE_EXPIRY_MINUTES even more
```

---

## Files to Modify

| File | Line | Change |
|------|------|--------|
| `config.py` | 58 | `CACHE_EXPIRY_MINUTES: int = 10080` |

That's it! One line change fixes the issue.
