'''
Unit tests for task 6 of assignment 1.

Reminder, the method you are testing is:
    calculate_discount(age)
Data types and descriptions are provided in the assignment specification.

You can assume that the calculate_discount method is already imported into this python module,
so you can call "calculate_discount" directly.

Author: Er Jun Yet
Student ID: 33521026
'''
import unittest

class TestCalculateDiscount(unittest.TestCase):

    # ------------------- Test cases for "0%" discount category ------------------- #
    def test_zero_discount_age(self):
        """Equivalence Partitioning: Testing within the 0% discount category"""
        self.assertEqual(calculate_discount(10), 0) # type: ignore
        self.assertEqual(calculate_discount(30), 0) # type: ignore

    def test_zero_discount_upper_boundary(self):
        """Boundary Value Analysis: Testing the upper boundary of 0% discount"""
        self.assertEqual(calculate_discount(50), 0) # type: ignore

    # ------------------- Test cases for "10%" discount category ------------------- #
    def test_ten_discount_age(self):
        """Equivalence Partitioning: Testing within the 10% discount category"""
        self.assertEqual(calculate_discount(55), 10) # type: ignore
        self.assertEqual(calculate_discount(60), 10) # type: ignore
        
    def test_ten_discount_lower_boundary(self):
        """Boundary Value Analysis: Testing the lower boundary of 10% discount"""
        self.assertEqual(calculate_discount(51), 10) # type: ignore

    def test_ten_discount_upper_boundary(self):
        """Boundary Value Analysis: Testing the upper boundary of 10% discount"""
        self.assertEqual(calculate_discount(64), 10) # type: ignore

    # ------------------- Test cases for "15%" discount category ------------------- #
    def test_fifteen_discount_age(self):
        """Equivalence Partitioning: Testing within the 15% discount category"""
        self.assertEqual(calculate_discount(75), 15) # type: ignore
        self.assertEqual(calculate_discount(80), 15) # type: ignore

    def test_fifteen_discount_lower_boundary(self):
        """Boundary Value Analysis: Testing the lower boundary of 15% discount"""
        self.assertEqual(calculate_discount(65), 15) # type: ignore

    def test_fifteen_discount_upper_boundary(self):
        """Boundary Value Analysis: Testing the upper boundary of 15% discount"""
        self.assertEqual(calculate_discount(89), 15) # type: ignore

    # ------------------- Test cases for "100%" discount category ------------------- #
    def test_hundred_discount_age(self):
        """Equivalence Partitioning: Testing within the 100% discount category"""
        self.assertEqual(calculate_discount(95), 100) # type: ignore
        self.assertEqual(calculate_discount(100), 100) # type: ignore

    def test_hundred_discount_lower_boundary(self):
        """Boundary Value Analysis: Testing the lower boundary of 100% discount"""
        self.assertEqual(calculate_discount(90), 100) # type: ignore

    # ------------------- Test cases for Error category (invalid ages) ------------------- #
    def test_invalid_negative_age(self):
        """Boundary Value Analysis: Test invalid negative age (-5)"""
        self.assertEqual(calculate_discount(-1), "ERROR") # type: ignore
        self.assertEqual(calculate_discount(0), "ERROR") # type: ignore

if __name__ == '__main__':
    unittest.main()

