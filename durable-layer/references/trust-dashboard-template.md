# Trust Dashboard (App C, Ch 8)

One row per deployed task, reviewed **monthly** by the process owner and **six-monthly** at recalibration. Bands are initial alert thresholds from practitioner and pilot evidence, not peer-reviewed; **re-baseline from your own data after two quarters.**

| # | Measure | Definition | Healthy | Warning |
|:-:|:--------|:-------------|:---------|:-------------|
| 1 | **Override rate** | Decisions a human materially changed ÷ decisions that reached a human (rewording does not count) | Below 15 % | Above 15 %: recalibrate. **Near zero: rubber-stamping**, automated in all but name |
| 2 | **Escalation rate** · **unnecessary-escalation rate** | Decisions handed to a human ÷ all decisions; of those, share the agent could have resolved | Stable, set per task | Escalation rising while override falls; unnecessary escalations above 20–40 % |
| 3 | **Repeat-agreement rate** | Identical inputs giving the same decision across repeated runs, logged with model and prompt version | Above 95 % at R3–R4 | Below 90 %: no single call may act as a gate |
| 4 | **Process-alignment score** | Similarity between the model's cue weights and the written decision policy | Within the band set at acceptance | Drift beyond the band; a new model scoring below the one it replaces |
| 5 | **Auto-completion by level** | Tasks completed without human intervention, per readiness level | ≈ 95 % R4 · 70 % R3 · 40 % R2 | Well below the curve: task scored too high. Above it at R2–R3: check for rubber-stamping |
| 6 | **Golden-set pass rate, second model family** | Golden cases passed by a model other than the one in production | Equal to production within tolerance | Only one family passes: the process is tied to a vendor |
| 7 | **Model-requalification time** | Days from retirement notice or swap decision to a qualified replacement | Under 60 days; one sprint | Above 60 days: a notice becomes an outage |
| 8 | **Incidents and complaints** | Logged harms, drift alerts, complaints, suspensions; gates passed; overseer training complete | Every incident closed with a logged correction | Any incident without a corrective entry; overseers untrained |

**Precondition.** Two independent raters reach Cohen's κ ≥ 0.70 (agreement beyond chance) on the tasks behind the dashboard; below that, the levels and rows 5–7 are not yet meaningful.

## Six-monthly recalibration (Ch 8)

Policy owner, overseer and manager read the dashboard together and answer four questions:
1. Has the policy changed (mandate, vocabulary, exceptions)?
2. Have the bands moved, now that baselines exist?
3. Have the readiness levels held, or should a task move a rung?
4. Is the model's alignment score still what it was at acceptance?

Out-of-cycle triggers: a model swap; drift beyond a set threshold; a change in the regulation the process answers to.

## Filled-dashboard output shape

| Task | Level | Override | Escalation / unnecessary | Repeat-agreement | Alignment | Auto-completion | 2nd-family pass | Requalification | Incidents | Status |
|---|---|---|---|---|---|---|---|---|---|---|

Status per row: healthy / warning (name the row) / not yet meaningful (κ < 0.70 or no baseline). Missing data is reported as missing, never estimated.
