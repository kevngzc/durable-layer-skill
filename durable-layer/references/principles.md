# The method, chapter by chapter

**Readiness (Intro):** any current AI tool can be connected to your core processes in a week, evaluated against your own tests, and replaced without loss of knowledge, accountability or trust. A team is ready when it can say which decisions are its own, assisted or delegated — *and prove it: show the rule, show the test, show the log.* Three clauses → three Parts: **Ground** (connected), **People** (evaluated against your own tests), **Plumbing** (replaced without loss).

**The rule (Intro, App D):** invest in the durable layer, rent the replaceable one, and never let the replaceable layer hold the durable one.

Each entry: principle · practice · shortcut and the *sign you took it* · Monday-morning actions.

## Part I — Ground

**Ch 1 One Governed Source, Many Consumers** — *Govern once at source; connect before you generate.*
- Ten-question data audit for the five datasets your most-wanted use case needs (see `assess-readiness.md`). Data Readiness Levels: Band C can you get at it · Band B is it what it claims · Band A is it enough for *this* task.
- Graph with no big bang: start from the vocabulary and the archive, grow one Frame Card at a time. Test: *who is accountable, under which text, using which data?* answered by following edges alone; if a model must infer an edge, the edge is missing.
- Shortcut: index everything as it is, or migrate before governing. Sign: your assistant can answer a question your catalogue cannot.
- Partners: identifiers, metadata and links leave with you in an open format.
- Monday: name an owner (by role) for each of the five datasets · publish one with a licence and persistent ID, and time it (your unit cost) · draw one process graph on a whiteboard and circle the edges that exist in no system.

**Ch 2 The Vocabulary Dividend** — *A shared vocabulary is a guardrail you can read.*
- Eight steps: find the lists · keep one, owner and change procedure · persistent opaque IDs, never reused or deleted · describe in SKOS (prefLabel, altLabels, broader/narrower, scope note) · one preferred label per language · map to public vocabularies · publish at a stable address with an API · wire into every tool (tools output IDs; the gateway rejects what does not resolve).
- Habits: retired lists become mapping tables · deprecate, never delete · the model proposes concepts, the committee creates them · measure coverage (share of outputs resolving to an ID, by tool and month).
- Shortcut: "semantic search makes vocabularies unnecessary". Sign: nobody can say in writing what one tag means.
- Monday: gather three competing lists and keep one · give it an owner, a change procedure and IDs · ask one AI tool owner whether the tool takes the list as input and returns IDs.

**Ch 3 The Wiki That Teaches the Next Tool** — *Write for the next model as you would for the next colleague.*
- Decision pages, compile step, rule of entry, compile log, one-screen pages, the *why did we choose this?* test (`practice-templates.md`).
- Shortcut: knowledge in chat histories. Sign: a decision in force cannot be traced to a page.
- Monday: write three decision pages · turn the last model briefing into pages · ask the newest hire what they could not find.

**Ch 4 From Values to Guardrails in Four Translations** — *A value that is not a rule is a hope; a rule that is not a test is a slogan.*
- Value → policy sentence → actor-neutral MUST/MAY/MUST NOT rule → machine-checkable test → enforcement point at the gateway (`practice-templates.md`).
- Shortcut: responsible AI bought as a product feature. Sign: you cannot name one rule, in your own words, that the vendor's setting enforces.
- Monday: take one value through the four lines · ask which rule is enforced on every call today · write the unwritten MUST NOT and its test.

## Part II — People

**Ch 5 Processes Are Frames, Not Flowcharts** — *Describe the boundaries; let people — and later agents — choose the path inside them.*
- The seven-line Frame Card (`frame-card-template.md`). Normative frame (owned, versioned) kept apart from the operational flow (may go stale). Readiness per task. The signature is a commitment.
- Shortcut: auto-generated process maps. Sign: the diagram exists, and no one will sign it.
- Monday: ask the owner for the MUST NOT sentences only · read them back and get a signature · file the card in the wiki next to its governing text.

**Ch 6 Savoir-Faire: Making Expertise Promotable** — *Explicit expertise is promotable expertise.*
- Definition-of-done interview · decision-criteria capture · golden-example set (`practice-templates.md`). Expert first, tool second; one decision, not one post; reviewed six-monthly; ownership sentence before the first interview.
- Shortcut: fine-tuning on outputs without the criteria.
- Monday: have the expert describe one weekly decision · get five examples (three that show the rule, two lookalikes) into the wiki · make vendors run them case by case before any demo.

