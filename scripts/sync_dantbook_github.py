#!/usr/bin/env python3
"""Sync verified private-repo metadata and the evidence-reviewed progress manifest."""
import json, os, urllib.request, urllib.parse
from datetime import datetime
from zoneinfo import ZoneInfo

OWNER, REPO = "drpast", "dantbook-master"
TOKEN = os.environ["DANTBOOK_REPO_READ_TOKEN"]
TODAY = datetime.now(ZoneInfo("Asia/Kolkata")).strftime("%Y-%m-%d")
STAMP = datetime.now(ZoneInfo("Asia/Kolkata")).strftime("%d %B %Y, %I:%M %p IST")
API = "https://api.github.com"

def api(path):
    req = urllib.request.Request(API + path, headers={
        "Accept": "application/vnd.github+json",
        "Authorization": "Bearer " + TOKEN,
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "DantBook-Progress-Sync"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode())

def runs_for(branch):
    data = api(f"/repos/{OWNER}/{REPO}/actions/runs?branch={urllib.parse.quote(branch)}&per_page=10")
    return data.get("workflow_runs", [])

def summarize(runs):
    if not runs:
        return {"status": "not-found", "run_id": None, "url": None}
    r = runs[0]
    state = r.get("conclusion") if r.get("status") == "completed" else r.get("status")
    return {"status": state or "unknown", "run_id": r.get("id"), "url": r.get("html_url")}

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
main_ci = summarize(runs_for(repo["default_branch"]))
pr_data = []
for p in prs:
    ci = summarize(runs_for(p["head"]["ref"]))
    pr_data.append({"number": p["number"], "title": p["title"],
        "state": "open-draft" if p.get("draft") else "open", "url": p["html_url"],
        "head_branch": p["head"]["ref"], "head_sha": p["head"]["sha"],
        "updated_at": p["updated_at"], "ci": ci})

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
        "blocker": ("CI is failing; inspect linked workflow run for details." if first_pr["ci"]["status"] == "failure" else None)})
else:
    snapshot.update({"open_pull_request": None, "pull_request_title": None,
        "pull_request_state": None, "ci_status": main_ci["status"],
        "workflow_run_id": main_ci["run_id"], "workflow_run_url": main_ci["url"],
        "pr_url": None, "blocker": None})

# Apply the single progress source of truth. Progress changes are evidence-reviewed,
# not inferred from commit/PR/CI activity.
status["overall_progress_percent"] = progress["overall_progress_percent"]
status["target_mvp_date"] = progress["target_mvp_date"]
status["target_is_ambitious"] = progress["target_is_ambitious"]
status["current_master"] = progress["current_master"]
status["modules"] = progress["modules"]
status["milestones"] = progress["milestones"]
status["progress_tracking"] = {
    "source": "progress-manifest.json",
    "last_reviewed": progress["reviewed_on"],
    "method": progress["method"],
    "sync_poll_minutes": 30
}

old_progress = {
    "overall_progress_percent": status.get("overall_progress_percent"),
    "modules": status.get("modules"),
    "milestones": status.get("milestones"),
    "target_mvp_date": status.get("target_mvp_date"),
    "current_master": status.get("current_master")
}
new_progress = {
    "overall_progress_percent": progress["overall_progress_percent"],
    "modules": progress["modules"],
    "milestones": progress["milestones"],
    "target_mvp_date": progress["target_mvp_date"],
    "current_master": progress["current_master"]
}
changed_snapshot = {k: v for k, v in snapshot.items() if k != "checked_on"} != {k: v for k, v in old_snapshot.items() if k != "checked_on"}
changed_progress = old_progress != new_progress
if not changed_snapshot and not changed_progress:
    print("No meaningful GitHub metadata or progress-manifest changes; no commit created.")
    raise SystemExit(0)

status["dashboard_updated"] = TODAY
snapshot["checked_on"] = TODAY
status["latest_verified_snapshot"] = snapshot
status["source_repository"] = {"repository": OWNER + "/" + REPO,
    "visibility": "private", "default_branch": repo["default_branch"], "verified_at": STAMP}
if pr_data:
    p = pr_data[0]
    status["current_focus"] = f"GitHub sync: PR #{p['number']} ({p['title']}) {p['state']}; PR CI {p['ci']['status']}; main CI {main_ci['status']}"
    lines = [f"- Open PR: [#{p['number']} — {p['title']}]({p['url']}) ({p['state']}); branch CI: **{p['ci']['status']}**.",
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

block = "## Automatically verified GitHub snapshot\n\n**Checked:** " + STAMP + "\n\n" + "\n".join(lines) + "\n\nProgress is read from progress-manifest.json and is updated only after evidence review."
task = auto_block(task, block)
log += "\n\n## " + TODAY + " — GitHub/progress sync\n- Verified main commit: " + commit["sha"] + " (" + snapshot["main_commit_message"] + ").\n- Main CI: " + main_ci["status"] + ".\n"
if pr_data: log += "- Open PRs: " + "; ".join("#" + str(p["number"]) + " " + p["title"] + " (" + p["state"] + ", CI " + p["ci"]["status"] + ")" for p in pr_data) + ".\n"
log += "- Progress manifest reviewed " + progress["reviewed_on"] + "; overall progress " + str(progress["overall_progress_percent"]) + "%." + (" Progress values changed from manifest." if changed_progress else " Progress values unchanged.") + "\n"

with open("status.json", "w", encoding="utf-8") as f: json.dump(status, f, ensure_ascii=False, indent=2); f.write("\n")
with open("CURRENT_TASK.md", "w", encoding="utf-8") as f: f.write(task)
with open("CHANGELOG.md", "w", encoding="utf-8") as f: f.write(log)
print(f"Synced source {commit['sha']}; metadata_changed={changed_snapshot}; progress_changed={changed_progress}; PRs={len(pr_data)}; main CI={main_ci['status']}")
