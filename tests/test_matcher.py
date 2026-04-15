import unittest

from bugsquancher.matcher import match_pattern
from bugsquancher.parser import parse_output


class MatcherTests(unittest.TestCase):
    def test_matches_module_not_found(self):
        output = """Traceback (most recent call last):
ModuleNotFoundError: No module named 'does_not_exist'
"""
        parsed = parse_output(output)
        pattern = match_pattern(parsed)
        self.assertIsNotNone(pattern)
        self.assertEqual(pattern["name"], "modulenotfounderror")


if __name__ == "__main__":
    unittest.main()
