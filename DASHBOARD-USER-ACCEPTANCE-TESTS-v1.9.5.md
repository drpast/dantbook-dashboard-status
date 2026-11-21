# DantBook Progress Dashboard v1.9.5 — Windows User Acceptance Checklist

**Purpose:** Record manual acceptance results for the desktop dashboard before any merge, release, or replacement ZIP is considered.

**Selected desktop baseline:** `DantBook-Progress-Dashboard-v1.9.5.zip`  
**Status feed:** `https://raw.githubusercontent.com/drpast/dantbook-dashboard-status/main/status.json`  
**Progress authority:** `progress-manifest.json` in `drpast/dantbook-dashboard-status`  
**Important:** This repository is the public-safe metadata/feed repository. The Windows application source is maintained separately in the selected ZIP. Do not put desktop application source, patient data, credentials, or private configuration in this repository.

## How to record a result

For every test, record **Pass**, **Fail**, or **Not tested**, plus the Windows version, app version shown by the app, date/time, and a screenshot or sanitized log when useful. Do not include tokens, private URLs, patient data, or other secrets. A test marked Not tested is not a pass.

## A. Startup and reliability

- [ ] **A1 — Clean launch:** Extract the v1.9.5 archive to a new folder and launch using its documented startup method. Expected: the app opens without an unhandled exception or missing-file error.
- [ ] **A2 — Repeat launch:** Close and reopen the app several times. Expected: startup remains consistent and does not create duplicate windows or leave a stuck process.
- [ ] **A3 — Missing optional cache:** With the app closed, temporarily move its cache file/folder if identifiable, then relaunch. Expected: the app recovers using the live feed or documented fallback; restore the cache after the test.
- [ ] **A4 — Corrupt cache:** Back up and temporarily replace the cache with invalid content. Expected: invalid cache is rejected safely; the app remains usable and does not display fabricated progress. Restore the original cache.
- [ ] **A5 — Window behavior:** Minimize, maximize, resize, and close/reopen. Expected: controls remain visible and the app exits cleanly.

## B. GitHub feed and synchronization diagnostics

- [ ] **B1 — Live feed:** Launch while online. Expected: data is loaded from the configured raw `status.json` endpoint and the UI shows a successful/updated state.
- [ ] **B2 — Refresh cadence:** Leave the app open for at least 65 seconds. Expected: refresh occurs on the documented 30-second cadence, without requiring a restart.
- [ ] **B3 — Last-known-good/offline:** After a successful load, disconnect the network and wait through a refresh interval. Expected: cached last-known-good data remains visible and the UI clearly indicates stale/offline state.
- [ ] **B4 — Recovery:** Restore network access and wait through a refresh interval. Expected: a successful fetch replaces the stale snapshot and the stale/offline indication clears.
- [ ] **B5 — Feed diagnostics:** Inspect any displayed sync timestamp, source, HTTP/error state, or diagnostics. Expected: values describe feed synchronization and do not imply that project progress was re-reviewed.
- [ ] **B6 — Slow/unavailable endpoint:** If practical, block the endpoint temporarily or use Windows Firewall for the app. Expected: the app remains responsive and retains the last-known-good snapshot.

## C. Data integrity and progress authority

- [ ] **C1 — Manifest consistency:** Compare the displayed overall/module/task progress with the current authoritative `progress-manifest.json`. Expected: values match the feed-derived manifest values; no client-side recalculation is visible.
- [ ] **C2 — No activity inflation:** Confirm that open PRs, commits, and CI activity are shown as activity/status only and do not independently increase completion percentages.
- [ ] **C3 — Unknown/missing values:** If a safe test feed with a missing or invalid progress field is available, use it only in a disposable test environment. Expected: the affected value is shown as unknown/unavailable, not guessed or silently converted into completion.
- [ ] **C4 — Invalid JSON:** If a disposable test endpoint or local test harness is available, provide malformed JSON. Expected: parsing fails safely, last-known-good data is retained, and an understandable error is surfaced.
- [ ] **C5 — Oversized feed:** If a disposable test endpoint or local test harness is available, provide a response larger than the documented limit. Expected: it is rejected safely without UI freeze or replacement of good cached data.

## D. Workspace UI and visualization

- [ ] **D1 — Main workspace:** Verify the main dashboard presents the intended current-task/workspace view rather than an unusable wall of raw JSON or a long checkpoint list.
- [ ] **D2 — Progress presentation:** Check overall, module, milestone, and current-task visuals against the source values.
- [ ] **D3 — Status distinctions:** Verify completed, in-progress, review, pending, stale, and unknown states are visually distinguishable where applicable.
- [ ] **D4 — Long content:** Check long task names, notes, and file/activity rows at the normal window size and after resizing.
- [ ] **D5 — Empty/partial sections:** Verify missing optional sections do not crash the app or create misleading zero-completion claims.

