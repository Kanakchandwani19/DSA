# Longest Palindromic Substring

# Problem Statement:
# Given a string s, return the longest palindromic substring in s.
# A palindrome is a string that reads the same backward as forward.

# Examples:
# Example 1:
#   Input:  s = "babad"
#   Output: "bab" or "aba"

# Example 2:
#   Input:  s = "cbbd"
#   Output: "bb"

# Example 3:
#   Input:  s = "a"
#   Output: "a"

# Difficulty: Medium


def longest_palindromic_substring(s):
    # Write your code here
    # Hint: Expand around center approach
    # For each position, expand outward while characters match
    # Consider both odd-length (center is one char) and even-length (center is between two chars)
    pass


# --- Run & Test ---
print(longest_palindromic_substring("babad"))    # expected: "bab" or "aba"
print(longest_palindromic_substring("cbbd"))     # expected: "bb"
print(longest_palindromic_substring("a"))        # expected: "a"
