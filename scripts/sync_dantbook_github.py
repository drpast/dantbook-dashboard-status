#!/usr/bin/env python3
"""Sync verified private-repo metadata and the evidence-reviewed progress manifest."""
import json, os, re, sys, urllib.request, urllib.parse
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

OWNER, REPO = "drpast", "dantbook-master"
TOKEN = os.environ.get("DANTBOOK_REPO_READ_TOKEN", "").strip()
if not TOKEN:
    raise SystemExit("Missing required DANTBOOK_REPO_READ_TOKEN secret.")
SYNC_NOW = datetime.now(timezone.utc).replace(microsecond=0)
SYNC_ISO = SYNC_NOW.isoformat().replace("+00:00", "Z")
TODAY = datetime.now(ZoneInfo("Asia/Kolkata")).strftime("%Y-%m-%d")
STAMP = datetime.now(ZoneInfo("Asia/Kolkata")).strftime("%d %B %Y, %I:%M %p IST")
API = "https://api.github.com"
CI_WORKFLOW_NAME = "CI"

def api(path):
    """Fetch a bounded GitHub API response with retries for transient failures."""
    import time
    from email.utils import parsedate_to_datetime
    req = urllib.request.Request(API + path, headers={
        "Accept": "application/vnd.github+json",
        "Authorization": "Bearer " + TOKEN,
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "DantBook-Progress-Sync"})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=30) as response:
                raw = response.read(2 * 1024 * 1024 + 1)
                if len(raw) > 2 * 1024 * 1024:
                    raise RuntimeError("GitHub API response exceeded 2 MiB limit: " + path)
                return json.loads(raw.decode("utf-8"))
        except urllib.error.HTTPError as exc:
            if exc.code not in (408, 429, 500, 502, 503, 504) or attempt == 2:
                raise
            retry_after = exc.headers.get("Retry-After", "")
            try:
                delay = float(retry_after)
            except (TypeError, ValueError):
                try:
                    delay = max(0.0, (parsedate_to_datetime(retry_after) -
                        datetime.now(timezone.utc)).total_seconds())
                except (TypeError, ValueError, OverflowError):
                    delay = 0.5 * (2 ** attempt)
            time.sleep(min(10.0, max(0.25, delay)))
        except (urllib.error.URLError, TimeoutError, ConnectionError):
            if attempt == 2:
                raise
            time.sleep(min(8.0, 0.5 * (2 ** attempt)))
    raise RuntimeError("GitHub API request failed after retries: " + path)

def runs_for(branch, head_sha=None):
    query = {"branch": branch, "per_page": "100"}
    if head_sha:
        query["head_sha"] = head_sha
    data = api(f"/repos/{OWNER}/{REPO}/actions/runs?" + urllib.parse.urlencode(query))
    return data.get("workflow_runs", [])

def select_ci_run(runs, expected_sha=None):
    """Select only the CI workflow, never notification or other workflow runs."""
    candidates = [r for r in runs if r.get("name") == CI_WORKFLOW_NAME]
    if expected_sha:
        candidates = [r for r in candidates if r.get("head_sha") == expected_sha]
    return candidates[0] if candidates else None

def summarize(runs, expected_sha=None):
    r = select_ci_run(runs, expected_sha)
    if not r:
        return {"status": "not-found", "run_id": None, "url": None,
                "workflow_name": CI_WORKFLOW_NAME}
    state = r.get("conclusion") if r.get("status") == "completed" else r.get("status")
    return {"status": state or "unknown", "run_id": r.get("id"),
            "url": r.get("html_url"), "workflow_name": r.get("name")}

