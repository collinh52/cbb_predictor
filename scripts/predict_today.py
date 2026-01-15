"""
Generate predictions for upcoming games using the current pipeline.
This is a thin wrapper around scripts/daily_collect_odds.py so local runs
match the daily GitHub Actions workflow.
"""
import os
import sys

# Add project root and scripts directory to sys.path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
scripts_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)
sys.path.insert(0, scripts_dir)

from daily_collect_odds import collect_odds_and_predictions, collect_upcoming_days


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Generate predictions for upcoming games")
    parser.add_argument("--date", type=str, help="Target date (YYYY-MM-DD), defaults to today")
    parser.add_argument("--days", type=int, default=1, help="Number of days to collect (default: 1)")

    args = parser.parse_args()

    if args.days > 1:
        collect_upcoming_days(args.days)
    else:
        collect_odds_and_predictions(args.date)


if __name__ == "__main__":
    main()

