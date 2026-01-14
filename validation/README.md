# Validation Suite

Comprehensive backtesting to validate the rating system's accuracy.

## Three Validation Methods

### Option 1: Last Season Validation
**File**: `backtest_option1_last_season.py`

Tests the system on 2024-25 season games (completely different season).

**Method**:
- Fetches all 2024-25 season games
- Splits: 70% training, 30% testing
- Predicts weekly outcomes
- Most realistic test of generalization

**Run**:
```bash
python validation/backtest_option1_last_season.py
```

**Output**: `backtest_results_option1_last_season.txt`

---

### Option 2: Rolling Validation
**File**: `backtest_option2_rolling.py`

Tests on current 2025-26 season with time-based split.

**Method**:
- Uses current season games
- Splits: First 80% training, last 20% testing
- Simulates real-world prediction scenario
- Shows how well we predict recent games

**Run**:
```bash
python validation/backtest_option2_rolling.py
```

**Output**: `backtest_results_option2_rolling.txt`

---

### Option 3: K-Fold Cross-Validation
**File**: `backtest_option3_cross_validation.py`

Most rigorous statistical validation with confidence intervals.

**Method**:
- Splits games into 5 chronological folds
- Trains on 4 folds, tests on 1 (repeated 5 times)
- Calculates mean accuracy + standard deviation
- Provides 95% confidence intervals
- Tests statistical significance

**Run**:
```bash
python validation/backtest_option3_cross_validation.py
```

**Output**: `backtest_results_option3_cross_validation.txt`

---

## Run All Three

**File**: `run_all_backtests.py`

Master script that runs all three validation methods sequentially.

**Run**:
```bash
python validation/run_all_backtests.py
```

**Time**: ~10-15 minutes total

**Outputs**:
- `backtest_results_option1_last_season.txt`
- `backtest_results_option2_rolling.txt`
- `backtest_results_option3_cross_validation.txt`
- Comprehensive summary in terminal

---

## What Each Method Tells You

| Method | Validates | Best For | Key Metric |
|--------|-----------|----------|------------|
| **Option 1** | Generalization to new seasons | Out-of-sample accuracy | Different season test |
| **Option 2** | Real-world prediction | Practical usage | Recent games accuracy |
| **Option 3** | Statistical robustness | Research/publication | Confidence intervals |

---

## Interpreting Results

### Accuracy Metrics

- **Overall Accuracy**: % of games where winner was correctly predicted
- **ATS Accuracy**: % of games where spread pick was correct (industry standard)
- **Margin Error**: Average points difference between predicted and actual margin

### Confidence Levels

Results will show accuracy broken down by prediction confidence:
- **High Confidence** (>10 point margin): Should have 65-75% accuracy
- **Medium Confidence** (5-10 points): Should have 55-65% accuracy
- **Low Confidence** (<5 points, toss-ups): ~50% accuracy expected

### Industry Benchmarks

- **Random Guessing**: 50%
- **Good System**: 55-57%
- **Professional System**: 58-60% (KenPom, BartTorvik)
- **Elite System**: 60-65%

### Statistical Significance

Option 3 includes z-test for statistical significance:
- **z > 1.96**: Significantly better than random (p < 0.05) ✓
- **z > 1.645**: Marginally better than random (p < 0.10)
- **z < 1.645**: Not significantly different from random ✗

---

## Expected Results

Based on Phase 1 enhancements:

| Enhancement | Expected Gain |
|-------------|---------------|
| Baseline (SOS only) | ~52% |
| + Home Court Advantage | +1-2% |
| + Margin of Victory | +1-2% |
| + Recency Weighting | +0-1% |
| **Total (Phase 1)** | **~55-57%** |

**Note**: These are estimates. Run validation to get real measured accuracy!

---

## Troubleshooting

### Not Enough Data
If you see "Not enough games for reliable validation", you need more historical data. The system requires:
- Minimum: 100 completed games
- Recommended: 500+ completed games
- Optimal: Full season (3,000+ games)

### Teams Not Found
If many predictions are skipped due to teams not in ratings:
- Check that `min_games=5` threshold isn't too high
- Ensure historical data includes all relevant teams
- Verify ESPN API is returning complete data

### Import Errors
If you get import errors:
```bash
# Run from project root, not from validation directory
cd "/Users/collinhayes/Documents/Cursor Test"
python validation/run_all_backtests.py
```

---

## Next Steps After Validation

1. **Review Results**: Check detailed output files
2. **Analyze Errors**: Identify patterns in incorrect predictions
3. **Compare Methods**: Do all three methods agree on accuracy?
4. **Identify Improvements**: Where does system fail most?
5. **Iterate**: Implement Phase 2 enhancements if needed

---

**Last Updated**: January 12, 2026

