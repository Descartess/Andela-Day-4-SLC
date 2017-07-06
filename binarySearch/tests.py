""" unit tests for the BinarySearch Class"""
import unittest
from BinarySearch import BinarySearch

class TestBinary(unittest.TestCase):
    """ unit tests for the BinarySearch Class"""
    def setUp(self):
        """ configuration before each test run"""
        self.search = BinarySearch(6, 2)
    def test_init(self):
        """ test the init method for BinarySearch"""
        self.assertEqual([0, 2, 4, 6, 8, 10], self.search.array)
        