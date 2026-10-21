# Swap Rehearsal Runbook (App F, Ch 12)

Replace one model or tool end to end, against the evaluation set, **inside one sprint**. Failure demotes a deployment mode; it **never blocks the business**. Future-proof is a rehearsal, not a feature. Most organizations have not yet made it a standing drill — say so rather than assume it exists.

## Roles

| Role | Who | Does |
|:-----|:-------|:--------------|
| **Rehearsal owner** | Data & AI lead | Calls the rehearsal, keeps the clock, signs the log |
| **Process owner** | Named on the Frame Card | Confirms the frame; reviews failed cases; approves or refuses promotion |
| **Evaluator** | Staff who wrote the policy and golden set | Runs the four tests; second rater on disputed cases; records κ |
| **Integrator** | Engineer on the gateway | Pins the candidate; swaps adapters; restores the incumbent if asked |
| **Observer** | Legal, ethics or audit focal point | Checks gates G1–G6 still hold; witnesses the log |

## Triggers

- Calendar: first sprint of Q2 and Q4 (twice a year), dates ______ · ______
- Supplier notice of retirement, change or re-pricing: candidate qualified before the notice expires (plan for 60 days)
- Breaking protocol revision: before the deprecation window closes
- Trust Dashboard warning on alignment, repeat-agreement or golden-set pass rate: next sprint

**Timing, one sprint:** day 1 pin the candidate · days 2–5 tests 1–4 · days 6–8 review, decision, log entry · days 9–10 swap or demote.

## The four tests

| # | Test | Material | Pass |
|:-:|:-------|:-----------|:-----------|
| 1 | **Outcome equivalence on decision tables** | Scenario suite per decision point (20–50 scenarios) | Same outcomes as the table: 100 % for R4, agreed tolerance for R3; structural similarity does not count |
| 2 | **Alignment to policy** | The written decision policy (cues, weights, exceptions) and its cases | Alignment score within the acceptance band; not below the incumbent |
| 3 | **Implicit-constraint probes** | Cases where a MUST NOT rule is not restated in the prompt | Zero violations; the gateway blocks and logs any attempt |
| 4 | **Protocol migration** | Descriptors regenerated from the tool contract for the pinned protocol version; one call per tool | Every tool callable; side-effect classes and required authority unchanged |

## Pass, fail and demotion

| Result | Rule |
|:-------|:---------------|
| All four pass | Candidate replaces the incumbent at the same level; process owner signs |
| Test 1 or 2 fails | **Demote the task one level** (R4 → R3, R3 → R2); continue under the new mode; re-score before promotion |
| Test 3 fails | Nothing above R1 until the gateway rule that should have blocked it is fixed and re-tested |
| Test 4 fails | Keep the incumbent protocol version pinned; open a migration task |
| A gate G1–G6 no longer holds | Back to R1 until the gate is restored |

## Log entry (appended to the decision log)

| Field | Entry |
|:--------------|:--------|
| Rehearsal id · date · trigger · process · tasks · Frame Card version | |
| Incumbent · candidate · protocol version | |
| Tests 1–4: result each · rater κ on disputed cases | |
| Decision: swap / demote / hold · new level per task · days from notice to decision · signatures · hash of previous entry | |
