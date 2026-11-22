# DantBook — Current Shared Task

**Last checked:** 23 November 2026, 03:52 AM IST  
**Baseline archive:** `v0.1.2 Medical History UI` (preserved in ChatGPT Library)  
**Current source activity:** Main CI success; Open PRs: #15 test: medical history data model and migration acceptance (CI success).

## Verified CI

- Main CI: **success** — [run 44948187965](https://github.com/drpast/dantbook-master/actions/runs/44948187965). Verified job steps include migrations, foundation checks, PostgreSQL RLS, shared-patient access boundaries, concurrent patient-number allocation, type-check, build, browser acceptance, and authenticated API acceptance.
- PR #12 Codex development workflow docs: **success** — [run 44950575811](https://github.com/drpast/dantbook-master/actions/runs/44950575811). Documentation-only; open draft, not merged.
- PR #11 Dental Laboratory case API: **failure** — [run 44949784904](https://github.com/drpast/dantbook-master/actions/runs/44949784904). Failed at Prisma Client generation (P1012): five invalid bare `labOrders` relation declarations in Organization, Branch, Patient, PatientBranchAccess, and ClinicalRecord models. Later validation/build/acceptance stages were skipped. This blocks PR #11 only; main remains green.

## Recently merged milestones

- PR #3 patient browser acceptance — merged; latest PR-head CI passed [44929846484](https://github.com/drpast/dantbook-master/actions/runs/44929846484).
- PR #4 Medical History alert/correction browser acceptance — merged; CI passed [44932842340](https://github.com/drpast/dantbook-master/actions/runs/44932842340).
- PRs #5–#10 also merged with passing CI: clinical record, treatment plan, FDI odontogram, prescription workflow, billing workflow, and branch inventory workspace.
- These merged features are recorded as source activity. Overall/module progress remains at the conservative, evidence-reviewed **25%**; no percentages were increased in this synchronization.

## Granular task tracker

The tracker contains **39 checkpoints** across seven work groups:

- Engineering foundation: 6 checkpoints
- Medical History: 7 checkpoints
- Finance: 5 checkpoints
- Dental Laboratory: 5 checkpoints
- Recall & Follow-up: 5 checkpoints
- Integration & testing: 7 checkpoints
- Release & deployment: 4 checkpoints

Current checkpoint: **7/39 — Medical History data model and migration acceptance** (pending; Next checkpoint; no acceptance evidence recorded yet.). Checkpoint statuses are tracked separately from overall/module progress.

## Progress evidence

Percentages live in `progress-manifest.json`. Progress was reviewed on **22 November 2026** for checkpoint/PR state only. Overall progress remains **25%** and module percentages were not changed; a full module-evidence review is still required before adjusting them.

## Permanent exclusions

Digital treatment consent/consent management, enterprise features, initial-release X-ray/photo storage, NanoPix integration, and periodontal charting remain excluded.

<!-- AUTO-SYNC START -->
## Automatically verified GitHub snapshot

**Checked:** 23 November 2026, 03:52 AM IST

- Open PRs: [#15 — test: medical history data model and migration acceptance](https://github.com/drpast/dantbook-master/pull/15) (open-draft; CI **success**)
- Main CI: **success** ([run](https://github.com/drpast/dantbook-master/actions/runs/45077294368))
- Main commit: [11cb60e](https://github.com/drpast/dantbook-master/commit/11cb60e7ee89997e78f1923500ae6724778a6884) — feat: add branch-scoped dental laboratory case API (#11)
- Progress manifest reviewed: **2026-11-22**; overall **25%**.
- PR work is not treated as merged or complete; progress is changed only from evidence-reviewed manifest.

Progress is read from progress-manifest.json and is updated only after evidence review.
<!-- AUTO-SYNC END -->

## Current desktop view

The desktop app displays installer-style live task progress plus one row per involved file/activity, each with its own bar, status, and explanatory note. It polls the raw `status.json` feed and refreshes on its configured interval.
