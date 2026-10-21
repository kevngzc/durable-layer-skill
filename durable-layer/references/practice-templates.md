# Practice templates (from the chapters)

Smaller instruments the chapters define. Each is filled *with* the person who owns it; leave blanks blank.

## Decision page — the wiki (Ch 3)

One page per decision, one screen long, four headings in this order:

```markdown
# <decision, as a short title>
**Decision** — what was decided, one or two sentences. Date: ____ · Owner: ____
**Context** — the constraint, incident or request that made it necessary (one paragraph).
**Open questions** — what it did not settle.
**Sources** — documents, datasets, texts, earlier pages, each with an identifier or link.
```

- A page that cannot name its sources is an opinion and should say so. Longer than a screen = two decisions; split.
- **Compile step:** raw material (notes, transcripts, priorities) → a model drafts → a person approves and is accountable. Compile the week the decision is taken.
- **Rule of entry:** nothing enters a prompt that is not first in the wiki.
- **In:** decisions, architecture choices, incident lessons, Frame Cards, decision policies, glossary, current state of each system. **Out:** personal data, drafts with their own home, what a governing text says better, what is true in general.
- **Compile log:** raw input · page · drafting model · approver · date.
- **Test:** with only the wiki, answer *why did we choose this?* for three decisions from the last year.

## Value → guardrail, four translations (Ch 4)

One page per value; ethics, legal and the process owner write lines 1–3, engineers line 4. Source text at the top; version the page.

| Line | Content |
|---|---|
| Source text | the value as the governing text states it, with its reference |
| 1 Policy sentence | what it means *here*: the thing protected and who is responsible |
| 2 Rule | actor-neutral MUST / MAY / MUST NOT (write MUST NOT first); goes on the Frame Card |
| 3 Test | what is checked · on which data · at which point · by which component · what happens on failure. Judgement rule → classifier with measured error rate; unsure → a person decides |
| 4 Enforcement point | where every call passes (the gateway). Bypassable by calling the model directly = a suggestion, not a guardrail |

Worked example — human oversight: *Rule:* any actor MUST NOT transmit an output whose destination is a governing body unless an approval record naming a role exists. *Test:* at transmission the gateway checks for the record; absent or unsigned → refused and logged; the scenario suite includes an agent trying to send without approval.

## Expertise capture (Ch 6)

**Definition-of-done interview** — one recurring decision, the expert's words: What does a finished output look like? What would make you send it back? Who uses it next, and what do they do with it? What must never appear in it? If done cannot be observed by someone other than the expert, split the task.

**Decision criteria** — 5–10 per decision (more = two decisions confused):

| Name | Cue (what is looked at) | Rule (what the cue decides) | Exceptions | Lookalike (resembles this, is not) |
|---|---|---|---|---|

Probes past "I just know": *Show me one you got wrong. What would a new hire get wrong here? Which two answers compete most often?*

**Golden set** — a few dozen cases, weighted to hard cases and lookalikes. Header: set name · author (the expert) · version · ownership sentence: *"this set belongs to the role, is authored by its holder, and is exportable in full at any time."*

| Case id | Input | Correct output | Criterion exercised | Why (one line) | Cues that decided it |
|---|---|---|---|---|---|

Three jobs: training resource · test suite (any tool runs it before the demo; result is a pass/fail list with the violated criterion) · career artefact. Expert first, tool second. Reviewed six-monthly.

## Five-line decision policy (Ch 8)

| Line | Entry |
|---|---|
| Decision | |
| Cues a competent person looks at | |
| Weights — which cue wins when two disagree | |
| Exceptions | |
| Who may deviate, and how that is recorded | |

Signed by the decision-maker, versioned in the wiki. Written with legal and ethics in the room (a well-aligned model copies a wrong weight faithfully). **Alignment test:** score candidates on outcome *and* on process (did its reasons weight the cues as the policy does); the process score is the gate.

## Decision model — the contract (Ch 9)

For a deterministic decision point; judgement decisions stay human.
1. **Requirements diagram:** decision as a question; each input as data; arrows; no "who evaluates".
2. **Signatures first:** input and output names, types, allowed values — before any rule.
3. **Decision table** with hit policy (top-left): *Unique* (one rule fires; admissibility) · *First* / *Priority* (ordered) · *Collect* (several outputs; tagging). Two rules firing with no winner = decision not yet understood.

| U | input 1 | input 2 | input 3 | **output** |
|---|---|---|---|---|
| 1 | | | | |

4. **Knowledge source:** the governing text's identifier — every output can answer *under which text*.
5. **Scenario suite:** 20–50 real cases with known outputs = acceptance test for every table version and every tool. Pass → signed; fail → back, whoever drafted it.
- A model may draft the table (outcomes must still be tested) and a table may steer a model. Keep tables in the open standard format (DMN); ask vendors their conformance figure.
- Tabling does not change the oversight mode.

## Task-to-model map (Ch 10)

| Task (task level) | Level · oversight mode | Volume / month (incl. re-runs) | Evaluation set · scoring rule | Candidates: score · cost / 1k req · latency (≥ 2 families, ≥ 1 open-weight you can host) | Decision · route · review date |
|---|---|---|---|---|---|

Patterns: small open-weight models for high-volume, high-readiness work; frontier models through the gateway where breadth earns it; the evaluation set arbitrates and is never shared with a vendor in full. **Model choice never raises the readiness level.**

## Tool contract (Ch 11)

| Field | Entry |
|---|---|
| Name | |
| Inputs (typed) | |
| Outputs (typed) | |
| Side-effect class | read-only · reversible write · irreversible write · external reach |
| Required authority | which role, under which Frame Card |

Protocol- and vendor-neutral; lives in the wiki beside its Frame Card. Protocol descriptors (MCP tool listing, A2A agent card, function schema) are **generated** from it, versions pinned. The rest of the gateway: policy-as-code with two identities per call (delegation only narrows authority; model refusal logged separately from policy refusal); guardrail model as proxy; hash-chained decision log; kill switch held by a named duty manager, tested monthly. *Thin* adapter = one engineer rewrites it in a week.
