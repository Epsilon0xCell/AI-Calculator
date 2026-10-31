import subprocess
import sys
import unittest

try:
    import chatterbot  # noqa: F401

    HAS_CHATTERBOT = True
except ImportError:
    HAS_CHATTERBOT = False

from ai_calculator import is_quit


class QuitMatchTests(unittest.TestCase):
    def test_plain_quit(self):
        self.assertTrue(is_quit("quit"))

    def test_case_and_spaces(self):
        self.assertTrue(is_quit("  QUIT "))

    def test_other_text_is_not_quit(self):
        self.assertFalse(is_quit("quit now"))
        self.assertFalse(is_quit("2 + 2"))


class MissingDependencyTests(unittest.TestCase):
    @unittest.skipIf(
        HAS_CHATTERBOT,
        "ChatterBot is installed here, so the missing dependency path cannot run",
    )
    def test_missing_chatterbot_prints_hint_and_exits_1(self):
        out = subprocess.run(
            [sys.executable, "ai_calculator.py"],
            input="quit\n",
            capture_output=True,
            text=True,
        )
        self.assertEqual(out.returncode, 1)
        self.assertIn("ChatterBot is not installed", out.stderr)
        self.assertNotIn("Traceback", out.stderr)


if __name__ == "__main__":
    unittest.main()
