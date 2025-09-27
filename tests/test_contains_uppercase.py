import unittest

from string_utils import contains_uppercase


class TestContainsUppercase(unittest.TestCase):
    def test_ascii_cases(self):
        self.assertTrue(contains_uppercase("Hello"))
        self.assertFalse(contains_uppercase("hello"))
        self.assertTrue(contains_uppercase("MIXED case"))

    def test_unicode_cases(self):
        self.assertTrue(contains_uppercase("Äpfel"))       # Latin-1 uppercase
        self.assertFalse(contains_uppercase("ж"))          # Cyrillic lowercase
        self.assertTrue(contains_uppercase("Ж"))           # Cyrillic uppercase
        self.assertTrue(contains_uppercase("Ωmega"))       # Greek uppercase
        self.assertFalse(contains_uppercase("μπ"))         # Greek lowercase

    def test_digits_symbols_only(self):
        self.assertFalse(contains_uppercase("123!?-_"))
        self.assertFalse(contains_uppercase("😀🚀"))

    def test_empty_string(self):
        self.assertFalse(contains_uppercase(""))

    def test_invalid_input_types(self):
        with self.assertRaisesRegex(TypeError, "str"):
            contains_uppercase(None)
        with self.assertRaisesRegex(TypeError, "str"):
            contains_uppercase(123)
        with self.assertRaisesRegex(TypeError, "str"):
            contains_uppercase(["A"])  # list
        with self.assertRaisesRegex(TypeError, "str"):
            contains_uppercase(b"A")    # bytes


if __name__ == "__main__":
    unittest.main()
