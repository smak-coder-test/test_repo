# Palindrome Checker

# Function to check if a string is a palindrome
def is_palindrome(s):
    return s == s[::-1]

# Example usage
if __name__ == "__main__":
    input_string = "racecar"  # Example input
    if is_palindrome(input_string):
        print(f'\'{input_string}\' is a palindrome!')
    else:
        print(f'\'{input_string}\' is not a palindrome.')
