"""
Master script to run all three backtesting options sequentially.
Provides comprehensive validation of the rating system.
"""
import sys
import os
import time
from datetime import datetime

# Add parent directory to path so we can import from validation modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def run_all_backtests():
    """Run all three backtesting options and generate summary report."""
    
    print("\n" + "="*100)
    print("COMPREHENSIVE BACKTESTING SUITE")
    print("="*100)
    print()
    print("This will run three independent validation methods:")
    print("  1. Last Season Validation (2024-25)")
    print("  2. Rolling Validation (Current Season)")
    print("  3. Cross-Validation (5-Fold)")
    print()
    print("Estimated time: 10-15 minutes")
    print("="*100)
    print()
    
    print("Starting backtesting automatically...")
    # input("Press Enter to start backtesting...")  # Commented out for automated testing
    
    results = {}
    start_time = time.time()
    
    # Option 1: Last Season
    print("\n" + "█"*100)
    print("█" + " "*40 + "OPTION 1: LAST SEASON" + " "*39 + "█")
    print("█"*100 + "\n")
    
    try:
        from backtest_option1_last_season import backtest_last_season
        backtest_last_season()
        results['option1'] = 'COMPLETED'
    except Exception as e:
        print(f"✗ Option 1 failed: {e}")
        results['option1'] = f'FAILED: {e}'
    
    print("\n")
    time.sleep(2)
    
    # Option 2: Rolling Validation
    print("\n" + "█"*100)
    print("█" + " "*35 + "OPTION 2: ROLLING VALIDATION" + " "*36 + "█")
    print("█"*100 + "\n")
    
    try:
        from backtest_option2_rolling import backtest_rolling_current_season
        backtest_rolling_current_season()
        results['option2'] = 'COMPLETED'
    except Exception as e:
        print(f"✗ Option 2 failed: {e}")
        results['option2'] = f'FAILED: {e}'
    
    print("\n")
    time.sleep(2)
    
    # Option 3: Cross-Validation
    print("\n" + "█"*100)
    print("█" + " "*34 + "OPTION 3: CROSS-VALIDATION" + " "*39 + "█")
    print("█"*100 + "\n")
    
    try:
        from backtest_option3_cross_validation import backtest_cross_validation
        backtest_cross_validation(k_folds=5)
        results['option3'] = 'COMPLETED'
    except Exception as e:
        print(f"✗ Option 3 failed: {e}")
        results['option3'] = f'FAILED: {e}'
    
    # Summary
    elapsed_time = time.time() - start_time
    
    print("\n\n" + "="*100)
    print("BACKTESTING SUITE COMPLETE")
    print("="*100)
    print()
    print(f"Total Time: {elapsed_time/60:.1f} minutes")
    print()
    print("Results:")
    for option, status in results.items():
        status_symbol = "✓" if status == 'COMPLETED' else "✗"
        print(f"  {status_symbol} {option.upper()}: {status}")
    
    print()
    print("Output Files Generated:")
    print("  • backtest_results_option1_last_season.txt")
    print("  • backtest_results_option2_rolling.txt")
    print("  • backtest_results_option3_cross_validation.txt")
    print()
    print("Next Steps:")
    print("  1. Review detailed results in output files")
    print("  2. Compare accuracies across methods")
    print("  3. Analyze prediction errors and patterns")
    print("  4. Identify areas for improvement (Phase 2)")
    print()
    print("="*100)
    print()

if __name__ == "__main__":
    run_all_backtests()

