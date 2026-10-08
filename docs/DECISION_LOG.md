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

## W006 — 2026-10-08 — Profile-specific correctness and comparative value

**Problem**: A format-only visualization kill and universal positive/negative/UNKNOWN expectations bias the workflow toward feasibility calculators. User validation occurs late, and useful differences can remain qualitative.

**Decision**: Add DECISION_SUPPORT, ANALYSIS and VISUALIZATION profiles. Require early user screening before selection and matched baseline tasks plus OD contribution at Stage 07. Allow different correctness references while keeping real data, missing-data honesty and independent verification mandatory.

## W007 — 2026-10-08 — Bounded experiments and task-level iteration

**Decision**: Test the biggest unresolved assumption cheaply before detailed investment; permit bounded Stage 01–03 discovery loops and Stage 09/10 task iterations. Scope changes still follow rollback rules. Early-user gaps permit recruitment and bounded experiments only; unverified Stage 07 value blocks Core Freeze.

## W008 — 2026-10-08 — Separate readiness, receipt and operation

**Problem**: The submission template required completed submission inside pre-submission hard checks.

**Decision**: READY needs completed pre-submission checks; SUBMITTED additionally needs a receipt. Record operation costs, owners, data expiry, update failure and recovery for the required public period. Five-minute demos remain an internal preparation target, not an official hearing duration.

## W009 — 2026-10-08 — Project evidence consistency, not automatic certification

**Decision**: A standard-library checker validates local evidence hashes, input versions, dependency revisions, dates and conditional work limits. It rejects empty GO records and stale supporting evidence; human signoff and claim validity still require review. The workflow repository ships templates and regression tests, not fabricated app evidence.

## W010 — 2026-10-08 — Release as v2.0.0

**Reason**: Existing governance classifies Stage meaning and routing changes as MAJOR. New profiles and permitted early/iterative work change both. Keep Stage 00–12 IDs; migrate active v1 projects by reassessing affected evidence only.
