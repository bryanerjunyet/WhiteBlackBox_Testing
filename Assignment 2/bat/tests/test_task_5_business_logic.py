import unittest
from unittest import mock
from src.business_logic import (type_of_patron, can_borrow, calculate_discount, process_loan)
from src.patron import Patron
from src.data_mgmt import DataManager
from src.loan import Loan 
from datetime import date
from src.borrowable_item import BorrowableItem
  
class TestBusinessLogic(unittest.TestCase):
    """
    Unit tests for the business logic of the borrowing system, including patron classification,
    borrowing eligibility, discount calculations, and loan processing.

    This test suite aims to validate the functionality of various business logic functions,
    ensuring they handle different scenarios correctly. The tests cover patron classification,
    borrowing conditions, discount calculations, and loan processing.

    The following are the functions tested:
    - type_of_patron: Classifies patrons based on their age.
    - can_borrow: Determines if a patron can borrow an item based on various conditions.
    - calculate_discount: Calculates the discount a patron is eligible for based on their age.
    - process_loan: Processes the loan of an item to a patron, updating the necessary records.

    """

    def setUp(self):
        """
        Set up the test environment before each test method.

        This method initializes necessary objects and mock data used in the tests.
 
        """
        self.data_manager = DataManager() 
        self.mock_item = BorrowableItem() 
        self.mock_patron = Patron() 
        self.mock_item._id = 101 
        self.mock_item._name = "Novel" 
        self.mock_item._type = "Book" 
        self.mock_item._year = 2020 
        self.mock_item._on_loan = 0 
        self.mock_item._number_owned = 0  
        self.loan = Loan(self.mock_item, date(2024, 10, 20))  
        self.data_manager._catalogue_data = [self.mock_item] 


# ======================= Test Patron Classification ======================= #
    
    def test_minor_age(self):
        """
        Test the type_of_patron function for minor classification.

        This test verifies that ages between 0 and 17 return "Minor".
        """
        self.assertEqual(type_of_patron(17), "Minor")

    def test_adult_age(self):
        """
        Test the type_of_patron function for adult classification.

        This test verifies that ages between 18 and 89 return "Adult".
        """
        self.assertEqual(type_of_patron(20), "Adult") 

    def test_elderly_age(self):
        """
        Test the type_of_patron function for elderly classification.

        This test verifies that ages 90 and above return "Elderly".
        """
        self.assertEqual(type_of_patron(95), "Elderly")

    def test_invalid_age(self):
        """
        Test the type_of_patron function for invalid age.

        This test verifies that an invalid age returns "ERROR".
        """
        self.assertEqual(type_of_patron(-5), "ERROR")


# ======================= Test Borrowing Conditions ======================= #

# ---------------------- Borrowing Book Test Conditions ----------------------#
    def test_borrow_book_no_outstanding_fees(self):
        """
        Test borrowing a book with no outstanding fees.

        This test verifies that a book can be borrowed when there are no outstanding fees.
        """
        self.assertEqual(can_borrow("Book", 20, 20, 0, False, False), True)

    def test_borrow_book_with_outstanding_fees(self):
        """
        Test borrowing a book with outstanding fees.

        This test verifies that a book cannot be borrowed when there are outstanding fees.
        """
        self.assertEqual(can_borrow("Book", 20, 20, 20, False, False), False)

    def test_borrow_book_valid_loan_duration(self):
        """
        Test borrowing a book with a valid loan duration.

        This test verifies that valid loan durations for books return True.
        """
        self.assertEqual(can_borrow("Book", 20, 55, 0, False, False), True)

    def test_borrow_book_invalid_loan_duration(self):
        """
        Test borrowing a book with an invalid loan duration.

        This test verifies that invalid loan durations for books return False.
        """
        self.assertEqual(can_borrow("Book", 20, 56, 0, False, False), False)

# --------------------------Gardening Tools Test Conditions --------------------------#
    def test_borrow_gardening_tool_with_training(self):
        """
        Test borrowing a gardening tool with valid training.

        This test verifies that a gardening tool can be borrowed with valid training.
        """
        self.assertEqual(can_borrow("Gardening tool", 20, 20, 0, True, False), True)

    def test_borrow_gardening_tool_without_training(self):
        """
        Test borrowing a gardening tool without valid training.

        This test verifies that a gardening tool cannot be borrowed without valid training.
        """
        self.assertEqual(can_borrow("Gardening tool", 20, 20, 0, False, False), False)

    def test_borrow_gardening_tool_with_outstanding_fees(self):
        """
        Test borrowing a gardening tool with outstanding fees.

        This test verifies that a gardening tool cannot be borrowed when there are outstanding fees.
        """
        self.assertEqual(can_borrow("Gardening tool", 20, 20, 20, True, False), False)

    def test_borrow_gardening_tool_no_outstanding_fees(self):
        """
        Test borrowing a gardening tool with no outstanding fees.

        This test verifies that a gardening tool can be borrowed when there are no outstanding fees.
        """
        self.assertEqual(can_borrow("Gardening tool", 20, 20, 0, True, False), True)

    def test_borrow_gardening_tool_valid_loan_duration(self):
        """
        Test borrowing a gardening tool with a valid loan duration.

        This test verifies that valid loan durations for gardening tools return True.
        """
        self.assertEqual(can_borrow("Gardening tool", 20, 28, 0, True, False), True)

    def test_borrow_gardening_tool_invalid_loan_duration(self):
        """
        Test borrowing a gardening tool with an invalid loan duration.

        This test verifies that invalid loan durations for gardening tools return False.
        """
        self.assertEqual(can_borrow("Gardening tool", 20, 29, 0, True, False), False)

