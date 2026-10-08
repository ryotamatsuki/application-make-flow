#!/usr/bin/env python3
"""Check structural integrity of the contest-specific documentation (not product QA)."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md",
    "GOVERNANCE.md",
    "COMPETITION_RULES.md",
    "WORKFLOW.md",
    "AGENTS.md",
    "docs/START_NEW_PROJECT.md",
    "docs/DECISION_LOG.md",
    "docs/CHANGELOG.md",
    "docs/RESEARCH_TO_PRODUCT_MAPPING.md",
    "templates/STAGE_REPORT.md",
    "templates/CANDIDATE_REGISTER.md",
    "templates/DATA_FEASIBILITY.md",
    "templates/PRIOR_ART_AUDIT.md",
    "templates/INDEPENDENT_VALIDATION.md",
    "templates/PRODUCT_SPEC.md",
    "templates/SUBMISSION_QA.md",
    "templates/VALIDATION_PLAN.md",
    "templates/USER_COMPARISON.md",
    "templates/ITERATION_LOG.md",
    "templates/OPERATIONS_PLAN.md",
    "templates/PROJECT_STATE.json",
    "docs/PROJECT_EVIDENCE_CHECK.md",
    "scripts/check_project.py",
    "tests/test_project_evidence.py",
]
LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)\s]+)(?:\s+[^)]*)?\)")
STAGE = re.compile(r"(?m)^## Stage (\d{2}) — ")


def check() -> list[str]:
    errors: list[str] = []

    for rel in REQUIRED:
        if not (ROOT / rel).is_file():
            errors.append(f"missing required file: {rel}")

    for source in ROOT.rglob("*.md"):
        if ".git" in source.parts:
            continue
        body = source.read_text(encoding="utf-8")
        for match in LINK.finditer(body):
            link = match.group(1).strip().strip("<>")
            if link.startswith(("http:", "https:", "mailto:", "#")):
                continue
            parsed = urlsplit(link)
            if parsed.scheme:
                continue
            target_path = unquote(parsed.path)
            if not target_path:
                continue
            target = (source.parent / target_path).resolve()
            if not target.is_relative_to(ROOT) or not target.exists():
                errors.append(f"broken relative link: {source.relative_to(ROOT)} -> {link}")

    workflow_path = ROOT / "WORKFLOW.md"
    if workflow_path.exists():
        body = workflow_path.read_text(encoding="utf-8")
        actual_stages = [int(n) for n in STAGE.findall(body)]
        expected_stages = list(range(13))
        if actual_stages != expected_stages:
            errors.append(f"stage heading sequence must be 00..12: got {actual_stages}")
        for verdict in ("GO", "CONDITIONAL GO", "NO-GO"):
            if verdict not in body:
                errors.append(f"verdict not found in WORKFLOW.md: {verdict}")

    for path in ("README.md", "COMPETITION_RULES.md"):
        file = ROOT / path
        if file.exists() and "2027-01-11" not in file.read_text(encoding="utf-8"):
            errors.append(f"official deadline absent in {path}")

    for path, marker in (
        ("README.md", "**Version:** 2.0.0"),
        ("WORKFLOW.md", "**v2.0.0 /"),
        ("GOVERNANCE.md", "Workflow v2.0.0"),
        ("docs/START_NEW_PROJECT.md", "v2.0.0"),
        ("docs/CHANGELOG.md", "## v2.0.0"),
    ):
        file = ROOT / path
        if file.exists() and marker not in file.read_text(encoding="utf-8"):
            errors.append(f"current workflow version missing in {path}")

    state_path = ROOT / "templates/PROJECT_STATE.json"
    if state_path.exists():
        try:
            state = json.loads(state_path.read_text(encoding="utf-8"))
            if state.get("workflow_version") != "2.0.0" or any(s["status"] != "NOT EVALUATED" for s in state["stages"]):
                errors.append("state template must be v2.0.0 and wholly NOT EVALUATED")
            if state.get("inputs") or state.get("submission", {}).get("state") != "NOT READY":
                errors.append("state template must not contain actual input/entry claims")
        except (ValueError, KeyError, TypeError, AttributeError):
            errors.append("invalid PROJECT_STATE template")

    return errors


if __name__ == "__main__":
    problems = check()
    if problems:
        for p in problems:
            print("FAIL:", p)
        sys.exit(1)
    print("PASS: required files, links, Stage 00-12, deadline, v2.0.0 markers and unevaluated template")
    print("NOTE: This does not verify data validity, API licensing, product correctness, or submission.")
