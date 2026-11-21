# DantBook — Current Shared Task

**Last baseline:** 21 November 2026  
**Current recorded master:** `v0.1.2 Medical History UI` (package verification pending in the existing status record)  
**Current workstream:** Medical History & Clinical Alerts  
**Priority:** P0 — inspect and complete the existing implementation before starting another module.

## Required steps
1. Obtain and inspect the latest verified DantBook master ZIP/source.
2. Inspect the existing Prisma schema, migrations, database configuration and seed scripts. Do not reset, drop or rebuild an existing database.
3. Separate production functionality from demo screens, placeholders and mock data.
4. Compare existing Medical History & Clinical Alerts implementation with the approved requirements.
5. Implement only missing functionality, preserving working code and data.
6. Complete backend, frontend, permissions, audit logging, offline persistence and synchronization as applicable.
7. Run tests, lint, type checks and production build; record actual results.
8. Create and verify a versioned backup before promoting a new master.
9. Update `status.json` and append a dated entry to `CHANGELOG.md`.

## Next workstream
Financial Management begins only after Medical History & Clinical Alerts is verified complete.

## Evidence required before increasing progress
Record the source version/commit, completed acceptance criteria, test commands and results, build result, and backup reference. Do not infer progress from planned work or UI appearance alone.

## Permanent exclusions
Digital treatment consent/consent management, enterprise features, initial-release X-ray/photo storage, NanoPix integration, and previously excluded periodontal charting components.
