import unittest

class TestPalindromeCheck(unittest.TestCase):

    def test_is_palindrome(self):
        from palindrome_check import is_palindrome
        self.assertTrue(is_palindrome('racecar'))
        self.assertTrue(is_palindrome('level'))
        self.assertFalse(is_palindrome('hello'))
        # Edge cases
        self.assertTrue(is_palindrome(''))  # empty string
        self.assertTrue(is_palindrome('a'))  # single character
        self.assertTrue(is_palindrome('A man, a plan, a canal: Panama'))  # phrase with punctuation
        self.assertFalse(is_palindrome('not a palindrome'))  # non-palindromic phrase
        self.assertTrue(is_palindrome('racecar'))
        self.assertTrue(is_palindrome('level'))
        self.assertFalse(is_palindrome('hello'))

if __name__ == '__main__':
    unittest.main()