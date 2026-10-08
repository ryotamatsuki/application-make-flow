# Project Evidence Consistency Check

The workflow repository has no app evidence. Its blank state template is NOT EVALUATED. The checker validates records and local files; it cannot determine whether a user exists, a comparison is fair, a signoff actually occurred or a receipt is authentic.

## Setup in the product project

1. Copy [PROJECT_STATE.json](../templates/PROJECT_STATE.json) to `docs/PROJECT_STATE.json` and [check_project.py](../scripts/check_project.py) to `scripts/check_project.py`.
2. Set project, workflow_version (`2.0.0`) and the actual workflow commit SHA. Choose validation profiles after Stage 00.
3. Put actual reports, source snapshots/logs and observation evidence in the project, with private evidence kept private. Add local relative paths, SHA-256 and roles to the state. Paths are relative to the project root, not the manifest directory.
4. Register fixed input IDs and their actual versions, checked_at, valid_until and hashed evidence. A `null` input expiry requires a verified `no_expiry_reason`; unknown validity must not be represented as indefinite. Data with service/RT expiry uses an explicit date, while sub-day freshness still requires product tests and an operations contract.
5. For each evaluated Stage, record revision >=1, input_versions, upstream depends_on revisions, evidence, checked_at, valid_until, recorded HUMAN reviewer, bounded authorization and unresolved conditions. Stage 00 has no predecessor; every other Stage depends at least on its predecessor.

Dates are ISO calendar dates, inclusive valid_until. Default review date is today in Asia/Tokyo. Choose Stage validity from its actual evidence and review needs; there is no universal freshness duration. Checked dates may not be in the future. Machine records complement the Stage report rather than replacing its reasoning.

## Commands

```bash
python scripts/check_project.py docs/PROJECT_STATE.json --root .
python scripts/check_project.py docs/PROJECT_STATE.json --root . --require-stage 11
python scripts/check_project.py docs/PROJECT_STATE.json --root . --require-stage 12
```

The first checks consistency and may pass with zero GO stages. `--require-stage` additionally requires that Stage's GO and, via dependencies, valid predecessor records. A blank template therefore cannot pass a release/submission requirement. Historical reproduction may use `--as-of YYYY-MM-DD`; current-release CI must use the current date, not a fixed historical override.

For a real evidence file, compute its digest:

```bash
python -c 'import hashlib,pathlib,sys; print(hashlib.sha256(pathlib.Path(sys.argv[1]).read_bytes()).hexdigest())' docs/stages/STAGE_00.md
```

Each evidence object is `{ "path": "relative/local/file", "sha256": "actual digest", "role": "stage_report" }`. External URLs and claim provenance belong in the referenced report; a bare URL is not a locally reproducible evidence snapshot. Keep restricted raw data and personal observations private, and use lawful logs/manifests or redacted summaries where sufficient. Receipt checks need a privately available receipt file or a legitimate redacted receipt, not invented public evidence. If a private file is unavailable to public CI, do the submission check in the authorized private environment; do not weaken it.

## Evidence roles required for GO

Every evaluated Stage requires `stage_report`. GO requires these additional roles:

| Stage | Additional role(s) |
|---|---|
| 04 | early_user_screen |
| 05 | core_cases |
| 06 | independent_validation |
| 07 | early_user_screen, baseline_comparison, od_contribution |
| 08 | product_spec |
| 09 | operations_rehearsal |
| 10 | ux_evaluation |
| 11 | release_audit, operations_plan |
| 12 | readiness_check |

One report may support multiple roles with explicit references; hashing the same report does not create independent evidence. Non-applicable details and limits are explained inside the report. The checker verifies declared roles, not their substantive completeness.

## Dependencies, stale records and conditions

- `input_versions` maps each used input ID to the version reviewed. A changed catalog version or hashed source file invalidates the old evaluated record.
- `depends_on` maps earlier Stage IDs to reviewed revisions. Change a verdict/evidence/acceptance contract: increment that Stage's revision and mark dependent GO records STALE. Transitive dependents cannot remain GO through a STALE predecessor.
- Recheck affected evidence before refreshing dependencies or hashes. Do not update identifiers merely to silence errors.
- An evaluated Stage needs a future/current valid_until and no unresolved blockers. GO has no open conditions.
- CONDITIONAL GO requires conditions with item, owner, due and allowed_action. `authorization_kind` must be RECRUIT, BOUNDED_EXPERIMENT, LOCAL_FIX or READ_ONLY_REVIEW. At Stage 04/07 only RECRUIT or BOUNDED_EXPERIMENT is allowed. Text descriptions define the exact bounded work; the script does not enforce external tool actions.
- A conditional predecessor permits experimental IN PROGRESS work, but cannot support a downstream final GO. Close and re-evaluate the predecessor first.

## Readiness and submission

`submission.state = READY FOR SUBMISSION` needs current Stage 12 GO and a matching ready_stage_revision. It does **not** require a receipt or submitted_at.

`SUBMITTED WITH RECEIPT` additionally needs hashed evidence with the receipt role and the actual timezone-aware submitted_at. Store its exact timestamp; the checker only rejects malformed timestamps/future dates and cannot observe the portal.

Use the checker in product CI on state/evidence changes and at release audits. If the project schedules freshness checks, choose a frequency consistent with actual sources and budget. This repository's CI checks the blank template and regression behavior only; it does not certify an app.
