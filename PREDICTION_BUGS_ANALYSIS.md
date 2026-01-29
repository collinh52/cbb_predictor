# Critical Prediction Algorithm Bugs - Analysis & Solutions

## Executive Summary

Two critical bugs have been identified in the prediction algorithm:

1. **Spread Edge Calculation Bug**: Edge values are doubled due to incorrect sign convention
2. **Total Prediction Bug**: Predicted totals are systematically LOW because defensive ratings are not incorporated

Both bugs stem from inconsistent handling of basketball analytics formulas.

---

## Bug #1: Spread Edge Calculation (CRITICAL)

### Problem

**Example from output:**
```
🏠 Colorado @ Iowa State
   Line: -17.0 | O/U: 153.0
   Model: Iowa State by +17.3 | Edge: +34.3  ❌ WRONG
```

**Expected:**
- Edge should be: 17.3 - 17.0 = **0.3 points**

**Actual:**
- Edge shown: **34.3 points** (exactly 17.3 + 17.0)

### Root Cause

**Location:** `scripts/daily_collect_odds.py:147` and `scripts/daily_collect_odds.py:228`

**Bug in code:**
```python
# Line 147: Extract spread from API
if home_team.lower() in outcome.get('name', '').lower():
    vegas_spread = float(outcome.get('point', 0))  # Iowa State gets -17.0

# Line 228: Calculate edge
edge = predicted_margin - (vegas_spread or 0)
# = 17.3 - (-17.0) = 34.3  ❌ WRONG
```

**Sign Convention Issue:**

The Odds API returns spread with bookmaker convention:
- Iowa State `-17.0` means "Iowa State is favored by 17 points"
- Colorado `+17.0` means "Colorado gets 17 points"

The model's `predicted_margin` uses HOME TEAM perspective:
- `+17.3` means "Home team (Iowa State) wins by 17.3 points"

When calculating edge:
- Model: Home wins by +17.3
- Vegas: -17.0 (home favored by 17)
- Edge: 17.3 - (-17.0) = **34.3** ❌

**The fix:** Negate the spread when it's for the home team to match the model's sign convention.

### Solution

```python
# Line 147: Correct spread extraction
if home_team.lower() in outcome.get('name', '').lower():
    # API returns bookmaker convention: negative = favored
    # Model uses home perspective: positive = home wins by that much
    # So negate to convert: -17 (favored by 17) → +17 (expected to win by 17)
    vegas_spread = -float(outcome.get('point', 0))
```

**Why this works:**
- API: Iowa State `-17.0` (favored by 17)
- After negation: `vegas_spread = +17.0` (expected to win by 17, from home perspective)
- Edge = 17.3 - 17.0 = **0.3** ✅ CORRECT

**Gambling Logic:**
- If Iowa State is -17 and the model predicts them to win by 17.3, they should cover by 0.3 points
- The edge of 0.3 means the model slightly favors Iowa State to cover the spread
- This aligns with standard sports betting analysis

---

## Bug #2: Total Prediction (CRITICAL)

### Problem

**Every single game predicts UNDER:**
```
✈️ Wofford @ Chattanooga
   Line: +0.0 | O/U: 152.0
   Pick: AWAY 📉UNDER

🏠 Colorado @ Iowa State
   Line: -17.0 | O/U: 153.0
   Pick: HOME 📉UNDER

... (59/59 games predict UNDER)
```

**Statistical Impossibility:**
- If the model was correct, ~50% should be OVER and ~50% UNDER
- 100% UNDER indicates systematic bias (underestimation)

### Root Cause

**Location:** `src/predictor.py:282-300` and `src/ukf_model.py:178-183`

**Buggy Total Calculation:**
```python
# Current code (WRONG):
home_ukf_points = (home_off / 100.0) * avg_pace
away_ukf_points = (away_off / 100.0) * avg_pace
predicted_total = home_ukf_points + away_ukf_points
```

**The Problem:** This formula **completely ignores defensive ratings**!

- If Home has offense=110, Away has offense=100, pace=70:
  - home_points = (110/100) * 70 = 77.0
  - away_points = (100/100) * 70 = 70.0
  - total = 147.0

