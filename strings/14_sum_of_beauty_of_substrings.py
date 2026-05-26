# Sum of Beauty of All Substrings

# Problem Statement:
# The beauty of a string is the difference in frequencies between the most frequent and least frequent characters.
# - For example, the beauty of "abaacc" is 3 - 1 = 2.
# Given a string s, return the sum of beauty of all of its substrings.

# Examples:
# Example 1:
#   Input:  s = "aabcb"
#   Output: 5
#   Explanation:
#   "aab" -> beauty = 2 - 1 = 1
#   "aabc" -> beauty = 2 - 1 = 1
#   "aabcb" -> beauty = 2 - 1 = 1
#   "abcb" -> beauty = 1 - 1 = 0
#   "bcb" -> beauty = 2 - 1 = 1
#   "cb" -> beauty = 1 - 1 = 0
#   "aab", "abc", "bcb" contribute. Total = 1 + 1 + 1 + 1 + 1 = 5

# Example 2:
#   Input:  s = "aabcbaa"
#   Output: 17

# Difficulty: Medium


def sum_of_beauty(s):
    # Write your code here
    # Hint: For each starting position, extend the substring one character at a time
    # Maintain frequency map and calculate beauty for each substring
    # Only consider substrings with length >= 3 (need at least 2 different chars for beauty > 0)
    pass


# --- Run & Test ---
print(sum_of_beauty("aabcb"))      # expected: 5
print(sum_of_beauty("aabcbaa"))    # expected: 17
