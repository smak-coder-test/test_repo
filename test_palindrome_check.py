import unittest
from palindrome_check import is_palindrome

class TestPalindromeCheck(unittest.TestCase):

    def test_palindrome(self):
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome(""))  # Edge case: empty string

    def test_not_palindrome(self):
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("world"))

if __name__ == '__main__':
    unittest.main()