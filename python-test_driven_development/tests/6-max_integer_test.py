#!/usr/bin/python3
"""write unittests for the function"""


import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """"write unittests for the function"""

    def test_simple_case(self):
        """"write unittests for the function"""
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_negative_case(self):
        """"write unittests for the function"""
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_empty_case(self):
        """"write unittests for the function"""
        self.assertEqual(max_integer([]), None)

    def test_max_middle_case(self):
        """"write unittests for the function"""
        self.assertEqual(max_integer([1, 2, 5, 3, 4]), 5)

    def test_one_element_case(self):
        """"write unittests for the function"""
        self.assertEqual(max_integer([5]), 5)
