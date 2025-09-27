"""
String utilities module.

Provides simple helper functions for string operations.
"""

from typing import Any


def concat_strings(a: str, b: str) -> str:
    """Concatenate two strings and return the result.

    Args:
        a: First string.
        b: Second string.

    Returns:
        The concatenation of ``a`` and ``b``.
    """

    return a + b


def contains_uppercase(s: str) -> bool:
    """Check whether the given string contains any uppercase letters.

    Unicode-aware: uses ``str.isupper()`` on each character, which correctly
    recognizes uppercase letters beyond ASCII (e.g., 'Ä', 'Ж', 'Ω').

    Args:
        s: Input to check.

    Returns:
        True if any character in ``s`` is uppercase, otherwise False.

    Raises:
        TypeError: If ``s`` is not a ``str``.

    Examples:
        >>> contains_uppercase('Hello')
        True
        >>> contains_uppercase('hello')
        False
        >>> contains_uppercase('Äpfel')
        True
        >>> contains_uppercase('123!?')
        False
    """

    if not isinstance(s, str):
        raise TypeError(f"contains_uppercase expected str, got {type(s).__name__}")

    return any(ch.isupper() for ch in s)
