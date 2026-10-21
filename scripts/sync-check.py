#!/usr/bin/env python3
"""Check that the skill still states what the book states.

Each invariant is a (book file, regex) and a (skill file, regex). Both must match.
Run after any edit to the book's appendices or the skill's references.

    python3 scripts/sync-check.py ~/Documents/CODE/FUN/the-durable-layer
"""
import pathlib, re, subprocess, sys

SKILL = pathlib.Path(__file__).resolve().parent.parent / "durable-layer"

INVARIANTS = [  # name, book file, book regex, skill file, skill regex
    ("weighted mean", "appendices/en/B-readiness-scorecard.qmd", r"1\.5 × D5 \+ D6\) ÷ 6\.5",
     "references/scorecard-template.md", r"1\.5 × D5 \+ D6\) ÷ 6\.5"),
    ("level bands", "appendices/en/B-readiness-scorecard.qmd", r"R4\*\* \| 4\.1 – 5\.0.*\n.*R3\*\* \| 3\.1 – 4\.0",
     "references/scorecard-template.md", r"R4\*\* \| 4\.1 – 5\.0.*\n.*R3\*\* \| 3\.1 – 4\.0"),
    ("F1 stakes floor", "appendices/en/B-readiness-scorecard.qmd", r"F1 Stakes floor\*\* — D5 ≤ 2 \| At most \*\*R2",
     "references/scorecard-template.md", r"F1 Stakes floor\*\* — D5 ≤ 2 \| At most \*\*R2"),
    ("F2 logic floor", "appendices/en/B-readiness-scorecard.qmd", r"F2 Logic floor\*\* — D1 ≤ 2 \| At most \*\*R3",
     "references/scorecard-template.md", r"F2 Logic floor\*\* — D1 ≤ 2 \| At most \*\*R3"),
    ("borderline 0.15", "appendices/en/B-readiness-scorecard.qmd", r"± 0\.15",
     "references/scorecard-template.md", r"± 0\.15"),
    ("six gates", "appendices/en/B-readiness-scorecard.qmd", r"\*\*G6\*\*",
     "references/scorecard-template.md", r"\*\*G6\*\*"),
    ("kappa 0.70", "appendices/en/B-readiness-scorecard.qmd", r"κ ≥ 0\.70",
     "references/scorecard-template.md", r"κ ≥ 0\.70"),
    ("calibration phrase", "appendices/en/B-readiness-scorecard.qmd", r"LARA-derived, organization-calibrated",
     "references/scorecard-template.md", r"LARA-derived, organization-calibrated"),
    ("override band 15 %", "appendices/en/C-trust-dashboard.qmd", r"Below 15 %",
     "references/trust-dashboard-template.md", r"Below 15 %"),
    ("eight dashboard rows", "appendices/en/C-trust-dashboard.qmd", r"\| 8 \| \*\*Incidents",
     "references/trust-dashboard-template.md", r"\| 8 \| \*\*Incidents"),
    ("rider: 30-day export", "appendices/en/E-procurement-rider.qmd", r"Within 30 days of termination",
     "references/procurement-rider-template.md", r"Within 30 days of termination"),
    ("rider: 90 days' notice", "appendices/en/E-procurement-rider.qmd", r"At least 90 days' written notice",
     "references/procurement-rider-template.md", r"At least 90 days' written notice"),
    ("rider: ten clauses", "appendices/en/E-procurement-rider.qmd", r"\| 10 \| \*\*Personal data",
     "references/procurement-rider-template.md", r"\| 10 \| \*\*Personal data"),
    ("swap: 20–50 scenarios", "appendices/en/F-swap-rehearsal-runbook.qmd", r"20–50 scenarios",
     "references/swap-rehearsal-runbook-template.md", r"20–50 scenarios"),
    ("swap: demote one level", "appendices/en/F-swap-rehearsal-runbook.qmd", r"Demote the task one level",
     "references/swap-rehearsal-runbook-template.md", r"Demote the task one level"),
    ("frame card: 3–7 rules", "appendices/en/A-frame-card.qmd", r"three to seven rules",
     "references/frame-card-template.md", r"three to seven rules"),
    ("script weight 1.5", None, None, "scripts/score.py", r'"d5": 1\.5'),
    ("script thresholds", None, None, "scripts/score.py", r"UPPER = \[2\.0, 3\.0, 4\.0\]"),
]


def main(book):
    book = pathlib.Path(book).expanduser()
    failed = 0
    for name, bf, bre, sf, sre in INVARIANTS:
        problems = []
        if bf and not re.search(bre, (book / bf).read_text(encoding="utf-8")):
            problems.append(f"book {bf}")
        if not re.search(sre, (SKILL / sf).read_text(encoding="utf-8")):
            problems.append(f"skill {sf}")
        print(("FAIL " if problems else "ok   ") + name + (f"  ← {', '.join(problems)}" if problems else ""))
        failed += bool(problems)
    head = subprocess.run(["git", "-C", str(book), "rev-parse", "--short", "HEAD"],
                          capture_output=True, text=True).stdout.strip()
    src = (SKILL / ".source").read_text().strip()
    if head and head != src:
        print(f"note book HEAD {head} ≠ .source {src}: re-read changed chapters/appendices, then update .source")
    return failed


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    sys.exit(1 if main(sys.argv[1]) else 0)
