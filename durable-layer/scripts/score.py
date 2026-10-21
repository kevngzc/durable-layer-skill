#!/usr/bin/env python3
"""Readiness scorecard (The Durable Layer, Appendix B). Stdlib only.

Input: CSV or JSON rows with task, d1..d6 (1-5) and optional g1..g6
(met / unmet / na; blank = not yet checked).
Output: a markdown table with mean, floor, gates, level and oversight mode.

    python3 score.py tasks.csv
    python3 score.py tasks.json
    echo 'task,d1,d2,d3,d4,d5,d6' | python3 score.py -   # CSV on stdin

The level is LARA-derived and organization-calibrated: weights and thresholds
are provisional until re-estimated locally (Delphi, >= 100 tasks, kappa >= 0.70).
"""
import csv, io, json, sys

WEIGHTS = {"d1": 1.0, "d2": 1.0, "d3": 1.0, "d4": 1.0, "d5": 1.5, "d6": 1.0}
UPPER = [2.0, 3.0, 4.0]          # R1 <= 2.0 < R2 <= 3.0 < R3 <= 4.0 < R4
BORDERLINE = 0.15
MODE = {4: "agent executes · on the loop, 5 % audit",
        3: "agent drafts, human approves · in the loop, 100 %",
        2: "human-led, agent as copilot · in command",
        1: "human only, AI retrieval and summary · in command"}
# Gates that block any level above R1 when they apply and are not met.
# G1/G2 apply only when the user marks them; G4-G6 apply above R1 always.
# G3 never caps the level: it requires a named sign-off at every level.
CAPPING = ["g1", "g2", "g4", "g5", "g6"]


def score(row):
    d = {k: float(row[k]) for k in WEIGHTS}
    for k, v in d.items():
        if not 1 <= v <= 5:
            raise ValueError(f"{row.get('task', '?')}: {k}={v} outside 1-5")
    mean = sum(WEIGHTS[k] * d[k] for k in WEIGHTS) / sum(WEIGHTS.values())
    level = 1 + sum(mean > t for t in UPPER)
    notes = []
    for t in UPPER:  # just above a threshold rounds towards more human
        if t < mean <= t + BORDERLINE + 1e-9:
            level -= 1
            notes.append(f"borderline ({mean:.2f} within {BORDERLINE} of {t})")
    for dim, cap, name in (("d5", 2, "F1 stakes floor"), ("d1", 3, "F2 logic floor")):
        if d[dim] <= 2:
            notes.append(name if level > cap else f"{name.split()[0]} applies")
            level = min(level, cap)

    gates = {g: (row.get(g) or "").strip().lower() for g in ["g1", "g2", "g3", "g4", "g5", "g6"]}
    unmet = [g.upper() for g in CAPPING if gates[g] == "unmet"]
    unchecked = [g.upper() for g in ["g4", "g5", "g6"] if gates[g] == ""]
    gate_note = []
    if level > 1 and unmet:
        gate_note.append(f"{', '.join(unmet)} unmet → R1")
        level = 1
    elif level > 1 and unchecked:
        gate_note.append(f"pending {', '.join(unchecked)}")
    if gates["g3"] in ("met", "unmet", "applies", "yes"):
        gate_note.append("G3 named sign-off required")
    return {"task": row.get("task", ""), **{k: d[k] for k in WEIGHTS}, "mean": mean,
            "floor": "; ".join(notes) or "—", "gates": "; ".join(gate_note) or "—",
            "level": f"R{level}", "mode": MODE[level]}


def read(path):
    text = sys.stdin.read() if path == "-" else open(path, encoding="utf-8").read()
    if text.lstrip().startswith("["):
        rows = json.loads(text)
    else:
        rows = list(csv.DictReader(io.StringIO(text)))
    return [{k.strip().lower(): (str(v).strip() if v is not None else "") for k, v in r.items()} for r in rows]


def fmt(x):
    return f"{x:g}"


def table(results):
    out = ["| Task | D1 | D2 | D3 | D4 | D5 | D6 | Mean | Floor | Gates | Level | Mode |",
           "|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|---|---|:-:|---|"]
    for r in results:
        out.append(f"| {r['task']} | " + " | ".join(fmt(r[k]) for k in WEIGHTS)
                   + f" | {r['mean']:.2f} | {r['floor']} | {r['gates']} | {r['level']} | {r['mode']} |")
    out.append("\n> LARA-derived, organization-calibrated: provisional until weights and thresholds "
               "are re-estimated locally and two raters reach κ ≥ 0.70.")
    return "\n".join(out)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    print(table([score(r) for r in read(sys.argv[1])]))
