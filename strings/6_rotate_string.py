# Rotate String

# Problem Statement:
# Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
# A shift on s consists of moving the leftmost character of s to the rightmost position.
# For example, if s = "abcde", then it will be "bcdea" after one shift.

# Examples:
# Example 1:
#   Input:  s = "abcde", goal = "cdeab"
#   Output: True

# Example 2:
#   Input:  s = "abcde", goal = "abced"
#   Output: False

# Example 3:
#   Input:  s = "aa", goal = "a"
#   Output: False

# Difficulty: Easy


def rotate_string(s, goal):
    # Write your code here
    # Hint: If goal is a rotation of s, then goal will be a substring of s + s
    # Example: s = "abcde", s + s = "abcdeabcde", goal = "cdeab" is in s + s
    pass


# --- Run & Test ---
print(rotate_string("abcde", "cdeab"))   # expected: True
print(rotate_string("abcde", "abced"))   # expected: False
print(rotate_string("aa", "a"))          # expected: False
