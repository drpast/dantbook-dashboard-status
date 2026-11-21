import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
from progress_evidence import derive_task_status, build_task_evidence


class EvidenceStatusTests(unittest.TestCase):
    def setUp(self):
        self.step = {"id": "sample", "status": "pending", "note": "Manifest baseline"}

    def test_merged_pr_completes_task(self):
        status, note = derive_task_status(self.step, pull_request={"number": 12, "merged": True})
        self.assertEqual(status, "completed")
        self.assertIn("merged", note)

    def test_successful_ci_does_not_complete_open_pr(self):
        status, _ = derive_task_status(self.step, pull_request={
            "number": 12, "merged": False, "draft": False, "ci": {"status": "success"}})
        self.assertEqual(status, "review")

    def test_successful_draft_ci_stays_draft(self):
        status, _ = derive_task_status(self.step, pull_request={
            "number": 12, "merged": False, "draft": True, "ci": {"status": "success"}})
        self.assertEqual(status, "checks-passed-draft")

    def test_failed_ci_blocks_open_pr(self):
        status, _ = derive_task_status(self.step, pull_request={
            "number": 12, "merged": False, "draft": False, "ci": {"status": "failure"}})
        self.assertEqual(status, "blocked")

    def test_open_issue_is_in_progress(self):
        status, _ = derive_task_status(self.step, issue={
            "number": 34, "state": "open", "labels": []})
        self.assertEqual(status, "in-progress")

    def test_blocked_issue_label_is_blocked(self):
        status, _ = derive_task_status(self.step, issue={
            "number": 34, "state": "open", "labels": [{"name": "blocked"}]})
        self.assertEqual(status, "blocked")

    def test_issue_closed_as_completed_completes_task(self):
        status, _ = derive_task_status(self.step, issue={
            "number": 34, "state": "closed", "state_reason": "completed"})
        self.assertEqual(status, "completed")

    def test_issue_closed_as_not_planned_is_not_completed(self):
        status, note = derive_task_status(self.step, issue={
            "number": 34, "state": "closed", "state_reason": "not_planned"})
        self.assertEqual(status, "pending")
        self.assertIn("not counted as completed", note)

    def test_merged_pr_evidence_record_is_explainable(self):
        record = build_task_evidence(pull_request={
            "number": 11, "merged": True, "title": "Lab API",
            "url": "https://github.com/example/repo/pull/11",
            "head_sha": "abc123", "merged_at": "2026-11-22T00:00:00Z"
        }, observed_at="2026-11-22T01:00:00Z")
        self.assertEqual(record["kind"], "pull_request")
        self.assertEqual(record["state"], "merged")
        self.assertEqual(record["head_sha"], "abc123")
        self.assertEqual(record["observed_at"], "2026-11-22T01:00:00Z")

    def test_issue_evidence_record_includes_state_and_labels(self):
        record = build_task_evidence(issue={
            "number": 34, "title": "Task issue", "html_url": "https://github.com/example/repo/issues/34",
            "state": "open", "state_reason": None, "labels": [{"name": "blocked"}],
            "updated_at": "2026-11-22T00:00:00Z"
        }, observed_at="2026-11-22T01:00:00Z")
        self.assertEqual(record["kind"], "issue")
        self.assertEqual(record["labels"], ["blocked"])
        self.assertEqual(record["state"], "open")

    def test_unlinked_task_retains_manifest_state(self):
        status, note = derive_task_status(self.step)
        self.assertEqual(status, "pending")
        self.assertEqual(note, "Manifest baseline")


if __name__ == "__main__":
    unittest.main()
