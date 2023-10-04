#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer_normal_case(self):
        # Test when the list has some positive integers
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_max_integer_negative_case(self):
        # Test when the list has some negative integers
        result = max_integer([-1, -2, -3, -4])
        self.assertEqual(result, -1)

    def test_max_integer_mixed_case(self):
        # Test when the list has mixed positive and negative integers
        result = max_integer([-1, 2, -3, 4])
        self.assertEqual(result, 4)

    def test_max_integer_empty_list(self):
        # Test when the list is empty
        result = max_integer([])
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
