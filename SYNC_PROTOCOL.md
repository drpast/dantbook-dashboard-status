# DantBook — Progress Synchronization Protocol

## Repository role
This public repository is the canonical shared source for public-safe progress metadata, not product source code.

## Start of session
- Read `status.json`, `progress-manifest.json`, `CURRENT_TASK.md`, and the latest changelog entries.
- Confirm source ZIP/version/commit separately.
- Reconcile concurrent changes before writing.

## Updating progress
- Edit **`progress-manifest.json` only** for progress percentages, module statuses, milestones, target date, or current master.
- Update `reviewed_on` when the progress values have been evidence-reviewed.
- Do not infer progress from commit counts, PRs, CI, generated UI, mockups, demos, or placeholders.
- Require acceptance criteria, code review, and appropriate tests/build evidence for increases.
- The sync workflow applies this manifest to `status.json`; do not manually edit both files for progress values.

## End of session
- Update `CURRENT_TASK.md` and append a dated `CHANGELOG.md` entry with source version/commit, verified work, tests/build evidence, and next action.
- Confirm GitHub accepted the commit before reporting success.
- Never overwrite concurrent updates blindly.

## Automated sync
- Polls private `drpast/dantbook-master` every 5 minutes; manual dispatch is available. Feed heartbeat is committed every 15 minutes when otherwise unchanged.
- Reads main commit, open PRs, and CI metadata from the `CI` workflow only, matched to the exact commit or PR head SHA. Notification, dispatch, and other workflow runs are never treated as CI results.
- Applies the public progress manifest; meaningful changes are committed immediately, with a sync-health heartbeat at least every 15 minutes.
- Validation rejects any non-PR checkpoint status that differs from the reviewed manifest, so blocked or pending gap checkpoints cannot be auto-marked complete.
- `sync_generated_at` / `last_sync_success` records successful feed sync time only. It must never refresh `progress_tracking.last_reviewed` or imply progress review.
- Does not write to the private product repository.
- Public output is restricted to safe metadata. Never expose patient/clinic data, secrets, private source, backups, credentials, or connection strings.


## Installer-style current-task display
- `progress-manifest.json` is the source of truth for `current_task_files`, `current_task_percent`, and `current_task_files_title`.
- List the actual files and activity items involved in the current task, with status, percent, and a concise note. File edits/tests may show 100% when finished; CI/review/merge remain separate activity rows.
- Keep this list tied to the current task and refresh it when the active task changes. Never invent progress; percentages must be supported by evidence.
