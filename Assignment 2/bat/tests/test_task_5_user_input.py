import unittest
from unittest import mock
from src.user_input import (
    is_int, is_float, read_string, read_integer, read_float,
    read_integer_range, read_float_range, read_bool
)

class TestUserInput(unittest.TestCase):
    """
    Unit tests for the user input functions in the BAT system.

    This test suite aims to validate the functionality of various user input functions, ensuring they handle
    different scenarios correctly. The tests cover functions that check input types, read user input, and
    validate input ranges.

    The following are the functions tested:
    - is_int: Verifies if a string can be interpreted as an integer.
    - is_float: Verifies if a string can be interpreted as a float.
    - read_string: Reads a string input from the user.
    - read_integer: Reads an integer input from the user.
    - read_float: Reads a float input from the user.
    - read_integer_range: Reads an integer input within a specified range.
    - read_float_range: Reads a float input within a specified range.
    - read_bool: Reads a boolean input from the user.

    """
    def test_is_int(self):
        """
        Test the is_int function.

        This test verifies that the is_int function correctly identifies valid integer strings.
        """
        self.assertTrue(is_int('10'))

    def test_is_float(self):
        """
        Test the is_float function.

        This test verifies that the is_float function correctly identifies valid float strings.
        """
        self.assertTrue(is_float('10.5'))

    @mock.patch('builtins.input')
    def test_read_string(self, inp):
        """
        Test the read_string function.

        This test verifies that the read_string function correctly returns the user input.
        """
        inp.return_value = 'FIT2107'
        self.assertEqual('FIT2107', read_string(''))

    @mock.patch('src.user_input.read_string')
    def test_read_integer(self, readstr):
        """
        Test the read_integer function.

        This test verifies that the read_integer function correctly returns a valid integer input.
        """
        readstr.return_value = '10'
        self.assertEqual(10, read_integer(''))

    @mock.patch('src.user_input.read_string')
    def test_read_integer_invalid(self, readstr):
        """
        Test the read_integer function with invalid input.

        This test verifies that the read_integer function continues prompting until a valid integer is entered.
        """
        readstr.side_effect = ['abc', '10']
        self.assertEqual(10, read_integer(''))

    @mock.patch('src.user_input.read_string')
    def test_read_float(self, readstr):
        """
        Test the read_float function.

        This test verifies that the read_float function correctly returns a valid float input.
        """
        readstr.return_value = '10.5'
        self.assertEqual(10.5, read_float(''))

    @mock.patch('src.user_input.read_string')
    def test_read_float_invalid(self, readstr):
        """
        Test the read_float function with invalid input.

        This test verifies that the read_float function continues prompting until a valid float is entered.
        """
        readstr.side_effect = ['abc', '10.5']
        self.assertEqual(10.5, read_float(''))

    @mock.patch('src.user_input.read_integer')
    def test_read_integer_range(self, readint):
        """
        Test the read_integer_range function.

        This test verifies that the read_integer_range function correctly returns a valid integer within the specified range.
        """
        readint.side_effect = [5, 15]
        self.assertEqual(15, read_integer_range('', 10, 20))

    @mock.patch('src.user_input.read_float')
    def test_read_float_range(self, readflt):
        """
        Test the read_float_range function.

        This test verifies that the read_float_range function correctly returns a valid float within the specified range.
        """
        readflt.side_effect = [5.5, 15.5]
        self.assertEqual(15.5, read_float_range('', 10.0, 20.0))

    @mock.patch('src.user_input.read_string')
    def test_read_bool_with_y(self, readstr):
        """
        Test the read_bool function with lowercase 'y'.

        This test verifies that the read_bool function correctly returns 'y' for lowercase 'y'.
        """
        readstr.return_value = 'y'
        self.assertEqual('y', read_bool(''))

    @mock.patch('src.user_input.read_string')
    def test_read_bool_with_n(self, readstr):
        """
        Test the read_bool function with lowercase 'n'.

        This test verifies that the read_bool function correctly returns 'n' for lowercase 'n'.
        """
        readstr.return_value = 'n'
        self.assertEqual('n', read_bool(''))
    
    @mock.patch('src.user_input.read_string')
    def test_read_bool_with_Y(self, readstr):
        """
        Test the read_bool function with uppercase 'Y'.

        This test verifies that the read_bool function correctly returns 'y' for uppercase 'Y'.
        """
        readstr.return_value = 'Y'
        self.assertEqual('y', read_bool(''))

    @mock.patch('src.user_input.read_string')
    def test_read_bool_with_N(self, readstr):
        """
        Test the read_bool function with uppercase 'N'.

        This test verifies that the read_bool function correctly returns 'n' for uppercase 'N'.
        """
        readstr.return_value = 'N'
        self.assertEqual('n', read_bool(''))

    @mock.patch('src.user_input.read_string')
    def test_read_bool_with_multiple_invalid_then_valid_input(self, readstr):
        """
        Test the read_bool function with multiple invalid inputs followed by a valid input.

        This test verifies that the read_bool function prompts for input until a valid boolean value is entered.
        """
        readstr.side_effect = ['a', 'b', 'c', 'y']
        self.assertEqual('y', read_bool(''))

if __name__ == '__main__':
    unittest.main()