"""Version mismatches and non-LTS builds cannot silently pass verification."""
import importlib.util
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location("tool_version", Path(__file__).with_name("check-tool-version.py"))
versions = importlib.util.module_from_spec(spec)
spec.loader.exec_module(versions)


class ToolVersionTests(unittest.TestCase):
    def test_node_requires_exact_pin_and_lts(self):
        self.assertIn("Lithium", versions.check_node("26.13.0", {"version": "v26.13.0", "lts": "Lithium"}))
        for expected, runtime, reason in [
            ("26.13.0", {"version": "v24.22.1", "lts": "Krypton"}, "differs"),
            ("26.13.0", {"version": "v26.13.0", "lts": False}, "not an LTS"),
            ("26", {"version": "v26.13.0", "lts": "Lithium"}, "exact"),
        ]:
            with self.subTest(expected=expected, runtime=runtime), self.assertRaisesRegex(ValueError, reason):
                versions.check_node(expected, runtime)

    def test_hugo_matching_version_has_no_warning(self):
        self.assertIsNone(versions.check_hugo("0.167.0", "hugo v0.167.0+extended linux/amd64")[1])

    def test_newer_hugo_explicitly_warns_about_ci_coverage(self):
        self.assertIn("differs from CI", versions.check_hugo("0.167.0", "hugo v0.168.0+extended+withdeploy darwin/arm64")[1])

    def test_old_or_non_extended_hugo_fails(self):
        for output in ("hugo v0.166.0+extended linux/amd64", "hugo v0.167.0 linux/amd64", "invalid"):
            with self.subTest(output=output), self.assertRaises(ValueError):
                versions.check_hugo("0.167.0", output)

    def test_pr_and_deploy_must_pin_the_same_hugo(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            workflows = root / ".github/workflows"
            workflows.mkdir(parents=True)
            for name in ("deploy.yml", "verify.yml"):
                (workflows / name).write_text("hugo-version: '0.167.0'\n")
            self.assertEqual(versions.ci_hugo_version(root), "0.167.0")
            (workflows / "verify.yml").write_text("hugo-version: '0.168.0'\n")
            with self.assertRaisesRegex(ValueError, "different"):
                versions.ci_hugo_version(root)
            (workflows / "verify.yml").write_text("hugo-version: latest\n")
            with self.assertRaisesRegex(ValueError, "exactly one"):
                versions.ci_hugo_version(root)
