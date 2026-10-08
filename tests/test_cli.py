import json
import tempfile
import unittest
from pathlib import Path

from rabtech_diagnostic.cli import check_dependency, create_report


class TestDiagnosticCLI(unittest.TestCase):

    # Test 1: Successful report creation
    def test_success(self):
        report = create_report()

        self.assertIn("python_version", report)
        self.assertIn("disk_space_gb", report)
        self.assertIn("developer_tools", report)
        self.assertIn("environment_variables", report)

    # Test 2: Missing Python dependency
    def test_missing_dependency(self):
        with self.assertRaises(ImportError):
            check_dependency("this_dependency_does_not_exist")

    # Test 3: Malformed configuration
    def test_malformed_configuration(self):
        with tempfile.TemporaryDirectory() as temp_dir:

            config_file = Path(temp_dir) / "bad-config.json"

            config_file.write_text(
                "{ invalid json }",
                encoding="utf-8"
            )

            with self.assertRaises(json.JSONDecodeError):
                create_report(str(config_file))


if __name__ == "__main__":
    unittest.main()