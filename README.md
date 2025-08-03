# Initial Commit
This is the first commit in the repository.

## Palindrome Checker Script

This script checks if a given string is a palindrome:

```python
def is_palindrome(string):
    # Clean the string by removing spaces and converting it to lowercase.
    cleaned = ''.join(string.split()).lower()
    return cleaned == cleaned[::-1]

# Example usage:
if __name__ == '__main__':
    test_string = 'A man, a plan, a canal, Panama'
    print(f'Is the string a palindrome? {is_palindrome(test_string)}')
```
