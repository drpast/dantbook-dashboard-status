

## 22 Nov 2026 — Sync freshness improvement
- Added UTC `sync_generated_at` and `last_sync_success` heartbeat fields, separate from progress review date.
- GitHub metadata sync still polls every 5 minutes; heartbeat commits occur at least every 15 minutes when no data changes.
- Progress percentages/status remain copied from the evidence-reviewed manifest and are not calculated or changed by the heartbeat.
# DantBook Progress Changelog

## 2026-11-21 — Expanded granular tracker to 39 checkpoints
- Expanded the task tracker from 8 broad steps to 39 small checkpoints across engineering foundation, Medical History, Finance, Dental Laboratory, Recall & Follow-up, Integration & Testing, and Release & Deployment.
- Current checkpoint remains 5/39: Medical History alert and correction browser tests (PR #4; CI in progress).
- Preserved evidence-based statuses and kept overall progress at 25%; tracker detail does not inflate completion percentages.


## 2026-11-21 — Progress synchronization repair
- Added `progress-manifest.json` as the single source of truth for evidence-reviewed progress values.
- Updated sync workflow to poll every 30 minutes and still support manual dispatch.
- Sync script applies manifest percentages/modules/milestones to `status.json`, and only commits when meaningful data changes.
- Corrected stale task documentation: earlier PR CI failure is historical; latest PR run #44922607698 completed successfully, including migrations, RLS/shared-access/concurrency tests, type-check, and build (job steps verified).
- PR #1 remains open-draft and unmerged; no completion percentages were increased.
- Sync repair is submitted as a pull request; not yet active on main until merged.

## 2026-11-21 — GitHub-native sync (historical)
- Main commit snapshot: `7fd28e3061eba2c370459aea59523dad533c0ab2`.
- PR #1 open; CI status captured as success.
- Progress estimates were not automatically changed.

## 2026-11-21 — Earlier CI failure (historical)
- Run #44918122856 failed at PostgreSQL migration error 42830.
- This was superseded by the later successful run #44922607698; the PR remains unmerged pending review.


## 21 November 2026 — Dashboard sync repair
- Corrected stale snapshot: PR #1 and #2 are merged; PR #3 is open-draft with CI success; PR #4 is open-draft with CI in progress.
- Published current main commit and PR metadata directly to status.json.
- Changed polling schedule to every 5 minutes and sorted open PRs by updated_at descending.
- Added workflow push trigger for sync configuration/progress-manifest changes.
- Progress remains 25%; no completion increase claimed.


## 2026-11-21 — GitHub/progress sync
- Verified main commit: efa75f6ce3eaff024f41c3b8aabd59dcb404d60c (test: verify authenticated patient workflows).
- Main CI: success.
- Open PRs: #4 test: cover medical history alert and correction workflow (open-draft, CI in_progress); #3 test: add patient workflow browser acceptance (open-draft, CI success).
- Progress manifest reviewed 2026-11-21; overall progress 25%. Progress values changed from manifest.


## 21 November 2026 — Granular live step tracker
- Added an 8-step implementation tracker to the evidence-reviewed manifest and published it to status.json.
- Current step 5: Medical History alert/correction browser tests (PR #4, CI in progress); PR #3 has successful CI but remains a draft; PR #1 and #2 merged.
- Desktop Dashboard v1.8.0 now renders task steps separately from module percentages.
- Sync now records the 5-minute source poll interval; desktop refresh remains every 30 seconds.
- Overall progress remains 25%; this tracker reports task state without inflating percentages.


## 2026-11-21 — GitHub/progress sync
- Verified main commit: efa75f6ce3eaff024f41c3b8aabd59dcb404d60c (test: verify authenticated patient workflows).
- Main CI: success.
- Open PRs: #4 test: cover medical history alert and correction workflow (open-draft, CI in_progress); #3 test: add patient workflow browser acceptance (open-draft, CI success).
- Progress manifest reviewed 2026-11-21; overall progress 25%. Progress values changed from manifest.


## 2026-11-21 — GitHub/progress sync
- Verified main commit: efa75f6ce3eaff024f41c3b8aabd59dcb404d60c (test: verify authenticated patient workflows).
- Main CI: success.
- Open PRs: #4 test: cover medical history alert and correction workflow (open-draft, CI success); #3 test: add patient workflow browser acceptance (open-draft, CI success).
- Progress manifest reviewed 2026-11-21; overall progress 25%. Progress values changed from manifest.


## 2026-11-21 — GitHub/progress sync
- Verified main commit: efa75f6ce3eaff024f41c3b8aabd59dcb404d60c (test: verify authenticated patient workflows).
- Main CI: success.
- Open PRs: #4 test: cover medical history alert and correction workflow (open-draft, CI success); #3 test: add patient workflow browser acceptance (open-draft, CI success).
- Progress manifest reviewed 2026-11-21; overall progress 25%. Progress values changed from manifest.


## 2026-11-21 — GitHub/progress sync
- Verified main commit: efa75f6ce3eaff024f41c3b8aabd59dcb404d60c (test: verify authenticated patient workflows).
- Main CI: success.
- Open PRs: #4 test: cover medical history alert and correction workflow (open-draft, CI success); #3 test: add patient workflow browser acceptance (open-draft, CI success).
- Progress manifest reviewed 2026-11-21; overall progress 25%. Progress values changed from manifest.


## 2026-11-21 — GitHub/progress sync
- Verified main commit: efa75f6ce3eaff024f41c3b8aabd59dcb404d60c (test: verify authenticated patient workflows).
- Main CI: success.
- Open PRs: #4 test: cover medical history alert and correction workflow (open-draft, CI in_progress); #3 test: add patient workflow browser acceptance (open-draft, CI success).
- Progress manifest reviewed 2026-11-21; overall progress 25%. Progress values changed from manifest.


## 21 Nov 2026 — Installer-style current task progress
- Replaced checkpoint-list display in desktop app with a scrollable current-task activity list; every file/activity row has its own progress bar, status, and note.
- Task progress bar summarizes current task; completed files are shown individually, with CI and review/merge tracked separately.
- PR #4 CI run 44933570034 verified completed successfully; review/merge of PR #3 and #4 is now the active task. Overall progress remains 25%.


## 2026-11-22 — GitHub/progress sync
- Verified main commit: efa75f6ce3eaff024f41c3b8aabd59dcb404d60c (test: verify authenticated patient workflows).
- Main CI: success.
- Open PRs: #8 feat: add patient prescription workflow (open-draft, CI in_progress); #7 feat: add FDI odontogram workflow (open-draft, CI success); #6 feat: add patient treatment plan workflow (open-draft, CI success); #5 feat: add patient clinical record workflow (open-draft, CI success); #4 test: cover medical history alert and correction workflow (open-draft, CI success); #3 test: add patient workflow browser acceptance (open-draft, CI success).
- Progress manifest reviewed 2026-11-21; overall progress 25%. Progress values changed from manifest.
