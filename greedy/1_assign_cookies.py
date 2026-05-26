# Assign Cookies

# Problem Statement:
# You are given two arrays:
# - greed[i]: minimum size of cookie that the ith child will be content with
# - size[j]: size of jth cookie
# Each child can receive at most one cookie.
# Find the maximum number of children you can make content.

# Examples:
# Example 1:
#   Input:  greed = [1, 2, 3], size = [1, 1]
#   Output: 1
#   Explanation: You can satisfy only one child (the one with greed 1)

# Example 2:
#   Input:  greed = [1, 2], size = [1, 2, 3]
#   Output: 2
#   Explanation: You can satisfy both children

# Example 3:
#   Input:  greed = [1, 2, 3], size = [3]
#   Output: 1

# Difficulty: Easy


def assign_cookies(greed, size):
    # Write your code here
    # Hint: Sort both arrays
    # Use two pointers to match smallest cookie to smallest greed
    pass


# --- Run & Test ---
print(assign_cookies([1, 2, 3], [1, 1]))      # expected: 1
print(assign_cookies([1, 2], [1, 2, 3]))      # expected: 2
print(assign_cookies([1, 2, 3], [3]))         # expected: 1
