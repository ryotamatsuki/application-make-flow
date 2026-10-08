# Independent Computation / Adversarial Certificate

**Product/Candidate + SHA:**  
**Core user-facing claim:**  
**Inputs, dataset versions and test date:**  
**Builder and independent verifier:**  
**Shared code, libraries or prior results visible to verifier:**  
**Independent construction route and why it is independent:**  

## Claim scope

- Exactly what the application claims to calculate:
- Geography, date/time, modes and user attributes in scope:
- Assumptions, fallbacks, uncertainties, and user-displayed wording:
- Conditions where outcome must be `UNKNOWN`:
- Failure consequences and severity (especially missed last departure, inaccessible path):

## Reference cases

| Case ID | Minimal input and expected result from primary source/independent reasoning | Production result | Independent evaluator result | Discrepancy? | Evidence |
|---|---|---|---|---|---|
| POS-01 | NOT YET SPECIFIED | NOT RUN | NOT RUN | UNRESOLVED | — |
| NEG-01 | NOT YET SPECIFIED | NOT RUN | NOT RUN | UNRESOLVED | — |
| UNK-01 | NOT YET SPECIFIED | NOT RUN | NOT RUN | UNRESOLVED | — |

## Targeted counterexample sweep

- [ ] Weekday vs weekend, holidays, calendar_dates exception overrides
- [ ] Service date + midnight / 24:xx / DST or timezone assumptions where relevant
- [ ] Feed expired, feed absent, missing trip/stop ID, invalid time order
- [ ] Transfer, parent station, interchange distance, minimum transfer time
- [ ] Different walking speed, maximum walk, steep grade/wheelchair-access assumption where relevant
- [ ] Origin outside coverage; nearest stop not necessarily accessible
- [ ] First/last service, delay makes transfer impossible, uncertain arrival
- [ ] RT stale or missing; schedule/RT identity mismatch; misleading accuracy
- [ ] Flex booking cutoff/eligibility/service area where relevant
- [ ] Duplicate stop names, across-agency namespace collisions
- [ ] Not returning a feasible path does **not** imply no real-world transportation exists
- [ ] For all incidents, counterexample fixture added or explicit exclusion/UNKNOWN documented

## Verdict and decision

- Reference implementation code and SHA:
- Failing cases, severity and root causes:
- Regression test path and rerun result:
- Independent PASS only within stated domain?:
- Maker's manual judgment (not equivalent to AI or CI):
- `GO / CONDITIONAL GO / NO-GO`; earliest affected Stage and one diagnosed fix:
