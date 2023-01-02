#!usr/bin/python
"""tests for the max integer in a list"""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ unittests for the max integer in a list"""
    def test_list(self):
        """tests a list of integers"""
        self.assertEqual(max_integer([3, 4, 8, 6]), 8)
    
    def test_empty_list(self):
        """tests when the list is empty"""
        self.assertEqual(max_integer([]), None)
    
    def test_no_list(self):
        """tests when no argument"""
        self.assertEqual(max_integer(), None)
        
    def test_negatives(self):
        """tests for negatives in a list"""
        self.assertEqual(max_integer([-2, -1, -9, -4, -6]), -1)
        
    def test_negat_posit(self):
        """tests for negative and positive values"""
        self.assertEqual(max_integer([-1, 7, -3, 5, 0, 3]), 7)
    
    def test_int_floats(self):
        """tests for ints and floats"""
        self.assertEqual(max_integer([2.4, 1.2, 3.3, 5, 5.6]), 5.6)
        
        
if __name__ == '__main__':
    unittest.main()	
