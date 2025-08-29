"""
Utility text functions.

This module currently provides:
- most_frequent_char: find the most frequent character in a string with
  deterministic tie-breaking.
- edit_distance: compute the Levenshtein (unit-cost) edit distance between two strings.
"""
from __future__ import annotations

from typing import Tuple


def edit_distance(a: str, b: str) -> int:
    """
    Compute the Levenshtein edit distance between two strings.

    Definition:
    - Allowed operations are insertion, deletion, and substitution.
    - Each operation has a unit cost of 1.
    - The function is case-sensitive and works with arbitrary Unicode characters.

    Parameters
    ----------
    a : str
        First input string.
    b : str
        Second input string.

    Returns
    -------
    int
        The minimal number of single-character edits required to transform
        string `a` into string `b`.

    Examples
    --------
    >>> edit_distance("kitten", "sitting")
    3
    >>> edit_distance("", "abc")
    3
    >>> edit_distance("abc", "abc")
    0
    """
    # Quick responses for trivial cases
    if a == b:
        return 0
    if not a:
        return len(b)
    if not b:
        return len(a)

    # Use a classic dynamic programming approach with O(min(len(a), len(b))) space
    # Work on the shorter string horizontally to reduce memory
    if len(b) < len(a):
        a, b = b, a

    # prev[j] is the edit distance between a[:i-1] and b[:j]
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, start=1):
        curr = [i]
        for j, cb in enumerate(b, start=1):
            cost = 0 if ca == cb else 1
            insertion = curr[j - 1] + 1
            deletion = prev[j] + 1
            substitution = prev[j - 1] + cost
            curr.append(min(insertion, deletion, substitution))
        prev = curr
    return prev[-1]
 


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
