# GitHub Actions Cache Strategy

## Overview

The GitHub Actions workflow automatically manages three types of cache to optimize performance and avoid API quota issues:

1. **Game Data Cache** (`data/cache/`) - Historical completed games
2. **ATS Tracking Data** - Predictions and accuracy stats
3. **ML Models** - Trained prediction models

## Game Data Cache (Weekly Refresh)

### How It Works

The completed games cache is refreshed **automatically every week** using a smart cache key:

```yaml
# Cache key format: game-cache-2026-W05
# Where W05 = ISO week number
key: game-cache-${{ steps.week.outputs.week }}
```

**Automatic Refresh Cycle:**
- Monday of Week 1: Cache key = `game-cache-2026-W05`
- Monday of Week 2: Cache key = `game-cache-2026-W06` (new cache, old one ignored)
- This aligns with the 7-day `CACHE_EXPIRY_MINUTES` in config.py

### Why Weekly Refresh?

- Completed games don't change (final scores are immutable)
- New games are added throughout the season, so weekly refresh keeps data current
- Avoids hitting ESPN API quota limits (362 calls to fetch all team schedules)
- Cache size: ~2 MB for 4,000+ games

### Jobs That Use Cache

#### 1. `collect-odds` Job (10 AM ET daily)
- **Loads cache:** Uses cached historical games for predictions
- **Does NOT refresh cache:** Just reads existing data
- **Runs:** `predict_today.py --days 2`

**Cache Flow:**
```
1. Restore cache: game-cache-2026-W05 (if available)
2. Check cache status (log only)
3. Run predictions using cached data
4. No cache update (read-only)
```

#### 2. `check-results` Job (11 PM ET daily)
- **Loads cache:** Uses cached historical games
- **REFRESHES cache:** Runs `setup_and_train.py --populate 200 --train`
- **Saves cache:** Updated cache saved with current week number

**Cache Flow:**
```
1. Restore cache: game-cache-2026-W05 (if available)
2. Check cache status before
3. Run check_results (verify old predictions)
4. Run setup_and_train --populate 200 --train
   └─> Fetches ALL completed games from ESPN (if cache expired or missing)
   └─> Saves to data/cache/completed_games_2026.json
5. Verify cache updated (log confirmation)
6. GitHub Actions auto-saves cache with key: game-cache-2026-W05
```

**Note:** GitHub Actions automatically saves cache at the end of a job if the cache directory has been modified.

#### 3. `update-readme-only` Job (manual trigger)
- **Loads cache:** Uses existing cache
- **Does NOT refresh:** Read-only operation

### Weekly Refresh Schedule

**Typical Week:**

| Day | collect-odds (10 AM ET) | check-results (11 PM ET) |
|-----|-------------------------|--------------------------|
| Mon | Use cache W05 | Use cache W05, train model |
| Tue | Use cache W05 | Use cache W05, train model |
| Wed | Use cache W05 | Use cache W05, train model |
| Thu | Use cache W05 | Use cache W05, train model |
| Fri | Use cache W05 | Use cache W05, train model |
| Sat | Use cache W05 | Use cache W05, train model |
| Sun | Use cache W05 | Use cache W05, train model |

**New Week Starts:**

| Day | collect-odds (10 AM ET) | check-results (11 PM ET) |
|-----|-------------------------|--------------------------|
| Mon | Cache miss → Fetch fresh (W06) | Train model, cache as W06 |
| Tue | Use cache W06 | Use cache W06, train model |
| ... | ... | ... |

**First run of the week:** Cache key changes from W05 to W06, causing cache miss. The `setup_and_train.py` script will fetch fresh data from ESPN.

**Rest of the week:** All jobs use the W06 cache.

---

## ATS Tracking Data (Every Run)

### How It Works

```yaml
key: ats-data-${{ github.run_number }}
restore-keys: ats-data-
```

- Uses `github.run_number` which increments every workflow run
- Always creates a new cache but restores from most recent previous run
- Captures prediction accuracy tracking between runs

### Files Cached

- `data/ats_tracking.json` - All predictions with outcomes
- `data/ats_accuracy.json` - Accuracy statistics
- `data/predictions.json` - Recent predictions
- `data/results.json` - Game results

---

## ML Models Cache (Every Run)

### How It Works

```yaml
key: ml-models-${{ github.run_number }}
restore-keys: ml-models-
```

- Similar to ATS data: new key per run, restore from previous
- Updated whenever `setup_and_train.py --train` runs
- Allows models to improve over time

### Files Cached

- `data/models/` - Trained ML prediction models

---

## Cache Verification

### Automatic Checks

Each job logs cache status:

**collect-odds:**
```bash
✓ Cache found - checking status...
Cache: 2.01 MB, 4,174 games
Status: ✅ VALID (expires in 6 days 23 hours)
```

**check-results:**
```bash
📊 Cache status before processing:
Cache: 2.01 MB, 4,174 games
Status: ✅ VALID

[... after retrain ...]

📊 Cache status after retrain:
Cache: 2.05 MB, 4,250 games
Status: ✅ VALID (expires in 6 days 23 hours)
```

### Manual Verification

Check cache status from workflow logs:
1. Go to Actions tab in GitHub
2. Click on latest workflow run
3. Expand "Check cache status" step
4. Review cache age and game count

