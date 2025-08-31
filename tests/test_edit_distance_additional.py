import unittest

from edit_distance import levenshtein_distance


class TestLevenshteinDistanceAdditional(unittest.TestCase):
    def test_commutativity(self):
        pairs = [
            ("abc", "yabd"),
            ("kitten", "sitting"),
            ("", "longer"),
            ("abcd", "abxcd"),
        ]
        for a, b in pairs:
            with self.subTest(a=a, b=b):
                self.assertEqual(levenshtein_distance(a, b), levenshtein_distance(b, a))

    def test_repeat_characters_all_substitutions(self):
        self.assertEqual(levenshtein_distance("aaaa", "bbbb"), 4)

    def test_single_middle_change_long_string(self):
        a = "a" * 1000
        # Change one middle character
        b = a[:500] + "b" + a[501:]
        self.assertEqual(levenshtein_distance(a, b), 1)

    def test_unicode_emoji(self):
        # Different single-codepoint emoji should count as one substitution
        self.assertEqual(levenshtein_distance("😀", "😃"), 1)
        # One differing emoji among two
        self.assertEqual(levenshtein_distance("😀😀", "😀😃"), 1)


if __name__ == "__main__":
    unittest.main()
