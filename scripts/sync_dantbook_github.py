#!/usr/bin/env python3
"""Fetch verified GitHub metadata from the private DantBook repo and update public-safe progress status."""
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

old = status.get("latest_verified_snapshot", {})
snapshot = {"checked_on": TODAY, "main_commit": commit["sha"],
    "main_commit_url": commit["html_url"],
    "main_commit_message": commit["commit"]["message"].splitlines()[0],
    "main_ci_status": main_ci["status"], "main_workflow_run_id": main_ci["run_id"],
    "main_workflow_run_url": main_ci["url"], "open_pull_requests": pr_data}
changed = {k: v for k, v in snapshot.items() if k != "checked_on"} != {k: v for k, v in old.items() if k != "checked_on"}
if not changed:
    print("No meaningful repository changes detected; leaving dashboard files untouched.")
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
        "- PR work is not treated as merged or complete; progress percentages are not changed automatically."]
else:
    status["current_focus"] = f"GitHub sync: no open PRs; main CI {main_ci['status']}"
    lines = ["- No open pull requests returned by GitHub.",
        f"- Main CI: **{main_ci['status']}**" + (f" ([run]({main_ci['url']}))" if main_ci["url"] else ""),
        f"- Main commit: [{commit['sha'][:7]}]({commit['html_url']}) — {snapshot['main_commit_message']}"]
block = "## Automatically verified GitHub snapshot\n\n**Checked:** " + STAMP + "\n\n" + "\n".join(lines) + "\n\nProgress percentages remain manually evidence-verified."
task = auto_block(task, block)
if changed:
    log += "\n\n## " + TODAY + " — GitHub-native sync\n- Verified main commit: " + commit["sha"] + " (" + snapshot["main_commit_message"] + ").\n- Main CI: " + main_ci["status"] + ".\n"
    if pr_data: log += "- Open PRs: " + "; ".join("#" + str(p["number"]) + " " + p["title"] + " (" + p["state"] + ", CI " + p["ci"]["status"] + ")" for p in pr_data) + ".\n"
    else: log += "- No open PRs.\n"
    log += "- Progress estimates were not automatically changed.\n"
with open("status.json", "w", encoding="utf-8") as f: json.dump(status, f, ensure_ascii=False, indent=2); f.write("\n")
with open("CURRENT_TASK.md", "w", encoding="utf-8") as f: f.write(task)
with open("CHANGELOG.md", "w", encoding="utf-8") as f: f.write(log)
print(f"Snapshot updated for {commit['sha']}; changed={changed}; PR count={len(pr_data)}; main CI={main_ci['status']}")
