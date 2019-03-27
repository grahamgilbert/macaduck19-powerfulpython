import unittest
from powerful_python import requires_reboot


class RebootRequiredTestCase(unittest.TestCase):
    """Tests for `powerful_python.py`'s `requires_reboot`."""

    def test_returns_true(self):
        """Does it return true when restarts is in the output?"""
        out = "You really need to restart here"
        self.assertTrue(requires_reboot(out))

    def test_returns_false(self):
        """Does it return false when restarts is not in the output?"""
        out = "You really need to renppt here"
        self.assertFalse(requires_reboot(out))

    def test_is_boolean(self):
        """Do we always return a boolean?"""
        out = "You really need to restart"
        self.assertIsInstance(requires_reboot(out), bool)


if __name__ == "__main__":
    unittest.main()
