import unittest

from string_utils import concat_strings


class TestConcatStrings(unittest.TestCase):
    def test_basic_concatenation(self):
        self.assertEqual(concat_strings("Hello", "World"), "HelloWorld")
        self.assertEqual(concat_strings("foo", "bar"), "foobar")

    def test_empty_strings(self):
        self.assertEqual(concat_strings("", ""), "")
        self.assertEqual(concat_strings("Hello", ""), "Hello")
        self.assertEqual(concat_strings("", "World"), "World")

    def test_unicode(self):
        self.assertEqual(concat_strings("你好", "世界"), "你好世界")
        self.assertEqual(concat_strings("🙂", "🚀"), "🙂🚀")
        self.assertEqual(concat_strings("café", " au lait"), "café au lait")

    def test_long_strings(self):
        a = "a" * 100_000
        b = "b" * 100_000
        result = concat_strings(a, b)
        self.assertEqual(len(result), len(a) + len(b))
        self.assertTrue(result.startswith(a))
        self.assertTrue(result.endswith(b))


if __name__ == "__main__":
    unittest.main()
