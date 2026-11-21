# DantBook Progress Changelog

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
