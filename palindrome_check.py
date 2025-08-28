import re
def is_palindrome(string):
    import re
    normalized = re.sub(r'[^a-zA-Z0-9]', '', string.lower())  # Normalize and remove non-alphanumeric characters
    return normalized == normalized[::-1]
    return string == string[::-1]
