import unittest

from palindrome_check import is_palindrome
import re

class TestPalindromeCheck(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
        self.assertFalse(is_palindrome("not a palindrome"))

if __name__ == '__main__':
    unittest.main()