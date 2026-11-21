'''Evidence-based task status derivation from GitHub issue/PR state.

This module deliberately does not calculate progress percentages.
'''
from __future__ import annotations

CI_FAILURE_STATES = {"failure", "cancelled", "timed_out", "action_required", "startup_failure"}
CI_PENDING_STATES = {"queued", "waiting", "pending", "in_progress", "requested"}


def derive_task_status(task_step, issue=None, pull_request=None):
    """Return (status, note) using explicit issue/PR links only.

    A merged PR or an issue explicitly closed as completed is completion evidence.
    CI success only makes an open PR review-ready; it never completes a task.
    Unlinked tasks retain their manifest status.
    """
    if pull_request:
        number = pull_request.get("number", task_step.get("pr"))
        if pull_request.get("merged"):
            return "completed", f"PR #{number} merged"
        ci_state = (pull_request.get("ci") or {}).get("status", "unknown")
        if ci_state in CI_FAILURE_STATES:
            return "blocked", f"PR #{number} checks {ci_state}"
        if ci_state == "success":
            if pull_request.get("draft"):
                return "checks-passed-draft", f"PR #{number} draft; checks passed, awaiting review"
            return "review", f"PR #{number} checks passed; awaiting review/merge"
        if ci_state in CI_PENDING_STATES:
            return "in-progress", f"PR #{number} checks {ci_state}"
        return "in-progress", f"PR #{number} is open; CI state {ci_state}"

    if issue:
        number = issue.get("number", task_step.get("issue"))
        if issue.get("state") == "closed":
            if issue.get("state_reason") == "completed":
                return "completed", f"Issue #{number} closed as completed"
            if issue.get("state_reason") == "not_planned":
                return "pending", f"Issue #{number} closed as not planned; not counted as completed"
            return "pending", f"Issue #{number} is closed without completion evidence"
        labels = {str(label.get("name", "")).strip().lower()
                  for label in issue.get("labels", []) if isinstance(label, dict)}
        if "blocked" in labels or "status: blocked" in labels:
            return "blocked", f"Issue #{number} is open and labeled blocked"
        return "in-progress", f"Issue #{number} is open"

    return task_step.get("status", "pending"), task_step.get("note", "")


def build_task_evidence(issue=None, pull_request=None, observed_at=None):
    """Return a public-safe, explainable evidence record for a linked task."""
    if pull_request:
        ci = pull_request.get("ci") or {}
        merged = bool(pull_request.get("merged"))
        record = {
            "source": "github",
            "kind": "pull_request",
            "number": pull_request.get("number"),
            "title": pull_request.get("title"),
            "url": pull_request.get("url"),
            "state": "merged" if merged else "open",
            "merged_at": pull_request.get("merged_at"),
            "head_sha": pull_request.get("head_sha"),
            "ci": {
                "status": ci.get("status"),
                "run_id": ci.get("run_id"),
                "url": ci.get("url"),
            } if ci else None,
            "observed_at": observed_at,
        }
        return record

    if issue:
        labels = [
            label.get("name") for label in issue.get("labels", [])
            if isinstance(label, dict) and label.get("name")
        ]
        return {
            "source": "github",
            "kind": "issue",
            "number": issue.get("number"),
            "title": issue.get("title"),
            "url": issue.get("html_url"),
            "state": issue.get("state"),
            "state_reason": issue.get("state_reason"),
            "labels": labels,
            "updated_at": issue.get("updated_at"),
            "observed_at": observed_at,
        }
    return None
