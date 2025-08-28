import re
def is_palindrome(string):
    import re
    string = re.sub(r'[^a-zA-Z0-9]', '', string.lower())  # Normalize and remove non-alphanumeric characters
    return string == string[::-1]
