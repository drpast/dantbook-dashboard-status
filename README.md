# DantBook Progress Dashboard Status

This repository is the shared, public-safe progress source for the DantBook project.

## Canonical status
- Machine-readable status: [status.json](./status.json)
- **Progress source of truth:** [progress-manifest.json](./progress-manifest.json)
- Current task: [CURRENT_TASK.md](./CURRENT_TASK.md)
- Progress synchronization rules: [SYNC_PROTOCOL.md](./SYNC_PROTOCOL.md)
- Progress history: [CHANGELOG.md](./CHANGELOG.md)

Raw status endpoint:
https://raw.githubusercontent.com/drpast/dantbook-dashboard-status/main/status.json

## Workflow
1. Read status, current task, changelog, and the progress manifest before starting.
2. Inspect actual project source and acceptance criteria before claiming completion.
3. Update `progress-manifest.json` only when completion evidence supports the change.
4. The sync workflow copies that manifest into `status.json` and refreshes private-repository metadata.
5. Record source commit, tests/build evidence, and remaining work in the task/changelog.
6. Reconcile concurrent updates; do not blindly overwrite newer work.

## Privacy and scope
This repository is public. Store only non-sensitive project-progress metadata and public-safe instructions. Never store source code, patient data, clinic records, credentials, API keys, database URLs, secrets, private backups or confidential handover material.

## Dashboard behavior
The desktop dashboard should poll the raw `status.json` endpoint every 30 seconds and retain last-known-good data for offline display. A successful refresh should replace the displayed snapshot; stale-cache state should be visible.

Granular task steps show completed, in-progress, review, and pending work. Progress estimates are manually evidence-reviewed, not code metrics. Commits, PR activity, CI success, mockups, placeholders, or demos alone must not automatically raise completion.

## GitHub-native synchronization
The workflow polls the private DantBook repo every 5 minutes and supports manual dispatch. It reads the latest main commit, open PR metadata, and CI status, plus the public progress manifest and step tracker. It commits meaningful status/progress changes immediately and publishes a sync-health heartbeat at least every 15 minutes. `sync_generated_at` tracks feed sync; `progress_tracking.last_reviewed` remains the evidence-review date. Setup: [GITHUB_SYNC_SETUP.md](./GITHUB_SYNC_SETUP.md).
