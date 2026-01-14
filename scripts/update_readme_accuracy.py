#!/usr/bin/env python3
"""
README Accuracy Updater Script

This script updates the README.md file with current ATS accuracy statistics.
It looks for markers in the README and replaces the content between them.

Run this after checking results to keep the README up-to-date.
"""
import os
import sys
import re
from datetime import datetime

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.ats_tracker import get_ats_tracker


def update_readme():
    """Update README.md with current accuracy statistics."""
    print()
    print("=" * 80)
    print("README ACCURACY UPDATER")
    print("=" * 80)
    print()
    
    # Paths
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    readme_path = os.path.join(project_root, "README.md")
    
    # Get current accuracy stats
    ats_tracker = get_ats_tracker()
    summary = ats_tracker.get_accuracy_summary()
    all_time = summary["all_time"]
    r7 = summary["rolling_7_day"]
    r30 = summary["rolling_30_day"]
    
    print("📊 Current Accuracy Stats:")
    print(f"   With Vegas Lines: {all_time['with_vegas_spread_accuracy']*100:.1f}% ({all_time['with_vegas_predictions']} games)")
    print(f"   Without Vegas Lines: {all_time['without_vegas_accuracy']*100:.1f}% ({all_time['without_vegas_predictions']} games)")
    print(f"   Combined: {all_time['combined_straight_up']*100:.1f}% ({all_time['combined_predictions']} games)")
    print()
    
    # Generate the accuracy section
    accuracy_section = generate_accuracy_section(summary)
    
    # Read current README
    if not os.path.exists(readme_path):
        print(f"❌ README.md not found at {readme_path}")
        return False
    
    with open(readme_path, 'r') as f:
        readme_content = f.read()
    
    # Check for markers
    start_marker = "<!-- ACCURACY_STATS_START -->"
    end_marker = "<!-- ACCURACY_STATS_END -->"
    
    if start_marker in readme_content and end_marker in readme_content:
        # Replace existing section
        pattern = f"{re.escape(start_marker)}.*?{re.escape(end_marker)}"
        new_content = re.sub(
            pattern,
            f"{start_marker}\n{accuracy_section}\n{end_marker}",
            readme_content,
            flags=re.DOTALL
        )
        print("✓ Found existing accuracy section, updating...")
    else:
        # Insert new section after "## ✨ Key Features" or at the end
        insert_after = "## 📈 Performance Metrics"
        
        if insert_after in readme_content:
            # Find the end of Performance Metrics section
            insert_pos = readme_content.find(insert_after)
            next_section = readme_content.find("\n## ", insert_pos + len(insert_after))
            
            if next_section > 0:
                # Insert before next section
                new_section = f"\n{start_marker}\n{accuracy_section}\n{end_marker}\n"
                new_content = (
                    readme_content[:next_section] +
                    new_section +
                    readme_content[next_section:]
                )
            else:
                # Append at end
                new_section = f"\n\n{start_marker}\n{accuracy_section}\n{end_marker}\n"
                new_content = readme_content + new_section
        else:
            # Just append at end
            new_section = f"\n\n{start_marker}\n{accuracy_section}\n{end_marker}\n"
            new_content = readme_content + new_section
        
        print("✓ No existing accuracy section found, adding new section...")
    
    # Write updated README
    with open(readme_path, 'w') as f:
        f.write(new_content)
    
    print(f"✓ README.md updated at {readme_path}")
    print()
    
    return True


