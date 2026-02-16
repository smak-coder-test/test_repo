import unittest

from palindrome_check import is_palindrome


class TestPalindromeCheckAdditional(unittest.TestCase):
    def test_numeric_palindromes(self):
        self.assertTrue(is_palindrome("12321"))
        self.assertFalse(is_palindrome("123210"))

    def test_phrase_variation(self):
        self.assertTrue(is_palindrome("No lemon, no melon"))

    def test_unicode_accents_filtered(self):
        # Current implementation filters non-ASCII letters; "réer" -> "rer"
        self.assertTrue(is_palindrome("réer"))

    def test_only_non_alnum(self):
        # Normalizes to empty string -> palindrome
        self.assertTrue(is_palindrome("!!!"))

    def test_unicode_palindromes(self):
        # Unicode-only palindrome characters (non-ASCII letters) are removed by regex -> empty -> True
        self.assertTrue(is_palindrome("あいいあ"))
        # Mixed ASCII + emoji: emoji removed, leaving ASCII palindrome
        self.assertTrue(is_palindrome("a😊a"))


if __name__ == "__main__":
    unittest.main()
