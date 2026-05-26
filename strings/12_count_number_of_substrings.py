# Count Number of Substrings

# Problem Statement:
# Given a string s and an integer k, return the number of substrings that contain exactly k distinct characters.

# Examples:
# Example 1:
#   Input:  s = "aba", k = 2
#   Output: 3
#   Explanation: Substrings are "ab", "ba", "aba"

# Example 2:
#   Input:  s = "abaaca", k = 1
#   Output: 7
#   Explanation: Substrings are "a", "b", "a", "aa", "a", "c", "a"

# Example 3:
#   Input:  s = "abc", k = 2
#   Output: 2
#   Explanation: Substrings are "ab", "bc"

# Difficulty: Easy


def count_substrings_with_k_distinct(s, k):
    # Write your code here
    # Hint: Use sliding window technique
    # Count substrings with at most k distinct - count substrings with at most (k-1) distinct
    pass


# --- Run & Test ---
print(count_substrings_with_k_distinct("aba", 2))      # expected: 3
print(count_substrings_with_k_distinct("abaaca", 1))   # expected: 7
print(count_substrings_with_k_distinct("abc", 2))      # expected: 2
