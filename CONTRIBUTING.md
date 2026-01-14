# Contributing to CBB Predictor

Thank you for your interest in contributing to the College Basketball Predictor! This project aims to provide accurate college basketball predictions using advanced statistical methods.

## How to Contribute

### Reporting Issues
- Use the GitHub issue tracker to report bugs or request features
- Include detailed information about the issue, including steps to reproduce
- Mention your Python version, OS, and any relevant error messages

### Code Contributions
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Make your changes
4. Add tests if applicable
5. Run the backtesting to ensure accuracy isn't degraded
6. Commit your changes: `git commit -m 'Add some feature'`
7. Push to the branch: `git push origin feature/your-feature-name`
8. Submit a pull request

### Development Setup
```bash
# Clone the repository
git clone https://github.com/yourusername/cbb_predictor.git
cd cbb_predictor

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your API keys

# Run basic tests
python scripts/show_team_ratings_v3.py
```

## Code Style
- Follow PEP 8 Python style guidelines
- Use descriptive variable and function names
- Add docstrings to new functions
- Keep functions focused on single responsibilities

## Testing
- Run backtests to validate any changes to the rating system
- Ensure prediction accuracy doesn't degrade
- Test with different seasons/data sources

## Areas for Improvement
- Additional rating factors (player stats, advanced metrics)
- More sophisticated neutral court detection
- Enhanced pace adjustment algorithms
- Machine learning model integration
- Web interface improvements

## Questions?
Feel free to open an issue or discussion on GitHub for questions about contributing.
