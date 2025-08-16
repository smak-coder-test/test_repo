def is_palindrome(string):
    string = string.lower().replace("\s+", "")  # Normalize string
    return string == string[::-1]

def reverse_string(string):
    """Reverses the input string."""
    return string[::-1]