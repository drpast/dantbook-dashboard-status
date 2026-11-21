# Desktop dashboard feed contract

## Purpose
This document defines the public JSON contract between the GitHub Actions status publisher and the Windows Progress Dashboard. GitHub is the only operational source of progress and task evidence. The desktop application is a read-only consumer.

## Source URL
`https://raw.githubusercontent.com/drpast/dantbook-dashboard-status/main/status.json`

## Compatibility rules
- Existing top-level fields and their meanings remain unchanged.
- `task_steps` remains an array of task objects.
- New task fields are additive and optional. Older desktop builds must continue to parse and render the fields they already understand, ignoring unknown properties.
- The desktop must not calculate completion percentages from evidence records, PR counts, commits, or CI.
- A missing evidence record means evidence is unavailable or the task has no verified GitHub link; it does not mean completed.
- A closed pull request that was not merged is published with state `closed` and never counts as completion.
- The desktop must continue to use its last-known-good cache only when the GitHub feed cannot be reached. An online GitHub response is authoritative over packaged/local snapshots.

## Existing progress authority
- `overall_progress_percent`, module and milestone percentages, `current_task_percent`, and task manifest values are authored in `progress-manifest.json`.
- GitHub activity may update task `status` and `note` only for explicitly linked issues/PRs.
- GitHub activity must never automatically increase or otherwise recalculate percentages.

## Task evidence extension
A task can optionally include an `evidence` object when the manifest explicitly links it to a verified issue or PR.

### Pull request evidence
```json
{
  "source": "github",
  "kind": "pull_request",
  "number": 11,
  "title": "Dental Laboratory case API foundation",
  "url": "https://github.com/drpast/dantbook-master/pull/11",
  "state": "open",
  "merged_at": null,
  "head_sha": "0123456789abcdef",
  "ci": {
    "status": "success",
    "run_id": 123456789,
    "url": "https://github.com/drpast/dantbook-master/actions/runs/123456789"
  },
  "observed_at": "2026-11-22T00:00:00Z"
}
```

The example values are illustrative only. A real feed must use values retrieved from GitHub; unavailable optional values may be null.

### Issue evidence
An issue evidence object contains `source`, `kind`, `number`, `title`, `url`, `state`, `state_reason`, `labels`, `updated_at`, and `observed_at`.

## Recommended desktop presentation
When the desktop UI is updated to support this extension:
- Show the evidence kind and number as a link to the GitHub issue/PR.
- Show the current GitHub state and CI result when supplied.
- Show the observation timestamp so users can judge freshness.
- Keep evidence details separate from percentage/progress bars.
- If evidence is absent, show an unassessed/not-linked indication rather than inventing a source.
- Do not display private source code, patient/clinic data, tokens, or secrets.

## Validation status
The publisher's evidence-record helper and unit tests are covered by the dashboard sync validation workflows. Compatibility against the user's v1.9.2 Windows executable/source has not yet been verified. The v1.9.2 archive remains the required desktop baseline for that work; do not substitute the separately uploaded v1.9.5 source file.
