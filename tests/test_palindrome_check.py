    def test_single_character(self):
        self.assertTrue(is_palindrome("a"))  # Edge case: single character
        self.assertTrue(is_palindrome("A"))  # Edge case: single character (case insensitive)
    
    def test_long_palindrome(self):
        self.assertTrue(is_palindrome("Able was I, I saw Elba"))  # Edge case: longer palindrome with punctuation
        self.assertTrue(is_palindrome("Madam, in Eden, I’m Adam"))  # Edge case: mixed case and punctuation
    
    def test_long_non_palindrome(self):
        self.assertFalse(is_palindrome("This is not a palindrome"))  # Edge case: a long non-palindrome
import re
import unittest
import re
from palindrome_check import is_palindrome

class TestPalindromeCheck(unittest.TestCase):
    def test_whitespace_handling(self):
        self.assertTrue(is_palindrome("   A man a plan a canal Panama   "))  # Edge case: leading/trailing spaces

    def test_special_characters(self):
        self.assertTrue(is_palindrome("A! man a plan a canal: Panama!"))  # Edge case: special characters

    def test_numeric_palindrome(self):
        self.assertTrue(is_palindrome("12321"))

    def test_long_string_palindrome(self):
        long_palindrome = "a" * 10000 + "b" + "a" * 10000  # Edge case: very long string
        self.assertFalse(is_palindrome(long_palindrome))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):  # Edge case: non-string input.
            is_palindrome(12345)
        with self.assertRaises(TypeError):
            is_palindrome(None)

    def test_palindrome(self):
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome(""))  # Edge case: empty string

    def test_not_palindrome(self):
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("world"))

    
