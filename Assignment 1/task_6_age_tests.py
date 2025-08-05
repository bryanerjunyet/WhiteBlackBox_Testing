'''
Unit tests for task 6 of assignment 1.

Reminder, the method you are testing is:
    type_of_patron(age)
Data types and descriptions are provided in the assignment specification.

You can assume that the type_of_patron method is already imported into this python module,
so you can call "type_of_patron" directly.

Author: Er Jun Yet
Student ID: 33521026
'''
import unittest

class TestTypeOfPatron(unittest.TestCase):

    # ------------------- Test cases for Minor category ------------------- #
    def test_minor_age(self):
        """Equivalence Partitioning: Testing within the Minor category"""
        self.assertEqual(type_of_patron(1), "Minor") # type: ignore
        self.assertEqual(type_of_patron(10), "Minor") # type: ignore

    def test_minor_upper_boundary(self):
        """Boundary Value Analysis: Testing the upper boundary of Minor"""
        self.assertEqual(type_of_patron(17), "Minor") # type: ignore

    # ------------------- Test cases for Adult category ------------------- #
    def test_adult_age(self):
        """Equivalence Partitioning: Testing within the Adult category"""
        self.assertEqual(type_of_patron(30), "Adult") # type: ignore
        self.assertEqual(type_of_patron(70), "Adult") # type: ignore

    def test_adult_lower_boundary(self):
        """Boundary Value Analysis: Testing the lower boundary of Adult"""
        self.assertEqual(type_of_patron(18), "Adult") # type: ignore

    def test_adult_upper_boundary(self):
        """Boundary Value Analysis: Testing the upper boundary of Adult"""
        self.assertEqual(type_of_patron(89), "Adult") # type: ignore

    # ------------------- Test cases for Elderly category ------------------- #
    def test_elderly_age(self):
        """Equivalence Partitioning: Testing within the Elderly category"""
        self.assertEqual(type_of_patron(100), "Elderly") # type: ignore

    def test_elderly_lower_boundary(self):
        """Boundary Value Analysis: Testing the lower boundary of Elderly"""
        self.assertEqual(type_of_patron(90), "Elderly") # type: ignore

    # ------------------- Test cases for Error category ------------------- #
    def test_invalid_age(self):
        """Boundary Value Analysis: Testing invalid ages """
        self.assertEqual(type_of_patron(-1), "ERROR") # type: ignore
        self.assertEqual(type_of_patron(0), "ERROR") # type: ignore
        self.assertEqual(type_of_patron(200), "ERROR") # type: ignore

if __name__ == '__main__':
    unittest.main()
