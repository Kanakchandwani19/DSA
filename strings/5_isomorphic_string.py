# Isomorphic String

# Problem Statement:
# Given two strings s and t, determine if they are isomorphic.
# Two strings are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order.
# No two characters may map to the same character, but a character may map to itself.

# Examples:
# Example 1:
#   Input:  s = "egg", t = "add"
#   Output: True
#   Explanation: e -> a, g -> d

# Example 2:
#   Input:  s = "foo", t = "bar"
#   Output: False
#   Explanation: o cannot map to both a and r

# Example 3:
#   Input:  s = "paper", t = "title"
#   Output: True
#   Explanation: p -> t, a -> i, e -> l, r -> e

# Difficulty: Easy


def isomorphic_string(s, t):
    # Write your code here
    # Hint: Use two hash maps to maintain bidirectional mapping
    # Check if s[i] maps to t[i] and t[i] maps to s[i]
    pass


# --- Run & Test ---
print(isomorphic_string("egg", "add"))       # expected: True
print(isomorphic_string("foo", "bar"))       # expected: False
print(isomorphic_string("paper", "title"))   # expected: True
