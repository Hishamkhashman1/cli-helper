import os
import unittest

from bugsquancher.formatter import format_hint


class FormatterTests(unittest.TestCase):
    def setUp(self):
        self.pattern = {
            "name": "modulenotfounderror",
            "cause": "A required Python package or local module could not be found.",
            "solution": "Install the missing package or check your import path/module name.",
            "recommended_command": "pip install <package_name>",
            "context": "Run in your active virtual environment or fix the import statement.",
        }
        self.previous_style = os.environ.get("BUGSQUANCHER_STYLE")

    def tearDown(self):
        if self.previous_style is None:
            os.environ.pop("BUGSQUANCHER_STYLE", None)
        else:
            os.environ["BUGSQUANCHER_STYLE"] = self.previous_style

    def test_default_style(self):
        os.environ.pop("BUGSQUANCHER_STYLE", None)
        output = format_hint("python3 -c 'import does_not_exist'", 1, self.pattern)
        self.assertIn("Bugsquancher detected a squanch", output)
        self.assertIn("Cause", output)
        self.assertIn("Try", output)

    def test_squanchy_style(self):
        os.environ["BUGSQUANCHER_STYLE"] = "2"
        output = format_hint("python3 -c 'import does_not_exist'", 1, self.pattern)
        self.assertIn("Portal squanch detected", output)
        self.assertIn("Status: get schwifty", output)


if __name__ == "__main__":
    unittest.main()
