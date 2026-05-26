# First and Last Occurrence

# Problem Statement:
# Given a sorted array with possible duplicates, find the first and last position of a given target value.
# If target is not found in the array, return [-1, -1].

# Examples:
# Example 1:
#   Input:  arr = [5, 7, 7, 8, 8, 10], target = 8
#   Output: [3, 4]

# Example 2:
#   Input:  arr = [5, 7, 7, 8, 8, 10], target = 6
#   Output: [-1, -1]

# Example 3:
#   Input:  arr = [2, 2, 2, 2], target = 2
#   Output: [0, 3]

# Difficulty: Medium


def first_last_occurrence(arr, target):
    # Write your code here
    # Hint: Use lower bound to find first occurrence
    # Use upper bound - 1 to find last occurrence
    pass


# --- Run & Test ---
print(first_last_occurrence([5, 7, 7, 8, 8, 10], 8))   # expected: [3, 4]
print(first_last_occurrence([5, 7, 7, 8, 8, 10], 6))   # expected: [-1, -1]
print(first_last_occurrence([2, 2, 2, 2], 2))          # expected: [0, 3]
