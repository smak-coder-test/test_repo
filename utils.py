def is_palindrome(s):
    """
    Check if the input string is a palindrome.
    A palindrome is a word, phrase, number, or other sequence of characters
    which reads the same backward as forward.
    """
    return s == s[::-1]