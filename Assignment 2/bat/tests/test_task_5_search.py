import unittest
import src.search as search
import src.data_mgmt as data_mgmt

class TestSearch(unittest.TestCase):
    """
    Unit tests for the search functions in the search module.

    This test suite aims to validate the functionality of various search functions,
    ensuring they handle different scenarios correctly. The tests cover searching
    for patrons by name, age, and a combination of both.

    The following functions are tested:
    - find_patron_by_name: Searches for patrons by their name.
    - find_patron_by_age: Searches for patrons by their age.
    - find_patron_by_name_and_age: Searches for patrons by both their name and age.
    
    """

    def setUp(self):
        """
        Set up the test environment before each test method.

        This method initializes an instance of the DataManager class and loads the patron data.
        """
        self.manager = data_mgmt.DataManager()
        self.manager.load_patrons()

    def test_find_patron_by_valid_name(self):
        """
        Test the find_patron_by_name function with a valid name.

        This test verifies that the function correctly finds a patron by the name "Timothy Allen".
        """
        result = search.find_patron_by_name("Timothy Allen", self.manager._patron_data)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]._name, "Timothy Allen")

    def test_find_patron_by_valid_age(self):
        """
        Test the find_patron_by_age function with a valid age.

        This test verifies that the function correctly finds a patron by the age 15.
        """
        result = search.find_patron_by_age(15, self.manager._patron_data)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]._age, 15)
        self.assertEqual(result[0]._name, "Leon Kelly")

    def test_find_patron_by_valid_name_and_age(self):
        """
        Test the find_patron_by_name_and_age function with a valid name and age.

        This test verifies that the function correctly finds a patron by the name "Timothy Allen" and age 13.
        """
        result = search.find_patron_by_name_and_age("Timothy Allen", 13, self.manager._patron_data)
        self.assertEqual(result._name, "Timothy Allen")
        self.assertEqual(result._age, 13)

    def test_find_patron_by_invalid_name(self):
        """
        Test the find_patron_by_name function with an invalid name.

        This test verifies that the function correctly returns an empty list when the name "Timothy Thumpkin" is not found.
        """
        result = search.find_patron_by_name("Timothy Thumpkin", self.manager._patron_data)
        self.assertEqual(len(result), 0)

    def test_find_patron_by_invalid_age(self):
        """
        Test the find_patron_by_age function with an invalid age.

        This test verifies that the function correctly returns an empty list when the age 1000 is not found.
        """
        result = search.find_patron_by_age(1000, self.manager._patron_data)
        self.assertEqual(len(result), 0)

    def test_find_patron_by_invalid_name_and_age(self):
        """
        Test the find_patron_by_name_and_age function with an invalid name and age.

        This test verifies that the function correctly returns None when the name "Timothy Thumpkin" and age 1000 are not found.
        """
        result = search.find_patron_by_name_and_age("Timothy Thumpkin", 1000, self.manager._patron_data)
        self.assertEqual(result, None)


if __name__ == '__main__':
    unittest.main()