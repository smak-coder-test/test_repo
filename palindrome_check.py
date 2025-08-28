import re
def is_palindrome(string):
    import re
    string = string.lower().replace("\s+", "")  # Normalize string
    string = re.sub(r'[\W_]+', '', string).lower()  # Normalize string
    return string == string[::-1]