- But what if Home has ELITE defense (def=85)?
  - Away should score LESS than 70 points!
  - Current formula still gives away_points = 70.0 ❌

**Compare to Margin Calculation (which IS correct):**
```python
# Margin calculation (CORRECT):
predicted_margin = (home_off - away_def) - (away_off - home_def) + home_adv
```

This properly accounts for:
- Home team's offense vs Away team's defense: `home_off - away_def`
- Away team's offense vs Home team's defense: `away_off - home_def`

### Basketball Analytics Background

**KenPom Efficiency Ratings:**
- `AdjO` (Adjusted Offensive Efficiency) = points scored per 100 possessions
- `AdjD` (Adjusted Defensive Efficiency) = points allowed per 100 possessions
- `AdjEM` (Efficiency Margin) = AdjO - AdjD

**Proper Expected Score Formula:**

When Team A (offense=O_A, defense=D_A) plays Team B (offense=O_B, defense=D_B):

```
Team A's expected score = (O_A - D_B + 100) * (possessions / 100)
Team B's expected score = (O_B - D_A + 100) * (possessions / 100)
```

**Why the +100?**
- `O_A - D_B` is the net efficiency (points above/below average)
- Adding 100 converts to absolute points per 100 possessions
- Example: If O_A=110, D_B=95, then Team A scores (110-95+100)=115 per 100 poss

**Example Calculation:**
```
Duke (O=115, D=90) vs UNC (O=108, D=95), pace=72

Duke's expected score:
  = (115 - 95 + 100) / 100 * 72
  = 120 / 100 * 72
  = 86.4 points

UNC's expected score:
  = (108 - 90 + 100) / 100 * 72
  = 118 / 100 * 72
  = 84.96 points

Predicted total = 86.4 + 84.96 = 171.36 points
Predicted margin = 86.4 - 84.96 = 1.44 points (Duke by 1.4)
```

### Solution

**Fix in `src/predictor.py` (lines 282-300):**

```python
# OLD (WRONG):
home_ukf_points = (home_off / 100.0) * avg_pace
away_ukf_points = (away_off / 100.0) * avg_pace

# NEW (CORRECT):
# Expected score = (team_offense - opponent_defense + baseline) * pace
# This matches the margin calculation logic
home_ukf_points = ((home_off - away_def + 100.0) / 100.0) * avg_pace
away_ukf_points = ((away_off - home_def + 100.0) / 100.0) * avg_pace
```

**Fix in `src/ukf_model.py` (lines 178-183):**

```python
# OLD (WRONG):
our_expected = (our_off / 100.0) * actual_pace_clamped
opp_expected = (opp_off / 100.0) * actual_pace_clamped

# NEW (CORRECT):
our_expected = ((our_off - opp_def + 100.0) / 100.0) * actual_pace_clamped
opp_expected = ((opp_off - our_def + 100.0) / 100.0) * actual_pace_clamped
```

**Hybrid Predictor:** Same fix needed in `src/hybrid_predictor.py` if it has similar logic.

### Why This Fixes the UNDER Bias

**Current (Buggy) Behavior:**
- All teams default to OFF=100, DEF=100, pace=70
- Predicted total = (100/100)*70 + (100/100)*70 = 140 points
- Most college games have Vegas O/U of 145-160
- 140 < 150 → Always UNDER ❌

**After Fix (Correct) Behavior:**
- Duke (O=110, D=95) vs UNC (O=105, D=92), pace=70
- Duke expected: (110-92+100)/100*70 = 118/100*70 = 82.6
- UNC expected: (105-95+100)/100*70 = 110/100*70 = 77.0
- Total = 159.6 points
- If Vegas O/U = 155 → Pick OVER ✅
- If Vegas O/U = 162 → Pick UNDER ✅
- Natural distribution around 50/50 based on matchup

---

## Impact Assessment

### Bug #1: Edge Calculation
- **Severity:** HIGH
- **Impact:** All edge calculations are 2x too large (misleading value)
- **Betting Impact:** Cannot trust edge values for betting decisions
- **Example:** Edge of 34.3 suggests massive value, but real edge is only 0.3

