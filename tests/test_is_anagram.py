import unittest

from string_utils import is_anagram


class TestIsAnagram(unittest.TestCase):
    def test_basic_true_cases(self):
        self.assertTrue(is_anagram("listen", "silent"))
        self.assertTrue(is_anagram("evil", "vile"))
        self.assertTrue(is_anagram("the eyes", "they see"))

    def test_case_and_whitespace_ignored(self):
        self.assertTrue(is_anagram("Dormitory", "Dirty room!!"))
        self.assertTrue(is_anagram("Conversation", "Voices rant on"))

    def test_numbers_supported(self):
        self.assertTrue(is_anagram("123", "321"))
        self.assertFalse(is_anagram("1123", "321"))

    def test_unicode_letters(self):
        # Unicode-aware: diacritics are preserved under casefold; not equivalent to ASCII 'e'
        self.assertFalse(is_anagram("caf\u00e9", "face"))
        # But rearrangements of the same Unicode letters should match
        self.assertTrue(is_anagram("b\u00e0", "\u00e0b"))

    def test_cyrillic(self):
        # "сон" and "нос" are anagrams in Cyrillic when normalized
        self.assertTrue(is_anagram("Сон", "Нос"))

    def test_different_lengths(self):
        self.assertFalse(is_anagram("ab", "abc"))
        self.assertFalse(is_anagram("abc", "ab"))

    def test_negative_cases(self):
        self.assertFalse(is_anagram("rat", "car"))

    def test_only_non_alphanumerics(self):
        # After normalization both become empty; treat as anagrams
        self.assertTrue(is_anagram("!!!", "   "))


if __name__ == "__main__":
    unittest.main()