# --------------------------Carpentry Tools Test Conditions --------------------------#
    def test_borrow_carpentry_tool_with_training(self):
        """
        Test borrowing a carpentry tool with valid training.

        This test verifies that a carpentry tool can be borrowed with valid training.
        """
        self.assertEqual(can_borrow("Carpentry tool", 20, 10, 0, False, True), True)

    def test_borrow_carpentry_tool_without_training(self):
        """
        Test borrowing a carpentry tool without valid training.

        This test verifies that a carpentry tool cannot be borrowed without valid training.
        """
        self.assertEqual(can_borrow("Carpentry tool", 20, 10, 0, False, False), False)

    def test_borrow_carpentry_tool_valid_age(self):
        """
        Test borrowing a carpentry tool with a valid age.

        This test verifies that a carpentry tool can be borrowed by patrons of valid ages.
        """
        self.assertEqual(can_borrow("Carpentry tool", 30, 10, 0, False, True), True)

    def test_borrow_carpentry_tool_invalid_age(self):
        """
        Test borrowing a carpentry tool with an invalid age.

        This test verifies that a carpentry tool cannot be borrowed by patrons of invalid ages.
        """
        self.assertEqual(can_borrow("Carpentry tool", 90, 10, 0, False, True), False)

    def test_borrow_carpentry_tool_with_outstanding_fees(self):
        """
        Test borrowing a carpentry tool with outstanding fees.

        This test verifies that a carpentry tool cannot be borrowed when there are outstanding fees.
        """
        self.assertEqual(can_borrow("Carpentry tool", 20, 10, 10, False, True), False)

    def test_borrow_carpentry_tool_no_outstanding_fees(self):
        """
        Test borrowing a carpentry tool with no outstanding fees.

        This test verifies that a carpentry tool can be borrowed when there are no outstanding fees.
        """
        self.assertEqual(can_borrow("Carpentry tool", 20, 10, 0, False, True), True)

    def test_borrow_carpentry_tool_valid_loan_duration(self):
        """
        Test borrowing a carpentry tool with a valid loan duration.

        This test verifies that valid loan durations for carpentry tools return True.
        """
        self.assertEqual(can_borrow("Carpentry tool", 20, 14, 0, False, True), True)

    def test_borrow_carpentry_tool_invalid_loan_duration(self):
        """
        Test borrowing a carpentry tool with an invalid loan duration.

        This test verifies that invalid loan durations for carpentry tools return False.
        """
        self.assertEqual(can_borrow("Carpentry tool", 20, 15, 0, False, True), False)

# -------------------------- Invalid Item Test Conditions --------------------------#
    def test_borrow_invalid_item(self):
        """
        Test borrowing an invalid item type.

        This test verifies that an invalid item type returns False for borrowing.
        """
        self.assertEqual(can_borrow("Car", 25, 14, 0, True, True), False)


# ========================= Discount Selection Test Conditions ==========================#

    def test_discount_0_percent(self):
        """
        Test discount calculation for ages under 50.

        This test verifies that ages under 50 receive a 0% discount.
        """
        self.assertEqual(calculate_discount(49), 0)

    def test_discount_10_percent(self):
        """
        Test discount calculation for ages between 50 and 64.

        This test verifies that ages between 50 and 64 receive a 10% discount.
        """
        self.assertEqual(calculate_discount(50), 10)

    def test_discount_15_percent(self):
        """
        Test discount calculation for ages between 65 and 89.

        This test verifies that ages between 65 and 89 receive a 15% discount.
        """
        self.assertEqual(calculate_discount(65), 15)

    def test_discount_100_percent(self):
        """
        Test discount calculation for ages 90 and above.

        This test verifies that ages 90 and above receive a 100% discount.
        """
        self.assertEqual(calculate_discount(90), 100)

    def test_discount_for_invalid_age(self):
        """
        Test discount calculation for an invalid age.

        This test verifies that a negative age returns "ERROR" for discount calculation.
        """
        self.assertEqual(calculate_discount(-1), "ERROR")

# ========================= Loan Process Test Conditions ==========================#

    @mock.patch('src.business_logic.can_borrow')
    def test_successful_loan_process(self, mock_can_borrow):
        """
        Test the loan process for a successful loan.

        This test verifies that the loan process is successful when borrowing conditions are met.
        """
        # Mock can_borrow to return True
        mock_can_borrow.return_value = True  
        # Process loan
        process_loan(self.mock_patron, self.mock_item, 7)  
        # Check item loan count
        self.assertEqual(self.mock_item._on_loan, 1)  
        # Check patron loans
        self.assertEqual(len(self.mock_patron._loans), 1)  

    @mock.patch('src.business_logic.can_borrow')
    def test_unsuccessful_loan_process(self, mock_can_borrow):
        """
        Test the loan process for an unsuccessful loan.

        This test verifies that the loan process is unsuccessful when borrowing conditions are not met.
        """
        # Mock can_borrow to return False
        mock_can_borrow.return_value = False  
        # Process loan
        process_loan(self.mock_patron, self.mock_item, 7)  
        # Check item loan count
        self.assertEqual(self.mock_item._on_loan, 0)  
        # Check patron loans
        self.assertEqual(len(self.mock_patron._loans), 0)  
 

if __name__ == '__main__':
    unittest.main()