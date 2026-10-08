# Workflow Design Decisions

## W001 — 2026-10-08 — Dedicated, greenfield, competition-specific workflow

**Decision**: `application-make-flow` is designed only for Public Transit Open Data Challenge 2026. It starts before idea selection and does not assume an existing product or code. Competing transit concepts are candidates, not preset winners.

**Reason**: Reusing production-specific roadmaps from mobility projects would bias selection and skip proof of user value. Competition constraints and entry evidence must be first-class.

## W002 — 2026-10-08 — Adapt research workflow v2.8 but do not duplicate it

**Source**: [research-paper-workflow](https://github.com/ryotamatsuki/research-paper-workflow), including Governance, bounded search (2026-10-07), independent red-team, novelty re-kill, counterexample regression and freeze.

**Decision**: Translate research idea discovery→novelty→minimal model→independent mathematical attack→verification/robustness→submission to app problem discovery→prior art→minimum real-data prototype→independent computational validation→UX→competition release. Do **not** import mathematical theorem/falsification requirements or journal targeting.

## W003 — 2026-10-08 — Hard gates and non-prescriptive product choices

**Decision**: official entry, licensed data, publicly accessible free usage and critical calculation validity block `GO`. Novelty/user value remain evidence-driven but are not judged by synthetic numerical official scores. No mandated stack, data count or visuals.

## W004 — 2026-10-08 — Isolate workflow, prototypes and product

**Decision**: This repository stores the reusable workflow, not code for a selected app. Exploratory artifacts precede Stage 08; product repository becomes formal only after core specification. Existing apps may be referenced as prior art, but are not automatically accepted.

## W005 — 2026-10-08 — Automated internal-consistency check

**Decision**: Standard-library Python check of relative Markdown links and required Stage definitions will run as lightweight CI. It is a documentation integrity test, not a certificate of competition eligibility, real-data correctness or product safety.
