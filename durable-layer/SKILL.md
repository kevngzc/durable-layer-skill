---
name: durable-layer
description: Apply the method of "The Durable Layer" (Kevin Guezennec) to make an organization AI-ready without rebuilding it for every new model — readiness scoring (R1–R4, oversight modes, floors and gates), Frame Cards, Two-Layer and Dependency Ledgers, trust dashboard, five-line policies, decision tables, tool contracts, procurement rider, Swap Rehearsal, review of AI plans, RFPs, contracts and architectures, and a 90-day roadmap. Use when someone asks how to make a team, process or organization AI-ready, which tasks AI can take on and under what oversight, how to avoid vendor or model lock-in, how to govern or procure AI, what to put in an AI contract, how to prepare for a model retirement or swap, or mentions the durable layer, Frame Card, Swap Rehearsal or Two-Layer Ledger.
---

# The Durable Layer — apply the method

**Invest in the durable layer, rent the replaceable one, and never let the replaceable layer hold the durable one.** The durable layer is what the organization owns and every future tool reads (governed data, vocabulary, wiki, rules and tests, Frame Cards, expertise, roles, policies, decision tables, tool contracts, logs). The replaceable layer is what it rents (models, assistants, frameworks, interfaces, protocol versions).

A team is ready when any current AI tool can be connected to its core processes in a week, evaluated against its own tests, and replaced without loss of knowledge, accountability or trust — and it can *show the rule, the test and the log*.

## Invariants

1. **Never invent the user's facts.** Ask; or leave the field blank and mark it *open*. A template half-filled with real answers beats one filled with plausible ones.
2. **Use the fixed vocabulary** (`references/glossary.md`): Two-Layer Ledger (never "Asset Ledger"); Frame Card decision points D1–D3 ≠ scorecard dimensions D1–D6; R1–R4; in command / in the loop / on the loop; MUST / MAY / MUST NOT.
3. **Score tasks, not activities or jobs.** Floors are non-compensable (D5 ≤ 2 → max R2; D1 ≤ 2 → max R3); just above a threshold rounds towards more human; an unmet gate keeps the task at R1. Model choice never raises the level.
4. **Every score carries the caveat:** *LARA-derived, organization-calibrated* — weights and thresholds are provisional until re-estimated locally and two raters reach κ ≥ 0.70. Until then the ladder is a conversation, not a verdict. Dashboard bands are practitioner-sourced; say so.
5. **Demote, never block.** A failed test lowers a deployment mode; the business continues.
6. **The evaluation set is the arbiter and is never shared with a vendor in full.**
7. **Partners sit above a stable line.** Criticise designs that let the replaceable layer hold the durable one — not vendors for selling. Contract wording is a starting point for the legal adviser, not legal advice.
8. **Cite the source** of every rule you apply: `Ch N` or `App X`.

## Modes — pick one, load its reference

| The user wants… | Mode | Load | Ask first |
|---|---|---|---|
| to know which tasks AI can do, at what level, under what oversight | **Assess** | `references/assess-readiness.md` + `scorecard-template.md` | process, owner, tasks, evidence per dimension, who the second rater is |
| a filled Frame Card, ledger, rider, runbook, dashboard, policy, table, contract, wiki page, golden set | **Fill a template** | the matching `references/*-template.md` or `practice-templates.md` | the owner and the facts for each line; fill only what they give |
| a verdict on a plan, proposal, RFP, contract or architecture | **Review** | `references/review-checklist.md` (+ `procurement-rider-template.md` for contracts) | the full document; its purpose and stage |
| a plan of what to do next | **Roadmap** | `references/roadmap.md` | the first process, what exists, upcoming dates, available people |
| the idea behind a step, or "what does the book say about X" | **Explain** | `references/principles.md` | — |

Modes chain: an assessment ends by offering a Frame Card and a roadmap; a review ends with the three changes that protect the most.

| Template | File |
|---|---|
| Frame Card (App A) | `references/frame-card-template.md` |
| Readiness Scorecard (App B) | `references/scorecard-template.md` · compute with `scripts/score.py` |
| Trust Dashboard + recalibration (App C, Ch 8) | `references/trust-dashboard-template.md` |
| Two-Layer Ledger + Dependency Ledger (App D) | `references/ledgers-template.md` |
| Procurement Rider, 10 clauses (App E) | `references/procurement-rider-template.md` |
| Swap Rehearsal Runbook (App F) | `references/swap-rehearsal-runbook-template.md` |
| Decision page · value→guardrail · expertise capture · golden set · five-line policy · decision table · task-to-model map · tool contract | `references/practice-templates.md` |
| Standards (BPMN, DMN, SKOS, MCP, ISO/IEC 42001 …) | `references/sources.md` |

## Scoring script

```bash
python3 scripts/score.py tasks.csv     # columns: task,d1..d6[,g1..g6]  (gates: met / unmet / na)
```

Stdlib only. Use it whenever code execution is available; otherwise compute by hand and show the arithmetic: mean = (D1 + D2 + D3 + D4 + 1.5·D5 + D6) ÷ 6.5.

## Output

- Language follows the user; English terms are canonical — give them in parentheses on first use in another language, e.g. *niveau de préparation (readiness level)*, *plancher de logique (logic floor)*, *fiche-cadre (Frame Card)* (`glossary.md` has provisional French).
- Markdown tables and templates ready to paste into a wiki or a document; blanks stay visible.
- First person plural is fine; British spelling with "organization"; none of: leverage, unlock, game-changer, journey, ecosystem, robust, seamless, delve, navigate, landscape.
- End with up to three concrete next actions (owner, date), drawn from the chapter's Monday-morning list — and, for leadership audiences, the closing question: *What will be in your durable layer by the end of this year that every future tool can use?*
