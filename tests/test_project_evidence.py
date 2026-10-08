"""Synthetic fixtures test rejection behavior, not evidence about an actual app."""
import hashlib
import importlib.util
import json
import tempfile
import unittest
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("check_project", ROOT / "scripts/check_project.py")
CHECK = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECK)
AS_OF = date(2026, 10, 8)


class EvidenceChecks(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.file = self.root / "synthetic.txt"
        self.file.write_text("Synthetic unit-test evidence; no real project claim.\n")
        self.digest = hashlib.sha256(self.file.read_bytes()).hexdigest()
        self.state = json.loads((ROOT / "templates/PROJECT_STATE.json").read_text())

    def evidence(self, role="stage_report"):
        return {"path": "synthetic.txt", "sha256": self.digest, "role": role}

    def go_through(self, final):
        self.state.update(project="Synthetic test only", workflow_sha="a" * 40, profiles=["VISUALIZATION"])
        self.state["inputs"] = [{"id": "D-TEST", "version": "test-v1", "checked_at": "2026-10-08", "valid_until": "2027-03-12", "evidence": [self.evidence("source")]}]
        for i in range(final + 1):
            stage = self.state["stages"][i]
            stage.update(status="GO", revision=1, checked_at="2026-10-08", valid_until="2027-03-12", reviewer={"kind": "HUMAN", "name": "Synthetic reviewer"}, authorization="Only the next bounded test")
            stage["depends_on"] = {} if i == 0 else {f"{i - 1:02d}": 1}
            stage["input_versions"] = {"D-TEST": "test-v1"}
            stage["evidence"] = [self.evidence(role) for role in {"stage_report"} | CHECK.REQUIRED_ROLES.get(stage["id"], set())]

    def check(self, required=None):
        return CHECK.validate(self.state, self.root, AS_OF, required)

    def assert_error(self, fragment, required=None):
        self.assertTrue(any(fragment in err for err in self.check(required)), self.check(required))

    def test_blank_is_consistent_but_not_release_ready(self):
        self.assertEqual(self.check(), [])
        self.assert_error("required Stage 11", "11")

    def test_empty_go_is_rejected(self):
        self.state["stages"][0]["status"] = "GO"
        self.assert_error("evidence required")

    def test_valid_record(self):
        self.go_through(4)
        self.assertEqual(self.check(), [])

    def test_changed_evidence_hash(self):
        self.go_through(0)
        self.file.write_text("changed after approval")
        self.assert_error("evidence hash changed")

    def test_empty_evidence_is_not_accepted_even_with_matching_hash(self):
        self.go_through(0)
        self.file.write_text("")
        for evidence in self.state["stages"][0]["evidence"]:
            evidence["sha256"] = hashlib.sha256(b"").hexdigest()
        self.assert_error("empty evidence")

    def test_outside_root_evidence(self):
        self.go_through(0)
        self.state["stages"][0]["evidence"][0]["path"] = "../outside.txt"
        self.assert_error("outside-root")

    def test_changed_input_version(self):
        self.go_through(1)
        self.state["inputs"][0]["version"] = "test-v2"
        self.assert_error("input version missing/changed")

    def test_changed_predecessor_revision(self):
        self.go_through(1)
        self.state["stages"][0]["revision"] = 2
        self.assert_error("upstream status/revision changed")

    def test_stale_predecessor_cannot_support_go(self):
        self.go_through(1)
        self.state["stages"][0]["status"] = "STALE"
        self.assert_error("upstream status/revision changed")

    def test_expired_source_and_evaluation(self):
        self.go_through(0)
        self.state["inputs"][0]["valid_until"] = "2026-10-07"
        self.state["stages"][0]["valid_until"] = "2026-10-07"
        self.assert_error("expired")

    def test_future_checked_date(self):
        self.go_through(0)
        self.state["stages"][0]["checked_at"] = "2026-10-09"
        self.assert_error("in the future")

    def test_unknown_expiry_cannot_be_indefinite(self):
        self.go_through(0)
        self.state["inputs"][0]["valid_until"] = None
        self.assert_error("no_expiry_reason")

    def test_user_screen_required_before_selection_go(self):
        self.go_through(4)
        self.state["stages"][4]["evidence"] = [self.evidence()]
        self.assert_error("early_user_screen")

    def test_comparative_value_roles_required(self):
        self.go_through(7)
        self.state["stages"][7]["evidence"] = [self.evidence()]
        self.assert_error("baseline_comparison")
        self.assert_error("od_contribution")

    def test_conditional_recruitment_is_bounded(self):
        self.go_through(4)
        stage = self.state["stages"][4]
        stage.update(status="CONDITIONAL GO", evidence=[self.evidence()], authorization_kind="RECRUIT", conditions=[{"item":"Early screen missing", "owner":"Synthetic owner", "due":"2026-10-10", "allowed_action":"Recruit for rough-screen test only"}])
        self.assertEqual(self.check(), [])
        stage["authorization_kind"] = "PUBLISH"
        self.assert_error("limited work only")

    def test_blocker_disallows_conditional_go(self):
        self.go_through(0)
        self.state["stages"][0]["blockers"] = ["Unresolved mandatory license"]
        self.assert_error("unresolved blocking")

    def test_ready_requires_no_receipt(self):
        self.go_through(12)
        self.state["submission"].update(state="READY FOR SUBMISSION", ready_stage_revision=1)
        self.assertEqual(self.check(), [])

    def test_submission_requires_receipt_and_actual_timestamp(self):
        self.go_through(12)
        self.state["submission"].update(state="SUBMITTED WITH RECEIPT", ready_stage_revision=1)
        self.assert_error("receipt")
        self.assert_error("submitted_at")
        self.state["submission"].update(receipt=[self.evidence("receipt")], submitted_at="2026-10-08T16:00:00+09:00")
        self.assertEqual(self.check(), [])

    def test_readiness_stales_after_final_revision_changes(self):
        self.go_through(12)
        self.state["submission"].update(state="READY FOR SUBMISSION", ready_stage_revision=1)
        self.state["stages"][12]["revision"] = 2
        self.assert_error("current Stage 12")

    def test_malformed_types_produce_errors_without_crashing(self):
        self.go_through(1)
        self.state["stages"][0]["status"] = []
        self.state["profiles"] = [{}]
        self.state["submission"]["state"] = []
        self.assert_error("invalid status")
        self.assert_error("validation profile")
        self.assert_error("submission: invalid state")


if __name__ == "__main__":
    unittest.main()