if "--self-test" in sys.argv[1:]:
    sample = [
        {"id": 99, "name": "Notify DantBook dashboard", "head_sha": "current",
         "status": "completed", "conclusion": "success", "html_url": "https://example.test/99"},
        {"id": 42, "name": "CI", "head_sha": "current",
         "status": "completed", "conclusion": "success", "html_url": "https://example.test/42"},
        {"id": 41, "name": "CI", "head_sha": "older",
         "status": "completed", "conclusion": "failure", "html_url": "https://example.test/41"},
        {"id": 98, "name": "Notify DantBook dashboard", "head_sha": "older",
         "status": "completed", "conclusion": "success", "html_url": "https://example.test/98"},
    ]
    current = summarize(sample, "current")
    assert current["run_id"] == 42 and current["status"] == "success", current
    assert summarize(sample, "older")["run_id"] == 41, summarize(sample, "older")
    assert summarize(sample, "missing")["status"] == "not-found"
    assert all(x["workflow_name"] == CI_WORKFLOW_NAME for x in (current, summarize(sample, "older")))
    print("CI run selection self-test passed")
    raise SystemExit(0)

def auto_block(text, block):
    start, end = "<!-- AUTO-SYNC START -->", "<!-- AUTO-SYNC END -->"
    section = start + "\n" + block.strip() + "\n" + end
    if start in text and end in text:
        before, rest = text.split(start, 1)
        _, after = rest.split(end, 1)
        return before.rstrip() + "\n\n" + section + after
    return text.rstrip() + "\n\n" + section + "\n"

with open("status.json", encoding="utf-8") as f: status = json.load(f)
with open("progress-manifest.json", encoding="utf-8") as f: progress = json.load(f)
with open("CURRENT_TASK.md", encoding="utf-8") as f: task = f.read()
with open("CHANGELOG.md", encoding="utf-8") as f: log = f.read()

repo = api(f"/repos/{OWNER}/{REPO}")
commit = api(f"/repos/{OWNER}/{REPO}/commits/{repo['default_branch']}")
prs = api(f"/repos/{OWNER}/{REPO}/pulls?state=open&per_page=100")
closed_prs = api(f"/repos/{OWNER}/{REPO}/pulls?state=closed&per_page=100")
merged_pr_numbers = {p["number"] for p in closed_prs if p.get("merged_at")}
main_ci = summarize(runs_for(repo["default_branch"], commit["sha"]), commit["sha"])
pr_data = []
for p in prs:
    head_sha = p["head"]["sha"]
    ci = summarize(runs_for(p["head"]["ref"], head_sha), head_sha)
    pr_data.append({"number": p["number"], "title": p["title"],
        "state": "open-draft" if p.get("draft") else "open", "url": p["html_url"],
        "head_branch": p["head"]["ref"], "head_sha": p["head"]["sha"],
        "updated_at": p["updated_at"], "ci": ci})

# The API defaults to creation order; explicitly sort by activity so the most recently
# updated open PR is always the dashboard's current focus.
pr_data.sort(key=lambda p: p.get("updated_at", ""), reverse=True)

old_snapshot = status.get("latest_verified_snapshot", {})
snapshot = {"checked_on": TODAY, "main_commit": commit["sha"],
    "main_commit_url": commit["html_url"],
    "main_commit_message": commit["commit"]["message"].splitlines()[0],
    "main_ci_status": main_ci["status"], "main_workflow_run_id": main_ci["run_id"],
    "main_workflow_run_url": main_ci["url"], "open_pull_requests": pr_data}
if pr_data:
    first_pr = pr_data[0]
    snapshot.update({"open_pull_request": first_pr["number"],
        "pull_request_title": first_pr["title"], "pull_request_state": first_pr["state"],
        "ci_status": first_pr["ci"]["status"], "workflow_run_id": first_pr["ci"]["run_id"],
        "workflow_run_url": first_pr["ci"]["url"], "pr_url": first_pr["url"],
        "blocker": ("CI failing for " + ", ".join(f"PR #{p['number']}" for p in pr_data if p["ci"]["status"] == "failure") + "; inspect linked run(s)." if any(p["ci"]["status"] == "failure" for p in pr_data) else None)})
else:
    snapshot.update({"open_pull_request": None, "pull_request_title": None,
        "pull_request_state": None, "ci_status": main_ci["status"],
        "workflow_run_id": main_ci["run_id"], "workflow_run_url": main_ci["url"],
        "pr_url": None, "blocker": None})

