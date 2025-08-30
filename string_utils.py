"""
String utilities module.

Provides simple helper functions for string operations.
"""

from typing import Any
from collections import Counter


def concat_strings(a: str, b: str) -> str:
    """Concatenate two strings and return the result.

    Args:
        a: First string.
        b: Second string.

    Returns:
        The concatenation of ``a`` and ``b``.
    """

    return a + b


def is_anagram(a: str, b: str) -> bool:
    """Return True if two strings are anagrams of each other.

    Behavior:
    - Case-insensitive using Unicode-aware casefolding.
    - Ignores whitespace and punctuation by considering only alphanumeric characters.
    - Supports Unicode letters and digits via ``str.isalnum()``.

    Examples:
        >>> is_anagram("listen", "silent")
        True
        >>> is_anagram("Dormitory", "Dirty room!!")
        True
        >>> is_anagram("caf\u00e9", "face")
        False

    Args:
        a: First input string.
        b: Second input string.

    Returns:
        True if ``a`` and ``b`` are anagrams under the normalization rules; otherwise False.
    """

    def _normalize(s: str) -> str:
        # Unicode-aware normalization: casefold and keep only alphanumeric characters
        return "".join(ch for ch in s.casefold() if ch.isalnum())

    na = _normalize(a)
    nb = _normalize(b)
    if len(na) != len(nb):
        return False
    return Counter(na) == Counter(nb)
