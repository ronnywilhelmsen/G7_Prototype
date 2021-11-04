import unittest
from unittest import TestCase


class TryTesting(TestCase):
    def test_always_passes(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
