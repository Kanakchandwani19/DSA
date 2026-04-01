# Union of Two Sorted Arrays

# Problem Statement:
# Given two sorted arrays, return their union as a sorted array
# containing each element only once (no duplicates).

# Examples:
# Example 1:
#   Input:  a = [1, 2, 3, 4, 5], b = [1, 2, 7]
#   Output: [1, 2, 3, 4, 5, 7]

# Example 2:
#   Input:  a = [1, 1, 2], b = [2, 3]
#   Output: [1, 2, 3]

# Example 3:
#   Input:  a = [1, 3, 5], b = [2, 4, 6]
#   Output: [1, 2, 3, 4, 5, 6]

# Hint: use two pointers — compare elements from both arrays,
#       always pick the smaller one, skip duplicates


def union_sorted(a, b):
    # write your code here
    pass


# --- Run & Test ---
print(union_sorted([1, 2, 3, 4, 5], [1, 2, 7]))   # expected: [1, 2, 3, 4, 5, 7]
print(union_sorted([1, 1, 2], [2, 3]))              # expected: [1, 2, 3]
print(union_sorted([1, 3, 5], [2, 4, 6]))           # expected: [1, 2, 3, 4, 5, 6]
