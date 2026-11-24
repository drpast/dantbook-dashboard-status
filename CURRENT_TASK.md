# DantBook — Current Shared Task

**Last checked:** 24 November 2026, 06:45 AM IST  
**Baseline archive:** `v0.1.2 Medical History UI` (preserved in ChatGPT Library)  
**Current source activity:** Main CI success; Open PRs: .

## Verified CI
- Latest main commit: [1cee206](https://github.com/drpast/dantbook-master/commit/1cee2068ef77649b2ef9035da7495acd6ca6bbe8) — merge pull request #15. PR-head CI [45079372471](https://github.com/drpast/dantbook-master/actions/runs/45079372471) passed; post-merge main CI is reported in the auto-sync snapshot.
- PR #11 Dental Laboratory case API: **merged**. Earlier CI [44949784904](https://github.com/drpast/dantbook-master/actions/runs/44949784904) failed at Prisma generation (P1012), but the final rerun [45041948662](https://github.com/drpast/dantbook-master/actions/runs/45041948662) passed; the PR was merged.
- PR #12 Codex development workflow docs: **merged**; final CI [45042687063](https://github.com/drpast/dantbook-master/actions/runs/45042687063) passed.
- PR #13 immediate dashboard notification: **merged**.
- PR #15 Medical History data-model acceptance: **merged**; CI **success** [45079372471](https://github.com/drpast/dantbook-master/actions/runs/45079372471). Live acceptance covers snapshot constraints, alert/date checks, append-only revision immutability, correction/audit flow, and branch-local isolation. This completes checkpoint 7/39.
- PR #15's dashboard-notification run [45079372414](https://github.com/drpast/dantbook-master/actions/runs/45079372414) also passed; this is separate from CI.

## Recently merged milestones
- PRs #3 and #4 merged with passing acceptance CI; PRs #5–#10 also merged with passing CI.
- PR #11 Dental Laboratory case API, #12 Codex workflow docs, and #13 dashboard notification are merged. PR #11's initial P1012 failure was superseded by a successful rerun.
- PR #15 adds live Medical History data-model/migration acceptance coverage. It merged with passing CI; checkpoint 7/39 is complete. Overall/module percentages remain unchanged pending separate evidence review.

## Granular task tracker

The tracker contains **39 checkpoints** across seven work groups:

- Engineering foundation: 6 checkpoints
- Medical History: 7 checkpoints
- Finance: 5 checkpoints
- Dental Laboratory: 5 checkpoints
- Recall & Follow-up: 5 checkpoints
- Integration & testing: 7 checkpoints
- Release & deployment: 4 checkpoints

Current checkpoint: **21/39 — Case status, expected delivery and tracking** (pending; awaiting verified work). Checkpoint statuses are tracked separately from overall/module progress.

## Progress evidence
Progress percentages live in `progress-manifest.json`. Reviewed **23 November 2026** for repository and checkpoint status. Overall remains **25%**; module percentages were not increased. PR #15 merged with passing CI and completes checkpoint 7; the next evidence-backed checkpoint is #8.

## Permanent exclusions

Digital treatment consent/consent management, enterprise features, initial-release X-ray/photo storage, NanoPix integration, and periodontal charting remain excluded.

<!-- AUTO-SYNC START -->
## Automatically verified GitHub snapshot

**Checked:** 24 November 2026, 06:45 AM IST

- No open pull requests returned by GitHub.
- Main CI: **success** ([run](https://github.com/drpast/dantbook-master/actions/runs/45279997678))
- Main commit: [09b7b62](https://github.com/drpast/dantbook-master/commit/09b7b62b5c82672c5b4969da3be009849b6c56ec) — Merge pull request #31 from drpast/feat/lab-submission-checkpoint-20-clean
- Progress manifest reviewed: **2026-11-23**; overall **25%**.

Progress is read from progress-manifest.json and is updated only after evidence review.
<!-- AUTO-SYNC END -->

## Current desktop view

The desktop app displays installer-style live task progress plus one row per involved file/activity, each with its own bar, status, and explanatory note. It polls the raw `status.json` feed and refreshes on its configured interval.
