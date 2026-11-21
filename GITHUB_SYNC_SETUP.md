# GitHub-native Progress Dashboard synchronization

This repository can automatically synchronize public-safe project metadata from the private drpast/dantbook-master repository. It does not copy source code or modify the DantBook product repository.

## One-time setup

1. Create a fine-grained personal access token (or GitHub App token) limited to the private drpast/dantbook-master repository.
2. Grant read-only permissions: **Metadata (read), Contents (read), Actions (read), and Pull requests (read)**. Contents read is required to query the latest commit.
3. In this repository, go to Settings → Secrets and variables → Actions → New repository secret.
4. Name it DANTBOOK_REPO_READ_TOKEN and paste the token.
5. After merging this workflow, run it once from Actions → Sync DantBook progress from GitHub → Run workflow.
6. Verify the run succeeded and the three status files updated. The desktop dashboard will pick up status.json on its next polling interval.

## Behavior

- Runs daily at 09:00 IST; can also be started manually.
- Reads default-branch commit, open PRs, and GitHub Actions status.
- Updates status.json, CURRENT_TASK.md, and CHANGELOG.md.
- Does not automatically increase progress percentages.
- Does not write to the private product repository.
- Dashboard repo GITHUB_TOKEN is scoped to Contents write; no sync loop.
- Public output contains only safe metadata (commit message/SHA, PR title/URL/branch, and CI state).

## Privacy

Never publish patient data, clinic records, source code, credentials, API keys, database URLs, private backups, or confidential documents in this repository.
