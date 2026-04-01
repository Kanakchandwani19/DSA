# Check if String is Palindrome or Not (Using Recursion)

# Problem Statement:
# Given a string S, check whether it is a palindrome using recursion.
# A string is a palindrome if it reads the same forwards and backwards.
# Do NOT use any built-in reverse or slicing trick — solve it recursively.

# Examples:
# Example 1:
#   Input:  S = "racecar"
#   Output: True

# Example 2:
#   Input:  S = "madam"
#   Output: True

# Example 3:
#   Input:  S = "hello"
#   Output: False
#   Explanation: "hello" reversed is "olleh" — different

# Example 4:
#   Input:  S = "a"
#   Output: True
#   Explanation: single character is always a palindrome

# Hint: compare first and last characters, then recurse on the inner substring


def is_palindrome(s, left, right):
    # write your code here
    pass


# --- Run & Test ---
s1 = "racecar"
print(is_palindrome(s1, 0, len(s1) - 1))   # expected: True

s2 = "madam"
print(is_palindrome(s2, 0, len(s2) - 1))   # expected: True

s3 = "hello"
print(is_palindrome(s3, 0, len(s3) - 1))   # expected: False

s4 = "a"
print(is_palindrome(s4, 0, len(s4) - 1))   # expected: True
