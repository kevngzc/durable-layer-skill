# Readiness Scorecard (App B, Ch 7)

Score **tasks**, not activities: most activities contain tasks at two or more levels. Two independent raters per task; the weighted mean gives a level, the **floor rules** cap it, the **gates** sit outside the score. D1–D6 here are scoring dimensions, not the decision points D1–D3 of a Frame Card.

Compute with `scripts/score.py` when code execution is available; otherwise by hand, showing the arithmetic.

## Six dimensions (1 = least ready, 5 = most ready)

| Dimension | 1 | 3 | 5 | Weight |
|:-----------|:-----------|:-----------|:-----------------|:-:|
| **D1 Logic explicitness** | Tacit expert judgement | Documented rules with exceptions | Executable table or deterministic procedure, with tests | 1.0 |
| **D2 Data readiness** | Inputs unlocated or inaccessible; no identifiers | Accessible, partly structured, some identifiers | FAIR-described, machine-readable, provenance known | 1.0 |
| **D3 Volume and standardisation** | Rare, highly variant | Regular, several variants | Frequent, few variants, low rework (from event logs) | 1.0 |
| **D4 Interaction simplicity** | Cross-organizational negotiation | Intra-team coordination | Independent task | 1.0 |
| **D5 Stakes and reversibility** | Very high impact, irreversible, affects rights or mandate outputs | Medium, correctable before effect | Low, fully reversible, internal | **1.5** |
| **D6 Ownership and change readiness** | No owner; unstable; staff untrained or unwilling | Owner named; partly stable | Owner, stable, simplified; trained staff and a champion | 1.0 |

Weighted mean = (D1 + D2 + D3 + D4 + 1.5 × D5 + D6) ÷ 6.5

## Four readiness levels

| Level | Weighted mean | Deployment mode | Human review | Oversight mode |
|:---|:-----|:-----------|:-----------|:---|
| **R4** | 4.1 – 5.0 | Agent executes | 5 % spot audit | on the loop |
| **R3** | 3.1 – 4.0 | Agent drafts, human approves | 100 % approval | in the loop |
| **R2** | 2.1 – 3.0 | Human-led, agent as copilot | Human does the task; agent suggests | in command |
| **R1** | 1.0 – 2.0 | Human only | AI limited to retrieval and summarisation | in command |

## Floor rules (non-compensable)

| Rule | Effect |
|:-----------|:----------------------|
| **F1 Stakes floor** — D5 ≤ 2 | At most **R2**, whatever the mean. High or very high impact never runs autonomously. |
| **F2 Logic floor** — D1 ≤ 2 | At most **R3**. No execution without explicit logic. |
| Borderline — within ± 0.15 of a threshold | Round towards more human involvement. |
| Pilot failure | Demote one level; re-score before promotion (App F). |

## Six gates (pass / fail, outside the score)