**Ch 7 Every Employee Is a Role, Every Role Has an Oversight Mode** — *People do not fear automation; they fear undefined accountability.*
- Oversight modes (EU High-Level Expert Group on AI, 2019; ISO/IEC 42001 asks that oversight scale with risk): in command · in the loop · on the loop. Overseer duties (EU AI Act Art. 14): understand the system's limits, watch for automation bias, interpret output, override, halt.
- R1–R4 ladder scored per task by two raters (`scorecard-template.md`); floor: high-stakes, rights-affecting, governing-body or irreversible tasks never rise above R2. Expected auto-completion ≈ 95 / 70 / 40 % at R4 / R3 / R2.
- HR artefacts: role descriptions as tagged tasks (one rung at a time; a failed pilot demotes) · competencies per oversight mode · the right to override · the duty to log it.
- Shortcut: assistants for everyone, no mode set. Sign: nobody can say who approved last week's output.
- Monday: tag ten tasks · have staff tag the same ten independently; disagreements are implicit rules · add the override right and logging duty to one role description.

**Ch 8 Trust Is Measured Against Your Own Policy** — *If nobody ever overrides the machine, nobody is overseeing it; and the model should learn your policy, not the other way round.*
- Five-line policy → alignment test (process score is the gate) → trust dashboard (`trust-dashboard-template.md`) → six-monthly recalibration. The policy's authors become the model's auditors.
- Shortcut: usage presented as adoption; model defaults becoming policy.
- Monday: write one five-line policy · ask how often a human changed an AI answer last month · book the recalibration with three names.

## Part III — Plumbing

**Ch 9 The Decision Model Is the Contract** — *Decide in a table; execute with whatever is best this year.*
- Requirements diagram · signatures first · decision table with hit policy · knowledge source · 20–50-case scenario suite · portable open format (`practice-templates.md`). Tables fail precisely and at volume; tabling does not change the oversight mode.
- Shortcut: the decision left in the prompt. Sign: the only way to learn the rule is to ask the model.
- Monday: take one decision made by email thread and list its inputs and output · draft a table of 4–8 rules, hit policy *unique*, with a knowledge source · collect ten cases and run them by hand.

**Ch 10 Small Models for Small Jobs, Large Models Where They Earn It** — *Match the model to the task's readiness level; let the evaluation set decide.*
- Task-to-model map (`practice-templates.md`). Evaluation set never shared with a vendor in full. Model choice never raises the readiness level.
- Shortcut: a per-seat general assistant as the AI strategy. Sign: the AI budget is a headcount, not a task list.
- Monday: list the top five use cases by volume · estimate yearly list-price cost of each · ask whether each could run small, and start a 20-example set where none exists.

**Ch 11 One Gateway, Thin Adapters, Boring Interfaces** — *The organization owns the interface; the tools plug into it.*
- Tool contract (five fields) · generated, pinned protocol descriptors · policy-as-code · guardrail proxy · hash-chained decision log · kill switch (`practice-templates.md`).
- Shortcut: direct SDK integrations. Sign: nobody can count the model call sites in an afternoon.
- Monday: count direct call sites and the keys they use · write one five-field contract · plan one door and who holds the kill switch — buy nothing yet.

**Ch 12 Fewer Dependencies, and a Rehearsal on the Calendar** — *Every dependency is a future cost; every open contract is a future option; future-proof is a rehearsal, not a feature.*
- Dependency Ledger (`ledgers-template.md`) · small-service rule · procurement rider (`procurement-rider-template.md`) · Swap Rehearsal twice a year (`swap-rehearsal-runbook-template.md`); failure demotes, never blocks.
- Shortcut: the do-everything platform, or the integration that lived in one head. Sign: the Swap Rehearsal cannot be scheduled, because nobody can say what would be swapped for what.
- Monday: find the exit clause in the largest AI contract · start the ledger with five components · book two rehearsals six months apart, each with an owner.

## Conclusion — five takeaways for leaders

1. Be ready to receive the next model, not to predict it.
2. Ethics made executable: rules and tests, not statements.
3. Your people wrote the durable layer, so they own it.
4. Partners above a stable line: vendors compete on the replaceable layer; the line is yours.
5. The cheapest architecture is the one that welcomes change.

Closing question to put to the user: ***What will be in your durable layer by the end of this year that every future tool can use?***
