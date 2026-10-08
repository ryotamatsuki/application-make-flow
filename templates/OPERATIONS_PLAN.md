# Public-period Operation / Data Update Plan

**Product / release / owner / review date:**

Draft at Stage 00; refine with actual sources at Stage 02, freeze at Stage 08, rehearse at Stage 09 and audit at Stage 11/12.

## Public service and cost

- Official required public period, source URL and checked date:
- Intended availability through at least the required end date:
- Hosting/build/API/map/data costs and budget ceiling:
- Expected usage assumptions, quota alerts and action before the ceiling:
- Public support/contact owner and backup/recovery owner:
- Check frequency and evidence location; manual versus automated checks:

## Per-source update contract

| Input ID | Current version and validity | Update method/frequency | Freshness/expiry threshold | Owner | Failure display | Legal fallback/termination plan |
|---|---|---|---|---|---|---|
| NOT CONFIGURED | UNVERIFIED | — | TO DEFINE | — | UNKNOWN | UNVERIFIED |

- Validate new snapshot before replacement; retain the last valid one only if terms and dates allow:
- Distinguish acquisition time, service validity, last successful update and stale RT:
- No valid source: UNKNOWN or clearly scoped outage; never fabricate available service:
- Provider/API closure, terms change or budget limit: compliant contingency and affected claims:

## Rehearsal and recovery

| Incident | Predefined expected behavior | Actual result | Recovery/rollback steps | Evidence |
|---|---|---|---|---|
| Fetch/update failure | TO DEFINE | NOT RUN | — | — |
| Feed expired / RT stale | TO DEFINE | NOT RUN | — | — |
| Invalid new snapshot | TO DEFINE | NOT RUN | — | — |
| Hosting/API quota or outage | TO DEFINE | NOT RUN | — | — |

- Relevant incident selection and non-applicable reasons:
- Recovery target and restored version/SHA; verify live task after recovery:
- After submission: maintenance/bugfix scope, change log and official FAQ check:
- Handoff recipient, review date and next check:

Fallbacks must preserve license and core correctness. A warning cannot make an invalid travel guarantee acceptable. Record successful recovery evidence instead of marking an unperformed rehearsal as PASS.
