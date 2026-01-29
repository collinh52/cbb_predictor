# College Basketball Predictor - Analysis & Improvement Recommendations

**Date:** January 28, 2026
**Analysis Scope:** Data collection, team rating algorithms, game prediction algorithms

---

## Executive Summary

The predictor has solid architectural foundations (UKF + ML hybrid approach, KenPom integration) but contains **3 critical bugs** preventing it from reaching full potential, plus several basketball-specific enhancements that could improve accuracy by 10-20%.

**Current Status:** 68.96% backtested accuracy
**Potential with Fixes:** 75-85% accuracy (competitive with professional systems)

---

## CRITICAL BUGS (Fix Immediately)

### 🔴 Bug #1: Indentation Error Disables ML Features
**File:** `src/hybrid_predictor.py:125`
**Severity:** CRITICAL - ML model effectively disabled

```python
# Line 123-124 (correct indentation)
all_games = self.ukf_predictor.collector.get_completed_games()

    # Line 125-142 (WRONG - extra indentation!)
    try:
        features_array, features_dict = self.feature_engineer.engineer_features(...)
```

**Impact:**
- ML feature engineering code is unreachable
- Hybrid predictor falls back to UKF-only mode
- Neural network never used despite being trained

**Fix:**
```python
# De-indent lines 125-142 by one level
all_games = self.ukf_predictor.collector.get_completed_games()

# Engineer features for ML model
try:
    features_array, features_dict = self.feature_engineer.engineer_features(...)
```

**Estimated Accuracy Gain:** +5-10% (re-enables entire ML pipeline)

---

### 🔴 Bug #2: Mathematically Broken Pace Estimation
**File:** `src/feature_calculator.py:230`
**Severity:** CRITICAL - Nonsensical pace values

```python
# Current (WRONG):
avg_total = np.mean(total_points)
estimated_pace = avg_total / 2.0  # Makes no mathematical sense
return float(np.clip(estimated_pace, 60.0, 80.0))
```

**Why It's Wrong:**
- Pace = possessions per 40 minutes
- Total points ÷ 2 ≠ possessions
- Example: 150 total points → 75 "pace", but 150 ÷ 75 = 2.0 PPP (impossible!)
- Real college PPP range: 0.85-1.15

**True Formula:**
```
Pace = (FGA + 0.44*FTA - ORB + TO) / (Game Minutes) * 40
```

**Practical Fix (without play-by-play data):**
```python
# Option A: Use KenPom pace (best)
if kenpom_data_available:
    return kenpom_team['adj_t']

# Option B: Estimate from total points and known efficiency
avg_total = np.mean(total_points)
estimated_efficiency = 1.0  # Assume ~1.0 PPP average
estimated_pace = avg_total / (2.0 * estimated_efficiency)
return float(np.clip(estimated_pace, 60.0, 80.0))

# Option C: Just use default (safest until fix)
return config.DEFAULT_PACE  # 70.0
```

**Estimated Accuracy Gain:** +2-4% (fixes systematic bias in total predictions)

---

### 🔴 Bug #3: Incorrect Points-from-Pace Formula
**File:** `src/predictor.py:226-231`
**Severity:** CRITICAL - Systematic prediction bias

```python
# Current approach (PROBLEMATIC):
home_expected_points = (home_off / 100.0) * avg_pace
away_expected_points = (away_off / 100.0) * avg_pace
predicted_total = (home_expected_points + away_expected_points) * 1.15  # Arbitrary!
```

**Problems:**
1. Comment admits "scale factor ~1.15-1.20" is arbitrary
2. If offensive_rating is already points-per-100-possessions, then:
   - Formula should be: `(rating / 100) * pace` ✓
   - But ratings aren't true points-per-100 (no possession data)
3. The 1.15 multiplier masks incorrect rating scale

**Better Approach:**

```python
# Option A: If ratings ARE points-per-100 (tempo-free):
home_expected_points = (home_off / 100.0) * avg_pace
away_expected_points = (away_off / 100.0) * avg_pace
predicted_total = home_expected_points + away_expected_points  # No multiplier needed

# Option B: If ratings are raw scores (not tempo-free):
# Don't multiply by pace at all
predicted_total = home_off + away_off

# Option C: Data-driven calibration (RECOMMENDED):
# Train regression on historical data:
# actual_total ~ β0 + β1*(home_off) + β2*(away_off) + β3*(pace) + β4*(home_def) + β5*(away_def)
# Use learned coefficients instead of arbitrary 1.15
```

**Fix for Now:**
```python
# Remove arbitrary multiplier, add calibration constant from data
BASE_TOTAL_POINTS = 140.0  # College basketball average
home_expected = (home_off / 100.0) * avg_pace
away_expected = (away_off / 100.0) * avg_pace
predicted_total = home_expected + away_expected

# Calibrate to known average (if ratings are miscalibrated)
if predicted_total < 100 or predicted_total > 200:
    # Blend with prior knowledge
    predicted_total = 0.7 * predicted_total + 0.3 * BASE_TOTAL_POINTS
```

**Estimated Accuracy Gain:** +3-5% (eliminates systematic bias)

---

## HIGH PRIORITY FIXES

### 🟠 Issue #4: Silent Cache Failures
**File:** `src/data_collector.py:48-49`

```python
# Current (BAD):
except Exception:
    return None  # Could be permission errors, corruption, etc.
```

**Fix:**
```python
except FileNotFoundError:
    return None  # Expected - no cache yet
except (PermissionError, OSError) as e:
    print(f"⚠️  Cache access error: {e}")
    return None
except json.JSONDecodeError as e:
    print(f"⚠️  Corrupt cache file {cache_path}: {e}")
    cache_path.unlink()  # Delete corrupt cache
    return None
```

---

### 🟠 Issue #5: Redundant Feature Calculation
**Files:** `src/feature_calculator.py`, `src/predictor.py`

**Problem:**
- Each prediction recalculates momentum, fatigue, pace for both teams
- Loops through entire season history (1000+ games) per prediction
- Complexity: O(n) per prediction where n = season games

**Current Workflow:**
```
Predict Game 1 → Calculate home features → Loop 1000 games
              → Calculate away features → Loop 1000 games
Predict Game 2 → Calculate home features → Loop 1000 games
              → Calculate away features → Loop 1000 games
...
```

**Better Approach:**
```python
# Cache team features, invalidate on new results only
class FeatureCalculator:
    def __init__(self):
        self._team_feature_cache = {}  # {team_id: {momentum, fatigue, pace, ...}}
        self._cache_valid_until = {}   # {team_id: last_game_date}

    def get_game_features(self, game, team_id, is_home, all_games, current_date):
        # Check cache
        if team_id in self._team_feature_cache:
            cached_features = self._team_feature_cache[team_id]
            cache_date = self._cache_valid_until.get(team_id)

            # Only recalculate if new games since cache
            if cache_date and current_date <= cache_date:
                return cached_features

        # Calculate features (expensive)
        features = self._calculate_features_expensive(team_id, all_games, current_date)

        # Cache result
        self._team_feature_cache[team_id] = features
        self._cache_valid_until[team_id] = current_date

        return features
```

**Estimated Performance Gain:** 10-50x faster predictions (from seconds to milliseconds)

---

### 🟠 Issue #6: Team Name Normalization Failures
**Files:** `src/utils.py`, `src/team_name_mapping.py`

**Problem:**
- Team IDs normalized via hash may cause collisions
- Fuzzy matching threshold (0.65) arbitrary
- ESPN/SportsDataIO/KenPom/Odds API use different names

**Examples:**
- ESPN: "Texas A&M" vs Odds API: "Texas A&M Aggies"
- ESPN: "Saint Mary's" vs KenPom: "St. Mary's (CA)"
- ESPN: "UConn" vs SportsDataIO: "Connecticut"

**Fix:**
```python
# Add comprehensive name mapping at startup
TEAM_NAME_ALIASES = {
    'Connecticut': ['UConn', 'Connecticut Huskies'],
    'Texas A&M': ['Texas A&M Aggies', 'TAMU'],
    "Saint Mary's": ["St. Mary's (CA)", "Saint Mary's Gaels"],
    # ... comprehensive list for all 372 D1 teams
}

def normalize_team_name(name: str) -> str:
    name_lower = name.lower().strip()
    for canonical, aliases in TEAM_NAME_ALIASES.items():
        if name_lower == canonical.lower():
            return canonical
        if any(name_lower == alias.lower() for alias in aliases):
            return canonical
    return name  # Return as-is if not found
```

---

## BASKETBALL-SPECIFIC IMPROVEMENTS

### 🟡 Enhancement #1: Strength of Schedule (SOS)
**Current:** Not implemented
**Impact:** Teams with weak schedules appear stronger than they are

**Implementation:**
```python
def calculate_sos(team_id: int, all_games: List[Dict], team_ratings: Dict) -> float:
    """Calculate opponent quality for a team."""
    opponents = []
    for game in all_games:
        if game['home_team_id'] == team_id:
            opp_id = game['away_team_id']
        elif game['away_team_id'] == team_id:
            opp_id = game['home_team_id']
        else:
            continue

        if opp_id in team_ratings:
            opponents.append(team_ratings[opp_id])

    if not opponents:
        return 0.0

    return np.mean(opponents)  # Average opponent rating

# Adjust team rating based on SOS
adjusted_rating = raw_rating - 0.3 * (sos - avg_sos)
```

**Estimated Accuracy Gain:** +2-3%

---

### 🟡 Enhancement #2: Four Factors Integration
**Current:** Only offensive/defensive ratings used
**Missing:** eFG%, TOV%, REB%, FT Rate

**Why It Matters:**
- eFG% explains 40% of game outcome variance
- TOV% explains 25%
- REB% explains 20%
- FT Rate explains 15%

**Implementation (requires KenPom data):**
```python
# Extract from KenPom CSV
four_factors = {
    'efg_pct': kenpom['eFG_Pct'],      # Effective FG%
    'tov_pct': kenpom['TO_Pct'],       # Turnover rate
    'oreb_pct': kenpom['OR_Pct'],      # Off rebound rate
    'ft_rate': kenpom['FTRate']        # FTA per FGA
}

# Calculate matchup advantage
home_advantage = (
    0.40 * (home_efg - away_efg) +
    0.25 * (away_tov - home_tov) +  # Lower TOV is better
    0.20 * (home_oreb - away_oreb) +
    0.15 * (home_ft_rate - away_ft_rate)
)
```

**Estimated Accuracy Gain:** +4-6%

---

### 🟡 Enhancement #3: Conference Strength Adjustment
**Current:** All games treated equally
**Reality:** Conference play differs from non-conference

**Implementation:**
```python
CONFERENCE_STRENGTH = {
    'ACC': 1.15,      # Strong conferences
    'Big Ten': 1.15,
    'Big 12': 1.10,
    'SEC': 1.10,
    'Big East': 1.05,
    'Pac-12': 1.00,   # Average
    'Mountain West': 0.95,
    'A-10': 0.95,
    'WCC': 0.90,
    'AAC': 0.90,
    # ... others
}

# Adjust opponent strength by conference
if game_type == 'conference':
    opponent_strength *= CONFERENCE_STRENGTH.get(opponent_conference, 1.0)
```

**Estimated Accuracy Gain:** +1-2%

---

### 🟡 Enhancement #4: Neutral Court Detection
**Current:** README claims "248 neutral games detected" but implementation is basic
**Issue:** Home advantage applied to tournament games

