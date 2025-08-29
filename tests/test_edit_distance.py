import unittest

from edit_distance import levenshtein_distance


class TestLevenshteinDistance(unittest.TestCase):
    def test_empty_strings(self):
        self.assertEqual(levenshtein_distance("", ""), 0)

    def test_one_empty(self):
        self.assertEqual(levenshtein_distance("", "abc"), 3)
        self.assertEqual(levenshtein_distance("abc", ""), 3)

    def test_same_strings(self):
        self.assertEqual(levenshtein_distance("a", "a"), 0)
        self.assertEqual(levenshtein_distance("abc", "abc"), 0)

    def test_simple_cases(self):
        self.assertEqual(levenshtein_distance("kitten", "sitting"), 3)
        self.assertEqual(levenshtein_distance("flaw", "lawn"), 2)
        self.assertEqual(levenshtein_distance("gumbo", "gambol"), 2)

    def test_case_sensitivity(self):
        # Function is case-sensitive by default
        self.assertEqual(levenshtein_distance("Apple", "apple"), 1)

    def test_unicode(self):
        self.assertEqual(levenshtein_distance("café", "cafe"), 1)


if __name__ == "__main__":
    unittest.main()
