# DantBook Progress Dashboard Status

This repository is the shared, public-safe progress source for the DantBook project.

## Canonical status
- Machine-readable status: [status.json](./status.json)
- Current task: [CURRENT_TASK.md](./CURRENT_TASK.md)
- Progress synchronization rules: [SYNC_PROTOCOL.md](./SYNC_PROTOCOL.md)
- Progress history: [CHANGELOG.md](./CHANGELOG.md)

Raw status endpoint:
https://raw.githubusercontent.com/drpast/dantbook-dashboard-status/main/status.json

## Two-account workflow
1. Before starting work, each AI account reads `status.json` and `CURRENT_TASK.md`.
2. The AI inspects the actual project source before changing code or claiming progress.
3. After verified work, it updates `status.json`, `CURRENT_TASK.md`, and `CHANGELOG.md` in one coherent update session.
4. It records test/build evidence and the exact source version or commit.
5. The other account reads the latest GitHub commit before continuing.
6. If two updates conflict, do not overwrite blindly; compare commits and reconcile.

## Privacy and scope
This repository is public. Store only non-sensitive project-progress metadata and public-safe instructions here. Never store source code, patient data, clinic records, credentials, API keys, database URLs, secrets, private backups or confidential handover material.

Full source code and detailed private project instructions should live in a separate private repository or approved private storage.

## Dashboard behavior
The dashboard may poll the raw `status.json` endpoint every 30 seconds and retain the last successful response for offline display.

Progress figures are manually verified estimates, not automated code metrics. A feature is not complete just because a screen, mockup, placeholder or demo exists.