# Capture prior progress values before applying the manifest.
old_progress = {
    "overall_progress_percent": status.get("overall_progress_percent"),
    "modules": status.get("modules"),
    "milestones": status.get("milestones"),
    "target_mvp_date": status.get("target_mvp_date"),
    "current_master": status.get("current_master"),
    "task_steps": status.get("task_steps"),
    "current_task_step_id": status.get("current_task_step_id"),
    "current_task_step_number": status.get("current_task_step_number"),
    "task_steps_total": status.get("task_steps_total"),
    "current_task_files": status.get("current_task_files"),
    "current_task_percent": status.get("current_task_percent"),
    "current_task_files_title": status.get("current_task_files_title")
}
old_progress_tracking = status.get("progress_tracking", {})
# Apply the single progress source of truth. Progress changes are evidence-reviewed,
# not inferred from commit/PR/CI activity.
status["overall_progress_percent"] = progress["overall_progress_percent"]
status["target_mvp_date"] = progress["target_mvp_date"]
status["target_is_ambitious"] = progress["target_is_ambitious"]
status["current_master"] = progress["current_master"]
status["modules"] = progress["modules"]
status["milestones"] = progress["milestones"]
status["task_steps"] = progress.get("task_steps", [])
status["task_steps_title"] = progress.get("task_steps_title", "Implementation step tracker")
status["current_task_step_id"] = progress.get("current_task_step_id")
status["current_task_step_number"] = progress.get("current_task_step_number")
status["task_steps_total"] = progress.get("task_steps_total", len(progress.get("task_steps", [])))
status["current_task_files"] = progress.get("current_task_files", [])
status["current_task_percent"] = progress.get("current_task_percent", 0)
status["current_task_files_title"] = progress.get("current_task_files_title", "Current task activity")
# PR-backed steps are refreshed from live GitHub state on every poll.
open_pr_by_number = {p["number"]: p for p in pr_data}
for step in status["task_steps"]:
    pr_number = step.get("pr")
    if not pr_number:
        continue
    if pr_number in merged_pr_numbers:
        step["status"] = "completed"
        step["note"] = f"PR #{pr_number} merged"
    elif pr_number in open_pr_by_number:
        pr_item = open_pr_by_number[pr_number]
        ci_state = pr_item["ci"]["status"]
        step["ci"] = ci_state
        if ci_state == "success":
            step["status"] = "checks-passed-draft" if pr_item["state"] == "open-draft" else "review"
        elif ci_state == "failure":
            step["status"] = "blocked"
        elif ci_state in ("in_progress", "queued", "waiting", "pending"):
            step["status"] = "in-progress"
        else:
            step["status"] = "in-progress"
        step["note"] = f"PR #{pr_number} {pr_item['state']}; CI {ci_state}"
    else:
        step["status"] = "pending"
        step["note"] = f"PR #{pr_number} not currently open"
# Once both browser-acceptance PR checks pass, review/merge becomes the active next step.
acceptance_steps = [x for x in status["task_steps"] if x.get("pr") in (3, 4)]
merge_step = next((x for x in status["task_steps"] if x["id"] == "pr-review-merge"), None)
if len(acceptance_steps) == 2 and merge_step:
    states = [x["status"] for x in acceptance_steps]
    if all(x == "completed" for x in states):
        merge_step["status"] = "completed"
        merge_step["note"] = "PR #3 and #4 merged"
    elif any(x == "blocked" for x in states):
        merge_step["status"] = "blocked"
        merge_step["note"] = "Resolve failing acceptance PR checks before merge"
    elif all(x in ("checks-passed-draft", "review", "completed") for x in states):
        merge_step["status"] = "in-progress"
        merge_step["note"] = "Acceptance PR checks passed; review and merge are next"
    else:
        merge_step["status"] = "pending"
        merge_step["note"] = "Waiting for both acceptance PR checks to pass"
# Pick the live active step automatically: in-progress, then review-ready, then draft-checks-passed, then pending.
active_step = next((x for x in status["task_steps"] if x["status"] == "in-progress"), None)
if active_step is None:
    active_step = next((x for x in status["task_steps"] if x["status"] in ("review", "checks-passed-draft")), None)
