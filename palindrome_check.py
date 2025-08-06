def is_palindrome(string):
    string = string.lower().replace("\s+", "")  # Normalize string
    return string == string[::-1]