### Bug #2: Total Prediction
- **Severity:** CRITICAL
- **Impact:** 100% of predictions are systematically biased
- **Betting Impact:** Model is completely unusable for totals betting
- **Accuracy Impact:** Likely 0% accuracy on over/under picks
- **Statistical Evidence:** 59/59 games picking UNDER is statistically impossible for a calibrated model

---

## Testing Plan

### Test #1: Edge Calculation Fix

Run predictions for known games and verify:
```
Iowa State -17 vs model prediction +17.3:
  Expected edge: 0.3
  Verify: Edge displayed as "+0.3"
```

### Test #2: Total Prediction Fix

Run predictions and verify:
1. Distribution of OVER/UNDER picks is roughly 50/50
2. Predicted totals vary based on matchup:
   - High-offense vs weak-defense → Higher totals
   - Strong-defense matchup → Lower totals
3. Predicted totals are in reasonable range (130-170 for most games)

### Test #3: Consistency Check

Verify that margin and total calculations are mathematically consistent:
```
If predicted margin = +5 (home by 5)
And predicted total = 150
Then:
  Home score = (150 + 5) / 2 = 77.5
  Away score = (150 - 5) / 2 = 72.5
```

---

## Files to Modify

1. **scripts/daily_collect_odds.py** (Line 147)
   - Fix: Negate spread when extracting for home team

2. **src/predictor.py** (Lines 282-283)
   - Fix: Incorporate defense in total calculation

3. **src/ukf_model.py** (Lines 180-181)
   - Fix: Incorporate defense in UKF expected total

4. **src/hybrid_predictor.py** (if applicable)
   - Check and fix any similar total calculations

---

## Gambling & Basketball Logic Validation

### Spread Edge (Bug #1)

**Standard Sports Betting:**
- Spread of -17 means favorite must win by MORE than 17 to cover
- If model predicts win by 17.3, that's 0.3 points better than the spread
- Edge of 0.3 is marginal (low confidence bet)
- Edge of 34.3 would be astronomical and unrealistic

**Fix Validation:** ✅ Edge of 0.3 makes sense for marginal advantage

### Totals (Bug #2)

**College Basketball Averages (2025-2026):**
- Average total points: 140-145 (varies by conference/style)
- High-tempo, offensive teams: 160-180 totals
- Slow-pace, defensive teams: 120-140 totals

**Defensive Impact:**
- Elite defense (D=85): Opponent scores ~10-15 points LESS
- Weak defense (D=110): Opponent scores ~10-15 points MORE
- This is well-documented in basketball analytics

**Fix Validation:** ✅ Incorporating defense will:
- Increase totals when both teams have weak defense
- Decrease totals when both teams have strong defense
- Create realistic variance in predicted totals

---

## Commit Message (when implementing fixes)

```
Fix critical prediction bugs: spread edge and total calculation

BUG #1: Spread edge calculation doubled
- Edge was calculating as predicted_margin - (-spread) instead of predicted_margin - spread
- Fixed by negating spread when extracting from home team perspective
- Example: Iowa State -17 with prediction +17.3 now shows edge of 0.3 (was 34.3)

BUG #2: Total predictions systematically low (100% UNDER bias)
- Total calculation ignored defensive ratings, using only offense
- Fixed by incorporating opponent defense: score = (offense - opp_defense + 100) * pace
- Now properly accounts for defensive matchups in total predictions

Both fixes align with standard basketball analytics (KenPom methodology)
and correct gambling logic for spread and total betting.

Fixes:
- scripts/daily_collect_odds.py: Negate home team spread
- src/predictor.py: Add defense to total calculation
- src/ukf_model.py: Add defense to UKF total calculation
```

---

## Priority

**IMMEDIATE FIX REQUIRED**

Both bugs make the prediction system unreliable for actual gambling use:
- Bug #1: Cannot trust edge values (inflated 2x)
- Bug #2: Cannot use for totals betting (0% expected accuracy)

After fixing, re-run backtest to measure actual accuracy improvement.
