def is_palindrome(s):
    return s == s[::-1]

# Example usage
if __name__ == '__main__':
    test_string = 'racecar'
    result = is_palindrome(test_string)
    print(f'Is the string "{test_string}" a palindrome? {result}')