## E. Notifications and user feedback

- [ ] **E1 — Notification behavior:** If notification controls are present, verify their actual behavior and permission/error feedback. A visible placeholder or setting alone does not count as a working notification.
- [ ] **E2 — Error feedback:** Cause a recoverable network/feed error. Expected: the app communicates the problem without an unhandled exception or misleading success message.

## F. History, snapshots, and comparisons

- [ ] **F1 — History availability:** Verify whether history/snapshot views are implemented or are placeholders. Record the exact behavior; do not mark a placeholder as complete.
- [ ] **F2 — Comparison accuracy:** If comparison is implemented, compare two known snapshots. Expected: differences come from stored source snapshots, not locally invented progress history.

## G. Settings, cache, backup, and restore

- [ ] **G1 — Settings persistence:** Change each available setting, close the app, and reopen. Expected: supported settings persist accurately.
- [ ] **G2 — Cache reset:** If a reset control exists, use it after backing up the cache. Expected: cache is reset safely and the app can fetch fresh data again.
- [ ] **G3 — Backup/restore:** If backup/restore controls exist, test with a disposable backup. Expected: restore is validated and does not overwrite unrelated files or silently accept corrupt data.
- [ ] **G4 — Honest capability labeling:** Record controls that are present but do not perform the advertised operation as not implemented.

## H. Export and print

- [ ] **H1 — JSON export:** If available, export and validate that the result is parseable JSON and reflects the currently displayed source snapshot.
- [ ] **H2 — CSV export:** If available, open the exported file in a spreadsheet application and check headers, rows, encoding, and values.
- [ ] **H3 — Excel/PDF/print:** Test each advertised option separately. Record missing formats as not implemented; do not infer support from a disabled or decorative control.
- [ ] **H4 — Privacy:** Verify exports contain only intended public-safe dashboard data and no credentials or private application data.

## I. Windows packaging and lifecycle

- [ ] **I1 — Icon and identity:** Verify the app icon and displayed product identity are correct.
- [ ] **I2 — Version consistency:** Record the version shown in the UI, executable metadata (if present), and startup script. The selected archive is v1.9.5; inconsistent internal labels must be reported, not treated as a new release.
- [ ] **I3 — Shortcuts/tray:** Test only if the feature is actually provided. Record missing functionality as not implemented.
- [ ] **I4 — Upgrade/uninstall:** Do not overwrite a working installation. Test only with a disposable copy and confirm user data/cache behavior before and after.
- [ ] **I5 — Installer:** If no installer is included, record Not implemented rather than assuming the ZIP is an installer.

## J. Security and dependency checks

- [ ] **J1 — Secret handling:** Confirm no GitHub token, credential, or private endpoint is embedded in public feed data or exported files.
- [ ] **J2 — Feed trust:** Confirm the app treats feed content as data, validates expected types/ranges, and does not execute feed-supplied content.
- [ ] **J3 — Local data:** Record where settings/cache are stored and whether permissions are appropriately limited.
- [ ] **J4 — Dependencies:** Record dependency/runtime warnings shown by Windows. A full dependency audit requires source-level review and is not replaced by this manual test.

## K. Performance and usability

- [ ] **K1 — Startup responsiveness:** Record approximate time from launch to first usable view.
- [ ] **K2 — Refresh responsiveness:** Confirm refresh does not freeze the UI or spawn overlapping requests.
- [ ] **K3 — Memory/process stability:** Leave the app open for at least 10 minutes and observe abnormal CPU/memory growth or duplicate processes.
- [ ] **K4 — Readability:** Check text scaling, clipping, contrast, and keyboard navigation at the display scale you normally use.

## L. Evidence and sign-off

Record:
- Windows edition/version:
- Display scaling:
- Archive filename:
- Version shown by application:
- Date/time tested:
- Tests passed:
- Tests failed:
- Tests not tested:
- Reproduction steps for each failure:
- Sanitized screenshots/logs:
- Overall decision: **Accept / Accept with issues / Reject**

## Boundaries

- This checklist is a manual acceptance aid, not proof that any feature is implemented.
- The user-run Windows results are required for Windows runtime, installer, and usability acceptance.
- A test result does not authorize merging a PR, changing the authoritative progress manifest, publishing a release, or creating a replacement release ZIP.
- Never change progress percentages solely because this checklist was created or because tests were attempted.
