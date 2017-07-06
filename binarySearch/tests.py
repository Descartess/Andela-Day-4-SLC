""" unit tests for the BinarySearch Class"""
import unittest
from BinarySearch import BinarySearch

class TestBinary(unittest.TestCase):
    """ unit tests for the BinarySearch Class"""
    def setUp(self):
        """ configuration before each test run"""
        self.b_search = BinarySearch(20, 1)
    def test_init(self):
        """ test the init method for BinarySearch"""
        self.assertEqual([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], self.b_search)
    def test_search(self):
        """ tests the binary search method """
        self.assertDictEqual({'count': 3, 'index':1},self.b_search.search(1))

    def test_search2(self):
        """ tests the binary search method small list """
        self.b_search = BinarySearch(8, 2)
        self.assertDictEqual({'count': 1, 'index':3},self.b_search.search(6))

    def test_search3(self):
        """ tests the binary search method small list """
        self.b_search = BinarySearch(100, 5)
        self.assertDictEqual({'count': 4, 'index':4},self.b_search.search(20))

    def test_search_not_found(self):
        """ tests the binary search method small list """
        self.b_search = BinarySearch(100, 5)
        self.assertDictEqual({'count': 5, 'index':-1},self.b_search.search(16))

if __name__ == "__main__":
    unittest.main()
