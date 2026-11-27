# DantBook — Current Shared Task

**Last checked:** 27 November 2026, 10:07 PM IST  
**Baseline archive:** `v0.1.2 Medical History UI` (preserved in ChatGPT Library)  
**Current source:** `drpast/dantbook-master`, branch `main`  
**Latest main commit:** [94ba933](https://github.com/drpast/dantbook-master/commit/94ba9330c751a827f55b7a1eb7b5dfe1d0b188cf) — docs: record checkpoint 39 merged evidence (#89); exact-HEAD CI and security scan both passed
**Current source activity:** Main CI success; Open PRs: #73 build(deps-dev): bump prisma from 6.19.3 to 7.10.1 (CI failure); #74 build(deps-dev): bump @nestjs/cli from 11.0.24 to 12.0.15 (CI success); #72 build(deps): bump @nestjs/platform-express from 11.2.11 to 12.6.0 (CI failure); #71 build(deps): bump @nestjs/core from 11.2.11 to 12.6.0 (CI failure); #70 build(deps): bump dotenv from 16.6.1 to 18.0.10 (CI success); #69 build(deps): bump @nestjs/common from 11.2.11 to 12.6.0 (CI failure); #68 build(deps): bump actions/checkout from 4 to 7 (CI success); #67 build(deps): bump actions/setup-node from 4 to 7 (CI success).

## Current task

**Checkpoint 39/39 — Release readiness and launch checklist**  
Status: **Pending / blocked**. PR #60/#61 audited the release-readiness gap. PR #88 merged a draft launch checklist, consolidated 39-step matrix, readiness contract, read-only verifier and CI report step; it explicitly keeps publication, rollback rehearsal, support coverage, sign-offs, go/no-go and release records false. PR #89 merged the evidence record: 18 foundation checks, 27 Playwright tests, readiness:verify covers 4 artifacts and 13 sections with 0 decisions, and the no-go gate correctly fails. Latest main CI run [45911264253](https://github.com/drpast/dantbook-master/actions/runs/45911264253) and security scan [45911264323](https://github.com/drpast/dantbook-master/actions/runs/45911264323) passed on exact HEAD 94ba933. GitHub reports 0 releases. Checkpoint 39 remains pending owner acceptance; checkpoints 31-38 remain pending/blocked and overall progress stays at 72%.

## Verified repository state

- Latest verified main HEAD is [94ba933](https://github.com/drpast/dantbook-master/commit/94ba9330c751a827f55b7a1eb7b5dfe1d0b188cf); exact-HEAD CI and security scan both passed.
- PRs #32–#61 remain merged; PRs #88 and #89 are also merged. Eight open Dependabot PRs #67–#74 remain: CI fails on #73, #72, #71 and #69; CI passes on #74, #70, #68 and #67.
- Failure logs show PR #73's Prisma 7.10.1 upgrade is incompatible with the current schema's datasource `url`/`directUrl` fields (P1012). PRs #72/#71/#69 have npm ERESOLVE peer-dependency conflicts because NestJS 11 and 12 packages are being mixed; these are confined to the unmerged dependency branches.
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
- PR #88 added draft release-readiness artifacts, a consolidated 39-step matrix, readiness contract and read-only verifier; it explicitly leaves release publication, rollback rehearsal, support coverage, sign-offs, go/no-go and release records false. PR #89 records the merged evidence and a correctly failing no-go gate. Checkpoint 39 remains pending owner acceptance.
- PR #44 recorded checkpoint 31/39 as not implemented: no IndexedDB, PWA service worker, sync queue, temporary-ID mapping, field-level conflict UI, device lifecycle or cross-device/offline tests; it added a read-only readiness checker.
- PR #45 refreshed checkpoint 31 merged evidence; checkpoint 31 remains pending/blocked.
- PR #46 recorded checkpoint 32/39 as not implemented: no backup/restore command, scheduler, PITR, retention/encryption, restore drill, deployment artifact, security policy, SAST/secret scanning, Dependabot or blocking dependency gate; it added a read-only readiness checker.
- PR #47 refreshed checkpoint 32 merged evidence; checkpoint 32 remains pending/blocked.
- PR #48 recorded checkpoint 33/39 as not implemented: the repository has 11 per-module Playwright specs with 21 tests and two narrow handoffs, but no dedicated cross-module regression suite, shared fixture layer, regression matrix/tags, full clinic-flow scenario or continuous regression gate; it added a read-only readiness checker.
- PR #49 refreshed checkpoint 33 merged evidence; checkpoint 33 remains pending/blocked.
- PR #50 recorded checkpoint 34/39 as not implemented: no Lighthouse/axe/pa11y/web-vitals gate, performance budget, Core Web Vitals threshold, keyboard/screen-reader/contrast/WCAG test, usability record or device matrix; it added a read-only readiness checker.
- PR #51 refreshed checkpoint 34 merged evidence; checkpoint 34 remains pending/blocked.
- PR #52 recorded checkpoint 35/39 as not implemented: no issue templates, blocker register, severity/owner/reproduction linkage, blocker-to-fix linkage, re-test matrix, open-blocker CI gate or release sign-off record; it added a read-only readiness checker.
- PR #53 refreshed checkpoint 35 merged evidence; checkpoint 35 remains pending/blocked.
- PR #54 recorded checkpoint 36/39 as not implemented: no deployment artifact, production config, deploy/release workflow, deployment environment/secrets, staged rollout, rollback plan, promotion gate, secret rotation, TLS/ingress config, monitoring/alerting or operational runbook; it added a read-only readiness checker.
- PR #55 refreshed checkpoint 36 merged evidence; checkpoint 36 remains pending/blocked.
- PR #56 recorded checkpoint 37/39 as not implemented: no acceptance report, scope matrix, requirement-to-evidence trace, owner test record, go/no-go decision, release tag or independent clinical/security/privacy/accounting/jurisdictional sign-off; it added a read-only readiness checker.
- PR #57 refreshed checkpoint 37 merged evidence; checkpoint 37 remains pending/blocked.
- PR #58 recorded checkpoint 38/39 as not implemented: no user/admin guide, operator manual, clinic quick-start, role workflow guide, onboarding/training material, support guide, FAQ, release notes or handover checklist; it added a read-only readiness checker.
- PR #59 refreshed checkpoint 38 merged evidence; checkpoint 38 remains pending/blocked.
- PR #60 recorded checkpoint 39/39 as not implemented: no release checklist, launch record, release approval, go/no-go decision, version-to-build mapping, rollout/promotion record, verified rollback, support coverage or consolidated 39-checkpoint evidence; it added a read-only readiness checker.
- PR #61 refreshed checkpoint 39 merged evidence; the active tracker step advances to 39/39 for evidence work while overall stays at 72%.
- PR #38 [Verify workspace CI run 45468296638](https://github.com/drpast/dantbook-master/actions/runs/45468296638) passed.
- PR #39 [Verify workspace CI run 45589292148](https://github.com/drpast/dantbook-master/actions/runs/45589292148) passed with 17 Playwright tests, migrations/RLS checks, typecheck, build and live API acceptance.
- PR #40 [Verify workspace CI run 45650514543](https://github.com/drpast/dantbook-master/actions/runs/45650514543) passed with 19 Playwright tests, migrations/RLS checks, typecheck, build and live API acceptance.
- PR #42 [Verify workspace CI run 45661690949](https://github.com/drpast/dantbook-master/actions/runs/45661690949) passed with 21 Playwright tests, migrations/RLS checks, typecheck, build and live API acceptance.
- PR #44 [Verify workspace CI run 45685840444](https://github.com/drpast/dantbook-master/actions/runs/45685840444) passed with 9 foundation checks, 21 Playwright tests and live API acceptance.
- PR #45 [Verify workspace CI run 45688017120](https://github.com/drpast/dantbook-master/actions/runs/45688017120) passed after the merged-evidence refresh.
- PR #46 [Verify workspace CI run 45693177069](https://github.com/drpast/dantbook-master/actions/runs/45693177069) passed with 10 foundation checks, 21 Playwright tests and live API acceptance.
- PR #47 [Verify workspace CI run 45695275738](https://github.com/drpast/dantbook-master/actions/runs/45695275738) passed after the merged-evidence refresh.
- PR #48 [Verify workspace CI run 45699696290](https://github.com/drpast/dantbook-master/actions/runs/45699696290) passed with 11 foundation checks, 21 Playwright tests and live API acceptance.
- PR #49 [Verify workspace CI run 45701640374](https://github.com/drpast/dantbook-master/actions/runs/45701640374) passed after the merged-evidence refresh.
- PR #50 [Verify workspace CI run 45705350058](https://github.com/drpast/dantbook-master/actions/runs/45705350058) passed with 12 foundation checks, 21 Playwright tests and live API acceptance.
- PR #51 [Verify workspace CI run 45707018581](https://github.com/drpast/dantbook-master/actions/runs/45707018581) passed after the merged-evidence refresh.
- PR #52 [Verify workspace CI run 45709807207](https://github.com/drpast/dantbook-master/actions/runs/45709807207) passed with 13 foundation checks, 21 Playwright tests and live API acceptance.
- PR #53 [Verify workspace CI run 45711415543](https://github.com/drpast/dantbook-master/actions/runs/45711415543) passed after the merged-evidence refresh.
- PR #54 [Verify workspace CI run 45811450429](https://github.com/drpast/dantbook-master/actions/runs/45811450429) passed with 14 foundation checks, 21 Playwright tests and live API acceptance.
- PR #55 [Verify workspace CI run 45813380851](https://github.com/drpast/dantbook-master/actions/runs/45813380851) passed after the merged-evidence refresh.
- PR #56 [Verify workspace CI run 45823083773](https://github.com/drpast/dantbook-master/actions/runs/45823083773) passed with 15 foundation checks, 21 Playwright tests and live API acceptance.
- PR #57 [Verify workspace CI run 45824738481](https://github.com/drpast/dantbook-master/actions/runs/45824738481) passed after the merged-evidence refresh.
- PR #58 [Verify workspace CI run 45829984369](https://github.com/drpast/dantbook-master/actions/runs/45829984369) passed with 16 foundation checks, 21 Playwright tests and live API acceptance.
- PR #59 [Verify workspace CI run 45831752129](https://github.com/drpast/dantbook-master/actions/runs/45831752129) passed after the merged-evidence refresh.
- PR #60 [Verify workspace CI run 45835150505](https://github.com/drpast/dantbook-master/actions/runs/45835150505) passed with 17 foundation checks, 21 Playwright tests and live API acceptance.
- PR #61 [Verify workspace CI run 45837000971](https://github.com/drpast/dantbook-master/actions/runs/45837000971) passed after the merged-evidence refresh.
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
- Post-merge main [CI run 45700644773](https://github.com/drpast/dantbook-master/actions/runs/45700644773) passed after the checkpoint 33 gap record.
- Post-merge main [CI run 45702589407](https://github.com/drpast/dantbook-master/actions/runs/45702589407) passed after the checkpoint 33 gap evidence refresh.
- Post-merge main [CI run 45706279519](https://github.com/drpast/dantbook-master/actions/runs/45706279519) passed after the checkpoint 34 gap record.
- Post-merge main [CI run 45707642453](https://github.com/drpast/dantbook-master/actions/runs/45707642453) passed after the checkpoint 34 gap evidence refresh.
- Post-merge main [CI run 45710667363](https://github.com/drpast/dantbook-master/actions/runs/45710667363) passed after the checkpoint 35 gap record.
- Post-merge main [CI run 45712017862](https://github.com/drpast/dantbook-master/actions/runs/45712017862) passed after the checkpoint 35 gap evidence refresh.
- Post-merge main [CI run 45812396171](https://github.com/drpast/dantbook-master/actions/runs/45812396171) passed after the checkpoint 36 gap record.
- Post-merge main [CI run 45814068739](https://github.com/drpast/dantbook-master/actions/runs/45814068739) passed after the checkpoint 36 gap evidence refresh.
- Post-merge main [CI run 45823988572](https://github.com/drpast/dantbook-master/actions/runs/45823988572) passed after the checkpoint 37 gap record.
- Post-merge main [CI run 45825406042](https://github.com/drpast/dantbook-master/actions/runs/45825406042) passed after the checkpoint 37 gap evidence refresh.
- Post-merge main [CI run 45830949289](https://github.com/drpast/dantbook-master/actions/runs/45830949289) passed after the checkpoint 38 gap record.
- Post-merge main [CI run 45832771718](https://github.com/drpast/dantbook-master/actions/runs/45832771718) passed after the checkpoint 38 gap evidence refresh.
- Post-merge main [CI run 45836120819](https://github.com/drpast/dantbook-master/actions/runs/45836120819) passed after the checkpoint 39 gap record.
- Post-merge main [CI run 45837733923](https://github.com/drpast/dantbook-master/actions/runs/45837733923) passed after the checkpoint 39 gap evidence refresh.
- [Run 45470784324](https://github.com/drpast/dantbook-master/actions/runs/45470784324) is the separate dashboard-notification workflow, not the CI run.
- No published releases were returned by GitHub. The tag-ref query returned 404, so no tag listing was available.

## Recall automation limitations

The new automation remains **queue-only**. It does not dispatch real email, SMS or push messages and does not add a background scheduler. The workspace's Run automated reminders action queues eligible reminders; local outcome recording and retry preserve attempt history. Do not represent queued reminders as messages sent.

## Completed checkpoints

Checkpoints **1–30/39** are recorded complete in the task tracker. Checkpoints **31/39 — Offline mode, sync and conflict scenarios**, **32/39 — Backup, restore and security checks**, **33/39 — Cross-module end-to-end regression testing**, **34/39 — Performance, accessibility and usability checks**, **35/39 — Resolve blockers and verify fixes**, **36/39 — Production configuration and deployment preparation**, **37/39 — Final MVP acceptance against scope**, **38/39 — User/admin documentation and handover** and **39/39 — Release readiness and launch checklist** remain pending/blocked. The active evidence checkpoint is **39/39**.

## Progress evidence

- Overall progress is now **72%**; `Recall & Follow-up` remains **100%**, `Integration & testing` is now **20%**, and all other module percentages are unchanged.
- Percentages were not recalculated from commit counts, PR merges or CI runs. They remain evidence-reviewed manifest values.
- The manifest review date is now **27 November 2026**; overall progress remains 72%.
- The target MVP date remains **20 December 2026** (ambitious).

## Dashboard data-quality notes

- The milestone-level status/percentage entries still conflict with the module-level statuses (for example, completed modules alongside milestone entries marked not started). They were left unchanged pending a separate evidence review.
- The sync script currently selects the newest workflow run on a branch without filtering for the CI workflow. This caused the earlier snapshot to attach notification run [45470784324](https://github.com/drpast/dantbook-master/actions/runs/45470784324) to the main-CI field. This monitor corrected status.json and the auto-sync block to the actual CI runs [45470198858](https://github.com/drpast/dantbook-master/actions/runs/45470198858), [45633000700](https://github.com/drpast/dantbook-master/actions/runs/45633000700), [45651429692](https://github.com/drpast/dantbook-master/actions/runs/45651429692), [45654373006](https://github.com/drpast/dantbook-master/actions/runs/45654373006), [45662918098](https://github.com/drpast/dantbook-master/actions/runs/45662918098) and [45667246148](https://github.com/drpast/dantbook-master/actions/runs/45667246148); notification runs [45654999024](https://github.com/drpast/dantbook-master/actions/runs/45654999024), [45667896133](https://github.com/drpast/dantbook-master/actions/runs/45667896133), [45687787085](https://github.com/drpast/dantbook-master/actions/runs/45687787085), [45689921001](https://github.com/drpast/dantbook-master/actions/runs/45689921001), [45696003925](https://github.com/drpast/dantbook-master/actions/runs/45696003925), [45696846391](https://github.com/drpast/dantbook-master/actions/runs/45696846391), [45702589714](https://github.com/drpast/dantbook-master/actions/runs/45702589714), [45703145657](https://github.com/drpast/dantbook-master/actions/runs/45703145657), [45707642392](https://github.com/drpast/dantbook-master/actions/runs/45707642392), [45708182171](https://github.com/drpast/dantbook-master/actions/runs/45708182171), [45712018094](https://github.com/drpast/dantbook-master/actions/runs/45712018094), [45712574458](https://github.com/drpast/dantbook-master/actions/runs/45712574458), [45814068900](https://github.com/drpast/dantbook-master/actions/runs/45814068900) and [45814602941](https://github.com/drpast/dantbook-master/actions/runs/45814602941) are not CI. The script defect remains and may recur until separately fixed. No code was changed in this monitoring run.
- The Windows sidebar was verified locally after checkpoint 30: its cache and UI showed overall **72%**, the active **Step 31/39**, step 30 recorded as completed with PR #42/CI success, and step 31 pending.
- Checkpoint 31/39 remains pending because offline-first implementation is absent; PR #44/#45 only record that verified gap.
- Checkpoint 32/39 remains pending because backup/restore and continuous security verification are absent; PR #46/#47 only record that verified gap.
- Checkpoint 33/39 remains pending because consolidated cross-module regression coverage is absent; PR #48/#49 only record that verified gap.
- Checkpoint 34/39 remains pending because formal performance, accessibility and usability checks are absent; PR #50/#51 only record that verified gap.
- Checkpoint 35/39 remains pending because blocker resolution and fix verification are absent; PR #52/#53 only record that verified gap.
- Checkpoint 36/39 remains pending because production configuration and deployment preparation are absent; PR #54/#55 only record that verified gap.
- Checkpoint 37/39 remains pending because final MVP acceptance against scope is absent; PR #56/#57 only record that verified gap.
- Checkpoint 38/39 remains pending because user/admin documentation and handover are absent; PR #58/#59 only record that verified gap.
- Checkpoint 39/39 remains pending owner acceptance. PR #60/#61 recorded the gap; PR #88/#89 added draft readiness artifacts and evidence but did not satisfy publication, rollback, support, sign-off, go/no-go or release-record requirements.

## Permanent exclusions

Enterprise features, initial-release X-ray/photo storage and integrations, NanoPix/radiograph integration, digital treatment consent forms, and periodontal charting remain excluded.

<!-- AUTO-SYNC START -->
## Automatically verified GitHub snapshot

**Checked:** 27 November 2026, 10:07 PM IST

- Open PRs: [#73 — build(deps-dev): bump prisma from 6.19.3 to 7.10.1](https://github.com/drpast/dantbook-master/pull/73) (open; CI **failure**); [#74 — build(deps-dev): bump @nestjs/cli from 11.0.24 to 12.0.15](https://github.com/drpast/dantbook-master/pull/74) (open; CI **success**); [#72 — build(deps): bump @nestjs/platform-express from 11.2.11 to 12.6.0](https://github.com/drpast/dantbook-master/pull/72) (open; CI **failure**); [#71 — build(deps): bump @nestjs/core from 11.2.11 to 12.6.0](https://github.com/drpast/dantbook-master/pull/71) (open; CI **failure**); [#70 — build(deps): bump dotenv from 16.6.1 to 18.0.10](https://github.com/drpast/dantbook-master/pull/70) (open; CI **success**); [#69 — build(deps): bump @nestjs/common from 11.2.11 to 12.6.0](https://github.com/drpast/dantbook-master/pull/69) (open; CI **failure**); [#68 — build(deps): bump actions/checkout from 4 to 7](https://github.com/drpast/dantbook-master/pull/68) (open; CI **success**); [#67 — build(deps): bump actions/setup-node from 4 to 7](https://github.com/drpast/dantbook-master/pull/67) (open; CI **success**)
- Main CI: **success** ([run](https://github.com/drpast/dantbook-master/actions/runs/46027334422))
- Main commit: [a809743](https://github.com/drpast/dantbook-master/commit/a809743cfe1d2c888f47eb12b753f452efec96d2) — docs: refresh final handover verified state (#92)
- Progress manifest reviewed: **2026-11-27**; overall **72%**.
- PR work is not treated as merged or complete; progress is changed only from evidence-reviewed manifest.

Progress is read from progress-manifest.json and is updated only after evidence review.
<!-- AUTO-SYNC END -->


## Checkpoint 39 verification — 26 November 2026, 08:00 PM IST (historical)

This section is a dated historical record. Current verified main, CI and tracker state is in the auto-sync section above.

- Main HEAD: [1240456](https://github.com/drpast/dantbook-master/commit/124045686ac334fcff1294ea944cba7123ed061d) — docs: record checkpoint 39 gap merged evidence (#61).
- Main CI: **passed** on the exact HEAD in [run 45837733923](https://github.com/drpast/dantbook-master/actions/runs/45837733923) (workflow name CI, push event).
- [Run 45838402567](https://github.com/drpast/dantbook-master/actions/runs/45838402567) is the separate notification workflow and is not a CI result.
- Open PRs: none. PRs #60 and #61 are merged; no release is published.
- Checkpoint 39/39 — Release readiness and launch checklist: **pending**, not complete. Checkpoints 31–38 remain pending/blocked for offline sync, backup/restore/security, cross-module regression, performance/accessibility/usability, blocker/fix verification, production deployment, final MVP acceptance and operator handover evidence.
- Milestone consistency flag: the module summary shows Medical History, Finance, Dental Laboratory and Recall & Follow-up at 100%, while similarly named milestone entries remain at 20%/0%. Values are intentionally unchanged pending semantic/evidence review; no milestone completion is inferred from module percentages.
- Overall progress remains **72%**; progress-manifest.json percentages were not changed.
