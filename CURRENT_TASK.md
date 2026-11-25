# DantBook — Current Shared Task

**Last checked:** 25 November 2026, 09:40 AM IST  
**Baseline archive:** `v0.1.2 Medical History UI` (preserved in ChatGPT Library)  
**Current source:** `drpast/dantbook-master`, branch `main`  
**Latest main commit:** [0b5784c](https://github.com/drpast/dantbook-master/commit/0b5784c3a5fde247842d91e0aa14a8959993ff17) — merged PR #38, checkpoint 27/39  
**Current source activity:** Main CI success; Open PRs: .

## Current task

**Checkpoint 28/39 — Recall/follow-up acceptance and scheduling tests**  
Status: **Pending**. Checkpoint 27/39 (Automated reminders, retry and opt-out handling) is complete through merged PR #38. Do not mark checkpoint 28 complete until its implementation and acceptance evidence are verified.

## Verified repository state

- Compared with the previous monitoring baseline [09b7b62](https://github.com/drpast/dantbook-master/commit/09b7b62b5c82672c5b4969da3be009849b6c56ec), GitHub reports **20 commits ahead** and no commits behind.
- **PRs #32–#38 are merged**; GitHub search returned no open PRs.
- PR #32 completed checkpoint 21/39: expected-delivery and ordered status-history tracking acceptance.
- PR #33 completed checkpoint 22/39: one-time laboratory expense recording and case linkage.
- PR #34 completed checkpoint 23/39: Dental Laboratory workflow acceptance evidence.
- PR #35 completed checkpoint 24/39: branch-scoped recall rules, due evaluation and idempotent queueing.
- PR #36 completed checkpoint 25/39: all-rules recall due list, patient links and queue workflow.
- PR #37 completed checkpoint 26/39: fixed follow-up templates and queue-only EMAIL/SMS/PUSH options.
- PR #38 completed checkpoint 27/39: automated due-reminder queueing, retry, local FAILED/SENT outcomes and patient/rule opt-out suppression with audit history.
- PR #38 [Verify workspace CI run 45468296638](https://github.com/drpast/dantbook-master/actions/runs/45468296638) passed.
- Post-merge main [CI run 45470198858](https://github.com/drpast/dantbook-master/actions/runs/45470198858) passed the full Verify workspace job, including Prisma validation, migrations, PostgreSQL/RLS checks, type-check, build, browser acceptance and authenticated patient API acceptance.
- [Run 45470784324](https://github.com/drpast/dantbook-master/actions/runs/45470784324) is the separate dashboard-notification workflow, not the CI run.
- No published releases were returned by GitHub. The tag-ref query returned 404, so no tag listing was available.

## Recall automation limitations

The new automation remains **queue-only**. It does not dispatch real email, SMS or push messages and does not add a background scheduler. The workspace's Run automated reminders action queues eligible reminders; local outcome recording and retry preserve attempt history. Do not represent queued reminders as messages sent.

## Completed checkpoints

Checkpoints **1–27/39** are recorded complete in the task tracker. The next checkpoint is **28/39 — Recall/follow-up acceptance and scheduling tests**.

## Progress evidence

- Overall progress remains **67%**; module percentages are unchanged.
- Percentages were not recalculated from commit counts, PR merges or CI runs. They remain evidence-reviewed manifest values.
- The manifest review date remains **25 November 2026**.
- The target MVP date remains **20 December 2026** (ambitious).

## Dashboard data-quality notes

- The milestone-level status/percentage entries still conflict with the module-level statuses (for example, completed modules alongside milestone entries marked not started). They were left unchanged pending a separate evidence review.
- The sync script currently selects the newest workflow run on a branch without filtering for the CI workflow. This can attach a successful notification run to the main-CI field. The verified main CI run for this commit is **45470198858**.
- The Windows app's actual refresh on the user's PC is not directly verified by this GitHub check.

## Permanent exclusions

Enterprise features, initial-release X-ray/photo storage and integrations, NanoPix/radiograph integration, digital treatment consent forms, and periodontal charting remain excluded.

<!-- AUTO-SYNC START -->
## Automatically verified GitHub snapshot

**Checked:** 25 November 2026, 09:40 AM IST

- No open pull requests returned by GitHub.
- Main CI: **success** ([run](https://github.com/drpast/dantbook-master/actions/runs/45470784324))
- Main commit: [0b5784c](https://github.com/drpast/dantbook-master/commit/0b5784c3a5fde247842d91e0aa14a8959993ff17) — Feat: checkpoint 27/39 automated recall reminders, retry and opt-out (#38)
- Progress manifest reviewed: **2026-11-25**; overall **67%**.

Progress is read from progress-manifest.json and is updated only after evidence review.
<!-- AUTO-SYNC END -->
