#!/usr/bin/env python3
"""
Script to populate database with all games from the 2025-26 season.
This "trains" the predictor up to the current date so it has accurate ratings.
"""
import os
import sys
from datetime import datetime

# Add parent directory to path so we can import from src
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Force SQLite for development if needed
if 'DATABASE_URL' not in os.environ or 'postgresql' in os.environ.get('DATABASE_URL', '').lower():
    os.environ.pop('DATABASE_URL', None)
    os.environ['SQLITE_DB_URL'] = 'sqlite:///./basketball_predictor.db'

import config
from src.database import get_database, Prediction, GameResult
from src.predictor import get_predictor
from src.espn_collector import get_espn_collector

def populate_season():
    """Process all games from the 2025-26 season."""
    print("="*70)
    print(f"POPULATING {config.CURRENT_SEASON} SEASON DATA")
    print("="*70)
    
    # Initialize components
    db = get_database()
    predictor = get_predictor()
    # Reset predictor state to ensure clean slate
    predictor.initialized = False
    predictor.ukf.states = {} 
    
    espn = get_espn_collector()
    
    # Get all completed games using date range (FASTER than team schedules)
    print("\nFetching games from ESPN (date-by-date)...")
    
    # Season start: Nov 4, 2025
    start_date = datetime(2025, 11, 4)
    end_date = datetime.now()
    
    # Use get_games_for_season which iterates dates if start/end provided
    # Or just call get_games_for_date in a loop here for visibility
    
    completed_games = []
    current_date = start_date
    while current_date <= end_date:
        date_str = current_date.strftime('%Y-%m-%d')
        print(f"  Fetching {date_str}...", end='\r')
        
        try:
            day_games = espn.get_games_for_date(current_date)
            valid_games = [
                g for g in day_games 
                if g.get('HomeTeamScore') is not None 
                and g.get('AwayTeamScore') is not None
                and g.get('HomeTeamID') is not None
                and g.get('AwayTeamID') is not None
            ]
            completed_games.extend(valid_games)
        except Exception as e:
            print(f"\n  ⚠️ Error fetching {date_str}: {e}")
            
        current_date = datetime.fromtimestamp(current_date.timestamp() + 86400)
    
    print(f"\n✓ Found {len(completed_games)} completed games")
    
    # Parse dates and sort chronologically
    for game in completed_games:
        try:
            game['date_obj'] = datetime.fromisoformat(game.get('DateTime', '').replace('Z', '+00:00'))
        except:
            game['date_obj'] = datetime.now() # Should not happen often
            
    completed_games.sort(key=lambda x: x['date_obj'])
    
    print(f"✓ Found {len(completed_games)} completed games")
    
    if not completed_games:
        print("❌ No completed games found! Check season configuration.")
        return

    # Check what we already have in DB
    session = db.get_session()
    try:
        existing_preds = session.query(Prediction).count()
        print(f"Current predictions in database: {existing_preds}")
    finally:
        session.close()
    
    # Process ALL games through the predictor to update ratings
    # We do this even if they are in DB, to ensure UKF state is built correctly in-memory
    # (The DB is for persistent storage, but UKF needs sequential processing)
    print(f"\nProcessing {len(completed_games)} games to update team ratings...")
    
    processed_count = 0
    saved_count = 0
    
    for i, game in enumerate(completed_games):
        # Update progress
        if i % 100 == 0:
            print(f"  Processed {i}/{len(completed_games)} games...")
            
        # 1. Update UKF state
        try:
            # this method updates the team ratings based on the game result
            predictor._process_completed_game(game, completed_games, i)
            processed_count += 1
        except Exception as e:
            print(f"  ⚠️ Error processing game {game.get('GameID')}: {e}")
            continue
            
        # 2. Save to database if not exists (optional, but good for history)
        # We can skip this if we just want to train the model, but saving is better
        # For speed, we might only save if the DB is empty or we specifically want to backfill
        # Let's save new ones
        
        game_id = game.get('GameID')
        # ... logic to save to DB ...
        # (Skipping DB save for every game to keep this script focused on training state
        #  unless you want a full DB backfill)
        
    print(f"\n✓ Processed {processed_count} games through UKF predictor")
    
    # Save the current state of the predictor (if predictor supports state persistence)
    # Currently predictor rebuilds state on init. 
    # To make this persistent for daily_collect_odds.py, we rely on DataCollector caching
    # or the fact that daily_collect_odds.py calls initialize().
    
    # IMPORTANT: The daily_collect_odds.py script calls get_predictor().initialize().
    # initialize() calls collector.get_completed_games().
    # If collector.get_completed_games() returns the games we just fetched, we are good.
    # The default DataCollector (in src/data_collector.py) might be failing to get games.
    
    # We need to ensure the DataCollector cache is populated with these games.
    # src/data_collector.py uses a cache file.
    
    print("\nUpdating DataCollector cache...")
    # Get the global collector used by the application
    from src.data_collector import get_collector
    app_collector = get_collector()
    
    # Force save to cache so other scripts see these games
    cache_key = f"completed_games_{config.CURRENT_SEASON}"
    cache_games = []
    for game in completed_games:
        cleaned = dict(game)
        if isinstance(cleaned.get('date_obj'), datetime):
            cleaned['date_obj'] = cleaned['date_obj'].isoformat()
        cache_games.append(cleaned)
    app_collector._save_to_cache(cache_key, cache_games)
    print(f"✓ Cached {len(completed_games)} games to {app_collector._get_cache_path(cache_key)}")
    
    print("\n" + "="*70)
    print("SEASON DATA POPULATION COMPLETE")
    print("="*70)
    print("The predictor should now have access to historical data for accurate ratings.")

if __name__ == "__main__":
    populate_season()
