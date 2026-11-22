# DantBook — Current Shared Task

**Last checked:** 22 November 2026, 09:52 AM IST  
**Baseline archive:** `v0.1.2 Medical History UI` (preserved in ChatGPT Library)  
**Current source activity:** Main CI success; Open PRs: #12 docs: add Codex development workflow (CI success); #11 feat: add branch-scoped dental laboratory case API (CI failure).

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

Current checkpoint: **7/39 — Medical History data model and migration acceptance** (pending; Next checkpoint; no acceptance evidence recorded yet.). Checkpoint statuses are tracked separately from overall/module progress.

## Progress evidence
Percentages live in `progress-manifest.json`. Review acceptance criteria and tests before changing values; no automatic increases based on activity alone.

## Permanent exclusions
Digital treatment consent/consent management, enterprise features, initial-release X-ray/photo storage, NanoPix integration, and periodontal charting remain excluded.

<!-- AUTO-SYNC START -->
## Automatically verified GitHub snapshot

**Checked:** 22 November 2026, 09:52 AM IST

- Open PRs: [#12 — docs: add Codex development workflow](https://github.com/drpast/dantbook-master/pull/12) (open-draft; CI **success**); [#11 — feat: add branch-scoped dental laboratory case API](https://github.com/drpast/dantbook-master/pull/11) (open-draft; CI **failure**)
- Main CI: **success** ([run](https://github.com/drpast/dantbook-master/actions/runs/44948187965))
- Main commit: [e711c78](https://github.com/drpast/dantbook-master/commit/e711c78569257c7370a2fa9fa4fd43bcd672daf6) — feat: add branch inventory workspace (#10)
- Progress manifest reviewed: **2026-11-22**; overall **25%**.
- PR work is not treated as merged or complete; progress is changed only from evidence-reviewed manifest.

Progress is read from progress-manifest.json and is updated only after evidence review.
<!-- AUTO-SYNC END -->


## Current desktop view
The desktop app now displays an installer-style live task: task-level progress plus one row per involved file/activity, each with its own bar, status, and explanatory note. It no longer renders the long checkpoint list as the main task view.
