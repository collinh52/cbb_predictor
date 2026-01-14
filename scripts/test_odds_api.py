"""
Test script for The Odds API integration.
"""
import os
import sys

# Add parent directory to path so we can import from src
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.pop('DATABASE_URL', None)

from src.odds_collector import get_odds_collector
from src.data_collector import get_collector
from datetime import datetime

def test_odds_api():
    """Test The Odds API connection and data."""
    print("\n" + "="*70)
    print("TESTING THE ODDS API INTEGRATION")
    print("="*70 + "\n")
    
    odds_collector = get_odds_collector()
    
    # Test 1: Check if API key is configured
    if not odds_collector.api_key:
        print("❌ THE_ODDS_API_KEY not configured in .env file")
        return
    
    print("✓ API key found")
    print()
    
    # Test 2: Get available sports
    print("Fetching available sports...")
    sports = odds_collector.get_sports_list()
    
    if sports:
        print(f"✓ Found {len(sports)} sports")
        # Check if NCAAB is available
        ncaab = [s for s in sports if 'basketball_ncaab' in s.get('key', '')]
        if ncaab:
            print(f"✓ College Basketball (NCAAB) is available")
            print(f"  - Active: {ncaab[0].get('active')}")
            print(f"  - Title: {ncaab[0].get('title')}")
        else:
            print("⚠ College Basketball not found in available sports")
    else:
        print("❌ Could not fetch sports list")
    print()
    
    # Test 3: Get current NCAAB odds
    print("Fetching current NCAAB odds...")
    odds_data = odds_collector.get_ncaab_odds()
    
    if odds_data:
        print(f"✓ Found {len(odds_data)} games with odds")
        print()
        
        # Display first few games
        print("Sample games (first 5):")
        print("-" * 70)
        for i, game in enumerate(odds_data[:5]):
            home = game.get('home_team')
            away = game.get('away_team')
            commence = game.get('commence_time')
            
            print(f"\n{i+1}. {away} @ {home}")
            print(f"   Commence: {commence}")
            
            # Extract spread and total
            bookmakers = game.get('bookmakers', [])
            if bookmakers:
                bookie = bookmakers[0]
                print(f"   Bookmaker: {bookie.get('title')}")
                
                for market in bookie.get('markets', []):
                    if market.get('key') == 'spreads':
                        outcomes = market.get('outcomes', [])
                        for outcome in outcomes:
                            name = outcome.get('name')
                            point = outcome.get('point')
                            price = outcome.get('price')
                            print(f"   Spread - {name}: {point:+.1f} ({price:+d})")
                    
                    elif market.get('key') == 'totals':
                        outcomes = market.get('outcomes', [])
                        for outcome in outcomes:
                            name = outcome.get('name')
                            point = outcome.get('point')
                            price = outcome.get('price')
                            print(f"   Total - {name}: {point:.1f} ({price:+d})")
    else:
        print("❌ No odds data found. Possible reasons:")
        print("   - No games currently scheduled")
        print("   - API key invalid")
        print("   - Rate limit exceeded")
    print()
    
    # Test 4: Test integration with data collector
    print("="*70)
    print("TESTING INTEGRATION WITH DATA COLLECTOR")
    print("="*70 + "\n")
    
    collector = get_collector()
    print("Fetching today's games with odds...")
    games = collector.get_todays_games(use_odds_api=True)
    
    if games:
        print(f"✓ Found {len(games)} games for today")
        
        # Check how many have odds
        games_with_spread = sum(1 for g in games if g.get('PointSpread') is not None)
        games_with_total = sum(1 for g in games if g.get('OverUnder') is not None)
        
        print(f"  - Games with spread: {games_with_spread}/{len(games)}")
        print(f"  - Games with total: {games_with_total}/{len(games)}")
        
        # Show a sample game
        if games:
            print("\nSample game:")
            game = games[0]
            print(f"  {game.get('AwayTeam')} @ {game.get('HomeTeam')}")
            print(f"  Spread: {game.get('PointSpread')}")
            print(f"  Total: {game.get('OverUnder')}")
            print(f"  DateTime: {game.get('DateTime')}")
    else:
        print("⚠ No games found for today")
    
    print("\n" + "="*70)
    print("TEST COMPLETE")
    print("="*70 + "\n")

if __name__ == "__main__":
    test_odds_api()

