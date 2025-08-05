import unittest
from src.data_mgmt import DataManager
from src.borrowable_item import BorrowableItem
import src.config as config
import json

class TestDataMgmtClass(unittest.TestCase):
    """
    Unit tests for the DataManager class in the BAT system.

    This test suite aims to validate the functionality of the DataManager class, which is responsible for managing
    patron and catalogue data. The tests cover various scenarios to ensure that the methods in the DataManager class
    operate correctly, including loading, saving, and registering new patrons.

    The following are the functions tested:
    - load_patrons: Verifies that patron data is loaded correctly from a file.
    - load_catalogue: Verifies that catalogue data is loaded correctly from a file.
    - register_patron: Ensures that a new patron is registered correctly.
    - save_patrons: Ensures that patron data is saved correctly to a file.
    - save_catalogue: Ensures that catalogue data is saved correctly to a file.

    """

    def setUp(self):
        """
        Set up the test environment.

        This method initializes an instance of the DataManager class and sets up sample data for testing.
        It runs before each test case to ensure a consistent test environment.
        """
        self.data_manager = DataManager()
        self.patron_name = "Er Jun Yet"
        self.patron_age = 25
        self.item_name = "Story book"
        self.item_id = 101
        self.item_type = "Book"
        self.year = 2020
        self.number_owned = 8
        self.on_loan = 0

    def test_patrons_data_loading(self):
        """
        Test the load_patrons method.

        This test verifies that the patron data is correctly loaded from the file.
        """
        self.assertEqual(len(self.data_manager._patron_data), 100)

    def test_catalogue_data_loading(self):
        """
        Test the load_catalogue method.

        This test verifies that the catalogue data is correctly loaded from the file.
        """
        self.assertEqual(len(self.data_manager._catalogue_data), 7)
    
    def test_patrons_data_loading_error(self):
        """
        Test the load_patrons method with an invalid file path.

        This test ensures that the load_patrons method correctly handles errors when the file path is invalid.
        """
        # Set an invalid file path for patron data
        config.PATRON_DATA = "invalid_path.json"
        error = False

        try: # Attempt to load patrons from the invalid file path
            self.data_manager.load_patrons()
        except SystemExit: # Catch the SystemExit exception if it occurs
            error = True

        self.assertTrue(error)
        # Reset the file path to the original value
        config.PATRON_DATA = "data/patrons.json"

    def test_catalogue_data_loading_error(self):
        """
        Test the load_catalogue method with an invalid file path.

        This test ensures that the load_catalogue method correctly handles errors when the file path is invalid.
        """
        # Set an invalid file path for catalogue data
        config.CATALOGUE_DATA = "invalid_catalogue_path.json"
        error = False

        try:  # Attempt to load catalogue from the invalid file path
            self.data_manager.load_catalogue()
        except SystemExit: # Catch the SystemExit exception if it occurs
            error = True

        self.assertTrue(error)
        config.CATALOGUE_DATA = "data/catalogue.json" # Reset the file path to the original value

    def test_patron_registration(self):
        """
        Test the register_patron method.

        This test ensures that a new patron is correctly registered and added to the patron data.
        """
        self.data_manager.register_patron(self.patron_name, self.patron_age)
        # Verify the number of patrons after registration
        self.assertEqual(len(self.data_manager._patron_data), 101)
        
        new_patron = self.data_manager._patron_data[-1]
        # Get the newly registered patron
        self.assertEqual(new_patron._name, self.patron_name)
        self.assertEqual(new_patron._age, self.patron_age)
        self.assertEqual(new_patron._id, 101)

    def test_patrons_data_saving(self):
        """
        Test the save_patrons method.

        This test ensures that the patron data is correctly saved to a file.
        """
        # Set a temporary file path for saving patron data
        config.PATRON_DATA = "test_save_patron_data.json"

        self.data_manager.register_patron(self.patron_name, self.patron_age)
        # Save the patron data
        self.data_manager.save_patrons()
        # Load the saved patron data
        with open("test_save_patron_data.json", 'r') as saved_patron_file:
            all_patrons = json.load(saved_patron_file)
        # Verify the saved patron data
        self.assertEqual(all_patrons[100]["name"], self.patron_name)
        self.assertEqual(all_patrons[100]["age"], self.patron_age)
        self.assertEqual(len(all_patrons), 101)

        # Reset the temporary file path
        config.PATRON_DATA = "data/patrons.json"

    def test_catalogue_data_saving(self):
        """
        Test the save_catalogue method.

        This test ensures that the catalogue data is correctly saved to a file.
        """
        # Set a temporary file path for saving catalogue data
        config.CATALOGUE_DATA = "test_save_catalogue_data.json"

        # Create a new BorrowableItem and load sample data into it
        borrowable = BorrowableItem()
        borrowable.load_data({
            "item_id": self.item_id,
            "item_name": self.item_name,
            "item_type": self.item_type,
            "year": self.year,
            "number_owned": self.number_owned,
            "on_loan": self.on_loan,
        })

        self.data_manager._catalogue_data = [borrowable]
        # Save the catalogue data
        self.data_manager.save_catalogue()
        # Load the saved catalogue data
        with open("test_save_catalogue_data.json", 'r') as saved_catalogue_file:
            all_catalogue_data = json.load(saved_catalogue_file)
        
        # Verify the saved catalogue data
        self.assertEqual(len(all_catalogue_data), 1)
        self.assertEqual(all_catalogue_data[0]["item_id"], self.item_id)
        self.assertEqual(all_catalogue_data[0]["item_name"], self.item_name)
        self.assertEqual(all_catalogue_data[0]["item_type"], self.item_type)
        self.assertEqual(all_catalogue_data[0]["year"], self.year)
        self.assertEqual(all_catalogue_data[0]["number_owned"], self.number_owned)
        self.assertEqual(all_catalogue_data[0]["on_loan"], self.on_loan)

        # Reset the temporary file path
        config.CATALOGUE_DATA = "data/catalogue.json"



if __name__ == '__main__':
    unittest.main()