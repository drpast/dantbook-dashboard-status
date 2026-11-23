# DantBook — Current Shared Task

**Last checked:** 23 November 2026, 09:38 AM IST  
**Baseline archive:** `v0.1.2 Medical History UI` (preserved in ChatGPT Library)  
**Current source activity:** Main CI success; Open PRs: #15 test: medical history data model and migration acceptance (CI success).

## Verified CI
- Latest main commit: [11cb60e](https://github.com/drpast/dantbook-master/commit/11cb60e7ee89997e78f1923500ae6724778a6884). The connector's surfaced run [45079706235](https://github.com/drpast/dantbook-master/actions/runs/45079706235) is the **dashboard-notification workflow** (job `notify` only), not CI. Direct CI for this merge commit is **unverified**.
- PR #11 Dental Laboratory case API: **merged**. Earlier CI [44949784904](https://github.com/drpast/dantbook-master/actions/runs/44949784904) failed at Prisma generation (P1012), but the final rerun [45041948662](https://github.com/drpast/dantbook-master/actions/runs/45041948662) passed; the PR was merged.
- PR #12 Codex development workflow docs: **merged**; final CI [45042687063](https://github.com/drpast/dantbook-master/actions/runs/45042687063) passed.
- PR #13 immediate dashboard notification: **merged**.
- PR #15 Medical History data-model acceptance: **open draft**; CI **success** [45079372471](https://github.com/drpast/dantbook-master/actions/runs/45079372471). It is not merged and does not complete checkpoint 7/39 yet.
- PR #15's dashboard-notification run [45079372414](https://github.com/drpast/dantbook-master/actions/runs/45079372414) also passed; this is separate from CI.

## Recently merged milestones
- PRs #3 and #4 merged with passing acceptance CI; PRs #5–#10 also merged with passing CI.
- PR #11 Dental Laboratory case API, #12 Codex workflow docs, and #13 dashboard notification are merged. PR #11's initial P1012 failure was superseded by a successful rerun.
- PR #15 adds live Medical History data-model/migration acceptance coverage. Its CI passed, but it remains an **open draft** awaiting owner review/merge. Checkpoint 7/39 remains pending; no progress percentage changed.

## Granular task tracker

The tracker contains **39 checkpoints** across seven work groups:

- Engineering foundation: 6 checkpoints
- Medical History: 7 checkpoints
- Finance: 5 checkpoints
- Dental Laboratory: 5 checkpoints
- Recall & Follow-up: 5 checkpoints
- Integration & testing: 7 checkpoints
- Release & deployment: 4 checkpoints

Current checkpoint: **7/39 — Medical History data model and migration acceptance** (pending; PR #15 open draft; CI success (45079372471). Checkpoint awaits review/merge and verified acceptance.). Checkpoint statuses are tracked separately from overall/module progress.

## Progress evidence
Progress percentages live in `progress-manifest.json`. Reviewed **23 November 2026** for repository and checkpoint status. Overall remains **25%**; module percentages and task completion were not increased. PR #15 CI alone is not sufficient to complete checkpoint 7.

## Permanent exclusions

Digital treatment consent/consent management, enterprise features, initial-release X-ray/photo storage, NanoPix integration, and periodontal charting remain excluded.

<!-- AUTO-SYNC START -->
## Automatically verified GitHub snapshot

**Checked:** 23 November 2026, 09:38 AM IST

- Open PRs: [#15 — test: medical history data model and migration acceptance](https://github.com/drpast/dantbook-master/pull/15) (open-draft; CI **success**)
- Main CI: **success** ([run](https://github.com/drpast/dantbook-master/actions/runs/45079706235))
- Main commit: [11cb60e](https://github.com/drpast/dantbook-master/commit/11cb60e7ee89997e78f1923500ae6724778a6884) — feat: add branch-scoped dental laboratory case API (#11)
- Progress manifest reviewed: **2026-11-23**; overall **25%**.
- PR work is not treated as merged or complete; progress is changed only from evidence-reviewed manifest.

Progress is read from progress-manifest.json and is updated only after evidence review.
<!-- AUTO-SYNC END -->

## Current desktop view

The desktop app displays installer-style live task progress plus one row per involved file/activity, each with its own bar, status, and explanatory note. It polls the raw `status.json` feed and refreshes on its configured interval.
