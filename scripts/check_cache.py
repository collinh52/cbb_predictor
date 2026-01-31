#!/usr/bin/env python3
"""
Check cache status and manage historical game data cache.

This helps avoid API quota issues by showing cache age and allowing manual refresh.
"""
import os
import sys
from pathlib import Path
from datetime import datetime, timedelta
import json

# Add project root to path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

import config


def check_cache_status():
    """Check the status of all cache files."""
    cache_dir = Path(config.CACHE_DIR)

    if not cache_dir.exists():
        print("❌ Cache directory not found:", cache_dir)
        return

    print("=" * 80)
    print("CACHE STATUS")
    print("=" * 80)
    print()
    print(f"Cache directory: {cache_dir}")
    print(f"Cache expiry: {config.CACHE_EXPIRY_MINUTES} minutes ({config.CACHE_EXPIRY_MINUTES / 1440:.1f} days)")
    print()

    # Find all cache files
    cache_files = list(cache_dir.glob("*.json"))

    if not cache_files:
        print("❌ No cache files found")
        print()
        print("Run this to populate cache:")
        print("  python scripts/setup_and_train.py --populate 200 --train")
        return

    # Check completed games cache specifically
    completed_games_files = [f for f in cache_files if 'completed_games' in f.name]

    if not completed_games_files:
        print("❌ No completed games cache found")
        print()
        print("Run this to populate cache:")
        print("  python scripts/setup_and_train.py --populate 200 --train")
        return

    print(f"✓ Found {len(cache_files)} cache files")
    print()

    # Analyze completed games cache
    for cache_file in completed_games_files:
        print("-" * 80)
        print(f"File: {cache_file.name}")

        # Get file size
        size_mb = cache_file.stat().st_size / (1024 * 1024)
        print(f"  Size: {size_mb:.2f} MB")

        # Get modification time
        mod_time = datetime.fromtimestamp(cache_file.stat().st_mtime)
        age = datetime.now() - mod_time
        print(f"  Last modified: {mod_time.strftime('%Y-%m-%d %H:%M:%S')} ({age.days} days, {age.seconds // 3600} hours ago)")

        # Check if expired
        expiry_time = timedelta(minutes=config.CACHE_EXPIRY_MINUTES)
        if age > expiry_time:
            print(f"  Status: ❌ EXPIRED (older than {config.CACHE_EXPIRY_MINUTES / 1440:.1f} days)")
            print(f"  Action: Will fetch fresh data on next run")
        else:
            remaining = expiry_time - age
            print(f"  Status: ✅ VALID (expires in {remaining.days} days, {remaining.seconds // 3600} hours)")

        # Try to read and count games
        try:
            with open(cache_file, 'r') as f:
                data = json.load(f)
                games = data.get('data', [])
                print(f"  Games cached: {len(games)}")
        except Exception as e:
            print(f"  Error reading cache: {e}")

        print()

    # Summary
    print("=" * 80)
    print("RECOMMENDATIONS")
    print("=" * 80)
    print()

    expired_count = sum(1 for f in completed_games_files
                       if datetime.now() - datetime.fromtimestamp(f.stat().st_mtime)
                       > timedelta(minutes=config.CACHE_EXPIRY_MINUTES))

    if expired_count > 0:
        print("⚠️  Some cache files are expired")
        print()
        print("Option 1: Refresh cache (requires API calls)")
        print("  rm data/cache/completed_games_*.json")
        print("  python scripts/setup_and_train.py --populate 200 --train")
        print()
        print("Option 2: Extend cache expiry in config.py")
        print("  Change CACHE_EXPIRY_MINUTES to a larger value (e.g., 10080 for 7 days)")
    else:
        print("✅ All cache files are valid")
        print()
        print("You can run predictions without API quota issues:")
        print("  python scripts/predict_today.py --days 1")


def delete_cache(cache_type='all'):
    """Delete cache files."""
    cache_dir = Path(config.CACHE_DIR)

    if cache_type == 'all':
        files_to_delete = list(cache_dir.glob("*.json"))
    elif cache_type == 'completed':
        files_to_delete = list(cache_dir.glob("completed_games_*.json"))
    else:
        print(f"Unknown cache type: {cache_type}")
        return

    if not files_to_delete:
        print("No cache files to delete")
        return

    print(f"Deleting {len(files_to_delete)} cache files...")
    for f in files_to_delete:
        f.unlink()
        print(f"  Deleted: {f.name}")

    print()
    print("Cache cleared. Run this to repopulate:")
    print("  python scripts/setup_and_train.py --populate 200 --train")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Manage prediction cache")
    parser.add_argument('--delete', choices=['all', 'completed'],
                       help="Delete cache files")

    args = parser.parse_args()

    if args.delete:
        delete_cache(args.delete)
    else:
        check_cache_status()
