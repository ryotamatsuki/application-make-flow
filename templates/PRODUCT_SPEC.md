# Product Specification / Core Freeze

**Project title / URL / author:**  
**Candidate ID / selection evidence / workflow SHA:**  
**Validation profile(s): DECISION_SUPPORT / ANALYSIS / VISUALIZATION**
**Core Freeze commit/date/signoff:**  

## One-sentence user value

- Specific target person and their task/decision/understanding/experience:
- Why existing tools are not sufficient (strongest counterexample / tested service):
- Source of actual observed demand:
- Public transport OD data that fundamentally enables this feature:

## Core output contract

- Input: (date, time zone, geography, constraints, defaults and units)
- Data inputs and exact versions/terms:
- Processing rule and assumptions:
- Output and source-alignment rules for the selected profile:
- `SUCCESS` (if a feasibility decision is made): formal condition and UI copy
- `FAILURE` (if a feasibility decision is made): formal condition and UI copy (not equivalent to all transportation being impossible)
- `UNKNOWN` / missing-data display: conditions including missing/stale/out-of-coverage data and UI copy
- Never claim: (e.g., official guarantee, all services covered, precise live availability)
- Explainability: show which departure/service/condition produced the output
- Source display: update date, provider, feed, data and model limitations
- Critical counterexamples that must remain regressions:

## Comparative acceptance

- Early user-screen evidence and resolved gaps:
- Strongest existing/manual baseline and matched user task:
- Predeclared value criterion, metric and correctness rubric:
- Observed improvement, failures, participants, order effects and limits:
- Essential OD and optional-data contribution evidence:
- Non-applicable output states with reason; do not invent routing features:

## Minimum user journey

- User entry:
- Key action:
- Primary result:
- Recommended next step:
- Recovery guidance / contact link / reporting mistakes:
- Alternative to map-only interaction:

## Acceptance & nonfunctional requirements

| Requirement | Testable threshold chosen before testing | Evidence and owner |
|---|---|---|
| Profile-specific core correctness | TO DEFINE | |
| Matched baseline task improvement | TO DEFINE | |
| Misunderstanding / high-impact false-positive cases | TO DEFINE | |
| Mobile E2E | TO DEFINE | |
| Keyboard/focus/contrast | TO DEFINE | |
| Update failure + expiry + recovery | TO DEFINE | |
| Error + offline + missing feeds | TO DEFINE | |
| Performance at realistic data size | TO DEFINE | |
| Data licensing and public outputs | REQUIRE VERIFIED | |

No universal magic performance or accuracy thresholds; choose based on user harm, device and dataset.

## MVP / exclusions

- Must have for one meaningful user task:
- Should have only if they unblock existing user task:
- Deliberately out of scope:
- Not proven (data / user validation / generalization):
- Operational and data-freshness responsibilities, linked OPERATIONS_PLAN:
- Task-level implementation/UX iteration and revalidation routing:
- PROJECT_STATE location and evidence-check command:
- Consent and privacy design; persistence default:

## Freeze & changes

- Original frozen SHA:
- Approved change, reason and affected Stage:
- Independent test to rerun, result and new SHA:
