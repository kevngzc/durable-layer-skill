# One-Page Procurement Rider (App E, Ch 12)

Attach to any contract for a model, assistant, gateway, platform or integration service. Each clause protects the durable layer and keeps partners interchangeable; **strike none without the fallback below.** When reviewing a contract, report each clause as present / weaker / missing, quoting the contract's wording.

| # | Clause | Wording for the contract |
|:-:|:------|:------------------|
| 1 | **Data rights retained** | All data, documents, vocabularies, process descriptions, decision rules, evaluation sets and logs supplied to or generated through the service are the organization's; it holds all rights in them. The supplier acquires no rights beyond those needed to deliver the service during its term. |
| 2 | **No training on institutional data** | The supplier shall not use the organization's data, prompts, outputs or logs to train, fine-tune or improve any model or product without separate written permission. |
| 3 | **Interoperable formats, open standards** | Process, decision, case, vocabulary, event-log and architecture artefacts shall be stored and exchanged in open, royalty-free formats (BPMN, DMN, CMMN, SKOS, OCEL), architecture models in the published ArchiMate exchange format; tool interfaces described by schema and exposed through a standard tool protocol. |
| 4 | **Export of all artefacts on exit** | Within 30 days of termination or on request, the supplier shall deliver every artefact in clause 3, with all prompts, configurations, embeddings and logs, in those formats, at no charge, and certify deletion of its copies. |
| 5 | **Exit test before go-live** | Before production use, the organization shall redeploy the process on an alternative model or engine against its golden evaluation set, with the supplier's cooperation. Go-live is conditional on the test passing. |
| 6 | **Minimum model-retirement notice** | At least 90 days' written notice before retiring, materially changing or re-pricing any model or protocol version the organization depends on; the previous version maintained for that period. |
| 7 | **Audit log access** | Continuous, programmatic access to a tamper-evident log of every request, response, model identifier, prompt version, policy decision and human override, retained as the organization's rules require and exportable at any time. |
| 8 | **Evaluation on two model families** | The supplier shall support running the organization's golden evaluation set against at least two model families and shall accept the result as the acceptance criterion in place of benchmark rank. |
| 9 | **Oversight and kill switch** | The service shall enforce the organization's oversight modes and MUST NOT rules as configured at the gateway, and allow the organization to suspend it immediately, without a deployment, on its own authority. |
| 10 | **Personal data** | Processed in accordance with the UN Principles on Personal Data Protection and Privacy (or the organization's own data-protection regime), inside the perimeter the organization specifies, and nowhere else. |

Supplier ______________________ · date ____ / ____ / ____ · Dependency Ledger row ______

Not legal advice: the wording is a starting point for the organization's legal adviser, who reads the whole clause.

**In negotiation.** The rider sits beside the organization's general conditions of contract, not above them; privileges and immunities and the disputes clause stay as they are. Hold clauses 1, 2, 4 and 7 without exception: they are what makes the durable layer yours. Where a supplier refuses another, replace it with its fallback and record the gap as a risk in the Dependency Ledger.

- **5, exit test:** without the supplier's cooperation, run it yourself on the exported artefacts before go-live and before each renewal.
- **6, notice:** if 90 days is refused, take the supplier's published minimum plus the right to stay on the previous version, at the same price, until requalification ends.
- **8, two model families:** for a single-model product, require the evaluation results in an exportable form, so the set can be run elsewhere.
- **9, kill switch:** if the product cannot be suspended at will, route it through the gateway, where it can (Chapter 11).
