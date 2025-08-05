import unittest

from src.business_logic import can_borrow_carpentry_tool

'''
Let A be (fees_owed > 0)
Let B be (patron_age <= 18)
Let C be (patron_age >= 90)

Possible tests:
1: A = F, B = F, C = F, Outcome: T (Patron can borrow the tool)
2: A = F, B = F, C = T, Outcome: F (Patron is too old (Elderly))
3: A = F, B = T, C = F, Outcome: F (Patron is too young (Minor))
4: A = T, B = F, C = F, Outcome: F (Patron owes fees)
5. A = T, B = T, C = F, Outcome: F (Patron owes fees and is too young)

Possible optimal sets of tests using MC/DC:
- 1, 2, 3, 4

Set chosen: (1, 2, 3, 4)
'''

class TestCanBorrowCarpentryTool(unittest.TestCase):

    # Test 1: A = F, B = F, C = F, Outcome = T
    # All conditions = False: No fees owed, patron age between 18 to 90, completed training.
    def test_f_f_f(self):
        self.assertTrue(can_borrow_carpentry_tool(25, 10, 0, True))  # patron_age = 25, length of loan = 10, no outstanding fees, carpentry training completed

    # Test 2: A = F, B = F, C = T, Outcome = F
    # The patron is an Elderly (patron_age >= 90)
    def test_f_f_t(self):
        self.assertFalse(can_borrow_carpentry_tool(92, 10, 0, True))  # patron_age = 92, length of loan = 10, no outstanding fees, carpentry training completed

    # Test 3: A = F, B = T, C = F, Outcome = F
    # The patron is a Minor (patron_age <= 18)
    def test_f_t_f(self):
        self.assertFalse(can_borrow_carpentry_tool(17, 10, 0, True))  # patron_age = 17, length of loan = 10, no outstanding fees, carpentry training completed

    # Test 4: A = T, B = F, C = F, Outcome = F
    # The patron owes fees (fees_owed > 0)
    def test_t_f_f(self):
        self.assertFalse(can_borrow_carpentry_tool(30, 10, 15, True))  # patron_age = 30, length of loan = 10, outstanding fees = 15, carpentry training completed

if __name__ == '__main__':
    unittest.main()