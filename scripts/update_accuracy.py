#!/usr/bin/env python3
"""
Script to update accuracy tracking for all dates in the season.
"""
import os
import sys

# Add parent directory to path so we can import from src
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Force SQLite for development
if 'DATABASE_URL' not in os.environ or 'postgresql' in os.environ.get('DATABASE_URL', '').lower():
    os.environ.pop('DATABASE_URL', None)
    os.environ['SQLITE_DB_URL'] = 'sqlite:///./basketball_predictor.db'

import config
from src.accuracy_tracker import AccuracyTracker

def update_accuracy():
    """Update accuracy records for all dates."""
    print("="*70)
    print("UPDATING ACCURACY TRACKING")
    print("="*70)
    
    tracker = AccuracyTracker()
    tracker.update_all_daily_accuracy()
    
    print("\n" + "="*70)
    print("ACCURACY TRACKING UPDATE COMPLETE")
    print("="*70)
    
    # Show summary
    from src.database import get_database, ModelAccuracy
    db = get_database()
    session = db.get_session()
    try:
        total_records = session.query(ModelAccuracy).count()
        print(f"\nTotal accuracy records: {total_records}")
        
        # Show overall accuracy
        overall = db.calculate_accuracy()
        print(f"\nOverall Season Accuracy:")
        print(f"  Total predictions: {overall['total_predictions']}")
        print(f"  Spread accuracy: {overall['spread_accuracy']*100:.1f}%")
        print(f"  Total accuracy: {overall['total_accuracy']*100:.1f}%")
        print(f"  RMSE (margin): {overall['rmse_spread']:.2f} points")
        print(f"  RMSE (total): {overall['rmse_total']:.2f} points")
    finally:
        session.close()

if __name__ == "__main__":
    try:
        update_accuracy()
    except KeyboardInterrupt:
        print("\n\n⚠ Process interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

