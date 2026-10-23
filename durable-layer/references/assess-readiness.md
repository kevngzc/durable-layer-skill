# Mode: Assess readiness

Goal: for a process or use case, say which tasks can be delegated, to what level, under which oversight mode, and what must be true first. Output is a conversation starter, not a verdict, until the scorecard is calibrated locally.

## 1. Scope (ask, don't assume)

- Which process or use case? Who owns it (by role)? Which governing texts apply?
- Break the activity into **tasks** (verb + object: "check mandatory fields", "assign thesaurus terms", "draft the summary"). An activity hides tasks at different levels; score each.
- Who are the two raters? If the user is alone, score as rater 1 and say a second independent rater is required (Cohen's κ ≥ 0.70) before any level changes a deployment.

## 2. Ground check — ten-question data audit (Ch 1)

For the inputs the tasks depend on (start with the five datasets the most-wanted use case needs):

| # | Question | Answer · evidence |
|---|---|---|
| 1 | **Existence** — a real dataset, or a belief? | |
| 2 | **Access** — can a named person retrieve it today, programmatically, without a favour? | |
| 3 | **Description** — metadata a stranger could read (columns, units, population)? | |
| 4 | **Ownership** — one accountable owner, by role? | |
| 5 | **Licence** — who may reuse it, under which terms? | |
| 6 | **Identifier** — persistent IDs for records and dataset that survive a platform change? | |
| 7 | **Vocabulary** — categories from a controlled vocabulary other datasets also use? | |
| 8 | **Provenance** — where each figure came from, when, by what method? | |
| 9 | **Freshness** — last update, next update? | |
| 10 | **Consumer** — who reads it today? No consumer = unneeded or undiscovered | |

Place each dataset in a band: **C** can you get at it · **B** is it what it claims (deduplicated, gaps known) · **A** is it enough for this task. The audit informs D2.

## 3. Score each task (App B — load `scorecard-template.md`)

- Ask for evidence per dimension; quote it in the table. D3 comes from event logs or volumes, not impressions. D5 asks: who is affected, can it be undone before it takes effect?
- Compute the weighted mean (D1 + D2 + D3 + D4 + 1.5·D5 + D6) ÷ 6.5. With code execution, run `python3 scripts/score.py` (CSV or JSON in, table out); otherwise show the arithmetic.
- Apply in order: band → borderline (± 0.15 of a threshold rounds towards more human) → F1 (D5 ≤ 2 → max R2) → F2 (D1 ≤ 2 → max R3) → gates (an applicable G1/G2, or any of G4–G6, not met → R1). G3 keeps a named sign-off at every level.
- Map level → deployment mode and oversight mode (R4 on the loop, 5 % audit · R3 in the loop, 100 % approval · R2 and R1 in command).
- Model choice never raises the level.

## 4. Output

```markdown
## Readiness — <process> (<date>, rater: <name/role>, κ: not yet measured)

| Task | D1 | D2 | D3 | D4 | D5 | D6 | Mean | Floor | Gates | Level · mode | Evidence / open |
|---|---|---|---|---|---|---|---|---|---|---|---|

**What must be true before any task rises above R1:** <unmet gates, each with an owner>
**Biggest lever:** <the one dimension whose improvement moves most tasks — usually D1 (write the rule: Frame Card, decision table) or D2 (data audit)>
**Next actions:** <3 Monday-morning actions from `principles.md`, matched to the weakest dimensions>

> LARA-derived, organization-calibrated: weights and thresholds are provisional until re-estimated locally (Delphi, ≥ 100 scored tasks, κ ≥ 0.70). Until then the ladder is a conversation, not a verdict.
```

Also offer: draft the Frame Card for the process (line 7 decision points come straight from this assessment), or the five-line policy for the highest-volume task.
