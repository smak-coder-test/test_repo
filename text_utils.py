"""
Utility text functions.

This module currently provides:
- most_frequent_char: find the most frequent character in a string with
  deterministic tie-breaking.
"""

from __future__ import annotations

from typing import Tuple


def most_frequent_char(s: str) -> Tuple[str, int]:
    """
    Return the most frequent character in the input string and its count.

    Rules:
    - Case-sensitive: "A" and "a" are distinct.
    - Count all characters, including whitespace and punctuation.
    - Tie-breaking: if multiple characters have the same highest frequency,
      return the one whose first occurrence is earliest in the string.
    - Empty input: return ("", 0).

    Examples
    --------
    >>> most_frequent_char("abca")
    ('a', 2)
    >>> most_frequent_char("A aA")
    ('A', 2)
    >>> most_frequent_char("")
    ('', 0)
    """
    if not s:
        return ("", 0)

    counts: dict[str, int] = {}
    first_index: dict[str, int] = {}

    for idx, ch in enumerate(s):
        if ch not in counts:
            counts[ch] = 0
            first_index[ch] = idx
        counts[ch] += 1

    # Determine the best character by (count desc, first_index asc)
    best_char = None
    best_count = -1
    best_first_idx = len(s) + 1

    for ch, cnt in counts.items():
        fi = first_index[ch]
        if cnt > best_count or (cnt == best_count and fi < best_first_idx):
            best_char = ch
            best_count = cnt
            best_first_idx = fi

    # best_char cannot be None here because s is non-empty
    return best_char, best_count
