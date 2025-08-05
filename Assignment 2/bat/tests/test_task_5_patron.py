import unittest
from src.patron import Patron
from src.loan import Loan
from src.borrowable_item import BorrowableItem
from datetime import date


class TestPatron(unittest.TestCase):
    """
    Unit tests for the Patron class.

    This test suite aims to validate the functionality of the Patron class, ensuring it handles
    different scenarios correctly. The tests cover finding loans, string representation of a patron,
    and handling various patron attributes.
    """

    def setUp(self):
        """
        Set up the test environment before each test method.

        This method initializes a Patron object with mock data, including valid ID, name, age,
        training records, and loans. It runs before each test case to ensure a consistent test environment.
        """

        # Create a mock Patron object
        self.mock_patron = Patron()
        self.mock_patron._name = "Er Jun Yet"  
        self.mock_patron._age = 20  
        self.mock_patron._id = 101  
        self.mock_patron._outstanding_fees = 0  
        self.mock_patron._carpentry_tool_training = True  
        self.mock_patron._gardening_tool_training = True  
        self.mock_patron._makerspace_training = True  
        self.mock_patron._loans = []  

        # Create a mock BorrowableItem object that represents a book
        self.mock_item = BorrowableItem()
        self.mock_item._name = "Dictionary"  
        self.mock_item._type = "Book"  
        self.mock_item._id = 101  

        # Create a Loan object with the mock item and a due date
        self.loan = Loan(self.mock_item, date(2024, 10, 20))
        self.mock_patron._loans.append(self.loan)

    def test_find_existing_loan(self):
        """
        Test finding an existing loan.

        This test verifies that the find_loan method correctly identifies a loan for the specified item ID.
        """
        loan_found = self.mock_patron.find_loan(self.mock_item._id)
        self.assertEqual(loan_found._item._id, self.mock_item._id)

    def test_find_nonexistent_loan(self):
        """
        Test finding a nonexistent loan.

        This test verifies that the find_loan method returns None when searching for a loan with an invalid item ID.
        """
        self.assertEqual(self.mock_patron.find_loan(1000) is None, True)

    def test_string_representation(self):
        """
        Test the string representation of a patron.

        This test verifies that the __str__ method provides the correct formatted output for a patron.
        """
        expected_result = str ("Patron 101: Er Jun Yet (aged 20)\n" + "Outstanding fees: $0\n" + "Completed training:\n" + " - gardening tools\n" + " - carpentry tools\n" + " - makerspace\n" + "1 active loan:\n" + " - Item 101: Dictionary (Book); due 20/10/2024")
        result = str(self.mock_patron)
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
