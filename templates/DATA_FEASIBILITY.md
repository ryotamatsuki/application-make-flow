# Data Feasibility, License and Semantic Audit

**Candidate ID / core task / validation profile:**
**Snapshot date:**  
**Dataset owners, official source URLs and dates:**

## Data sources — measured, not conjectured

| Source ID | Registry/API + exact dataset/feed ID | Required or optional | License/API terms URL + checked at | Actual HTTP/result | Target area/date coverage | Can publicly redistribute derivatives? | Decision |
|---|---|---|---|---|---|---|---|
| D-001 | — | REQUIRED | — | NOT TESTED | UNKNOWN | UNVERIFIED | NO-GO UNTIL VERIFIED |

Status vocabulary: `ACQUIRED` / `PARTIAL` / `UNAVAILABLE` (e.g. 403) / `NOT FOUND` (verified scope) / `UNKNOWN`。取得不能≠対象地域に存在しない。`PASS` に憶測値を使用しない。

## Field and join coverage

| Core calculation input | File and column / API field | Example verified value & type | Null/missing rate and denominator | Join key/mapping | Availability across required cases | Missing-handling |
|---|---|---|---|---|---|---|
| Date-specific departure | stop_times.departure_time + calendar/calendar_dates | NOT TESTED | NOT TESTED | stop_id, trip_id, service_id | NOT TESTED | UNKNOWN |

## GTFS correctness checklist

- [ ] Actual feed downloaded or fetched under permitted access conditions; content hash, timestamp and size recorded
- [ ] ZIP safety and required files/foreign keys validated (stops, routes, trips, stop_times, calendar service semantics)
- [ ] Service date, holidays and exceptions handled; time values >24h supported when present
- [ ] Feed validity period checked, not inferred from fetch date
- [ ] pickup_type/drop_off_type boarding restrictions and advance-contact requirements checked when applicable
- [ ] frequencies.txt and exact_times handled when applicable; headway-based service not silently expanded into guaranteed departure times
- [ ] Approximate timepoint values reflected in claim precision when applicable
- [ ] Transfers, parent stations, walking access, maximum walk distance explicitly supported or marked as assumptions
- [ ] GTFS-RT applied only with freshness, identity mapping, missing-alert fallback and API permission confirmed
- [ ] GTFS-Flex (if used) reservation, service eligibility and geographical/time conditions validated; no fabricated fixed departure
- [ ] Duplicate stop/operator IDs across feeds properly namespaced
- [ ] Public display of reconstructed raw timetables/converted transit JSON independently license-reviewed
- [ ] Attribution and user-visible data scope/refresh status decided

## Coverage and update contract

| Required region/day/time/user condition | Representative case | Actual usable input | Missing or excluded condition | Evidence |
|---|---|---|---|---|
| NOT DEFINED | — | NOT TESTED | UNKNOWN | — |

- Input version/hash, checked-at and valid-until per source:
- Update owner and frequency; freshness threshold:
- Failed update / expired input display and recovery:
- Public availability period and source termination plan:
- Non-applicable semantic checks and reason (not an unexplained checkbox):

## Minimum real case (Stage 05 contract)

- Inputs (origin, destination, date, constraints): 
- DECISION_SUPPORT: expected positive, negative and UNKNOWN scenarios with source justification:
- ANALYSIS: independently checkable aggregation, condition change and missing-data scenario:
- VISUALIZATION: source-to-display comparison, reading task/misreading condition and missing-data scenario:
- Selected cases, non-applicable profiles and fallback UI:
- Necessary third-party fields and any assumed duration:
- Script/commit/manifest SHA for reproduction:
- Reliability boundaries, no inference outside them:

## Decision

- Mandatory source passes licensing and functional ability?:
- If not, exact fatal gap and alternative/rollback:
- Human reviewer/date and `GO / CONDITIONAL GO / NO-GO`:
