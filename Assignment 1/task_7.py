'''
Unit tests for task 7 of assignment 1.

Reminder, the method you are testing is:
    can_borrow(item_type, patron_age, length_of_loan, outstanding_fees, gardening_training, carpentry_training)
Data types and descriptions are provided in the assignment specification.

You can assume that the can_borrow method is already imported into this python module,
so you can call "can_borrow" directly.

Author: Er Jun Yet
Student ID: 33521026
'''
import unittest

class TestCanBorrow(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(can_borrow("Book", 70, 7, 0.00, False, False), True) # type: ignore

    def test_case_2(self):
        self.assertEqual(can_borrow("Book", 91, 14, 0.00, True, False), True) # type: ignore

    def test_case_3(self):
        self.assertEqual(can_borrow("Book", 91, 7, 1.00, True, True), True) # type: ignore

    def test_case_4(self):
        self.assertEqual(can_borrow("Book", 91, 2, 0.00, True, True), True) # type: ignore

    def test_case_5(self):
        self.assertEqual(can_borrow("Book", 17, 7, 0.00, True, True), True) # type: ignore

    def test_case_6(self):
        self.assertEqual(can_borrow("Carpentry", 70, 14, 1.00, True, False), False) # type: ignore

    def test_case_7(self):
        self.assertEqual(can_borrow("Carpentry", 91, 7, 1.00, True, False), False) # type: ignore

    def test_case_8(self):
        self.assertEqual(can_borrow("Carpentry", 17, 14, 0.00, False, True), False) # type: ignore

    def test_case_9(self):
        self.assertEqual(can_borrow("Carpentry", 17, 2, 1.00, False, False), False) # type: ignore

    def test_case_10(self):
        self.assertEqual(can_borrow("Gardening", 70, 2, 1.00, False, True), False) # type: ignore

    def test_case_11(self):
        self.assertEqual(can_borrow("Gardening", 91, 14, 0.00, False, True), False) # type: ignore

    def test_case_12(self):
        self.assertEqual(can_borrow("Gardening", 17, 7, 0.00, True, True), True) # type: ignore

    def test_case_13(self):
        self.assertEqual(can_borrow("Gardening", 17, 2, 1.00, True, False), False) # type: ignore

if __name__ == '__main__':
    unittest.main()
