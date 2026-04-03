# Palindrome Number

# Problem Statement:
# Given a number N, check whether it is a palindrome.
# A number is a palindrome if it reads the same forwards and backwards.

# Examples:
# Example 1:
#   Input:  N = 121
#   Output: True
#   Explanation: 121 reversed is 121 — same

# Example 2:
#   Input:  N = 1331
#   Output: True

# Example 3:
#   Input:  N = 1234
#   Output: False
#   Explanation: 1234 reversed is 4321 — different

# Example 4:
#   Input:  N = -121
#   Output: False
#   Explanation: negative numbers are not palindromes


def is_palindrome(n):
   if n<0:
      return False
   s = str(n) 
   rev = s[::-1]
   return s == rev



print(is_palindrome(121))    # expected: True
print(is_palindrome(1331))   # expected: True
print(is_palindrome(1234))   # expected: False
print(is_palindrome(-121))   # expected: False
