#!/usr/bin/env python3
"""
README Updater Script

This script updates the README.md file with:
1. Current ATS accuracy statistics
2. Today's predictions table
3. Top 25 team rankings

Run this after checking results or generating predictions to keep the README up-to-date.
"""
import os
import sys
import re
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.ats_tracker import get_ats_tracker
from src.espn_collector import get_espn_collector
import config


def generate_rankings_section(top_n: int = 25) -> str:
    """Generate Top 25 rankings markdown table."""
    # Import from the same directory - handle both direct run and module run
    try:
        from show_team_ratings_v3 import calculate_team_ratings
    except ImportError:
        from scripts.show_team_ratings_v3 import calculate_team_ratings
    from src.espn_collector import get_espn_collector

    print("📊 Generating Top 25 Rankings...")

    # Get games and calculate ratings
    espn = get_espn_collector()
    games = espn.get_all_games_via_team_schedules(config.CURRENT_SEASON)
    completed = [g for g in games if g.get('HomeTeamScore') is not None]

    print(f"   Processing {len(completed)} completed games...")
    ratings, _ = calculate_team_ratings(completed, min_games=5)

    # Build markdown table
    lines = [
        "",
        "### 🏆 Top 25 Team Rankings",
        "",
        f"*Updated: {datetime.now().strftime('%B %d, %Y')}*",
        "",
        "| Rank | Team | Record | Rating | Off | Def |",
        "|------|------|--------|--------|-----|-----|",
    ]

    for i, team in enumerate(ratings[:top_n], 1):
        record = f"{team['wins']}-{team['losses']}"
        rating = f"{team['overall_rating']:+.1f}"
        off = f"{team['offensive_rating']:.1f}"
        def_ = f"{team['defensive_rating']:.1f}"
        lines.append(f"| {i} | {team['team_name']} | {record} | {rating} | {off} | {def_} |")

    lines.append("")
    lines.append("> *Rankings based on tempo-free efficiency ratings with strength of schedule adjustment.*")
    lines.append("")

    print(f"   ✓ Generated rankings for top {top_n} teams")
    return "\n".join(lines)


def update_readme():
    """Update README.md with current accuracy statistics and rankings."""
    print()
    print("=" * 80)
    print("README UPDATER")
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
    
    # Update rankings section
    print()
    rankings_section = generate_rankings_section(top_n=25)

    rankings_start = "<!-- RANKINGS_START -->"
    rankings_end = "<!-- RANKINGS_END -->"

    if rankings_start in new_content and rankings_end in new_content:
        # Replace existing rankings section
        pattern = f"{re.escape(rankings_start)}.*?{re.escape(rankings_end)}"
        new_content = re.sub(
            pattern,
            f"{rankings_start}\n{rankings_section}\n{rankings_end}",
            new_content,
            flags=re.DOTALL
        )
        print("✓ Found existing rankings section, updating...")
    else:
        # Insert after accuracy section
        insert_pos = new_content.find("<!-- ACCURACY_STATS_END -->")
        if insert_pos > 0:
            insert_pos = new_content.find("\n", insert_pos) + 1
            new_section = f"\n{rankings_start}\n{rankings_section}\n{rankings_end}\n"
            new_content = new_content[:insert_pos] + new_section + new_content[insert_pos:]
            print("✓ No existing rankings section found, adding after accuracy section...")
        else:
            print("⚠️  Could not find ACCURACY_STATS_END marker, skipping rankings insertion")

    # Write updated README
    with open(readme_path, 'w') as f:
        f.write(new_content)

    print(f"✓ README.md updated at {readme_path}")
    print()

    return True


def generate_conference_section(ats_tracker) -> str:
    """Generate ATS accuracy by conference markdown table."""
    espn = get_espn_collector()
    conference_mappings = espn.get_conference_mappings(season=config.CURRENT_SEASON)

    if not conference_mappings:
        return ""

    conf_stats = ats_tracker.get_conference_accuracy(conference_mappings)

    # Filter to conferences with 5+ predictions
    qualified = {k: v for k, v in conf_stats.items() if v["predictions"] >= 5}

    if not qualified:
        return ""

    # Sort by accuracy descending
    sorted_confs = sorted(qualified.items(), key=lambda x: x[1]["accuracy"], reverse=True)

    lines = [
        "#### 🏀 ATS Accuracy by Conference",
        "",
        "| Conference | Record | Accuracy |",
        "|------------|--------|----------|",
    ]

    for conf_name, data in sorted_confs:
        # Trim " Conference" suffix for cleaner display
        display_name = conf_name.replace(" Conference", "")
        wins = data["correct"]
        losses = data["predictions"] - wins
        lines.append(f"| {display_name} | {wins}-{losses} | **{data['accuracy']*100:.1f}%** |")

    lines.append("")
    lines.append("> *A game counts for a conference if either team is a member.*")
    lines.append("")

    return "\n".join(lines)


