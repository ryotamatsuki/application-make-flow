# Changelog

## v2.0.0 — 2026-10-08 — Comparative value and iterative delivery

- Added validation profiles for decision support, analysis and visualization; removed format-only visualization rejection.
- Required early user screening before selection, bounded tests of the biggest unresolved assumption, matched baseline tasks and OD contribution evidence.
- Allowed bounded discovery loops and task-level build/UX iterations with explicit rollback and stale evidence rules.
- Added conditional GTFS boarding, headway and approximate-time checks, coverage and update contracts, and operations rehearsals.
- Split pre-submission READY checks from post-submission receipt checks.
- Added reusable planning, comparison, iteration, operations and project-state templates; added an evidence consistency checker with regression tests.
- MAJOR under the existing governance rule because gate meanings and permitted routing change. Stage numbering remains 00–12; existing projects reassess affected evidence only. No candidate, app or entry was created by this release.

## v1.0.0 — 2026-10-08 — Initial greenfield competition workflow

- Introduced strict official contest eligibility ledger and source hierarchy.
- Established Stage 00–12 (competition intake → problem discovery → data feasibility → prior-art kill → candidate selection → minimal empirical prototype → independent red-team → real user value/portability/re-kill → product freeze → vertical build → UX → independent release audit → submission freeze).
- Added explicit routing, independent validation provenance, no-false-certainty and high-impact safety controls.
- Added reusable evidence templates and zero-to-one kickoff guidance.
- Added workflow integrity checks. This release defines the **workflow only**; no app selected, built, deployed or submitted.

### Relation to source

Inspired by [research-paper-workflow v2.8](https://github.com/ryotamatsuki/research-paper-workflow), but an independently versioned product workflow with contest-specific legal/data/release gates.
