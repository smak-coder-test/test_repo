import unittest

class TestPalindromeCheck(unittest.TestCase):

    def test_palindromic_simple_words(self):
        from palindrome_check import is_palindrome
        for word in ["racecar", "level"]:
            with self.subTest(word=word):
                self.assertTrue(is_palindrome(word))

    def test_non_palindromic_words(self):
        from palindrome_check import is_palindrome
        for word in ["hello", "not a palindrome"]:
            with self.subTest(word=word):
                self.assertFalse(is_palindrome(word))

    def test_edge_cases(self):
        from palindrome_check import is_palindrome
        cases_true = [
            "",  # empty string
            "a",  # single character
            "A man, a plan, a canal: Panama",  # punctuation and casing
        ]
        for s in cases_true:
            with self.subTest(value=s):
                self.assertTrue(is_palindrome(s))

if __name__ == '__main__':
    unittest.main()