import unittest

from string_utils import concat_strings


class TestConcatStringsInvalidTypes(unittest.TestCase):
    def test_type_error_on_non_string(self):
        with self.assertRaises(TypeError):
            _ = concat_strings("a", 1)  # type: ignore[arg-type]
        with self.assertRaises(TypeError):
            _ = concat_strings(2, "b")  # type: ignore[arg-type]


if __name__ == "__main__":
    unittest.main()
