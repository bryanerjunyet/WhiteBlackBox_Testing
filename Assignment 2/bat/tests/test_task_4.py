import unittest
from src.bat_ui import BatUI
from unittest import mock
from src.data_mgmt import DataManager

class TestMainMenu(unittest.TestCase):
    """
    Unit tests for the main menu navigation in the BatUI class.

    This test suite verifies that the BatUI class correctly navigates to the appropriate screens
    based on user input from the main menu. It ensures that valid inputs navigate to the correct
    screens and that invalid inputs are handled appropriately.
    """

    def setUp(self):
        """
        Set up the test environment.

        This method initializes an instance of the DataManager class and the BatUI class.
        It runs before each test case to ensure a consistent test environment.
        """
        self.data_manager = DataManager()
        self.ui = BatUI(self.data_manager)

    @mock.patch("src.user_input.read_string")
    def test_navigate_to_loan_item_screen(self, mock_read_string):
        """
        Test navigation to the 'LOAN ITEM' screen.

        This test verifies that when the user selects option '1' from the main menu,
        the UI correctly navigates to the 'LOAN ITEM' screen.
        """
        mock_read_string.return_value = 1
        self.ui.run_current_screen()
        self.assertEqual(self.ui.get_current_screen(), "LOAN ITEM")

    @mock.patch("src.user_input.read_string")
    def test_navigate_to_return_item_screen(self, mock_read_string):
        """
        Test navigation to the 'RETURN ITEM' screen.

        This test verifies that when the user selects option '2' from the main menu,
        the UI correctly navigates to the 'RETURN ITEM' screen.
        """
        mock_read_string.return_value = 2
        self.ui.run_current_screen()
        self.assertEqual(self.ui.get_current_screen(), "RETURN ITEM")

    @mock.patch("src.user_input.read_string")
    def test_navigate_to_search_for_patron_screen(self, mock_read_string):
        """
        Test navigation to the 'SEARCH FOR PATRON' screen.

        This test verifies that when the user selects option '3' from the main menu,
        the UI correctly navigates to the 'SEARCH FOR PATRON' screen.
        """
        mock_read_string.return_value = 3
        self.ui.run_current_screen()
        self.assertEqual(self.ui.get_current_screen(), "SEARCH FOR PATRON")

    @mock.patch("src.user_input.read_string")
    def test_navigate_to_register_patron_screen(self, mock_read_string):
        """
        Test navigation to the 'REGISTER PATRON' screen.

        This test verifies that when the user selects option '4' from the main menu,
        the UI correctly navigates to the 'REGISTER PATRON' screen.
        """
        mock_read_string.return_value = 4
        self.ui.run_current_screen()
        self.assertEqual(self.ui.get_current_screen(), "REGISTER PATRON")

    @mock.patch("src.user_input.read_string")
    def test_navigate_to_access_makerspace_screen(self, mock_read_string):
        """
        Test navigation to the 'ACCESS MAKERSPACE' screen.

        This test verifies that when the user selects option '5' from the main menu,
        the UI correctly navigates to the 'ACCESS MAKERSPACE' screen.
        """
        mock_read_string.return_value = 5
        self.ui.run_current_screen()
        self.assertEqual(self.ui.get_current_screen(), "ACCESS MAKERSPACE")
    
    @mock.patch("src.user_input.read_string")
    def test_navigate_to_quit_screen(self, mock_read_string):
        """
        Test navigation to the 'QUIT' screen.

        This test verifies that when the user selects option '6' from the main menu,
        the UI correctly navigates to the 'QUIT' screen.
        """
        mock_read_string.return_value = 6
        self.ui.run_current_screen()
        self.assertEqual(self.ui.get_current_screen(), "QUIT")

    @mock.patch("src.user_input.read_string")
    def test_invalid_then_valid_input(self, mock_read_string):
        """
        Test handling of invalid inputs followed by a valid input.

        This test verifies that the UI handles invalid inputs appropriately and,
        after several invalid inputs, correctly navigates to the 'LOAN ITEM' screen
        when the user finally selects option '1'.
        """
        mock_read_string.side_effect = [50, "x", 0.11, 18, -5, 1]
        self.ui.run_current_screen()
        self.assertEqual(self.ui.get_current_screen(), "LOAN ITEM")

if __name__ == '__main__':
    unittest.main()