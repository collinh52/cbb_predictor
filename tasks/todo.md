# Task List

This file tracks current and completed tasks for the project.

## Active Tasks

- [ ] Retrain ML model with fixed features (required after feature changes)

## Completed Tasks

- [x] Initial CLAUDE.md created with workflow guidelines (2026-02-02)
- [x] Fix 5 critical bugs in prediction algorithm (2026-02-02)
  - Fixed ML model verbose parameter bug
  - Fixed UKF pace normalization inconsistency (70→100)
  - Fixed home/away feature asymmetry (added away_home_adv)
  - Added hybrid weight normalization
  - Removed Vegas lines from ML features (data leakage fix)
- [x] Unify storage to database (2026-02-02)
  - Added database saving in daily_collect_odds.py (both main flow and ESPN fallback)

## Task Template

When starting a new task, use this format:

```markdown
### [Task Name]
**Started**: [Date]
**Status**: [ ] Not Started / [~] In Progress / [x] Complete

**Description**:
Brief description of what needs to be done

**Plan**:
1. Step 1
2. Step 2
3. Step 3

**Verification**:
- [ ] Tests pass
- [ ] Manual testing completed
- [ ] Code reviewed for elegance

**Results**:
Summary of what was accomplished
```

---
