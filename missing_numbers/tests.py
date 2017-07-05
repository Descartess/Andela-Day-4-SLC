""" unit tests for find_missing function """
import unittest
from find_missing import find_missing


class TestFindMissing(unittest.TestCase):
    """ unit tests for find missing """
    def test_find_missing(self):
        """ find missing occurance """
        self.assertEqual(4, find_missing([1, 2], [1, 2, 4]))

    def test_find_missing_2(self):
        """ find missing occurance 2 """
        self.assertEqual(44, find_missing([44, 13, 22], [13, 22]))

if __name__ == "__main__":
    unittest.main()
