# Candidate Universe / Bounded Idea Search

## Exploration setup

- Discovery period and evidence sources:
- Users and tasks being searched:
- Candidate budget (count or hours) and stop condition (precommit):
- Scope boundaries / what would be off-topic:
- Current evidence maturity:
- Validation profiles (DECISION_SUPPORT / ANALYSIS / VISUALIZATION):
- Early user screen: participants, recruitment method, rough screen/task, evidence:
- Biggest unresolved assumption per candidate, consequence, smallest experiment, cost and stop condition:
- Research owner / actual date / workflow SHA:
- Official contest relevance: [COMPETITION_RULES](../COMPETITION_RULES.md)

## Structural deduplication

候補は名称ではなく、`user → task/constraint → public transport data → processing → decision/understanding/experience` で同定する。単なる地図テーマ・対象エリア・ブランド名の違いなら同一案を検討。

| ID | User and actual task | Problem evidence (official/observed/hypothesis) | Essential OD data and acquisition status | Decision/understanding/experience enabled | Strongest substitute | Difference / falsification test | Disposition & why |
|---|---|---|---|---|---|---|---|
| C-001 | NOT EVALUATED | — | — | — | — | — | UNSCREENED |

Disposition: `ACTIVE` / `MERGED INTO C-...` / `REJECTED` / `DEFERRED` / `SELECTED FOR SPIKE`。件数は成果指標にしない。

## Selection memo (Stage 04)

- Selected candidate ID, target task and validation profile:
- Early user-screen evidence and observed misunderstandings:
- Biggest unresolved assumption and minimal experiment result:
- Matched baseline task, metric and predeclared success criterion:
- Top alternatives and **specific** reasons for nonselection:
- Evidence that the proposed user problem is real:
- Source data that was **actually downloaded and parsed**, with version:
- Closest rival that could eliminate differentiation, comparison date:
- What Stage 05 will demonstrate, what would refute it:
- Time/budget/complexity ceiling, stop rule:
- Principal data/license/technical/safety blockers:
- Independent-verification design (separate logic):
- Profile-specific correctness cases and missing/UNKNOWN case:
- OD contribution comparison plan:
- Recruitment gap and bounded conditional action, if any:
- Human signoff / timestamp / `GO` verdict:
- Conditions under which a rejected candidate can be reopened:

### Anti-selection-bias check
- Was an idea preferred because development was already underway?
- Was the candidate chosen because an attractive API, framework or 3D technique was available?
- Are competitor claims based on actual usage or marketing summaries only?
- Does the proposed feature affect a user decision, understanding or useful experience, with evidence?
- Has mandatory ODPT/GTFS-type data been verified, rather than assumed?

Initial user screening is not proof of finished-product effectiveness. If missing, Stage 04 permits recruitment and bounded experiments only under CONDITIONAL GO; no final Stage 07 GO or Core Freeze without value evidence.
