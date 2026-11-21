# DantBook — Current Shared Task

**Last verified snapshot:** 21 November 2026  
**Recorded master baseline:** `v0.1.2 Medical History UI` (Library/GitHub reconciliation was previously reported exact; ongoing implementation activity is tracked separately on GitHub main)  
**Latest main commit checked:** `7fd28e3061eba2c370459aea59523dad533c0ab2`  
**Current workstream:** CI baseline verification, migration repair, and Medical History & Clinical Alerts  
**Priority:** P0 — resolve the first migration blocker before relying on CI results or increasing progress.

## Verified GitHub snapshot
- Main commit: [`7fd28e3`](https://github.com/drpast/dantbook-master/commit/7fd28e3061eba2c370459aea59523dad533c0ab2)
- Draft PR #1: [CI: Establish DantBook baseline verification](https://github.com/drpast/dantbook-master/pull/1) — open, not merged.
- PR branch reports 22 files changed, +1,159 / −88 lines; includes PostgreSQL 16 CI, patient ID generation `YYMNNNN`, primary mobile validation, organization-wide patient identity, cross-branch patient access, shared demographics/allergy alerts, branch-access UI, RLS tests, and concurrent patient-number allocation testing.
- CI run [#93](https://github.com/drpast/dantbook-master/actions/runs/44918122856) failed at migration `20261121000300_shared_patient_branch_access`, PostgreSQL error `42830`: no unique constraint matches referenced table columns `patients(organization_id, id)`.
- Migration 16 failed; later checks (typecheck/build/RLS verification) were not reached. Do not call this branch fully verified.

## Immediate next steps
1. Fix the FK target by ensuring the referenced column pair has a matching unique constraint/index (or adjust the FK to the correct existing key), with migration-safe ordering.
2. Re-run CI and verify migrations, typecheck, build, and RLS tests actually execute and pass.
3. Review the PR branch changes against the approved scope and preserve existing data.
4. Merge only when verification is successful and appropriately reviewed.
5. Continue Medical History & Clinical Alerts completion after the baseline is stable; update progress only with evidence.

## Progress evidence rule
Record source version/commit, completed acceptance criteria, actual test commands/results, build result, and verified backup reference before increasing module percentages. Planned work, mockups, demos and placeholders are not completion evidence.

## Permanent exclusions
Digital treatment consent/consent management, enterprise features, initial-release X-ray/photo storage, NanoPix integration, and previously excluded periodontal charting components.