---

## Cache Size Limits

**GitHub Actions Cache Limits:**
- Total cache storage: 10 GB per repository
- Individual cache size: No limit, but recommend < 500 MB per cache
- Cache retention: 7 days for unused caches (our weekly refresh prevents expiration)

**Current Usage:**
- Game data cache: ~2 MB (well under limit)
- ATS data: < 1 MB
- ML models: ~10-50 MB (varies)
- **Total: ~60 MB (0.6% of 10 GB limit)**

---

## Troubleshooting

### Cache Not Found

**Symptom:**
```
⚠️  No cache found - predictions will fetch fresh data from ESPN
```

**Cause:** First run of the week or cache manually deleted

**Solution:** Automatic - `setup_and_train.py` will populate cache

**Manual Fix:**
```bash
# Trigger check-results job manually to populate cache
# GitHub Actions → Run workflow → check_results
```

### Cache Expired

**Symptom:**
```
Status: ❌ EXPIRED (older than 7.0 days)
```

**Cause:** Cache file is more than 7 days old (shouldn't happen with weekly refresh)

**Solution:** Delete old cache and let it refresh:
```bash
# In workflow:
rm data/cache/completed_games_*.json
python scripts/setup_and_train.py --populate 200 --train
```

### ESPN API Quota Hit During Refresh

**Symptom:**
```
Error: API quota exceeded
```

**Cause:** Too many requests to ESPN API

**Solution:**
1. Use existing cache (extend `CACHE_EXPIRY_MINUTES` temporarily)
2. Wait for quota to reset
3. GitHub Actions uses free ESPN API (no auth), so quota should be rare

---

## Manual Cache Management

### Force Cache Refresh

To manually force a cache refresh in GitHub Actions:

1. **Option A: Trigger check-results job**
   ```
   GitHub Actions → Daily Predictions → Run workflow
   Select: check_results
   ```

2. **Option B: Delete cache via workflow**
   Add this step before `setup_and_train`:
   ```yaml
   - name: Force cache refresh
     run: rm -rf data/cache/*.json
   ```

### Check Cache Without Refreshing

Trigger `collect-odds` job:
```
GitHub Actions → Daily Predictions → Run workflow
Select: collect_odds
```

This will show cache status without modifying it.

---

## Cache Keys Reference

### Game Data Cache
| Key Format | Example | When Created |
|------------|---------|--------------|
| `game-cache-YYYY-WWW` | `game-cache-2026-W05` | Automatically based on ISO week |

### ATS Data Cache
| Key Format | Example | When Created |
|------------|---------|--------------|
| `ats-data-NNNN` | `ats-data-1234` | Every workflow run (increments) |

### ML Models Cache
| Key Format | Example | When Created |
|------------|---------|--------------|
| `ml-models-NNNN` | `ml-models-1234` | Every workflow run (increments) |

---

## Benefits of This Strategy

✅ **Avoids API Quota Issues**
- ESPN API called once per week instead of every run
- Reduced from 362 calls/hour to 362 calls/week (98% reduction)

✅ **Fast Predictions**
- Cache hit: Predictions run in ~30 seconds
- Cache miss: Predictions run in ~5 minutes (first run of week)

✅ **Always Up-to-Date**
- Weekly refresh ensures new games are included
- Old games remain cached (they don't change)

✅ **Resilient**
- If cache fails, automatically fetches fresh data
- Graceful degradation (predictions still work)

✅ **Efficient Storage**
- Only ~60 MB of 10 GB GitHub cache limit used
- Old caches automatically cleaned up by GitHub

---

## Configuration

**Local:** `config.py`
```python
CACHE_EXPIRY_MINUTES: int = 10080  # 7 days
```

**GitHub Actions:** `.github/workflows/daily_predictions.yml`
```yaml
- name: Get current week
  id: week
  run: echo "week=$(date +%Y-W%V)" >> $GITHUB_OUTPUT

- name: Cache completed games data
  uses: actions/cache@v4
  with:
    path: data/cache
    key: game-cache-${{ steps.week.outputs.week }}
    restore-keys: game-cache-
```

---

## Monitoring

**What to Watch:**

1. **Cache hit rate:** Should be ~6/7 days (85%+)
   - 1 cache miss per week (Monday) = expected
   - Multiple cache misses per week = problem

2. **Cache size:** Should stay under 10 MB
   - If growing rapidly, investigate data accumulation

3. **Workflow duration:**
   - With cache: ~2-3 minutes
   - Without cache: ~7-10 minutes (fetch all games)

4. **API usage:**
   - The Odds API: 276/500 remaining (should stay high)
   - ESPN API: No quota, but monitor for rate limiting

**Check these in GitHub Actions workflow logs**

---

## Summary

| Aspect | Details |
|--------|---------|
| **Refresh Frequency** | Weekly (automatic) |
| **Cache Size** | ~2 MB (4,000+ games) |
| **Storage Used** | 60 MB / 10 GB (0.6%) |
| **API Calls Saved** | 98% reduction (362/week vs 362/hour) |
| **Prediction Speed** | 30 sec (cache) vs 5 min (no cache) |
| **Maintenance** | Zero - fully automatic |

The cache strategy ensures predictions are fast, accurate, and don't hit API quotas, while automatically refreshing weekly to stay current with the basketball season.