def generate_accuracy_section(summary: dict) -> str:
    """Generate the markdown content for the accuracy section."""
    ats_tracker = get_ats_tracker()
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
        ])

        # Add yesterday's row if data exists
        yesterday = datetime.now(ZoneInfo("America/New_York")).date() - timedelta(days=1)
        yesterday_key = yesterday.strftime("%Y-%m-%d")
        accuracy_history = ats_tracker.accuracy_history if hasattr(ats_tracker, 'accuracy_history') else {}
        daily_breakdown = accuracy_history.get("with_vegas_lines", {}).get("daily_breakdown", {})
        yesterday_data = daily_breakdown.get(yesterday_key)
        if yesterday_data and yesterday_data.get("predictions", 0) > 0:
            y_correct = yesterday_data["spread_correct"]
            y_total = yesterday_data["predictions"]
            y_wrong = y_total - y_correct
            y_acc = y_correct / y_total * 100
            lines.append(f"| **Yesterday** ({yesterday_key}) | {y_correct}-{y_wrong} | **{y_acc:.1f}%** |")

        lines.extend([
            f"| **Last 7 Days** | {r7['with_vegas']['spread_correct']}-{r7['with_vegas']['predictions'] - r7['with_vegas']['spread_correct']} | **{r7['with_vegas']['accuracy']*100:.1f}%** |",
            f"| **Last 30 Days** | {r30['with_vegas']['spread_correct']}-{r30['with_vegas']['predictions'] - r30['with_vegas']['spread_correct']} | **{r30['with_vegas']['accuracy']*100:.1f}%** |",
            f"| **All-Time** | {vegas_correct}-{all_time['with_vegas_predictions'] - vegas_correct} | **{all_time['with_vegas_spread_accuracy']*100:.1f}%** |",
            "",
        ])
        
        # Over/Under if available
        if all_time['with_vegas_total_accuracy'] > 0:
            lines.append(f"**Over/Under Accuracy**: {all_time['with_vegas_total_accuracy']*100:.1f}%")
            lines.append("")
            
        # Confidence Tiers Table
        tiers = summary.get("confidence_tiers", {})
        if tiers:
            lines.extend([
                "#### 🎯 Accuracy by Confidence (ATS)",
                "",
                "| Confidence | Record | Accuracy |",
                "|------------|--------|----------|",
            ])
            
            # Sort tiers by min confidence
            sorted_tiers = sorted(tiers.items(), key=lambda x: x[1]["min"])
            
            has_tier_data = False
            for key, data in sorted_tiers:
                if data["predictions"] > 0:
                    has_tier_data = True
                    accuracy_fmt = f"**{data['accuracy']*100:.1f}%**"
                    record = f"{data['correct']}-{data['predictions'] - data['correct']}"
                    lines.append(f"| **{data['min']}%+** | {record} | {accuracy_fmt} |")
            
            if not has_tier_data:
                lines.append("| Any | 0-0 | N/A |")

            lines.append("")

        # Conference accuracy section
        conference_section = generate_conference_section(ats_tracker)
        if conference_section:
            lines.append(conference_section)

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
    
    # Combined stats
    if all_time['combined_predictions'] > 0:
        lines.extend([
            "#### Combined Statistics",
            "",
            f"- **Total Predictions**: {all_time['combined_predictions']}",
            f"- **Overall Winner Accuracy**: {all_time['combined_straight_up']*100:.1f}%",
            "",
        ])
    
    # Add Daily Predictions Table
    daily_table = ats_tracker.generate_daily_predictions_table()
    lines.append(daily_table)
    lines.append("")
    
    # Add note about tracking
    lines.extend([
        "> 📈 *ATS = Against The Spread (with Vegas lines). Updated daily via GitHub Actions.*",
        "",
    ])
    
    return "\n".join(lines)


if __name__ == "__main__":
    update_readme()
