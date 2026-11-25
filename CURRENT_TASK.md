# DantBook — Current Shared Task

**Last checked:** 25 November 2026, 10:43 PM IST  
**Baseline archive:** `v0.1.2 Medical History UI` (preserved in ChatGPT Library)  
**Current source:** `drpast/dantbook-master`, branch `main`  
**Latest main commit:** [1c9e991](https://github.com/drpast/dantbook-master/commit/1c9e991ade0800ab19d30b8dfdb574980ad7832d) — docs: record checkpoint 29 merged evidence (#41); checkpoint 29 implementation merged in PR #40  
**Current source activity:** Main CI success; Open PRs: #42 test: checkpoint 30 role access boundaries (CI success).

## Current task

**Checkpoint 30/39 — Role permissions and access-boundary verification**  
Status: **Pending**. Checkpoint 29/39 (Integrated patient registration and appointment workflow) is complete through merged PR #40. Do not mark checkpoint 30 complete until its implementation and acceptance evidence are verified.

## Verified repository state

- Compared with the previous monitoring baseline [09b7b62](https://github.com/drpast/dantbook-master/commit/09b7b62b5c82672c5b4969da3be009849b6c56ec), GitHub reports **23 commits ahead** and no commits behind.
- **PRs #32–#40 are merged**; GitHub search returned no open PRs.
- PR #32 completed checkpoint 21/39: expected-delivery and ordered status-history tracking acceptance.
- PR #33 completed checkpoint 22/39: one-time laboratory expense recording and case linkage.
- PR #34 completed checkpoint 23/39: Dental Laboratory workflow acceptance evidence.
- PR #35 completed checkpoint 24/39: branch-scoped recall rules, due evaluation and idempotent queueing.
- PR #36 completed checkpoint 25/39: all-rules recall due list, patient links and queue workflow.
- PR #37 completed checkpoint 26/39: fixed follow-up templates and queue-only EMAIL/SMS/PUSH options.
- PR #38 completed checkpoint 27/39: automated due-reminder queueing, retry, local FAILED/SENT outcomes and patient/rule opt-out suppression with audit history.
- PR #39 completed checkpoint 28/39: deterministic scheduling fixtures for the 180-day boundary, exact 180/90-day due dates, too-recent/non-matching/superseded visit exclusions, branch isolation, descending overdue ordering and browser display of calculated due windows.
- PR #40 completed checkpoint 29/39: role-gated patient-card booking handoff to `/schedule`, branch-scoped patient resolution, future-slot preselection, live HTTP registration-to-booking acceptance and fixture browser coverage with read-only denial.
- PR #38 [Verify workspace CI run 45468296638](https://github.com/drpast/dantbook-master/actions/runs/45468296638) passed.
- PR #39 [Verify workspace CI run 45589292148](https://github.com/drpast/dantbook-master/actions/runs/45589292148) passed with 17 Playwright tests, migrations/RLS checks, typecheck, build and live API acceptance.
- PR #40 [Verify workspace CI run 45650514543](https://github.com/drpast/dantbook-master/actions/runs/45650514543) passed with 19 Playwright tests, migrations/RLS checks, typecheck, build and live API acceptance.
- Post-merge main [CI run 45470198858](https://github.com/drpast/dantbook-master/actions/runs/45470198858) passed the full Verify workspace job for checkpoint 27/39.
- Post-merge main [CI run 45633000700](https://github.com/drpast/dantbook-master/actions/runs/45633000700) passed the full Verify workspace job for checkpoint 28/39, including 17 Playwright tests and live API acceptance.
- Post-merge main [CI run 45651429692](https://github.com/drpast/dantbook-master/actions/runs/45651429692) passed the full Verify workspace job for checkpoint 29/39, including 19 Playwright tests and live API acceptance.
- Post-merge main [CI run 45654373006](https://github.com/drpast/dantbook-master/actions/runs/45654373006) passed after the checkpoint 29 evidence-doc refresh.
- [Run 45470784324](https://github.com/drpast/dantbook-master/actions/runs/45470784324) is the separate dashboard-notification workflow, not the CI run.
- No published releases were returned by GitHub. The tag-ref query returned 404, so no tag listing was available.

## Recall automation limitations

The new automation remains **queue-only**. It does not dispatch real email, SMS or push messages and does not add a background scheduler. The workspace's Run automated reminders action queues eligible reminders; local outcome recording and retry preserve attempt history. Do not represent queued reminders as messages sent.

## Completed checkpoints

Checkpoints **1–29/39** are recorded complete in the task tracker. The next checkpoint is **30/39 — Role permissions and access-boundary verification**.

## Progress evidence

- Overall progress is now **71%**; `Recall & Follow-up` remains **100%**, `Integration & testing` is now **15%**, and all other module percentages are unchanged.
- Percentages were not recalculated from commit counts, PR merges or CI runs. They remain evidence-reviewed manifest values.
- The manifest review date remains **25 November 2026**.
- The target MVP date remains **20 December 2026** (ambitious).

## Dashboard data-quality notes

- The milestone-level status/percentage entries still conflict with the module-level statuses (for example, completed modules alongside milestone entries marked not started). They were left unchanged pending a separate evidence review.
- The sync script currently selects the newest workflow run on a branch without filtering for the CI workflow. This caused the earlier snapshot to attach notification run [45470784324](https://github.com/drpast/dantbook-master/actions/runs/45470784324) to the main-CI field. This monitor corrected status.json and the auto-sync block to the actual CI runs [45470198858](https://github.com/drpast/dantbook-master/actions/runs/45470198858), [45633000700](https://github.com/drpast/dantbook-master/actions/runs/45633000700), [45651429692](https://github.com/drpast/dantbook-master/actions/runs/45651429692) and [45654373006](https://github.com/drpast/dantbook-master/actions/runs/45654373006); notification run [45654999024](https://github.com/drpast/dantbook-master/actions/runs/45654999024) is not CI. The script defect remains and may recur until separately fixed. No code was changed in this monitoring run.
- The Windows sidebar was verified locally after checkpoint 29: its cache and UI showed overall **71%**, the active **Step 30/39**, step 29 recorded as completed with PR #40/CI success, and step 30 pending.

## Permanent exclusions

Enterprise features, initial-release X-ray/photo storage and integrations, NanoPix/radiograph integration, digital treatment consent forms, and periodontal charting remain excluded.

<!-- AUTO-SYNC START -->
## Automatically verified GitHub snapshot

**Checked:** 25 November 2026, 10:43 PM IST

- Open PRs: [#42 — test: checkpoint 30 role access boundaries](https://github.com/drpast/dantbook-master/pull/42) (open-draft; CI **success**)
- Main CI: **success** ([run](https://github.com/drpast/dantbook-master/actions/runs/45662381327))
- Main commit: [1c9e991](https://github.com/drpast/dantbook-master/commit/1c9e991ade0800ab19d30b8dfdb574980ad7832d) — docs: record checkpoint 29 merged evidence (#41)
- Progress manifest reviewed: **2026-11-25**; overall **71%**.
- PR work is not treated as merged or complete; progress is changed only from evidence-reviewed manifest.

Progress is read from progress-manifest.json and is updated only after evidence review.
<!-- AUTO-SYNC END -->
