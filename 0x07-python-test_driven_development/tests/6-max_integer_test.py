#!/usr/bin/python3
"""Unittest for max_integer([...])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Defines: a class TestMasIntegerMethod
             that inherits from unittest.TestCase
    """

    def test_normal_List(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_list_neg_and_0(self):
        self.assertEqual(max_integer([-1, -5, 0, -9]), 0)

    def test_list_only_neg(self):
        self.assertEqual(max_integer([-1, -4, -5]), -1)

    def test_no_args(self):
        """ when no arg is passeed"""
        self.assertEqual(max_integer(), None)

    def test_ordered_list(self):
        """when list is ordered"""
        self.assertEqual(max_integer([2, 4, 6, 8, 10]), 10)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)


if __name__ == "__main__":
    unittest.main()
