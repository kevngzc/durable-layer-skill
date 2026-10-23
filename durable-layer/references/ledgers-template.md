# Two-Layer Ledger and Dependency Ledger (App D, Intro, Ch 12)

The rule: **invest in the durable layer, rent the replaceable one, and never let the replaceable layer hold the durable one.** Decision logic that lives in a prompt is in the wrong column; so is a vocabulary that exists only inside a vendor's index, or a log only the supplier can export.

## Two-Layer Ledger

| Durable — owned, versioned, exportable | Replaceable — rented, pinned, swapped |
|:----------|:----------|
| *e.g.* one governed data source with owners, licences and identifiers | *e.g.* the frontier model behind the assistant |
| *e.g.* the vocabulary, with persistent concept identifiers | *e.g.* the agent framework |
| *e.g.* Frame Cards, signed, one per process | *e.g.* the assistant interface |
| *e.g.* decision tables linked to authorising texts | *e.g.* the protocol version the gateway speaks |
| *e.g.* golden sets and policy-alignment tests | *e.g.* the search index |
| *e.g.* the decision log and its schema | *e.g.* the managed inference service |

**Three checks on every left-hand row:** stored in an open format · exportable today without asking a vendor · the people who wrote it are named. A row failing a check is flagged, not moved.

## Dependency Ledger

One row for every component in the right-hand column; review it at every Swap Rehearsal.

| Component | Open / proprietary | What it holds of ours | Exit path | Requalification time | Notice in contract | Last rehearsed |
|:--------|:------|:--------|:--------|:-------|:------|:------|
| *e.g.* frontier model family A | proprietary | nothing; prompts and tests in our files | family B via the gateway; golden set | 6 days | 60 days | 2026-04 |
| *e.g.* decision engine | open source | decision tables (standard XML) | second conformant engine | 3 days | n/a | 2026-04 |
| *e.g.* vector search index | proprietary, managed | embeddings only; sources in the archive | rebuild from source, other embedding model | 10 days | 90 days | *not yet* |

**Priority rule.** Reduce first any row with **no exit path**, or a **requalification time longer than the notice period** — "a crisis that has not happened yet". An exit path never run is a risk, not a path.

Typical public notice periods to compare against (Ch 12, at the time of writing; check the supplier's current page): at least 60 days from one leading supplier; from another, 6 months for general models, 3 for specialised ones and as little as two weeks for previews; from a third, a retirement date set at launch, about a year out. Major protocols: about 12 months' deprecation window. Ask the user for the actual contract figure; do not assume.

**Small-service rule (Ch 12):** one capability, one contract, one service.

## Year-three view

For the budget committee: one column per year, your own figures, staff days at your own day rate. Fill one copy for scenario A, one project per use case, and one for scenario B, a shared durable layer; compare them at year three, not year one.

Scenario (A or B) ______ · Organization or unit ______________ · Date ____ / ____ / ____

| Line | Year 1 | Year 2 | Year 3 | Source in this book |
|:----------------|:---|:---|:---|:-------|
| **Durable layer** · staff days | | | | |
| Frame Cards · one per process, drafted with the owner and signed |   | | | Ch 5 · App A |
| Golden sets · one per task, written by the expert |   | | | Ch 6 |
| Readiness scoring · two raters per task, per scoring round |   | | | Ch 7 · App B |
| Swap Rehearsals · two a year, one sprint, five roles |   | | | Ch 12 · App F |
| Kill-switch tests · monthly |   | | | Ch 11 |
| Recalibration · six-monthly, three people |   | | | Ch 8 · App C |
| **Replaceable layer** · money | | | | |
| Licences and API · per task-month, from the task-to-model map |   | | | Ch 10 |
| Hardware · capital |   | | | Ch 10 |
| Hardware · operations, or managed inference |   | | | Ch 10 |
| Gateway · product, hosting, its owner's time |   | | | Ch 11 |
| **Exit** · for the rows of the Dependency Ledger | | | | |
| Requalification · staff days, notice to qualified replacement |   | | | Ch 12 · App D |
| Export · staff days to receive and check it; the supplier's part is free under the rider |   | | | App E, clause 4 |
| Parallel running · incumbent kept until the swap |   | | | App E, clause 6 · App F |
| Estimated exit cost · the three lines above, summed |   | | | App D |
| **Total cost** · durable + replaceable + exit |   | | | |
| **Value** | | | | |
| Staff hours per cycle · against the baseline before AI |   | | | Ch 12 · App C |
| Cost per completed task · total cost ÷ tasks completed |   | | | Ch 10 · App C |

**Planning assumptions to replace with your own.** Only what this book states; estimate everything else locally.

- A Frame Card: an hour at the process owner's desk, with the governing text open, then a signature (Ch 5).
- A golden set: a few dozen worked examples, chosen and explained by the expert, weighted towards the hard cases (Ch 6).
- A Swap Rehearsal: one sprint, five roles, twice a year; day 1 pin, days 2–5 the four tests, days 6–8 review and log, days 9–10 swap or demote (App F).
- The gateway: about a week to cut over each direct integration; each adapter small enough for one engineer to rewrite in a week (Ch 11).
- Two independent raters per task (App B); recalibration, three people every six months (Ch 8); the kill switch tested monthly (Ch 11). Day rates, prices, hardware and volumes: estimate locally.
