# DantBook — Current Shared Task

**Last checked:** 23 November 2026, 05:11 PM IST  
**Baseline archive:** `v0.1.2 Medical History UI` (preserved in ChatGPT Library)  
**Current source activity:** PR #16 merged; checkpoint 8/39 complete. Main CI and open-PR details are tracked in the auto-sync snapshot below.

## Verified CI
- Latest main commit: [1448365](https://github.com/drpast/dantbook-master/commit/1448365afb6b15603b67dbb511a489ab4e1b9dbb) — merge pull request #16. PR-head CI [45166134533](https://github.com/drpast/dantbook-master/actions/runs/45166134533) passed; post-merge main CI is reported in the auto-sync snapshot.
- PR #11 Dental Laboratory case API: **merged**. Earlier CI [44949784904](https://github.com/drpast/dantbook-master/actions/runs/44949784904) failed at Prisma generation (P1012), but the final rerun [45041948662](https://github.com/drpast/dantbook-master/actions/runs/45041948662) passed; the PR was merged.
- PR #12 Codex development workflow docs: **merged**; final CI [45042687063](https://github.com/drpast/dantbook-master/actions/runs/45042687063) passed.
- PR #13 immediate dashboard notification: **merged**.
- PR #15 Medical History data-model acceptance: **merged**; CI **success** [45079372471](https://github.com/drpast/dantbook-master/actions/runs/45079372471). Live acceptance covers snapshot constraints, alert/date checks, append-only revision immutability, correction/audit flow, and branch-local isolation. This completes checkpoint 7/39.
- PR #15's dashboard-notification run [45079372414](https://github.com/drpast/dantbook-master/actions/runs/45079372414) also passed; this is separate from CI.
- PR #16 Medical History API checkpoint docs: **merged**; CI **success** [45166134533](https://github.com/drpast/dantbook-master/actions/runs/45166134533). It records the already-merged PR #4 API/browser acceptance (final head [44933570034](https://github.com/drpast/dantbook-master/actions/runs/44933570034); acceptance [44932842340](https://github.com/drpast/dantbook-master/actions/runs/44932842340)) and PR #15 database acceptance. This completes checkpoint 8/39.

## Recently merged milestones
- PRs #3 and #4 merged with passing acceptance CI; PRs #5–#10 also merged with passing CI.
- PR #11 Dental Laboratory case API, #12 Codex workflow docs, and #13 dashboard notification are merged. PR #11's initial P1012 failure was superseded by a successful rerun.
- PR #15 adds live Medical History data-model/migration acceptance coverage and completes checkpoint 7/39. PR #4 and PR #15 evidence, documented by merged PR #16, complete checkpoint 8/39. Overall/module percentages remain unchanged pending separate evidence review.

## Granular task tracker

The tracker contains **39 checkpoints** across seven work groups:

- Engineering foundation: 6 checkpoints
- Medical History: 7 checkpoints
- Finance: 5 checkpoints
- Dental Laboratory: 5 checkpoints
- Recall & Follow-up: 5 checkpoints
- Integration & testing: 7 checkpoints
- Release & deployment: 4 checkpoints

Current checkpoint: **9/39 — Medical History forms and patient-record UI** (pending). Checkpoints 7 and 8 are complete via merged PR #15, PR #4, and PR #16 with passing CI. Checkpoint statuses are tracked separately from overall/module progress.

## Progress evidence
Progress percentages live in `progress-manifest.json`. Reviewed **23 November 2026** for repository and checkpoint status. Overall remains **25%**; module percentages were not increased. PR #15 completes checkpoint 7; PR #4/#15 evidence documented by PR #16 completes checkpoint 8; the next evidence-backed checkpoint is #9.

## Permanent exclusions

Digital treatment consent/consent management, enterprise features, initial-release X-ray/photo storage, NanoPix integration, and periodontal charting remain excluded.

<!-- AUTO-SYNC START -->
## Automatically verified GitHub snapshot

**Checked:** 23 November 2026, 05:11 PM IST

- No open pull requests returned by GitHub.
- Main CI: **in_progress** ([run](https://github.com/drpast/dantbook-master/actions/runs/45167422538))
- Main commit: [1448365](https://github.com/drpast/dantbook-master/commit/1448365afb6b15603b67dbb511a489ab4e1b9dbb) — Merge pull request #16 from drpast/docs/checkpoint-8-medical-history-api-evidence
- Progress manifest reviewed: **2026-11-23**; overall **25%**.

Progress is read from progress-manifest.json and is updated only after evidence review.
<!-- AUTO-SYNC END -->

## Current desktop view

The desktop app displays installer-style live task progress plus one row per involved file/activity, each with its own bar, status, and explanatory note. It polls the raw `status.json` feed and refreshes on its configured interval.