| Gate | Condition | Required before any deployment above R1 |
|:---|:--------------|:-----------------------|
| **G1** | Personal data is processed | Data protection impact assessment, consistent with the UN Principles on Personal Data Protection and Privacy (or the organization's own data-protection regime) |
| **G2** | Decision affects individuals' rights, entitlements or interests, or profiles persons | AI impact assessment; named, competent overseer; recourse route; review every 24 months |
| **G3** | Output goes to governing bodies or Member States (or a board, regulator, the public record) | Named human sign-off, whatever the score |
| **G4** | Any level above R1 | Tamper-evident decision log and override logging in place |
| **G5** | Any level above R1 | Golden evaluation set exists and has been run on at least two model families |
| **G6** | Any level above R1 | Exit test passed: data rights retained, no vendor training on our data, process re-deployable on another model or engine |

A gate that applies and is not met keeps the task at **R1**. G3 does not cap the level by itself, but the named sign-off stays whatever the level.

## Scoring sheet

| Task (id) | D1 | D2 | D3 | D4 | D5 | D6 | Mean | Floor | Level | Gates | Rater κ |
|:---------|:-:|:-:|:-:|:-:|:-:|:-:|:--:|:--:|:--:|:------------|:---:|
| | | | | | | | | | | G1 G2 G3 G4 G5 G6 | |

## Illustrative scores (mechanism only, not measured)

| Task | D1 | D2 | D3 | D4 | D5 | D6 | Mean | Result |
|:------------------|:-:|:-:|:-:|:-:|:-:|:-:|:--:|:----------------------|
| Check completeness against mandatory fields | 5 | 5 | 4 | 5 | 5 | 4 | 4.7 | R4 — agent executes, spot audit; G4–G6 required |
| Map reported measures to policy areas | 3 | 4 | 4 | 4 | 3 | 4 | 3.6 | R3 — agent drafts, focal point confirms every tag |
| Select findings for the governing bodies | 2 | 3 | 2 | 1 | 1 | 4 | 2.1 | F1, G3 and the borderline rule apply — R1, agent confined to retrieval and summaries |

## Calibration caveat — state it with every score

**LARA-derived, organization-calibrated.** The scorecard adapts the LARA matrix (Li & Ye, 2026, preprint), validated in financial-services IT operations with Fleiss' κ 0.80. D1, D2 and D5 descend from validated constructs; D3, D4 and D6 have no validation evidence. The 1.5 weight and the level thresholds are provisional. Before any score changes a deployment mode: re-estimate the weights with a 10–12-expert, three-round Delphi (programme, legal and ethics staff); re-estimate the R1–R4 cut-points by clustering at least 100 of your own scored tasks; reach Cohen's κ ≥ 0.70 between two independent raters. Recalibrate every six months, on any model swap, on drift above 0.5, or on a regulatory change. Until then, **the ladder is a conversation, not a verdict.**

## Gates and the law

For UN-system organizations these instruments are references, not obligations: privileges and immunities generally keep them outside national and EU law, and internal rules apply. For a national public body, many are binding law. Check with your legal office.

| Gate | UN-system reference | EU: AI Act · GDPR | National examples |
|:-----|:-------------|:--------------|:-------------|
| **G1** Personal data | HLCM data principles: risk-benefit assessment; model policy J–K: data protection impact assessments | GDPR art. 35 (impact assessment); AI Act art. 26(9) (provider information feeds it) | — |
| **G2** Rights or profiling | CEB principles: human autonomy and oversight, transparency and explainability; model policy F: AI impact assessment, reviewed at least every 24 months; M: complaints | AI Act art. 4 (AI literacy), 14 (human oversight), 26(2) (competent overseers), 26(11) (persons informed), 27 (fundamental-rights impact assessment, public bodies), 86 (explanation); GDPR art. 22 | Canada, Directive on Automated Decision-Making 6.1 (algorithmic impact assessment), 6.2 (notice, explanation), 6.3.9 (training), 6.4 (recourse); France, CRPA L311-3-1 (decision states an algorithm was used; main rules on request), L312-1-3 (main rules published online) |
| **G3** Governing bodies | CEB principles: responsibility and accountability; model policy K: labelling and quality control of AI-generated content | AI Act art. 50(4) (AI-generated text on public-interest matters disclosed unless a person with editorial responsibility reviewed it) | — |
| **G4** Decision log | Model policy L: tracking and explaining AI-driven decisions; retention for audit | AI Act art. 12 (automatic logs), 13(3)(f) (log mechanisms described), 26(6) (deployer keeps logs at least six months) | Canada directive 6.2.7 (decisions documented), 6.3.4 (overrides documented), 6.3.11 (protection against tampering) |
| **G5** Golden set | Model policy K: testing standards, quality control | AI Act art. 13(3)(b)(ii) (accuracy and the metrics it was tested against) | Canada directive 6.3.1 (testing before production), 6.3.2 (outcome monitoring) |
| **G6** Exit test | Model policy J: care with third-party systems that store or train on data; K: supplier evaluation, interoperability | — | Canada directive 6.2.5–6.2.6 (released versions kept; right to access, test and audit proprietary components) |

CEB principles: *Principles for the Ethical Use of AI in the UN System* (2022). HLCM data principles: *Principles on Personal Data Protection and Privacy* (2018). Model policy: HLCM *Framework for a Model Policy on the Responsible Use of AI* (2024), by section letter. AI Act articles 12–14, 26, 27 and 86 concern high-risk systems; article 4 concerns all.

**The floor and the law.** F1 keeps decisions that affect rights at R2 or below, with a person deciding. The same line runs through GDPR art. 22 (no decision based solely on automated processing with legal or similar effect, save exceptions), AI Act art. 14 (override and halt) and 86 (explanation), and CRPA L311-3-1 (the person is told an algorithm was used).
