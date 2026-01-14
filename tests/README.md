# CBB Predictor Test Suite

This directory contains comprehensive unit and integration tests for the CBB Predictor project.

## Test Structure

```
tests/
├── conftest.py              # Shared fixtures and configuration
├── test_ukf_model.py        # UKF model tests (23 tests)
├── test_feature_calculator.py # Feature calculation tests (24 tests)
├── test_predictor.py        # Predictor engine tests (26 tests)
├── test_ml_model.py         # Neural network model tests (31 tests)
├── test_ml_features.py      # ML feature engineering tests (28 tests)
├── test_ratings.py          # Rating calculation tests (32 tests)
├── test_integration.py      # Integration tests (11 tests)
└── README.md                # This file
```

## Running Tests

### Run All Tests
```bash
python -m pytest tests/ -v
```

### Run Specific Test File
```bash
python -m pytest tests/test_ukf_model.py -v
```

### Run Tests by Marker
```bash
# Run only unit tests
python -m pytest tests/ -m unit -v

# Run only integration tests
python -m pytest tests/ -m integration -v

# Skip slow tests
python -m pytest tests/ -m "not slow" -v
```

### Run with Coverage
```bash
python -m pytest tests/ --cov=src --cov-report=html
```

## Test Categories

### Unit Tests (`@pytest.mark.unit`)
- Test individual functions and classes in isolation
- Use mocked dependencies
- Fast execution (~1-2 seconds each)

### Integration Tests (`@pytest.mark.integration`)
- Test component interactions
- May use real dependencies
- Verify data flows correctly through the system

### Slow Tests (`@pytest.mark.slow`)
- Tests that take >5 seconds
- Include ML model training tests
- Full rating calculations

## Test Coverage by Component

### UKF Model (`test_ukf_model.py`)
- State initialization and defaults
- State updates from game results
- Uncertainty calculations
- Multi-team management
- Edge cases (extreme scores, zero differentials)

### Feature Calculator (`test_feature_calculator.py`)
- Momentum calculation
- Fatigue calculation
- Health status
- Home court advantage
- Pace estimation
- Combined game features

### Predictor (`test_predictor.py`)
- Team ID extraction and normalization
- Game prediction generation
- Probability calculations
- Empty predictions
- Batch predictions

### ML Model (`test_ml_model.py`)
- Model initialization
- Model building and architecture
- Prediction output shapes
- Training and history
- Model save/load
- Hyperparameter management

### ML Features (`test_ml_features.py`)
- UKF feature extraction
- Contextual feature extraction
- Rest days calculation
- Recent form calculation
- Feature engineering pipeline
- Scaler fitting and transformation

### Ratings (`test_ratings.py`)
- Adjusted margin calculation
- Recency weights
- Pythagorean expectation
- Luck factor
- Road warrior bonus
- Neutral court detection
- Pace adjustment
- Full rating integration

### Integration (`test_integration.py`)
- Full prediction pipeline
- Hybrid predictor fallback
- Feature consistency
- Ratings to prediction flow
- Edge cases (new teams, missing lines)
- Data flow and state updates

## Fixtures

The `conftest.py` provides shared fixtures:

- `sample_game`: Complete game dictionary with scores
- `sample_game_no_score`: Upcoming game without scores
- `sample_games_list`: List of 20 sample games
- `sample_team_state`: UKF state vector
- `sample_opponent_state`: Opponent UKF state
- `sample_features`: Game features dictionary
- `sample_ml_features`: ML feature array
- `sample_training_data`: Training data (X, y)

## Best Practices

1. **Mock External Dependencies**: Use `unittest.mock` for API calls
2. **Use Fixtures**: Share setup code through conftest.py fixtures
3. **Test Edge Cases**: Include boundary conditions and error cases
4. **Keep Tests Fast**: Minimize I/O and computation in unit tests
5. **Clear Assertions**: Use descriptive assertion messages

## Adding New Tests

1. Create test file in `tests/` directory
2. Import the module to test
3. Use fixtures from `conftest.py`
4. Add appropriate markers (`@pytest.mark.unit`, etc.)
5. Follow naming convention: `test_<functionality>()`

Example:
```python
import pytest
from src.new_module import NewClass

class TestNewClass:
    @pytest.mark.unit
    def test_initialization(self):
        obj = NewClass()
        assert obj is not None
```

## Continuous Integration

Tests are designed to run in CI/CD pipelines:

```yaml
# GitHub Actions example
- name: Run tests
  run: |
    pip install pytest pytest-cov
    python -m pytest tests/ --cov=src --cov-report=xml
```

## Test Results

Last run: **175 tests passed** in ~100 seconds

| Test File | Tests | Status |
|-----------|-------|--------|
| test_ukf_model.py | 23 | ✅ |
| test_feature_calculator.py | 24 | ✅ |
| test_predictor.py | 26 | ✅ |
| test_ml_model.py | 31 | ✅ |
| test_ml_features.py | 28 | ✅ |
| test_ratings.py | 32 | ✅ |
| test_integration.py | 11 | ✅ |
| **Total** | **175** | **✅** |