def generate_accuracy_section(summary: dict) -> str:
    """Generate the markdown content for the accuracy section."""
    all_time = summary["all_time"]
    r7 = summary["rolling_7_day"]
    r30 = summary["rolling_30_day"]
    last_updated = summary["last_updated"] or datetime.now().isoformat()
    
    # Format the timestamp
    try:
        dt = datetime.fromisoformat(last_updated.replace('Z', '+00:00'))
        formatted_date = dt.strftime("%B %d, %Y at %I:%M %p")
    except:
        formatted_date = last_updated
    
    # Determine accuracy level for badges
    def get_badge_color(accuracy: float) -> str:
        if accuracy >= 0.55:
            return "brightgreen"
        elif accuracy >= 0.52:
            return "green"
        elif accuracy >= 0.50:
            return "yellowgreen"
        elif accuracy >= 0.48:
            return "yellow"
        else:
            return "red"
    
    # Calculate correct counts
    vegas_correct = int(all_time['with_vegas_predictions'] * all_time['with_vegas_spread_accuracy'])
    no_vegas_correct = int(all_time['without_vegas_predictions'] * all_time['without_vegas_accuracy'])
    combined_correct = int(all_time['combined_predictions'] * all_time['combined_straight_up'])
    
    vegas_color = get_badge_color(all_time['with_vegas_spread_accuracy'])
    
    # Build the section - PRIORITIZE TRUE ATS (with Vegas lines)
    lines = [
        "",
        "### 🎯 Live ATS Prediction Tracking",
        "",
        f"**Last Updated**: {formatted_date}",
        "",
    ]
    
    # Primary badge: True ATS accuracy (with Vegas lines)
    if all_time['with_vegas_predictions'] > 0:
        vegas_pct = all_time['with_vegas_spread_accuracy'] * 100
        lines.append(f"![ATS Accuracy](https://img.shields.io/badge/ATS_Record-{vegas_pct:.1f}%25-{vegas_color})")
        lines.append("")
        
        # FEATURED: Rolling ATS Performance (True ATS with Vegas lines)
        lines.extend([
            "#### 🏆 Rolling ATS Performance",
            "",
            "| Timeframe | ATS Record | Accuracy |",
            "|-----------|------------|----------|",
            f"| **Last 7 Days** | {r7['with_vegas']['spread_correct']}-{r7['with_vegas']['predictions'] - r7['with_vegas']['spread_correct']} | **{r7['with_vegas']['accuracy']*100:.1f}%** |",
            f"| **Last 30 Days** | {r30['with_vegas']['spread_correct']}-{r30['with_vegas']['predictions'] - r30['with_vegas']['spread_correct']} | **{r30['with_vegas']['accuracy']*100:.1f}%** |",
            f"| **All-Time** | {vegas_correct}-{all_time['with_vegas_predictions'] - vegas_correct} | **{all_time['with_vegas_spread_accuracy']*100:.1f}%** |",
            "",
        ])
        
        # Over/Under if available
        if all_time['with_vegas_total_accuracy'] > 0:
            lines.append(f"**Over/Under Accuracy**: {all_time['with_vegas_total_accuracy']*100:.1f}%")
            lines.append("")
    else:
        lines.extend([
            "#### 🏆 Rolling ATS Performance",
            "",
            "*No predictions with Vegas lines yet. ATS tracking will begin once odds data is collected.*",
            "",
        ])
    
    # Secondary: Straight-up stats (without Vegas lines)
    if all_time['without_vegas_predictions'] > 0:
        lines.extend([
            "#### Straight-Up Predictions (Games Without Vegas Lines)",
            "",
            f"| **7-Day** | {r7['without_vegas']['correct']}/{r7['without_vegas']['predictions']} ({r7['without_vegas']['accuracy']*100:.1f}%) |",
            f"| **30-Day** | {r30['without_vegas']['correct']}/{r30['without_vegas']['predictions']} ({r30['without_vegas']['accuracy']*100:.1f}%) |",
            f"| **All-Time** | {no_vegas_correct}/{all_time['without_vegas_predictions']} ({all_time['without_vegas_accuracy']*100:.1f}%) |",
            "",
        ])
    
    # Total predictions summary
    if all_time['combined_predictions'] > 0:
        lines.extend([
            f"**Total Predictions Tracked**: {all_time['combined_predictions']}",
            "",
        ])
    
    # Add note about tracking
    lines.extend([
        "> 📈 *ATS = Against The Spread (with Vegas lines). Updated daily via GitHub Actions.*",
        "",
    ])
    
    return "\n".join(lines)


if __name__ == "__main__":
    update_readme()

