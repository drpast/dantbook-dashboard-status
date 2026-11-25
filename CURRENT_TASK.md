# DantBook — Current Shared Task

**Last checked:** 26 November 2026, 02:45 AM IST  
**Baseline archive:** `v0.1.2 Medical History UI` (preserved in ChatGPT Library)  
**Current source:** `drpast/dantbook-master`, branch `main`  
**Latest main commit:** [f63f848](https://github.com/drpast/dantbook-master/commit/f63f848aaf148b86352d42907f03c8be9e672241) — docs: record checkpoint 32 gap merged evidence (#47); checkpoint 32 audit recorded as not complete in PR #46  
**Current source activity:** Main CI cancelled; Open PRs: .

## Current task

**Checkpoint 32/39 — Backup, restore and security checks**  
Status: **Pending / blocked**. PR #46 audited the release-readiness target and recorded that backup/restore commands, PITR, retention/encryption, restore drills, deployment config, security policy, SAST/secret scanning, Dependabot and blocking dependency gates are not implemented. Checkpoint 31 remains pending/blocked; do not mark either checkpoint complete without genuine acceptance evidence.

## Verified repository state

- Compared with the previous monitoring baseline [09b7b62](https://github.com/drpast/dantbook-master/commit/09b7b62b5c82672c5b4969da3be009849b6c56ec), GitHub reports **29 commits ahead** and no commits behind.
- **PRs #32–#47 are merged**; GitHub search returned no open PRs.
- PR #32 completed checkpoint 21/39: expected-delivery and ordered status-history tracking acceptance.
- PR #33 completed checkpoint 22/39: one-time laboratory expense recording and case linkage.
- PR #34 completed checkpoint 23/39: Dental Laboratory workflow acceptance evidence.
- PR #35 completed checkpoint 24/39: branch-scoped recall rules, due evaluation and idempotent queueing.
- PR #36 completed checkpoint 25/39: all-rules recall due list, patient links and queue workflow.
- PR #37 completed checkpoint 26/39: fixed follow-up templates and queue-only EMAIL/SMS/PUSH options.
- PR #38 completed checkpoint 27/39: automated due-reminder queueing, retry, local FAILED/SENT outcomes and patient/rule opt-out suppression with audit history.
- PR #39 completed checkpoint 28/39: deterministic scheduling fixtures for the 180-day boundary, exact 180/90-day due dates, too-recent/non-matching/superseded visit exclusions, branch isolation, descending overdue ordering and browser display of calculated due windows.
- PR #40 completed checkpoint 29/39: role-gated patient-card booking handoff to `/schedule`, branch-scoped patient resolution, future-slot preselection, live HTTP registration-to-booking acceptance and fixture browser coverage with read-only denial.
- PR #41 refreshed checkpoint 29 evidence docs to the verified merged PR #40 state and post-merge CI run 45651429692.
- PR #42 completed checkpoint 30/39: live ADMIN and foreign-organization acceptance fixtures, patient role-matrix assertions, cross-organization and header/path denial, and fixture browser checks for STAFF and BILLING controls.
- PR #44 recorded checkpoint 31/39 as not implemented: no IndexedDB, PWA service worker, sync queue, temporary-ID mapping, field-level conflict UI, device lifecycle or cross-device/offline tests; it added a read-only readiness checker.
- PR #45 refreshed checkpoint 31 merged evidence; checkpoint 31 remains pending/blocked.
- PR #46 recorded checkpoint 32/39 as not implemented: no backup/restore command, scheduler, PITR, retention/encryption, restore drill, deployment artifact, security policy, SAST/secret scanning, Dependabot or blocking dependency gate; it added a read-only readiness checker.
- PR #47 refreshed checkpoint 32 merged evidence; the active tracker step advances to 32/39 for evidence work while overall stays at 72%.
- PR #38 [Verify workspace CI run 45468296638](https://github.com/drpast/dantbook-master/actions/runs/45468296638) passed.
- PR #39 [Verify workspace CI run 45589292148](https://github.com/drpast/dantbook-master/actions/runs/45589292148) passed with 17 Playwright tests, migrations/RLS checks, typecheck, build and live API acceptance.
- PR #40 [Verify workspace CI run 45650514543](https://github.com/drpast/dantbook-master/actions/runs/45650514543) passed with 19 Playwright tests, migrations/RLS checks, typecheck, build and live API acceptance.
- PR #42 [Verify workspace CI run 45661690949](https://github.com/drpast/dantbook-master/actions/runs/45661690949) passed with 21 Playwright tests, migrations/RLS checks, typecheck, build and live API acceptance.
- PR #44 [Verify workspace CI run 45685840444](https://github.com/drpast/dantbook-master/actions/runs/45685840444) passed with 9 foundation checks, 21 Playwright tests and live API acceptance.
- PR #45 [Verify workspace CI run 45688017120](https://github.com/drpast/dantbook-master/actions/runs/45688017120) passed after the merged-evidence refresh.
- PR #46 [Verify workspace CI run 45693177069](https://github.com/drpast/dantbook-master/actions/runs/45693177069) passed with 10 foundation checks, 21 Playwright tests and live API acceptance.
- PR #47 [Verify workspace CI run 45695275738](https://github.com/drpast/dantbook-master/actions/runs/45695275738) passed after the merged-evidence refresh.
- Post-merge main [CI run 45470198858](https://github.com/drpast/dantbook-master/actions/runs/45470198858) passed the full Verify workspace job for checkpoint 27/39.
- Post-merge main [CI run 45633000700](https://github.com/drpast/dantbook-master/actions/runs/45633000700) passed the full Verify workspace job for checkpoint 28/39, including 17 Playwright tests and live API acceptance.
- Post-merge main [CI run 45651429692](https://github.com/drpast/dantbook-master/actions/runs/45651429692) passed the full Verify workspace job for checkpoint 29/39, including 19 Playwright tests and live API acceptance.
- Post-merge main [CI run 45654373006](https://github.com/drpast/dantbook-master/actions/runs/45654373006) passed after the checkpoint 29 evidence-doc refresh.
- Post-merge main [CI run 45662918098](https://github.com/drpast/dantbook-master/actions/runs/45662918098) passed the full Verify workspace job for checkpoint 30/39, including 21 Playwright tests and live API acceptance.
- Post-merge main [CI run 45667246148](https://github.com/drpast/dantbook-master/actions/runs/45667246148) passed after the checkpoint 30 evidence-doc refresh.
- Post-merge main [CI run 45687165315](https://github.com/drpast/dantbook-master/actions/runs/45687165315) passed after the checkpoint 31 gap record.
- Post-merge main [CI run 45689303156](https://github.com/drpast/dantbook-master/actions/runs/45689303156) passed after the checkpoint 31 gap evidence refresh.
- Post-merge main [CI run 45693959604](https://github.com/drpast/dantbook-master/actions/runs/45693959604) passed after the checkpoint 32 gap record.
- Post-merge main [CI run 45696004411](https://github.com/drpast/dantbook-master/actions/runs/45696004411) passed after the checkpoint 32 gap evidence refresh.
- [Run 45470784324](https://github.com/drpast/dantbook-master/actions/runs/45470784324) is the separate dashboard-notification workflow, not the CI run.
- No published releases were returned by GitHub. The tag-ref query returned 404, so no tag listing was available.

## Recall automation limitations

The new automation remains **queue-only**. It does not dispatch real email, SMS or push messages and does not add a background scheduler. The workspace's Run automated reminders action queues eligible reminders; local outcome recording and retry preserve attempt history. Do not represent queued reminders as messages sent.

## Completed checkpoints

Checkpoints **1–30/39** are recorded complete in the task tracker. Checkpoints **31/39 — Offline mode, sync and conflict scenarios** and **32/39 — Backup, restore and security checks** remain pending/blocked. The active evidence checkpoint is **32/39**.

## Progress evidence

- Overall progress is now **72%**; `Recall & Follow-up` remains **100%**, `Integration & testing` is now **20%**, and all other module percentages are unchanged.
- Percentages were not recalculated from commit counts, PR merges or CI runs. They remain evidence-reviewed manifest values.
- The manifest review date is now **26 November 2026**.
- The target MVP date remains **20 December 2026** (ambitious).

## Dashboard data-quality notes

- The milestone-level status/percentage entries still conflict with the module-level statuses (for example, completed modules alongside milestone entries marked not started). They were left unchanged pending a separate evidence review.
- The sync script currently selects the newest workflow run on a branch without filtering for the CI workflow. This caused the earlier snapshot to attach notification run [45470784324](https://github.com/drpast/dantbook-master/actions/runs/45470784324) to the main-CI field. This monitor corrected status.json and the auto-sync block to the actual CI runs [45470198858](https://github.com/drpast/dantbook-master/actions/runs/45470198858), [45633000700](https://github.com/drpast/dantbook-master/actions/runs/45633000700), [45651429692](https://github.com/drpast/dantbook-master/actions/runs/45651429692), [45654373006](https://github.com/drpast/dantbook-master/actions/runs/45654373006), [45662918098](https://github.com/drpast/dantbook-master/actions/runs/45662918098) and [45667246148](https://github.com/drpast/dantbook-master/actions/runs/45667246148); notification runs [45654999024](https://github.com/drpast/dantbook-master/actions/runs/45654999024), [45667896133](https://github.com/drpast/dantbook-master/actions/runs/45667896133), [45687787085](https://github.com/drpast/dantbook-master/actions/runs/45687787085), [45689921001](https://github.com/drpast/dantbook-master/actions/runs/45689921001), [45696003925](https://github.com/drpast/dantbook-master/actions/runs/45696003925) and [45696846391](https://github.com/drpast/dantbook-master/actions/runs/45696846391) are not CI. The script defect remains and may recur until separately fixed. No code was changed in this monitoring run.
- The Windows sidebar was verified locally after checkpoint 30: its cache and UI showed overall **72%**, the active **Step 31/39**, step 30 recorded as completed with PR #42/CI success, and step 31 pending.
- Checkpoint 31/39 remains pending because offline-first implementation is absent; PR #44/#45 only record that verified gap.
- Checkpoint 32/39 remains pending because backup/restore and continuous security verification are absent; PR #46/#47 only record that verified gap.

## Permanent exclusions

Enterprise features, initial-release X-ray/photo storage and integrations, NanoPix/radiograph integration, digital treatment consent forms, and periodontal charting remain excluded.

<!-- AUTO-SYNC START -->
## Automatically verified GitHub snapshot

**Checked:** 26 November 2026, 02:45 AM IST

- No open pull requests returned by GitHub.
- Main CI: **cancelled** ([run](https://github.com/drpast/dantbook-master/actions/runs/45702589714))
- Main commit: [871241d](https://github.com/drpast/dantbook-master/commit/871241d3bc0e74186faa0519b8243c8fbe2f90ea) — docs: record checkpoint 33 gap merged evidence (#49)
- Progress manifest reviewed: **2026-11-26**; overall **72%**.

Progress is read from progress-manifest.json and is updated only after evidence review.
<!-- AUTO-SYNC END -->
