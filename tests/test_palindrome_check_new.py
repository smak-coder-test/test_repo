import unittest

class TestPalindromeCheck(unittest.TestCase):

    def test_is_palindrome(self):
        from palindrome_check import is_palindrome
        self.assertTrue(is_palindrome('racecar'))
        self.assertTrue(is_palindrome('level'))
        self.assertFalse(is_palindrome('hello'))
        self.assertTrue(is_palindrome('racecar'))
        self.assertTrue(is_palindrome('level'))
        self.assertFalse(is_palindrome('hello'))

if __name__ == '__main__':
    unittest.main()