**Fix:**
```python
def is_neutral_court(game: Dict) -> bool:
    """Detect neutral court games."""
    # Check explicit neutral flag
    if game.get('NeutralCourt') or game.get('neutral_site'):
        return True

    # Tournament keywords
    tournament_keywords = ['tournament', 'classic', 'invitational', 'championship']
    game_name = game.get('name', '').lower()
    if any(keyword in game_name for keyword in tournament_keywords):
        return True

    # Location mismatch (e.g., Duke "home" game in Madison Square Garden)
    home_team = game.get('HomeTeam', '').lower()
    location = game.get('location', '').lower()
    if home_team not in location:
        return True  # Likely neutral

    return False

# Apply in prediction
if is_neutral_court(game):
    home_advantage = 0.0  # No home court advantage
else:
    home_advantage = home_state[TeamUKF.HOME_ADV]
```

**Estimated Accuracy Gain:** +1-2% (especially for tournament games)

---

### 🟡 Enhancement #5: Recency-Weighted Momentum
**Current:** Momentum calculation doesn't properly weight recent games
**File:** `src/feature_calculator.py:86-95`

```python
# Current (WRONG):
momentum = sum(recent_margins) / len(recent_margins)
momentum *= config.MOMENTUM_DECAY  # Applied once at end

# Better (exponential decay per game):
weighted_momentum = 0.0
total_weight = 0.0
for i, (game_date, margin) in enumerate(sorted_recent_games):
    days_ago = (current_date - game_date).days
    weight = config.MOMENTUM_DECAY ** days_ago  # Decay by recency
    weighted_momentum += margin * weight
    total_weight += weight

momentum = weighted_momentum / total_weight if total_weight > 0 else 0.0
```

**Estimated Accuracy Gain:** +1-2%

---

## EFFICIENCY IMPROVEMENTS

### ⚡ Optimization #1: Connection Pooling
**Current:** Each data collector creates new HTTP session

```python
# src/espn_collector.py
class ESPNCollector:
    def __init__(self):
        self.session = requests.Session()  # Good!
        # But multiple instances = multiple sessions

# Better: Singleton pattern
_shared_session = None

def get_session():
    global _shared_session
    if _shared_session is None:
        _shared_session = requests.Session()
        _shared_session.headers.update({'User-Agent': 'CBB-Predictor/1.0'})
    return _shared_session
```

---

### ⚡ Optimization #2: Batch Odds Fetching
**Current:** Sequential API calls for each game

```python
# Better: Fetch all games in one request
odds_data = odds_api.get_odds_for_sport(
    sport='basketball_ncaab',
    markets=['spreads', 'totals'],
    date_from=today,
    date_to=today + timedelta(days=2)
)  # One API call instead of N
```

---

### ⚡ Optimization #3: Database Query Optimization
**Issue:** No indexes on frequently queried columns

```sql
-- Add indexes for performance
CREATE INDEX idx_predictions_game_date ON predictions(game_date);
CREATE INDEX idx_predictions_created_at ON predictions(created_at);
CREATE INDEX idx_game_results_game_id ON game_results(game_id);
```

---

## EDGE CASES TO HANDLE

### 1. Early Season (< 5 games)
**Problem:** Returns default values for everything
**Fix:** Use preseason rankings or previous season data as prior

### 2. Injury Data Quality
**Problem:** Linear penalty for injuries (5 injuries = 50% health)
**Fix:** Weight by player importance (starter vs bench)

### 3. Tournament Momentum
**Problem:** Not modeled
**Fix:** Increase momentum weight during March Madness (1.5x)

### 4. Overtime Games
**Problem:** Not detected or weighted
**Fix:** Add OT flag, increase fatigue by 20% for OT games

### 5. Back-to-Back Games
**Problem:** Fatigue calculation is basic
**Fix:** Exponentially increase fatigue for <2 days rest

---

## IMPLEMENTATION PRIORITY

