"""Unit tests for traffic signal control system"""

import unittest
from src.signal_control import adjust_signal_cycle


class TestSystem(unittest.TestCase):
    """Test cases for signal adjustment logic"""

    def test_signal_adjustment(self) -> None:
        """Verify green time calculations"""
        self.assertEqual(adjust_signal_cycle(65), 50)
        self.assertEqual(adjust_signal_cycle(30), 40)
        self.assertEqual(adjust_signal_cycle(10), 30)


if __name__ == "__main__":
    unittest.main()
