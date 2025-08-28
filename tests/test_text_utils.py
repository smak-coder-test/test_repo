import unittest


class TestMostFrequentChar(unittest.TestCase):
    def test_typical(self):
        from text_utils import most_frequent_char
        self.assertEqual(most_frequent_char("abca"), ("a", 2))

    def test_single_character(self):
        from text_utils import most_frequent_char
        self.assertEqual(most_frequent_char("x"), ("x", 1))

    def test_repeated_characters(self):
        from text_utils import most_frequent_char
        self.assertEqual(most_frequent_char("zzzz"), ("z", 4))

    def test_whitespace_included(self):
        from text_utils import most_frequent_char
        # Two spaces and one 'a' => space should win
        self.assertEqual(most_frequent_char("  a"), (" ", 2))

    def test_punctuation_included(self):
        from text_utils import most_frequent_char
        self.assertEqual(most_frequent_char("!!?!"), ("!", 3))

    def test_unicode_handling(self):
        from text_utils import most_frequent_char
        self.assertEqual(most_frequent_char("😀😃😃😀😀"), ("😀", 3))

    def test_tie_breaker_earliest_first_occurrence(self):
        from text_utils import most_frequent_char
        # 'a' and 'b' both occur twice; 'a' first appears at index 0 in "abba"
        self.assertEqual(most_frequent_char("abba"), ("a", 2))
        # In "baba", both occur twice; 'b' first appears at index 0
        self.assertEqual(most_frequent_char("baba"), ("b", 2))

    def test_case_sensitive(self):
        from text_utils import most_frequent_char
        # 'A' (2) vs 'a' (1)
        self.assertEqual(most_frequent_char("A aA"), ("A", 2))

    def test_empty_input(self):
        from text_utils import most_frequent_char
        self.assertEqual(most_frequent_char(""), ("", 0))


if __name__ == "__main__":
    unittest.main()
