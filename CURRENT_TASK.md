# DantBook — Current Shared Task

**Last checked:** 21 November 2026  
**Baseline archive:** `v0.1.2 Medical History UI` (preserved in ChatGPT Library)  
**Current source activity:** GitHub main and PR #1 are tracked separately from the archived baseline.

## Verified CI
- PR #1: [CI baseline verification](https://github.com/drpast/dantbook-master/pull/1), still open-draft and **not merged**.
- Latest reported successful run: [44922607698](https://github.com/drpast/dantbook-master/actions/runs/44922607698).
- Job step readback confirms success for migrations, foundation checks, PostgreSQL RLS, shared patient access boundaries, concurrent patient-number allocation, workspace type-check, and workspace build.
- Earlier run [44918122856](https://github.com/drpast/dantbook-master/actions/runs/44918122856) failed with migration error 42830. Treat that as historical; the later run passed the listed checks. PR changes are not merged into main.
- Main CI remains reported as `not-found` in the current snapshot.

## Next steps
1. Review the PR diff and scope before merging; the successful CI is verification evidence, not code review.
2. Merge only after review.
3. Continue Medical History/Clinical Alerts and update progress only after acceptance evidence.
4. Keep the progress manifest current at verified milestones.

## Progress evidence
Percentages live in `progress-manifest.json`. Review acceptance criteria and tests before changing values; no automatic increases based on activity alone.

## Permanent exclusions
Digital treatment consent/consent management, enterprise features, initial-release X-ray/photo storage, NanoPix integration, and periodontal charting remain excluded.

<!-- AUTO-SYNC START -->
## Automatically verified GitHub snapshot

**Checked:** 21 November 2026

- Open PR #1 — CI baseline verification: open-draft; latest PR CI **success**.
- Successful run: [44922607698](https://github.com/drpast/dantbook-master/actions/runs/44922607698).
- Main CI: **not-found** in the latest snapshot.
- Progress: **25%**, from `progress-manifest.json`; no increase claimed by this sync repair.

Progress manifest reviewed 21 November 2026.
<!-- AUTO-SYNC END -->
