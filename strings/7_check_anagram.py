# Check if two strings are anagram of each other

# Problem Statement:
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

# Examples:
# Example 1:
#   Input:  s = "anagram", t = "nagaram"
#   Output: True

# Example 2:
#   Input:  s = "rat", t = "car"
#   Output: False

# Example 3:
#   Input:  s = "listen", t = "silent"
#   Output: True

# Difficulty: Easy


def check_anagram(s, t):
    # Write your code here
    # Hint: Sort both strings and compare, or use a hash map to count characters
    pass


# --- Run & Test ---
print(check_anagram("anagram", "nagaram"))   # expected: True
print(check_anagram("rat", "car"))           # expected: False
print(check_anagram("listen", "silent"))     # expected: True
