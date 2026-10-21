# Mode: 90-day roadmap

Goal: turn what the user has (or an assessment/review) into a dated, owned, small-steps plan. The method compounds one artefact at a time; no big bang, no platform purchase first.

## Inputs to ask for

- Scope: one process or use case to start with (the most-wanted one), its owner, its governing text.
- What exists already, per Part (data owners, vocabulary, wiki, Frame Cards, golden sets, gateway, contracts).
- Upcoming dates: next procurement or contract renewal, known model retirement notices, governing-body sessions, budget cycle.
- Names or roles available: process owner, an expert, a legal/ethics focal point, an engineer, a Data & AI lead.

## Sequencing rules

1. **Ground → People → Plumbing**, overlapping. Never buy plumbing before Ground has an owner and a vocabulary for the chosen process.
2. Start with **one** process end to end rather than one layer everywhere: data audit → Frame Card → golden set → scorecard → table/gateway route.
3. Every item is an **artefact with an owner and a date**, written in the wiki. Draw items from the Monday-morning actions in `principles.md`.
4. Calendar items now, even if far off: two Swap Rehearsals six months apart; the six-monthly recalibration; the rider attached at the next procurement.
5. Gates (G1–G6) are scheduled before any task is promoted above R1.
6. State what is *not* in the 90 days, and why.

## Template

```markdown
## 90-day plan — <process> (<start date>)

**Readiness statement we are building towards:** <process> can be connected to any current AI tool in a week, evaluated against our own tests, and replaced without loss of knowledge, accountability or trust.

| Weeks | Part | Artefact (what exists at the end) | Owner | Ch / App | Done when |
|---|---|---|---|---|---|
| 1–2 | Ground | Owners named for the five datasets; ten-question audit filled | | Ch 1 | Audit in the wiki |
| 1–2 | People | Frame Card, MUST NOT lines signed | | Ch 5 · App A | Signed card filed beside the governing text |
| 3–4 | Ground | One vocabulary kept, IDs, change procedure | | Ch 2 | Tool test: does it accept the list and return IDs? |
| 3–6 | People | Definition of done + criteria + first 20 golden examples | | Ch 6 | Set versioned under the expert's name |
| 5–6 | People | Tasks scored by two raters; levels and modes | | Ch 7 · App B | κ recorded; gates listed with owners |
| 7–8 | People | Five-line policy; dashboard rows defined | | Ch 8 · App C | Baseline month started |
| 7–10 | Plumbing | One decision table + scenario suite | | Ch 9 | Suite passes by hand |
| 9–12 | Plumbing | Call sites counted; one tool contract; kill-switch holder named | | Ch 11 | Contract in the wiki |
| 9–12 | Plumbing | Dependency Ledger (5 rows); rider ready for next procurement | | Ch 12 · App D–E | Ledger reviewed by legal |
| Calendar | Plumbing | Swap Rehearsals booked (Q2/Q4) · recalibration booked | | App F | Dates and owners in the calendar |

**Not in these 90 days:** <…>
**Risks:** <e.g. retirement notice shorter than requalification time; no second rater>
**Closing question for the leadership team:** What will be in our durable layer by the end of this year that every future tool can use?
```

Shrink or stretch rows to what the user already has; never pad a row with work that already exists.
