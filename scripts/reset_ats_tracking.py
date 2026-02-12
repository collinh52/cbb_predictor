#!/usr/bin/env python3
"""
Reset ATS tracking data to clean state.

Use this after fixing bugs to start fresh accuracy tracking
without corrupted historical data.
"""
import json
import os
from pathlib import Path


def main():
    data_dir = Path(__file__).parent.parent / "data"

    files_to_reset = {
        "ats_tracking.json": {},
        "predictions.json": {},
        "ats_accuracy.json": {
            "with_vegas_lines": {
                "total_predictions": 0,
                "spread_correct": 0,
                "spread_accuracy": 0.0,
                "total_correct": 0,
                "total_accuracy": 0.0,
                "last_updated": None,
                "daily_breakdown": {}
            },
            "without_vegas_lines": {
                "total_predictions": 0,
                "implied_spread_correct": 0,
                "implied_spread_accuracy": 0.0,
                "total_correct": 0,
                "total_accuracy": 0.0,
                "last_updated": None,
                "daily_breakdown": {}
            },
            "combined": {
                "total_predictions": 0,
                "straight_up_correct": 0,
                "straight_up_accuracy": 0.0,
                "last_updated": None
            },
            "rolling_7_day": {
                "with_vegas": {"predictions": 0, "spread_correct": 0, "accuracy": 0.0},
                "without_vegas": {"predictions": 0, "correct": 0, "accuracy": 0.0}
            },
            "rolling_30_day": {
                "with_vegas": {"predictions": 0, "spread_correct": 0, "accuracy": 0.0},
                "without_vegas": {"predictions": 0, "correct": 0, "accuracy": 0.0}
            }
        }
    }

    print("Resetting ATS tracking data...")

    for filename, clean_content in files_to_reset.items():
        filepath = data_dir / filename

        if filepath.exists():
            backup_path = filepath.with_suffix(filepath.suffix + ".backup")
            print(f"  Backing up {filename} -> {backup_path.name}")
            os.rename(filepath, backup_path)

        print(f"  Resetting {filename}")
        with open(filepath, 'w') as f:
            json.dump(clean_content, f, indent=2)

    print("\nReset complete! ATS tracking is now in clean state.")
    print("Backups saved with .backup extension if you need to restore.")


if __name__ == "__main__":
    main()
