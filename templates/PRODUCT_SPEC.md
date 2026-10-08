# Product Specification / Core Freeze

**Project title / URL / author:**  
**Candidate ID / selection evidence / workflow SHA:**  
**Core Freeze commit/date/signoff:**  

## One-sentence user value

- Specific target person and their decision:
- Why existing tools are not sufficient (strongest counterexample / tested service):
- Source of actual observed demand:
- Public transport OD data that fundamentally enables this feature:

## Core decision contract

- Input: (date, time zone, geography, constraints, defaults and units)
- Data inputs and exact versions/terms:
- Processing rule and assumptions:
- `SUCCESS`: formal condition and UI copy
- `FAILURE`: formal condition and UI copy (not equivalent to all transportation being impossible)
- `UNKNOWN`: conditions including missing/stale/out-of-coverage data and UI copy
- Never claim: (e.g., official guarantee, all services covered, precise live availability)
- Explainability: show which departure/service/condition produced the output
- Source display: update date, provider, feed, data and model limitations
- Critical counterexamples that must remain regressions:

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
| Core scenario correctness | TO DEFINE | |
| False-positive high-impact safety cases | TO DEFINE | |
| Mobile E2E | TO DEFINE | |
| Keyboard/focus/contrast | TO DEFINE | |
| Error + offline + missing feeds | TO DEFINE | |
| Performance at realistic data size | TO DEFINE | |
| Data licensing and public outputs | REQUIRE VERIFIED | |

No universal magic performance or accuracy thresholds; choose based on user harm, device and dataset.

## MVP / exclusions

- Must have for one meaningful decision:
- Should have only if they unblock existing user task:
- Deliberately out of scope:
- Not proven (data / user validation / generalization):
- Operational and data-freshness responsibilities:
- Consent and privacy design; persistence default:

## Freeze & changes

- Original frozen SHA:
- Approved change, reason and affected Stage:
- Independent test to rerun, result and new SHA:
