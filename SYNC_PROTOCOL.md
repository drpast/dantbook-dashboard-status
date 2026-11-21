# DantBook — Two-Account Progress Synchronization Protocol

## Repository role
This public repository is the canonical shared source for progress metadata only. It is not the source-code repository.

## Start-of-session checklist
- Read the latest `status.json`.
- Read `CURRENT_TASK.md`.
- Read the latest `CHANGELOG.md` entries.
- Confirm the latest source ZIP/commit separately.
- Check whether another account has updated the repository since the previous session.

## End-of-session checklist
Only after inspecting and verifying actual code:
- Update module percentages/status in `status.json`.
- Update current task and next action in `CURRENT_TASK.md`.
- Append a dated entry to `CHANGELOG.md`.
- Record source version/commit, tests, build and backup evidence.
- Commit changes with a descriptive message.
- Report the GitHub commit URL and remaining work to the user.

## Concurrency rules
- Pull/read the latest main branch before writing.
- Never blindly replace newer content.
- If another account has committed since your read, reconcile both updates.
- Prefer small, descriptive commits.
- Do not claim a GitHub update succeeded until GitHub confirms it.

## Progress rules
- Percentages are estimates, not code metrics.
- Do not count planned work, mockups, demos or placeholders as completed production work.
- Mark a module complete only after its acceptance criteria and tests pass.
- Preserve historical progress and explain corrections.

## Privacy rules
This repository is public. Never commit patient data, clinic records, credentials, tokens, API keys, database connection strings, private source code, private backups or confidential documents.
