import unittest

class TestPalindromeCheck(unittest.TestCase):

    def test_is_palindrome(self):
        from palindrome_check import is_palindrome

    def test_single_character(self):
        self.assertTrue(is_palindrome('a'))

    def test_empty_string(self):
        self.assertTrue(is_palindrome(''))

    def test_numerical_palindrome(self):
        self.assertTrue(is_palindrome('12021'))

    def test_phrase_palindrome(self):
        self.assertTrue(is_palindrome('A man, a plan, a canal: Panama'))

    def test_palindrome_with_special_characters(self):
        self.assertTrue(is_palindrome('No 'x' in Nixon'))

    def test_non_palindrome(self):
        self.assertFalse(is_palindrome('This is not a palindrome'))
        self.assertTrue(is_palindrome('racecar'))
        self.assertTrue(is_palindrome('level'))
        self.assertFalse(is_palindrome('hello'))
        self.assertTrue(is_palindrome('racecar'))
        self.assertTrue(is_palindrome('level'))
        self.assertFalse(is_palindrome('hello'))

if __name__ == '__main__':
    unittest.main()