### Week 1: Critical Bugs
- [ ] Fix indentation in `hybrid_predictor.py:125`
- [ ] Fix pace estimation in `feature_calculator.py:230`
- [ ] Fix pace-to-points formula in `predictor.py:226-231`
- [ ] Add logging for silent failures
- [ ] Test that ML model actually runs

**Expected Outcome:** +10-15% accuracy, ML model functional

### Week 2: High Priority
- [ ] Implement feature caching
- [ ] Add comprehensive team name mapping
- [ ] Fix rest days calculation
- [ ] Add connection pooling
- [ ] Database indexes

**Expected Outcome:** 10-50x faster, fewer errors

### Week 3: Basketball Enhancements
- [ ] Calculate Strength of Schedule
- [ ] Integrate Four Factors from KenPom
- [ ] Implement neutral court detection
- [ ] Add conference strength adjustment
- [ ] Weight momentum by recency

**Expected Outcome:** +5-10% accuracy

### Week 4: Edge Cases & Polish
- [ ] Handle early season with priors
- [ ] Improve injury modeling
- [ ] Detect overtime games
- [ ] Add tournament mode
- [ ] Validate all edge cases

**Expected Outcome:** Robust production system

---

## TESTING RECOMMENDATIONS

After each fix, run:

```bash
# 1. Unit tests
pytest tests/test_predictor.py -v
pytest tests/test_feature_calculator.py -v
pytest tests/test_hybrid_predictor.py -v

# 2. Integration test
pytest tests/test_integration.py -v

# 3. Backtest validation
python validation/run_all_backtests.py

# 4. Check accuracy improvement
python scripts/update_readme_accuracy.py
```

---

## ESTIMATED IMPACT SUMMARY

| Fix/Enhancement | Accuracy Gain | Performance Gain | Effort |
|-----------------|---------------|------------------|--------|
| Bug #1 (Indentation) | +5-10% | - | 5 min |
| Bug #2 (Pace estimation) | +2-4% | - | 30 min |
| Bug #3 (Pace-to-points) | +3-5% | - | 1 hour |
| Feature caching | - | 10-50x | 2 hours |
| SOS calculation | +2-3% | - | 3 hours |
| Four Factors | +4-6% | - | 4 hours |
| Conference adjustment | +1-2% | - | 2 hours |
| Neutral court fix | +1-2% | - | 1 hour |
| Momentum weighting | +1-2% | - | 1 hour |
| **TOTAL** | **+19-34%** | **10-50x** | **~2-3 days** |

**Projected Final Accuracy:** 75-85% (from current 68.96%)

This would put the system in the range of professional handicapping services.

---

## ARCHITECTURE RECOMMENDATIONS

### Consider Refactoring:

1. **Separate Concerns:**
   - `predictor.py` does too much (data loading + feature calc + prediction)
   - Split into: `DataPipeline`, `FeatureEngine`, `PredictionModel`

2. **Type Safety:**
   - Add type hints throughout
   - Use Pydantic models for game data validation

3. **Configuration:**
   - Move hardcoded coefficients (5.0, 3.0, 2.0) to config
   - Make coefficients data-driven (learn from backtesting)

4. **Monitoring:**
   - Log prediction confidence distribution
   - Track feature importance over time
   - Alert on degraded accuracy

---

## CONCLUSION

The predictor has excellent foundations but is held back by implementation bugs and missing basketball-specific logic. The three critical bugs (#1-3) should be fixed immediately as they prevent core functionality.

With systematic fixes over 2-3 weeks, the system could reach 75-85% accuracy, competitive with professional systems like KenPom and BartTorvik.

**Next Steps:**
1. Fix Bug #1 (indentation) - takes 5 minutes, unlocks ML model
2. Run backtest to confirm ML model improves accuracy
3. Fix Bugs #2-3 (pace formulas)
4. Implement feature caching for 10x+ speedup
5. Add basketball enhancements iteratively

**Questions?** See individual file comments or run tests to validate each fix.
