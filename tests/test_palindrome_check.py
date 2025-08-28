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

    def test_palindrome(self):
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome(""))  # Edge case: empty string

    def test_not_palindrome(self):
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("world"))

    
