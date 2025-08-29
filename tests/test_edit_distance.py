import unittest


class TestEditDistance(unittest.TestCase):
    def test_empty_strings(self):
        from text_utils import edit_distance
        self.assertEqual(edit_distance("", ""), 0)

    def test_empty_and_nonempty(self):
        from text_utils import edit_distance
        self.assertEqual(edit_distance("", "abc"), 3)
        self.assertEqual(edit_distance("abc", ""), 3)

    def test_identical_strings(self):
        from text_utils import edit_distance
        self.assertEqual(edit_distance("abc", "abc"), 0)

    def test_substitution(self):
        from text_utils import edit_distance
        self.assertEqual(edit_distance("abc", "axc"), 1)

    def test_insertion(self):
        from text_utils import edit_distance
        self.assertEqual(edit_distance("abc", "abxc"), 1)

    def test_deletion(self):
        from text_utils import edit_distance
        self.assertEqual(edit_distance("abxc", "abc"), 1)

    def test_mixed_operations(self):
        from text_utils import edit_distance
        # classic example
        self.assertEqual(edit_distance("kitten", "sitting"), 3)
        # another known pair
        self.assertEqual(edit_distance("flaw", "lawn"), 2)

    def test_unicode(self):
        from text_utils import edit_distance
        self.assertEqual(edit_distance("😀", "😃"), 1)
        self.assertEqual(edit_distance("café", "cafe"), 1)
        self.assertEqual(edit_distance("mañana", "manana"), 1)

    def test_asymmetric_lengths(self):
        from text_utils import edit_distance
        self.assertEqual(edit_distance("a", "aaaaa"), 4)
        self.assertEqual(edit_distance("aaaaa", "a"), 4)


if __name__ == "__main__":
    unittest.main()
