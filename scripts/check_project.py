#!/usr/bin/env python3
"""Validate project evidence consistency; never certify user value or real submission."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

STATUSES = {"NOT EVALUATED", "IN PROGRESS", "GO", "CONDITIONAL GO", "NO-GO", "STALE"}
PROFILES = {"DECISION_SUPPORT", "ANALYSIS", "VISUALIZATION"}
IDS = [f"{i:02d}" for i in range(13)]
REQUIRED_ROLES = {
    "04": {"early_user_screen"},
    "05": {"core_cases"},
    "06": {"independent_validation"},
    "07": {"early_user_screen", "baseline_comparison", "od_contribution"},
    "08": {"product_spec"},
    "09": {"operations_rehearsal"},
    "10": {"ux_evaluation"},
    "11": {"release_audit", "operations_plan"},
    "12": {"readiness_check"},
}


def validate(state: object, root: Path, as_of: date, require_stage: str | None = None) -> list[str]:
    errors: list[str] = []
    root = root.resolve()

    def fail(message: str) -> None:
        errors.append(message)

    def text(value: object) -> bool:
        return isinstance(value, str) and bool(value.strip()) and value.upper() not in {
            "TODO", "TO DEFINE", "UNKNOWN", "UNVERIFIED", "NOT TESTED", "NOT EVALUATED"
        }

    def day(value: object, label: str, *, future: bool = False) -> date | None:
        if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
            fail(f"{label}: expected YYYY-MM-DD")
            return None
        try:
            parsed = date.fromisoformat(value)
        except ValueError:
            fail(f"{label}: invalid date")
            return None
        if future and parsed < as_of:
            fail(f"{label}: expired ({value})")
        if not future and parsed > as_of:
            fail(f"{label}: checked date is in the future")
        return parsed

    def evidence(items: object, label: str) -> set[str]:
        roles: set[str] = set()
        if not isinstance(items, list) or not items:
            fail(f"{label}: local hashed evidence required")
            return roles
        for i, item in enumerate(items):
            loc = f"{label}[{i}]"
            if not isinstance(item, dict):
                fail(f"{loc}: expected object")
                continue
            path, digest, role = (item.get(k) for k in ("path", "sha256", "role"))
            if not text(role):
                fail(f"{loc}: evidence role required")
            else:
                roles.add(role)
            if not isinstance(path, str) or not path or Path(path).is_absolute():
                fail(f"{loc}: relative local path required")
                continue
            file = (root / path).resolve()
            if not file.is_relative_to(root) or not file.is_file():
                fail(f"{loc}: missing or outside-root evidence: {path}")
                continue
            if not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest):
                fail(f"{loc}: SHA-256 required")
                continue
            content = file.read_bytes()
            if not content.strip():
                fail(f"{loc}: empty evidence")
            if hashlib.sha256(content).hexdigest() != digest:
                fail(f"{loc}: evidence hash changed: {path}")
        return roles

    if not isinstance(state, dict) or type(state.get("schema_version")) is not int or state.get("schema_version") != 1:
        return ["schema_version must be 1 in a JSON object"]
    stages = state.get("stages")
    if not isinstance(stages, list) or any(not isinstance(s, dict) for s in stages):
        return ["stages must be an array of objects"]
    if [s.get("id") for s in stages] != IDS:
        return ["stages must contain exactly 00..12 in order"]
    by_id = {s["id"]: s for s in stages}
    inputs = state.get("inputs")
    if not isinstance(inputs, list) or any(not isinstance(i, dict) for i in inputs):
        return ["inputs must be an array of objects"]
    input_map: dict[str, dict] = {}
    for item in inputs:
        ident = item.get("id")
        if not text(ident) or ident in input_map:
            fail("input IDs must be nonempty and unique")
        else:
            input_map[ident] = item

    active = [s for s in stages if isinstance(s.get("status"), str) and s["status"] in {"GO", "CONDITIONAL GO"}]
    if active:
        if not text(state.get("project")):
            fail("project name required for evaluated stages")
        if state.get("workflow_version") != "2.0.0":
            fail("this checker requires workflow_version 2.0.0")
        if not isinstance(state.get("workflow_sha"), str) or not re.fullmatch(r"[0-9a-f]{40}", state["workflow_sha"]):
            fail("workflow_sha must be the actual 40-character commit SHA")
        profiles = state.get("profiles")
        if any(s["id"] != "00" for s in active) and (
            not isinstance(profiles, list) or not profiles or any(not isinstance(p, str) or p not in PROFILES for p in profiles)
        ):
            fail("at least one valid validation profile required after Stage 00")

    for stage in stages:
        ident, status = stage["id"], stage.get("status")
        label = f"Stage {ident}"
        if not isinstance(status, str) or status not in STATUSES:
            fail(f"{label}: invalid status")
        rev = stage.get("revision")
        if type(rev) is not int or rev < 0:
            fail(f"{label}: revision must be a nonnegative integer")
        if not isinstance(status, str) or status not in {"GO", "CONDITIONAL GO"}:
            continue
        if type(rev) is not int or rev < 1:
            fail(f"{label}: evaluated revision must be positive")
        checked = day(stage.get("checked_at"), f"{label} checked_at")
        expiry = day(stage.get("valid_until"), f"{label} valid_until", future=True)
        if checked and expiry and expiry < checked:
            fail(f"{label}: valid_until precedes checked_at")
        reviewer = stage.get("reviewer")
        if not isinstance(reviewer, dict) or reviewer.get("kind") != "HUMAN" or not text(reviewer.get("name")):
            fail(f"{label}: recorded human signoff required (not verified by this checker)")
        if not text(stage.get("authorization")):
            fail(f"{label}: bounded authorized next action required")
        blockers = stage.get("blockers")
        if not isinstance(blockers, list) or blockers:
            fail(f"{label}: unresolved blocking items cannot accompany GO/CONDITIONAL GO")
        dependencies = stage.get("depends_on")
        if not isinstance(dependencies, dict):
            fail(f"{label}: depends_on must map Stage IDs to revisions")
            dependencies = {}
        if ident != "00" and IDS[IDS.index(ident) - 1] not in dependencies:
            fail(f"{label}: previous Stage dependency required")
        for parent_id, expected in dependencies.items():
            parent = by_id.get(parent_id)
            if parent is None or parent_id >= ident:
                fail(f"{label}: dependency must be an earlier Stage")
                continue
            if parent.get("status") != "GO" or type(expected) is not int or expected != parent.get("revision"):
                fail(f"{label}: upstream status/revision changed: {parent_id}")
        versions = stage.get("input_versions")
        if not isinstance(versions, dict) or not versions:
            fail(f"{label}: fixed input_versions required")
            versions = {}
        for input_id, expected in versions.items():
            item = input_map.get(input_id)
            if item is None or not text(expected) or expected != item.get("version"):
                fail(f"{label}: input version missing/changed: {input_id}")
                continue
            source_checked = day(item.get("checked_at"), f"input {input_id} checked_at")
            if item.get("valid_until") is None:
                if not text(item.get("no_expiry_reason")):
                    fail(f"input {input_id}: null expiry needs a verified no_expiry_reason")
            else:
                source_expiry = day(item.get("valid_until"), f"input {input_id} valid_until", future=True)
                if source_checked and source_expiry and source_expiry < source_checked:
                    fail(f"input {input_id}: validity precedes checked_at")
            evidence(item.get("evidence"), f"input {input_id} evidence")
        roles = evidence(stage.get("evidence"), f"{label} evidence")
        required = {"stage_report"} | (REQUIRED_ROLES.get(ident, set()) if status == "GO" else set())
        if required - roles:
            fail(f"{label}: missing evidence roles: {', '.join(sorted(required - roles))}")
        conditions = stage.get("conditions")
        if not isinstance(conditions, list):
            fail(f"{label}: conditions must be a list")
        elif status == "GO" and conditions:
            fail(f"{label}: open conditions require CONDITIONAL GO")
        elif status == "CONDITIONAL GO":
            allowed = {"RECRUIT", "BOUNDED_EXPERIMENT", "LOCAL_FIX", "READ_ONLY_REVIEW"}
            if ident in {"04", "07"}:
                allowed = {"RECRUIT", "BOUNDED_EXPERIMENT"}
            kind = stage.get("authorization_kind")
            if not isinstance(kind, str) or kind not in allowed:
                fail(f"{label}: conditional authorization_kind permits limited work only")
            if not conditions:
                fail(f"{label}: conditional work needs conditions")
            for item in conditions:
                if not isinstance(item, dict) or not all(text(item.get(k)) for k in ("item", "owner", "allowed_action")):
                    fail(f"{label}: each condition needs item, owner and allowed_action")
                else:
                    day(item.get("due"), f"{label} condition due", future=True)

    submission = state.get("submission")
    if not isinstance(submission, dict) or not isinstance(submission.get("state"), str) or submission["state"] not in {"NOT READY", "READY FOR SUBMISSION", "SUBMITTED WITH RECEIPT"}:
        fail("submission: invalid state")
    elif submission["state"] != "NOT READY":
        final = by_id["12"]
        if final.get("status") != "GO" or type(submission.get("ready_stage_revision")) is not int or submission["ready_stage_revision"] != final.get("revision"):
            fail("submission: readiness needs current Stage 12 GO revision")
        if submission["state"] == "SUBMITTED WITH RECEIPT":
            roles = evidence(submission.get("receipt"), "submission receipt")
            if "receipt" not in roles:
                fail("submission: receipt role required after submission")
            timestamp = submission.get("submitted_at")
            try:
                parsed = datetime.fromisoformat(timestamp) if isinstance(timestamp, str) else None
            except ValueError:
                parsed = None
            if parsed is None or parsed.utcoffset() is None or parsed.astimezone(ZoneInfo("Asia/Tokyo")).date() > as_of:
                fail("submission: actual timezone-aware submitted_at required; no future date")
    if require_stage is not None and (require_stage not in by_id or by_id[require_stage].get("status") != "GO"):
        fail(f"required Stage {require_stage} must be GO")
    return sorted(set(errors))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--root", type=Path, help="project root; defaults to manifest parent")
    parser.add_argument("--as-of", type=date.fromisoformat, default=datetime.now(ZoneInfo("Asia/Tokyo")).date())
    parser.add_argument("--require-stage", choices=IDS, help="reject an unevaluated target Stage")
    args = parser.parse_args()
    try:
        state = json.loads(args.manifest.read_text(encoding="utf-8"))
        errors = validate(state, args.root or args.manifest.parent, args.as_of, args.require_stage)
    except (OSError, ValueError) as exc:
        print(f"FAIL: cannot read/validate manifest: {exc}")
        return 1
    for error in errors:
        print("FAIL:", error)
    if errors:
        return 1
    count = sum(s["status"] == "GO" for s in state["stages"])
    print(f"PASS: evidence consistency at {args.as_of}; {count} GO stages (unstarted records are not GO)")
    print("NOTE: Does not certify claim truth, user identity, human approval, eligibility or receipt authenticity.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
