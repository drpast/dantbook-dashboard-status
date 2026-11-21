# DantBook — Current Shared Task

**Last checked:** 21 November 2026  
**Baseline archive:** `v0.1.2 Medical History UI` (preserved in ChatGPT Library)  
**Current source activity:** PR #4 is the active task; PR #3 is review-ready. The archived baseline is tracked separately from GitHub implementation activity.

## Verified CI
- PR #1 baseline verification: **merged**.
- PR #2 authenticated patient workflow API tests: **merged**.
- Latest reported successful run: [44922607698](https://github.com/drpast/dantbook-master/actions/runs/44922607698).
- Job step readback confirms success for migrations, foundation checks, PostgreSQL RLS, shared patient access boundaries, concurrent patient-number allocation, workspace type-check, and workspace build.
- Earlier run [44918122856](https://github.com/drpast/dantbook-master/actions/runs/44918122856) failed with migration error 42830. Treat that as historical; the later run passed the listed checks. PR changes are not merged into main.
- Main CI remains reported as `not-found` in the current snapshot.

## Step-by-step task tracker
1. Workspace and engineering scaffold — complete.
2. CI baseline and migration verification — complete (PR #1 merged).
3. Authenticated patient workflow API tests — complete (PR #2 merged).
4. Patient workflow browser acceptance — review-ready (PR #3 open draft; CI passed; not merged).
5. Medical History alert and correction browser tests — **in progress** (PR #4 open draft; CI in progress).
6. Review and merge open acceptance PRs — pending.
7. Medical History implementation acceptance — pending.
8. MVP integration, QA and release acceptance — pending.

Current active step: **5 of 8**. Step state is separate from overall/module percentages.

## Progress evidence
Percentages live in `progress-manifest.json`. Review acceptance criteria and tests before changing values; no automatic increases based on activity alone.

## Permanent exclusions
Digital treatment consent/consent management, enterprise features, initial-release X-ray/photo storage, NanoPix integration, and periodontal charting remain excluded.

<!-- AUTO-SYNC START -->
## Automatically verified GitHub snapshot

**Checked:** 21 November 2026, 11:33 PM IST

- Open PR: [#4 — test: cover medical history alert and correction workflow](https://github.com/drpast/dantbook-master/pull/4) (open-draft); branch CI: **in_progress**.
- Main CI: **success** ([run](https://github.com/drpast/dantbook-master/actions/runs/44927274198))
- Main commit: [efa75f6](https://github.com/drpast/dantbook-master/commit/efa75f6ce3eaff024f41c3b8aabd59dcb404d60c) — test: verify authenticated patient workflows
- Progress manifest reviewed: **2026-11-21**; overall **25%**.
- PR work is not treated as merged or complete; progress is changed only from evidence-reviewed manifest.

Progress is read from progress-manifest.json and is updated only after evidence review.
<!-- AUTO-SYNC END -->
