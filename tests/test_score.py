import pathlib, subprocess, sys, unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "durable-layer" / "scripts"))
from score import score  # noqa: E402

MET = {"g4": "met", "g5": "met", "g6": "met"}


def row(task, *d, **g):
    return {"task": task, **{f"d{i+1}": v for i, v in enumerate(d)}, **g}


class AppendixB(unittest.TestCase):
    """The three illustrative scores printed in Appendix B."""

    def test_completeness_check_is_r4(self):
        r = score(row("completeness", 5, 5, 4, 5, 5, 4, **MET))
        self.assertAlmostEqual(r["mean"], 4.69, places=2)
        self.assertEqual(r["level"], "R4")

    def test_policy_area_mapping_is_r3(self):
        r = score(row("policy areas", 3, 4, 4, 4, 3, 4, **MET))
        self.assertAlmostEqual(r["mean"], 3.62, places=2)
        self.assertEqual(r["level"], "R3")

    def test_findings_for_governing_bodies_is_r1(self):
        r = score(row("findings", 2, 3, 2, 1, 1, 4, g3="applies", **MET))
        self.assertAlmostEqual(r["mean"], 2.08, places=2)
        self.assertEqual(r["level"], "R1")
        self.assertIn("F1", r["floor"])
        self.assertIn("G3", r["gates"])


class Rules(unittest.TestCase):
    def test_stakes_floor_caps_at_r2(self):
        r = score(row("t", 5, 5, 5, 5, 2, 5, **MET))
        self.assertEqual(r["level"], "R2")
        self.assertIn("F1 stakes floor", r["floor"])

    def test_logic_floor_caps_at_r3(self):
        r = score(row("t", 2, 5, 5, 5, 5, 5, **MET))
        self.assertEqual(r["level"], "R3")
        self.assertIn("F2 logic floor", r["floor"])

    def test_borderline_rounds_towards_human(self):
        # mean = 26.5/6.5 = 4.077, just above 4.0
        r = score(row("t", 4, 4, 4, 4, 4.5, 4, **MET))
        self.assertEqual(r["level"], "R3")
        self.assertIn("borderline", r["floor"])

    def test_unmet_gate_keeps_task_at_r1(self):
        r = score(row("t", 5, 5, 5, 5, 5, 5, g4="met", g5="unmet", g6="met"))
        self.assertEqual(r["level"], "R1")
        self.assertIn("G5 unmet", r["gates"])

    def test_unchecked_gates_are_reported_not_assumed(self):
        r = score(row("t", 5, 5, 5, 5, 5, 5))
        self.assertEqual(r["level"], "R4")
        self.assertIn("pending G4, G5, G6", r["gates"])

    def test_personal_data_gate_unmet_caps(self):
        r = score(row("t", 5, 5, 5, 5, 5, 5, g1="unmet", **MET))
        self.assertEqual(r["level"], "R1")

    def test_out_of_range_rejected(self):
        with self.assertRaises(ValueError):
            score(row("t", 6, 5, 5, 5, 5, 5))


class Cli(unittest.TestCase):
    def test_csv_stdin_table(self):
        script = pathlib.Path(__file__).resolve().parent.parent / "durable-layer" / "scripts" / "score.py"
        csv_in = "task,d1,d2,d3,d4,d5,d6,g4,g5,g6\ncompleteness,5,5,4,5,5,4,met,met,met\n"
        out = subprocess.run([sys.executable, str(script), "-"], input=csv_in,
                             capture_output=True, text=True, check=True).stdout
        self.assertIn("| completeness |", out)
        self.assertIn("R4", out)
        self.assertIn("organization-calibrated", out)


if __name__ == "__main__":
    unittest.main()
