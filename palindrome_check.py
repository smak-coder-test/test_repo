import re
def is_palindrome(string):
    import re
    string = string.lower().replace("\s+", "")  # Normalize string
    return string == string[::-1]
