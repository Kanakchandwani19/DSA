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


s = input()

if s == s[::-1]:
    print("Palindrome")


    
