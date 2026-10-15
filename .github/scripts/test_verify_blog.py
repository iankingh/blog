"""Prove failed, missing and timed-out checks cannot become a green report."""
import importlib.util
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location("verify_blog", Path(__file__).with_name("verify-blog.py"))
verify = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = verify
spec.loader.exec_module(verify)


class VerificationTests(unittest.TestCase):
    def run_plan(self, steps, timeout=5):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        output = Path(temporary.name)
        return verify.execute_plan(steps, output, output, timeout, os.environ.copy()), output

    def test_failure_keeps_log_and_skips_dependent_checks(self):
        results, output = self.run_plan([
            verify.Step("build", (sys.executable, "-c", "print('broken template');raise SystemExit(7)")),
            verify.Step("generated", (sys.executable, "-c", "raise AssertionError('must not run')"), ("build",)),
            verify.Step("independent", (sys.executable, "-c", "pass")),
        ])
        self.assertEqual([r["status"] for r in results], ["failed", "skipped", "passed"])
        self.assertEqual(results[0]["exit_code"], 7)
        self.assertIn("broken template", (output / "logs/build.log").read_text())
        self.assertFalse(verify.all_passed(results))
        self.assertFalse((output / "logs/generated.log").exists())

    def test_missing_program_is_unavailable(self):
        results, _ = self.run_plan([verify.Step("missing", ("/definitely-missing-blog-check",))])
        self.assertEqual(results[0]["status"], "unavailable")
        self.assertFalse(verify.all_passed(results))

    def test_timeout_is_a_failure(self):
        results, _ = self.run_plan([verify.Step("slow", (sys.executable, "-c", "import time;time.sleep(30)"))], .1)
        self.assertEqual(results[0]["status"], "timed_out")
        self.assertFalse(verify.all_passed(results))

    def test_interruption_stops_remaining_work_and_keeps_checkpoint(self):
        completed = []
        with patch.object(verify, "run_step", return_value={"name": "first", "status": "interrupted"}) as runner:
            with tempfile.TemporaryDirectory() as directory:
                results = verify.execute_plan([
                    verify.Step("first", ("unused",)), verify.Step("second", ("unused",)),
                ], Path(directory), Path(directory), 5, {}, completed.append)
        self.assertEqual(runner.call_count, 1)
        self.assertEqual([r["status"] for r in results], ["interrupted", "skipped"])
        self.assertEqual(completed, results)
        self.assertFalse(verify.all_passed(results))

    def test_success_requires_nonempty_all_passed_results(self):
        results, _ = self.run_plan([verify.Step("ok", (sys.executable, "-c", "print('ok')"))])
        self.assertTrue(verify.all_passed(results))
        self.assertFalse(verify.all_passed([]))
        self.assertFalse(verify.all_passed([{"status": "skipped"}]))

    def test_output_cannot_reuse_stale_artifacts_or_write_in_source(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "repo"
            root.mkdir()
            with patch.object(verify, "ROOT", root):
                for output in (root / "generated", Path(directory)):
                    with self.subTest(output=output), self.assertRaises(SystemExit) as raised:
                        verify.main(["--output", str(output)])
                    self.assertEqual(raised.exception.code, 2)

    def test_changed_source_cannot_pass_cli(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "evidence"
            with patch.object(verify, "source_state", side_effect=[{"fingerprint": "before"}, {"fingerprint": "after"}]), \
                 patch.object(verify, "execute_plan", return_value=[{"status": "passed"}]):
                self.assertEqual(verify.main(["--output", str(output)]), 1)
            import json
            report = json.loads((output / "report.json").read_text())
            self.assertFalse(report["source_unchanged"])
            self.assertEqual(report["status"], "failed")


if __name__ == "__main__":
    unittest.main()
