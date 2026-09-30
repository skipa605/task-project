import unittest
from task_app import PRIORITY_ORDER, DEFAULT_PRIORITY


class TestPriority(unittest.TestCase):
    def test_default(self):
        self.assertEqual(DEFAULT_PRIORITY, "normal")

    def test_order(self):
        self.assertEqual(PRIORITY_ORDER["high"], 0)
        self.assertEqual(PRIORITY_ORDER["normal"], 1)
        self.assertEqual(PRIORITY_ORDER["low"], 2)


if __name__ == "__main__":
    unittest.main()
