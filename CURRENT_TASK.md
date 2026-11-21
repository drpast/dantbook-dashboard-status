# DantBook — Current Shared Task

**Last checked:** 21 November 2026  
**Baseline archive:** `v0.1.2 Medical History UI` (preserved in ChatGPT Library)  
**Current source activity:** PR #4 is the active task; PR #3 is review-ready. The archived baseline is tracked separately from GitHub implementation activity.

## Verified CI
- PR #1 baseline verification: **merged**.
- PR #2 authenticated patient workflow API tests: **merged**.
- Latest reported successful main CI: [44927274198](https://github.com/drpast/dantbook-master/actions/runs/44927274198).
- Job step readback confirms success for migrations, foundation checks, PostgreSQL RLS, shared patient access boundaries, concurrent patient-number allocation, workspace type-check, and workspace build.
- Earlier migration failure [44918122856](https://github.com/drpast/dantbook-master/actions/runs/44918122856) is historical; subsequent CI passed the listed checks.
- Main CI is currently reported as **success**.

## Granular task tracker

The tracker now contains **39 checkpoints** across seven work groups:

- Engineering foundation: 6 checkpoints
- Medical History: 7 checkpoints
- Finance: 5 checkpoints
- Dental Laboratory: 5 checkpoints
- Recall & Follow-up: 5 checkpoints
- Integration & testing: 7 checkpoints
- Release & deployment: 4 checkpoints

Current checkpoint: **5/39 — Medical History alert and correction browser tests** (PR #4 open draft; CI in progress). PR #3 has passed CI but remains an unmerged draft. Checkpoint statuses are tracked separately from overall/module progress.

## Progress evidence
Percentages live in `progress-manifest.json`. Review acceptance criteria and tests before changing values; no automatic increases based on activity alone.

## Permanent exclusions
Digital treatment consent/consent management, enterprise features, initial-release X-ray/photo storage, NanoPix integration, and periodontal charting remain excluded.

<!-- AUTO-SYNC START -->
## Automatically verified GitHub snapshot

**Checked:** 22 November 2026, 03:58 AM IST

- Open PR: [#12 — docs: add Codex development workflow](https://github.com/drpast/dantbook-master/pull/12) (open-draft); branch CI: **success**.
- Main CI: **success** ([run](https://github.com/drpast/dantbook-master/actions/runs/44948187965))
- Main commit: [e711c78](https://github.com/drpast/dantbook-master/commit/e711c78569257c7370a2fa9fa4fd43bcd672daf6) — feat: add branch inventory workspace (#10)
- Progress manifest reviewed: **2026-11-21**; overall **25%**.
- PR work is not treated as merged or complete; progress is changed only from evidence-reviewed manifest.

Progress is read from progress-manifest.json and is updated only after evidence review.
<!-- AUTO-SYNC END -->


## Current desktop view
The desktop app now displays an installer-style live task: task-level progress plus one row per involved file/activity, each with its own bar, status, and explanatory note. It no longer renders the long checkpoint list as the main task view.
