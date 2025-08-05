import unittest

from src.business_logic import can_use_makerspace

'''
Feasible paths:
1: 135->148->150->151->153->154->161->164
2: 135->148->150->151->153->155->156->161->164
3: 135->148->150->151->153->155->157->158->159->161->164
4: 135->148->150->151->153->155->157->158->159->161->162->164
'''

class TestCanUseMakerspace(unittest.TestCase):
    """
    Unit tests for the can_use_makerspace function in the business logic module.

    This test suite aims to validate the functionality of the can_use_makerspace function, ensuring it handles
    different scenarios correctly. The tests cover various feasible paths through the function to ensure
    comprehensive coverage.

    """
    def test_patron_type_invalid(self):
        # Test path: 135->148->150->151->153->154->161->164
        # Patron type is "ERROR", should return False!!
        result = can_use_makerspace(-10, 5, False)
        self.assertFalse(result)  # Expected result: False!!

    def test_elderly_or_minor_patron_type(self):
        # Test path: 135->148->150->151->153->155->156->161->164
        # Patron is either "Elderly" or "Minor", should return False!!
        result = can_use_makerspace(17, 10, False)
        self.assertFalse(result)  # Expected result: False!!

    def test_adult_patron_no_fees(self):
        # Test path: 135->148->150->151->153->155->157->158->159->161->164
        # Patron is an adult (neither "Elderly" nor "Minor"), no outstanding fees, return True!!
        result = can_use_makerspace(26, 0, True)
        self.assertTrue(result)  # Expected result: True!!

    def test_adult_patron_with_fees(self):
        # Test path: 135->148->150->151->153->155->157->158->159->161->162->164
        # Patron is an adult (neither "Elderly" nor "Minor"), has outstanding fees, return False!!
        result = can_use_makerspace(46, 25, True)
        self.assertFalse(result)  # Expected result: False!!

if __name__ == '__main__':
    unittest.main()