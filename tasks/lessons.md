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

---