if active_step is None:
    active_step = next((x for x in status["task_steps"] if x["status"] == "pending"), None)
if active_step:
    active_index = status["task_steps"].index(active_step) + 1
    status["current_task_step_id"] = active_step["id"]
    status["current_task_step_number"] = active_index
    status["task_steps_total"] = len(status["task_steps"])
    status["current_focus"] = f"Step {active_index}/{len(status['task_steps'])}: {active_step['title']} — {active_step.get('note', '')}"
    status["current_task"] = f"Step {active_index}/{len(status['task_steps'])}: {active_step['title']}"
    status["queue"] = [x["title"] for x in status["task_steps"][active_index-1:]]
else:
    status["current_task_step_id"] = None
    status["current_task_step_number"] = None
    status["current_focus"] = "All tracked implementation steps completed."
    status["current_task"] = "All tracked implementation steps completed."
    status["queue"] = []
status["progress_tracking"] = {
    "source": "progress-manifest.json",
    "last_reviewed": progress["reviewed_on"],
    "method": progress["method"],
    "sync_poll_minutes": 5
}

new_progress = {
    "overall_progress_percent": progress["overall_progress_percent"],
    "modules": progress["modules"],
    "milestones": progress["milestones"],
    "target_mvp_date": progress["target_mvp_date"],
    "current_master": progress["current_master"],
    "task_steps": progress.get("task_steps", []),
    "current_task_step_id": progress.get("current_task_step_id"),
    "current_task_step_number": progress.get("current_task_step_number"),
    "task_steps_total": progress.get("task_steps_total", len(progress.get("task_steps", []))),
    "current_task_files": progress.get("current_task_files", []),
    "current_task_percent": progress.get("current_task_percent", 0),
    "current_task_files_title": progress.get("current_task_files_title", "Current task activity")
}
changed_snapshot = {k: v for k, v in snapshot.items() if k != "checked_on"} != {k: v for k, v in old_snapshot.items() if k != "checked_on"}
changed_progress = (old_progress != new_progress or
    old_progress_tracking.get("last_reviewed") != progress.get("reviewed_on") or
    old_progress_tracking.get("method") != progress.get("method"))
percentages_changed = (old_progress.get("overall_progress_percent") != new_progress.get("overall_progress_percent") or
    old_progress.get("modules") != new_progress.get("modules") or
    old_progress.get("milestones") != new_progress.get("milestones"))
# Publish a sync-health heartbeat at least every 15 minutes, without changing progress review dates.
heartbeat_due = True
last_sync = status.get("sync_generated_at") or status.get("last_sync_success")
if last_sync:
    try:
        parsed_sync = datetime.fromisoformat(last_sync.replace("Z", "+00:00"))
        if parsed_sync.tzinfo is None:
            parsed_sync = parsed_sync.replace(tzinfo=timezone.utc)
        heartbeat_due = (SYNC_NOW - parsed_sync.astimezone(timezone.utc)).total_seconds() >= 900
    except (ValueError, TypeError):
        heartbeat_due = True

if not changed_snapshot and not changed_progress and not heartbeat_due:
    print("No meaningful data changes; heartbeat not due.")
    raise SystemExit(0)

status["dashboard_updated"] = TODAY
status["sync_generated_at"] = SYNC_ISO
status["last_sync_success"] = SYNC_ISO
status["sync_status"] = "healthy"
status["sync_poll_minutes"] = 5
snapshot["checked_on"] = TODAY
status["latest_verified_snapshot"] = snapshot
status["source_repository"] = {"repository": OWNER + "/" + REPO,
    "visibility": "private", "default_branch": repo["default_branch"], "verified_at": STAMP}
