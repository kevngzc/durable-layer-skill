# Mode: Review a plan, proposal, RFP, contract or architecture

Goal: say where the document builds the durable layer, where it lets the replaceable layer hold it, and what to change. Read the whole document first. Quote it; never paraphrase a clause you are judging.

## Checks, by Part

Mark each **met · partial · missing · n/a**, with the quote or the absence.

**Ground**
1. Data comes from one governed source with owners, licences, persistent IDs — not copied into a vendor's store (Ch 1).
2. A controlled vocabulary with IDs is an input to the tool; outputs return IDs; unresolved IDs are rejected (Ch 2).
3. Context reaches models from a versioned wiki by reference; nothing enters a prompt that is not first in the wiki (Ch 3).
4. Each value claimed (oversight, privacy, integrity) is carried down to a MUST NOT rule, a test, and an enforcement point every call passes (Ch 4).

**People**
5. Processes described as signed Frame Cards (boundaries, MUST NOT rules, decision points), not only as flowcharts (Ch 5).
6. An expert-authored golden set exists or is planned; vendors are tested against it, not the reverse (Ch 6).
7. Every task has a readiness level and an oversight mode; floors respected (no high-stakes task above R2); override right and logging duty in role descriptions (Ch 7).
8. Trust measured against a written five-line policy; override rate, alignment score and the other dashboard measures defined; recalibration booked (Ch 8).

**Plumbing**
9. Deterministic decisions live in tables (DMN) with knowledge sources and scenario suites, not in prompts (Ch 9).
10. Models chosen per task by evaluation set, ≥ 2 families, ≥ 1 open-weight option; evaluation set not shared in full (Ch 10).
11. One gateway: tool contracts, generated protocol descriptors with pinned versions, policy-as-code, guardrail proxy, hash-chained log, kill switch with a named holder (Ch 11).
12. Dependency Ledger, exit path per component, requalification time shorter than notice period; Swap Rehearsal on the calendar (Ch 12).

**Contracts** — check all ten rider clauses (`procurement-rider-template.md`): present / weaker / missing. Clauses 4 (30-day export), 5 (exit test before go-live) and 6 (≥ 90 days' notice) are the most often missing.

## Shortcut signs — flag any that appear

| Shortcut | Sign |
|---|---|
| Index everything as it is / migrate before governing | Assistant answers questions the catalogue cannot |
| Semantic search replaces the vocabulary | Nobody can say in writing what one tag means |
| Knowledge in chat histories | A decision in force cannot be traced to a page |
| Responsible AI as a product feature | No rule, in your own words, that the vendor's setting enforces |
| Auto-generated process maps | The diagram exists and no one will sign it |
| Fine-tuning on outputs without criteria | No golden set with criteria and reasons |
| Assistants for everyone, no mode set | Nobody can say who approved last week's output |
| Usage reported as adoption; model defaults as policy | No override rate; no written policy |
| Decision left in the prompt | The only way to learn the rule is to ask the model |
| Per-seat general assistant as strategy | AI budget is a headcount, not a task list |
| Direct SDK integrations | Nobody can count model call sites in an afternoon |
| Do-everything platform / integration in one head | The Swap Rehearsal cannot be scheduled |

## Output

```markdown
## Review — <document> (<date>)

**Verdict in one line:** <builds / partly builds / rents the durable layer>

| # | Check | Status | Evidence (quote or absence) | Change to ask for |
|---|---|---|---|---|

**Shortcuts detected:** <shortcut — sign — where in the document>
**Rider clauses:** <n>/10 present · missing: <list>
**Top three changes**, in order of what they protect: <…>
```

Tone: partners sit above a stable line. Criticise where a document lets the replaceable layer hold the durable one, not the vendor for selling. Not legal advice; contract wording goes to the legal adviser.
