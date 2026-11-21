# GitHub-native Progress Dashboard synchronization

This public repository syncs public-safe project metadata from private `drpast/dantbook-master`. It does not copy source code or modify the DantBook product repository.

## One-time setup
1. Create a fine-grained PAT (or GitHub App token) restricted to the private `drpast/dantbook-master` repository.
2. Grant read-only permissions: Metadata, Contents, Actions, and Pull requests.
3. In this repository, open Settings → Secrets and variables → Actions → New repository secret.
4. Name it `DANTBOOK_REPO_READ_TOKEN` and paste the token.
5. After merging, run the workflow once from Actions → **Sync DantBook progress from GitHub** → Run workflow.
6. Verify it succeeds and status files are updated/readable. The desktop app should refresh within its configured polling interval (30 seconds).

## Behavior
- Scheduled every 5 minutes; manual dispatch also supported. Meaningful updates are committed immediately; a sync-health heartbeat is committed at least every 15 minutes.
- Reads private repo default-branch commit, open PRs, and CI statuses.
- Reads `progress-manifest.json` as the single progress source of truth and applies it to `status.json`.
- Updates `status.json`, `CURRENT_TASK.md` auto-sync section, and `CHANGELOG.md` on meaningful changes or heartbeat. `sync_generated_at` is separate from the progress review date.
- Progress percentages are evidence-reviewed manually; CI/commits/PRs never auto-increase them.
- Does not write to the private product repository.
- Dashboard repo `GITHUB_TOKEN` has Contents write only. Sync does not trigger a loop.
- Public output contains safe metadata only (commit SHA/message/URL, PR title/URL/branch, CI state, and approved progress estimates).

## Privacy
Never publish patient data, clinic records, source code, credentials, tokens, API keys, database URLs, private backups, or confidential documents.