if pr_data:
    p = pr_data[0]
    step_focus = f"Step {status.get('current_task_step_number', '—')}/{status.get('task_steps_total', len(status['task_steps']))}: {active_step['title']} — {active_step.get('note', '')}" if active_step else "All tracked steps completed"
    pr_summary = "; ".join(f"#{p['number']} CI {p['ci']['status']}" for p in pr_data)
    status["current_focus"] = step_focus + f" | Open PRs: {pr_summary}; main CI {main_ci['status']}"
    lines = ["- Open PRs: " + "; ".join(f"[#{p['number']} — {p['title']}]({p['url']}) ({p['state']}; CI **{p['ci']['status']}**)" for p in pr_data),
        f"- Main CI: **{main_ci['status']}**" + (f" ([run]({main_ci['url']}))" if main_ci["url"] else ""),
        f"- Main commit: [{commit['sha'][:7]}]({commit['html_url']}) — {snapshot['main_commit_message']}",
        f"- Progress manifest reviewed: **{progress['reviewed_on']}**; overall **{progress['overall_progress_percent']}%**.",
        "- PR work is not treated as merged or complete; progress is changed only from evidence-reviewed manifest."]
else:
    status["current_focus"] = f"GitHub sync: no open PRs; main CI {main_ci['status']}"
    lines = ["- No open pull requests returned by GitHub.",
        f"- Main CI: **{main_ci['status']}**" + (f" ([run]({main_ci['url']}))" if main_ci["url"] else ""),
        f"- Main commit: [{commit['sha'][:7]}]({commit['html_url']}) — {snapshot['main_commit_message']}",
        f"- Progress manifest reviewed: **{progress['reviewed_on']}**; overall **{progress['overall_progress_percent']}%**."]

# Refresh the static summary as well as the auto-sync section, so old checkpoint
# descriptions cannot remain stale when the active step advances.
task = re.sub(r"^\*\*Last checked:\*\*.*$", "**Last checked:** " + STAMP + "  ", task, flags=re.MULTILINE)
activity = "Open PRs: " + "; ".join("#" + str(p["number"]) + " " + p["title"] + " (CI " + p["ci"]["status"] + ")" for p in pr_data)
task = re.sub(r"^\*\*Current source activity:\*\*.*$", "**Current source activity:** Main CI " + main_ci["status"] + "; " + activity + ".", task, flags=re.MULTILINE)
if active_step:
    checkpoint_line = f"Current checkpoint: **{active_index}/{len(status['task_steps'])} — {active_step['title']}** ({active_step['status']}; {active_step.get('note') or 'awaiting verified work'}). Checkpoint statuses are tracked separately from overall/module progress."
else:
    checkpoint_line = "Current checkpoint: all tracked steps completed."
task = re.sub(r"^Current checkpoint:.*$", checkpoint_line, task, flags=re.MULTILINE)
block = "## Automatically verified GitHub snapshot\n\n**Checked:** " + STAMP + "\n\n" + "\n".join(lines) + "\n\nProgress is read from progress-manifest.json and is updated only after evidence review."
task = auto_block(task, block)
log += "\n\n## " + TODAY + " — GitHub/progress sync\n- Verified main commit: " + commit["sha"] + " (" + snapshot["main_commit_message"] + ").\n- Main CI: " + main_ci["status"] + ".\n"
if pr_data: log += "- Open PRs: " + "; ".join("#" + str(p["number"]) + " " + p["title"] + " (" + p["state"] + ", CI " + p["ci"]["status"] + ")" for p in pr_data) + ".\n"
log += "- Progress manifest reviewed " + progress["reviewed_on"] + "; overall progress " + str(progress["overall_progress_percent"]) + "%." + (" Progress percentages updated from manifest." if percentages_changed else " Progress percentages unchanged; checkpoint/task state may have changed.") + "\n"

with open("status.json", "w", encoding="utf-8") as f: json.dump(status, f, ensure_ascii=False, indent=2); f.write("\n")
with open("CURRENT_TASK.md", "w", encoding="utf-8") as f: f.write(task)
with open("CHANGELOG.md", "w", encoding="utf-8") as f: f.write(log)
print(f"Synced source {commit['sha']}; metadata_changed={changed_snapshot}; progress_changed={changed_progress}; PRs={len(pr_data)}; main CI={main_ci['status']}")
