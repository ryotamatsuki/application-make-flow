# Data Feasibility, License and Semantic Audit

**Candidate ID / core decision:**  
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
- [ ] Transfers, parent stations, walking access, maximum walk distance explicitly supported or marked as assumptions
- [ ] GTFS-RT applied only with freshness, identity mapping, missing-alert fallback and API permission confirmed
- [ ] GTFS-Flex (if used) reservation, service eligibility and geographical/time conditions validated; no fabricated fixed departure
- [ ] Duplicate stop/operator IDs across feeds properly namespaced
- [ ] Public display of reconstructed raw timetables/converted transit JSON independently license-reviewed
- [ ] Attribution and user-visible data scope/refresh status decided

## Minimum real case (Stage 05 contract)

- Inputs (origin, destination, date, constraints): 
- Expected positive scenario, justified by source:
- Expected negative scenario, justified by source:
- Expected UNKNOWN scenario and fallback UI:
- Necessary third-party fields and any assumed duration:
- Script/commit/manifest SHA for reproduction:
- Reliability boundaries, no inference outside them:

## Decision

- Mandatory source passes licensing and functional ability?:
- If not, exact fatal gap and alternative/rollback:
- Human reviewer/date and `GO / CONDITIONAL GO / NO-GO`:
