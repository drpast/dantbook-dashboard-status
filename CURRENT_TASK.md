# DantBook — Current Shared Task

**Last checked:** 24 November 2026, 10:06 PM IST  
**Baseline archive:** `v0.1.2 Medical History UI` (preserved in ChatGPT Library)  
**Current source:** `drpast/dantbook-master`, branch `main`  
**Latest main commit:** [09b7b62](https://github.com/drpast/dantbook-master/commit/09b7b62b5c82672c5b4969da3be009849b6c56ec) — merged PR #31, checkpoint 20/39.

## Current task

**Checkpoint 21/39 — Case status, expected delivery and tracking**  
Status: **Pending**. Checkpoint 20/39 (Create and submit laboratory cases) is complete. Do not mark checkpoint 21 complete until its implementation and acceptance evidence are verified.

## Verified repository state

- Latest main commit: [09b7b62b5c82672c5b4969da3be009849b6c56ec](https://github.com/drpast/dantbook-master/commit/09b7b62b5c82672c5b4969da3be009849b6c56ec), merged from PR #31.
- Open PRs: **None returned by GitHub search**.
- PR #31, [Create and submit laboratory cases](https://github.com/drpast/dantbook-master/pull/31), is **merged**.
- PR #31 CI [run 45278584250](https://github.com/drpast/dantbook-master/actions/runs/45278584250) passed. Its `Verify workspace` job completed all steps successfully, including Prisma generation/validation, migrations, PostgreSQL RLS and Medical History acceptance, shared-patient access boundaries, type-check, build, browser acceptance and authenticated patient API acceptance.
- PR #30 was closed unmerged after an encoding regression; PR #31 is the clean replacement and is merged. This is not an active blocker.

## CI distinction — important

- The successful workflow [45279997678](https://github.com/drpast/dantbook-master/actions/runs/45279997678) on the latest main commit is **Notify DantBook dashboard**. Its only job is `notify`; it is not the CI workflow.
- The combined commit-status query returned no status contexts. Therefore **post-merge main CI for 09b7b62 is unverified**, not successful.
- PR-head CI success is verified separately by run 45278584250. Do not substitute notification success for main CI.

## Completed checkpoint evidence

- Checkpoints 1–20/39 are recorded complete in `progress-manifest.json`.
- Checkpoint 20/39 was completed by merged PR #31: a branch-local Dental Laboratory page linked from the patient record, a same-origin proxy, fictional draft creation, DRAFT-to-SUBMITTED submission, and fixture Playwright coverage.
- PR #31 reused the already-merged Dental Laboratory API/model; it introduced no schema or migration changes.
- Earlier merged checkpoints include Medical History data model/API/UI, alerts, correction/audit/safety, patient workflow integration and acceptance; Finance data model, billing UI, payments, reports and acceptance; and Dental Laboratory model/setup.

## Granular task tracker

The tracker contains **39 checkpoints** across seven work groups:

- Engineering foundation: 6 checkpoints
- Medical History: 7 checkpoints
- Finance: 5 checkpoints
- Dental Laboratory: 5 checkpoints
- Recall & Follow-up: 5 checkpoints
- Integration & testing: 7 checkpoints
- Release & deployment: 4 checkpoints

Current checkpoint: **24/39 — Recall and follow-up scheduling rules** (pending; awaiting verified work). Checkpoint statuses are tracked separately from overall/module progress.

## Progress evidence

- Overall progress remains **25%**.
- Module percentages remain unchanged.
- The progress manifest was last reviewed **23 November 2026**. Percentages are evidence-reviewed estimates, not inferred from commit counts, PR merges, or CI runs. No percentage increase is made by this synchronization.
- Target MVP date remains **20 December 2026** (ambitious).

## Permanent exclusions

Digital treatment consent/consent management, enterprise features, initial-release X-ray/photo storage and integrations, NanoPix/radiograph integration, and periodontal charting remain excluded.

## Current desktop view

The Windows Progress Dashboard consumes the raw `status.json` feed and polls it on its configured interval. Its current-task activity should show checkpoint 21/39 as pending at 0%; the desktop app's own refresh is not directly verified from this GitHub sync.

<!-- AUTO-SYNC START -->
## Automatically verified GitHub snapshot

**Checked:** 24 November 2026, 10:06 PM IST

- No open pull requests returned by GitHub.
- Main CI: **success** ([run](https://github.com/drpast/dantbook-master/actions/runs/45438973015))
- Main commit: [bf8247c](https://github.com/drpast/dantbook-master/commit/bf8247c7546352d0013db42bafa6b49f68b6fff3) — Feat: checkpoint 24/39 recall and follow-up scheduling rules (#35)
- Progress manifest reviewed: **2026-11-23**; overall **25%**.

Progress is read from progress-manifest.json and is updated only after evidence review.
<!-- AUTO-SYNC END -->
