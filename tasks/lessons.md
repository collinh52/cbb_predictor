# Lessons Learned

This file captures lessons learned from corrections and mistakes to prevent repeating them in future sessions.

## Format
Each lesson should include:
- **Date**: When the lesson was learned
- **Context**: What task/feature was being worked on
- **Mistake**: What went wrong
- **Correction**: How it was fixed
- **Rule**: The principle to follow going forward

---

## Lessons

### Feature Removal Requires Test Updates
**Date**: 2026-02-02
**Context**: Removing Vegas lines (pregame_spread, pregame_total) from ML features to fix data leakage
**Mistake**: Initially forgot that removing features would break tests that assert those features exist
**Correction**: Updated `tests/test_ml_features.py::TestContextualFeatureExtraction::test_extract_contextual_features_pregame_lines` to assert features are NOT present
**Rule**: When removing features or changing APIs, search for tests that verify the old behavior and update them to verify the new expected behavior.

### ML Model predict() Interface
**Date**: 2026-02-02
**Context**: Fixing verbose parameter bug in hybrid_predictor.py
**Mistake**: The code was passing `verbose=0` to `SpreadPredictionModel.predict()`, but that method doesn't accept verbose - it handles verbosity internally when calling keras predict
**Correction**: Removed the verbose parameter from the external call since SpreadPredictionModel.predict() already handles it
**Rule**: When wrapping external libraries (like Keras), check what parameters the wrapper method exposes vs. what the underlying library accepts. Don't assume wrapper methods pass through all underlying parameters.

### Pace Normalization Consistency
**Date**: 2026-02-02
**Context**: UKF model was using different normalization constants (70 vs 100) in different formulas
**Mistake**: Rating updates used division by 70.0, but measurement model and predictions used 100.0
**Correction**: Updated rating update formulas to use the same formula as the measurement model: `((off - def + 100) / 100) * pace`
**Rule**: When physics-based models have multiple formulas that should be mathematically consistent, verify they use the same constants and structure. Inconsistent normalization creates systematic bias.

### Vegas Spread Sign Convention
**Date**: 2026-02-04
**Context**: README showed "HOME (+8.0)" for Colorado @ Baylor when Baylor was actually favored at -8.0
**Mistake**:
1. Code in `daily_collect_odds.py` was negating spreads from The Odds API with incorrect comment claiming "model uses positive = home wins"
2. This caused all spreads to be stored backwards (favorites shown as underdogs)
3. Display showed "HOME (+8.0)" which is impossible for a favorite
**Correction**:
1. Removed negation in `daily_collect_odds.py` line 152 - The Odds API already returns spreads in correct format
2. Fixed all existing spreads in `ats_tracking.json` by negating them
3. Updated display logic in `ats_tracker.py` to flip sign when picking AWAY team
4. Added comprehensive explanation to CLAUDE.md
**Rule**:
- **Vegas spread convention**: Negative = favored, Positive = underdog
- **Storage**: Store spreads from home team perspective without modification from API
- **Display**: When showing a pick, flip sign if picking away team (so spread shows from picked team's perspective)
- **Validation**: If you see "HOME (+X)" where home is favored, the spread sign is wrong
- **Never assume** - always verify domain conventions match your mental model before implementing

---
