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

Typical public notice periods to compare against (Ch 12): about 60 days for some frontier model retirements; 3–6 months for others (as little as two weeks for previews); about 12 months for major protocol deprecations. Ask the user for the actual contract figure; do not assume.

**Small-service rule (Ch 12):** one capability, one contract, one service.
