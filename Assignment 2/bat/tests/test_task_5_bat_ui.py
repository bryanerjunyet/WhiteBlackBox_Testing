import unittest
from unittest import mock
from src.bat_ui import BatUI
import src.data_mgmt as data_mgmt
import src.borrowable_item as borrowable_item


class TestBatUI(unittest.TestCase):
    """
    Unit tests for the BatUI class in the BAT system.

    This test suite aims to validate the functionality of various methods in the BatUI class, ensuring they handle
    different scenarios correctly. The tests cover methods that manage the UI screens and transitions between them,
    including loaning items, returning items, searching for patrons, registering patrons, accessing the makerspace,
    and quitting the application.

    The following methods are tested:
    - _loan_item: Verifies the loaning of items to patrons.
    - _return_item: Verifies the returning of items by patrons.
    - _search_for_patron: Verifies the search functionality for patrons by name and age.
    - _register_patron: Verifies the registration of new patrons.
    - _access_makerspace: Verifies the access control for the makerspace.
    - _quit: Verifies the quitting functionality of the application.
    - get_current_screen: Verifies the retrieval of the current screen.

    """
    def setUp(self):
        """
        Set up the test environment.

        This method initializes an instance of the DataManager class and the BatUI class.
        It runs before each test case to ensure a consistent test environment.
        """
        self.data_mgmt = data_mgmt.DataManager()
        self.ui = BatUI(self.data_mgmt)
        self.mock_patron = self.data_mgmt._patron_data[0]

    @mock.patch("src.business_logic.process_loan")
    @mock.patch("src.user_input.read_integer_range")
    @mock.patch("src.search.find_patron_by_name_and_age")
    @mock.patch("src.user_input.read_integer")
    @mock.patch("src.user_input.read_string")
    @mock.patch("src.user_input.read_bool")
    @mock.patch("src.search.find_item_by_id")
    @mock.patch("src.user_input.read_integer")
    def test_successful_loan(self, read_id, find_item, confirm_item, read_name, read_age, find_patron, read_loan_duration, loan_process):
        """
        Test the successful loan of an item.

        This test verifies that the loan process is successful when all inputs are valid.
        """
        # Mock user inputs and method returns
        read_id.return_value = 7
        find_item.return_value = borrowable_item.BorrowableItem()
        confirm_item.return_value = "y"

        read_name.return_value = "John Doe"
        read_age.return_value = 95
        find_patron.return_value = self.mock_patron

        read_loan_duration.return_value = 7
        loan_process.return_value = True

        # Execute the loan item process
        self.ui._current_screen = self.ui._loan_item()
        self.assertEqual(self.ui.get_current_screen(), "MAIN MENU")

    @mock.patch("src.user_input.read_bool")
    @mock.patch("src.search.find_item_by_id")
    @mock.patch("src.user_input.read_integer")
    def test_unconfirm_loan_item(self, read_id, find_item, confirm_item):
        """
        Test the cancellation of the loan process.

        This test verifies that the loan process is cancelled when the user does not confirm the loan.
        """
        # Mock user inputs and method returns
        find_item.return_value = borrowable_item.BorrowableItem()
        read_id.return_value = 7
        confirm_item.return_value = "n"
        # Execute the loan item process
        self.ui._current_screen = self.ui._loan_item()
        self.assertEqual(self.ui.get_current_screen(), "MAIN MENU")

    @mock.patch("src.search.find_item_by_id")
    @mock.patch("src.user_input.read_integer")
    def test_invalid_loan_item(self, read_id, find_item):
        """
        Test the loan attempt of a non-existent item.

        This test verifies that the loan process is handled correctly when the item does not exist.
        """
        # Mock user inputs and method returns
        read_id.return_value = -1
        find_item.return_value = None
        # Execute the loan item process
        self.ui._current_screen = self.ui._loan_item()
        self.assertEqual(self.ui.get_current_screen(), "MAIN MENU")

    @mock.patch("src.search.find_patron_by_name_and_age")
    @mock.patch("src.user_input.read_integer")
    @mock.patch("src.user_input.read_string")
    @mock.patch("src.user_input.read_bool")
    @mock.patch("src.search.find_item_by_id")
    @mock.patch("src.user_input.read_integer")
    def test_invalid_patron_who_loan(self, read_id, find_item, confirm_item, read_name, read_age, find_patron):
        """
        Test the loan of an item to a non-existent patron.

        This test verifies that the loan process is handled correctly when the patron does not exist.
        """
        # Mock user inputs and method returns
        read_id.return_value = 7
        find_item.return_value = borrowable_item.BorrowableItem()
        confirm_item.return_value = "y"

        read_name.return_value = "John Doe"
        read_age.return_value = 95
        find_patron.return_value = None

        # Execute the loan item process
        self.ui._current_screen = self.ui._loan_item()
        self.assertEqual(self.ui.get_current_screen(), "MAIN MENU")

    @mock.patch("src.business_logic.process_loan")
    @mock.patch("src.user_input.read_integer_range")
    @mock.patch("src.search.find_patron_by_name_and_age")
    @mock.patch("src.user_input.read_integer")
    @mock.patch("src.user_input.read_string")
    @mock.patch("src.user_input.read_bool")
    @mock.patch("src.search.find_item_by_id")
    @mock.patch("src.user_input.read_integer")
    def test_unsuccessful_loan(self, read_id, find_item, confirm_item, read_name, read_age, find_patron, read_loan_duration, loan_process):
        """
        Test the unsuccessful loan of an item.

        This test verifies that the loan process is handled correctly when the loan cannot be processed.
        """
        # Mock user inputs and method returns
        read_id.return_value = 7
        find_item.return_value = borrowable_item.BorrowableItem()
        confirm_item.return_value = "y"

        read_name.return_value = "John Doe"
        read_age.return_value = 95
        find_patron.return_value = self.mock_patron

        read_loan_duration.return_value = 7
        loan_process.return_value = False

        # Execute the loan item process
        self.ui._current_screen = self.ui._loan_item()
        self.assertEqual(self.ui.get_current_screen(), "MAIN MENU")

    @mock.patch("src.business_logic.process_return")
    @mock.patch("src.user_input.read_integer")
    @mock.patch("src.search.find_patron_by_name_and_age")
    @mock.patch("src.user_input.read_integer")
    @mock.patch("src.user_input.read_string")
    def test_successful_return_item(self, read_name, read_age, find_patron, read_id, return_process):
        """
        Test the successful return of an item.

        This test verifies that the return process is successful when all inputs are valid.
        """
        # Mock user inputs and method returns
        read_name.return_value = "John Doe"
        read_age.return_value = 95
        find_patron.return_value = self.mock_patron

        read_id.return_value = 1
        return_process.return_value = True

        # Execute the return item process
        self.ui._current_screen = self.ui._return_item()
        self.assertEqual(self.ui.get_current_screen(), "MAIN MENU")

    @mock.patch("src.business_logic.process_return")
    @mock.patch("src.user_input.read_integer")
    @mock.patch("src.search.find_patron_by_name_and_age")
    @mock.patch("src.user_input.read_integer")
    @mock.patch("src.user_input.read_string")
    def test_successful_return_eventually(self, read_name, read_age, find_patron, read_id, return_process):
        """
        Test the successful return of an item after multiple incorrect attempts.

        This test verifies that the return process is successful after multiple incorrect attempts.
        """
        # Mock user inputs and method returns
        read_name.return_value = "John Doe"
        read_age.return_value = 95
        find_patron.return_value = self.mock_patron

        read_id.side_effect = [7, 2, 1]
        return_process.return_value = True

        # Execute the return item process
        self.ui._current_screen = self.ui._return_item()
        self.assertEqual(self.ui.get_current_screen(), "MAIN MENU")

    @mock.patch("src.search.find_patron_by_name_and_age")
    @mock.patch("src.user_input.read_integer")
    @mock.patch("src.user_input.read_string")
    def test_unsuccessful_return_item(self, read_name, read_age, find_patron):
        """
        Test the return of an item to a non-existent patron.

        This test verifies that the return process is handled correctly when the patron does not exist.
        """
        # Mock user inputs and method returns
        read_name.return_value = "John Doe"
        read_age.return_value = 95
        find_patron.return_value = None
        # Execute the return item process
        self.ui_current_screen = self.ui._return_item()
        self.assertEqual(self.ui.get_current_screen(), "MAIN MENU")

    @mock.patch("src.search.find_patron_by_name")
    @mock.patch("src.user_input.read_string")
    @mock.patch("src.user_input.read_integer_range")
    def test_successful_search_patron_name(self, read_option, read_name, find_patron):
        """
        Test the successful search for a patron by name.

        This test verifies that the search process is successful when the patron exists.
        """
        # Mock user inputs and method returns
        read_option.return_value = 1
        read_name.return_value = "John Doe"
        find_patron.return_value = [self.mock_patron]
        # Execute the search for patron process
        self.ui._current_screen = self.ui._search_for_patron()
        self.assertEqual(self.ui.get_current_screen(), "SEARCH FOR PATRON")

    @mock.patch("src.search.find_patron_by_name")
    @mock.patch("src.user_input.read_string")
    @mock.patch("src.user_input.read_integer_range")
    def test_unsuccessful_search_patron_name(self, read_option, read_name, find_patron):
        """
        Test the unsuccessful search for a patron by name.

        This test verifies that the search process is handled correctly when the patron does not exist.
        """
        # Mock user inputs and method returns
        read_option.return_value = 1
        read_name.return_value = "John Doe"
        find_patron.return_value = []
        # Execute the search for patron process
        self.ui._current_screen = self.ui._search_for_patron()
        self.assertEqual(self.ui.get_current_screen(), "SEARCH FOR PATRON")

    @mock.patch("src.search.find_patron_by_age")
    @mock.patch("src.user_input.read_integer")
    @mock.patch("src.user_input.read_integer_range")
    def test_successful_search_patron_age(self, read_option, read_age, find_patron):
        """
        Test the successful search for a patron by age.

        This test verifies that the search process is successful when the patron exists.
        """
        # Mock user inputs and method returns
        read_option.return_value = 2
        read_age.return_value = 95
        find_patron.return_value = [self.mock_patron]
        # Execute the search for patron process
        self.ui._current_screen = self.ui._search_for_patron()
        self.assertEqual(self.ui.get_current_screen(), "SEARCH FOR PATRON")

    @mock.patch("src.search.find_patron_by_age")
    @mock.patch("src.user_input.read_integer")
    @mock.patch("src.user_input.read_integer_range")
    def test_unsuccessful_search_patron_age(self, read_option, read_age, find_patron):
        """
        Test the unsuccessful search for a patron by age.

        This test verifies that the search process is handled correctly when the patron does not exist.
        """
        # Mock user inputs and method returns
        read_option.return_value = 2
        read_age.return_value = 95
        find_patron.return_value = []
        # Execute the search for patron process
        self.ui._current_screen = self.ui._search_for_patron()
        self.assertEqual(self.ui.get_current_screen(), "SEARCH FOR PATRON")

    @mock.patch("src.user_input.read_integer")
    def test_cancel_search(self, read_option):
        """
        Test the cancellation of the search for a patron.

        This test verifies that the search process is cancelled when the user chooses to cancel.
        """
        read_option.return_value = 3
        self.ui._current_screen = self.ui._search_for_patron()
        self.assertEqual(self.ui.get_current_screen(), "MAIN MENU")

    @mock.patch("src.search.find_patron_by_name")
    @mock.patch("src.user_input.read_string")
    @mock.patch("src.user_input.read_integer")
    def test_unsuccessful_search_input(self, read_option, read_age, find_patron):
        """
        Test the search for a patron with invalid input.

        This test verifies that the search process is handled correctly when the input is invalid.
        """
        # Mock user inputs and method returns
        read_option.side_effect = [0, 4, 1]
        read_age.return_value = "John Doe"
        find_patron.return_value = [self.mock_patron]
        # Execute the search for patron process
        self.ui._current_screen = self.ui._search_for_patron()
        self.assertEqual(self.ui.get_current_screen(), "SEARCH FOR PATRON")

    @mock.patch("src.user_input.read_integer_range")
    @mock.patch("src.user_input.read_string")
    def test_successful_register(self, read_name, read_age):
        """
        Test the successful registration of a patron.

        This test verifies that the registration process is successful when all inputs are valid.
        """
        # Mock user inputs and method returns
        read_name.return_value = "John Doe"
        read_age.return_value = 95
        # Execute the register patron process
        self.ui._current_screen = self.ui._register_patron()
        self.assertEqual(self.ui.get_current_screen(), "MAIN MENU")

    @mock.patch("src.business_logic.can_use_makerspace")
    @mock.patch("src.search.find_patron_by_name_and_age")
    @mock.patch("src.user_input.read_integer")
    @mock.patch("src.user_input.read_string")
    def test_successful_makerspace_access(self, read_name, read_age, find_patron, makerspace_access):
        """
        Test the successful access to the makerspace.

        This test verifies that the access process is successful when the patron is allowed to use the makerspace.
        """
        # Mock user inputs and method returns
        read_name.return_value = "Hannah Taylor"
        read_age.return_value = 25
        find_patron.return_value = self.mock_patron
        makerspace_access.return_value = True
        # Execute the access makerspace process
        self.ui._current_screen = self.ui._access_makerspace()
        self.assertEqual(self.ui.get_current_screen(), "MAIN MENU")

    @mock.patch("src.business_logic.can_use_makerspace")
    @mock.patch("src.search.find_patron_by_name_and_age")
    @mock.patch("src.user_input.read_integer")
    @mock.patch("src.user_input.read_string")
    def test_unsuccessful_makerspace_access(self, read_name, read_age, find_patron, makerspace_access):
        """
        Test the unsuccessful access to the makerspace.

        This test verifies that the access process is handled correctly when the patron is not allowed to use the makerspace.
        """
        # Mock user inputs and method returns
        read_name.return_value = "John Doe"
        read_age.return_value = 95
        find_patron.return_value = self.mock_patron
        makerspace_access.return_value = False
        # Execute the access makerspace process
        self.ui._current_screen = self.ui._access_makerspace()
        self.assertEqual(self.ui.get_current_screen(), "MAIN MENU")

    @mock.patch("src.search.find_patron_by_name_and_age")
    @mock.patch("src.user_input.read_integer")
    @mock.patch("src.user_input.read_string")
    def test_unsuccessful_makerspace_access_name(self, read_name, read_age, find_patron):
        """
        Test the access to the makerspace with an invalid name.

        This test verifies that the access process is handled correctly when the patron does not exist.
        """
        # Mock user inputs and method returns
        read_name.return_value = "Er Jun Yet"
        read_age.return_value = 99
        find_patron.return_value = None
        # Execute the access makerspace process
        self.ui._current_screen = self.ui._access_makerspace()
        self.assertEqual(self.ui.get_current_screen(), "MAIN MENU")

    @mock.patch('src.data_mgmt.DataManager.save_patrons')
    @mock.patch('src.data_mgmt.DataManager.save_catalogue')
    def test_successful_quit(self, save_catalogue, save_patrons):
        """
        Test the quit functionality of the UI.

        This test verifies that the quit process saves the current state and returns the correct value.
        """
        # Execute the quit process
        result = self.ui._quit()

        # Verify that the methods called once
        save_catalogue.assert_called_once()
        save_patrons.assert_called_once()

        self.assertEqual(result, self.ui._quit)


if __name__ == '__main__':
    unittest.main()
