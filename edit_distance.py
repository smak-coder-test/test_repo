from typing import List


def levenshtein_distance(s1: str, s2: str) -> int:
    """
    Compute the Levenshtein edit distance between two strings.

    The Levenshtein distance is the minimum number of single-character edits
    (insertions, deletions, or substitutions) required to change one string
    into the other.

    This implementation uses a dynamic programming approach with O(min(m, n))
    space, where m = len(s1) and n = len(s2).

    Args:
        s1: First input string.
        s2: Second input string.

    Returns:
        The Levenshtein distance between s1 and s2.
    """

    # Ensure the first string is the shorter one to keep memory usage minimal
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    m, n = len(s1), len(s2)

    # If one string is empty, distance is the length of the other
    if m == 0:
        return n

    # previous row of costs; transforming s1[:i] to empty string requires i deletions
    previous: List[int] = list(range(m + 1))

    for j in range(1, n + 1):
        current: List[int] = [j] + [0] * m
        cj = s2[j - 1]
        for i in range(1, m + 1):
            ci = s1[i - 1]
            if ci == cj:
                cost = 0
            else:
                cost = 1

            deletion = previous[i] + 1       # delete from s1
            insertion = current[i - 1] + 1   # insert into s1
            substitution = previous[i - 1] + cost

            current[i] = min(deletion, insertion, substitution)

        previous = current

    return previous[m]
