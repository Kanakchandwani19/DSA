# Count Occurrences in Sorted Array

# Problem Statement:
# Given a sorted array and a target value, count the number of times the target appears in the array.

# Examples:
# Example 1:
#   Input:  arr = [2, 2, 3, 3, 3, 3, 4], target = 3
#   Output: 4

# Example 2:
#   Input:  arr = [2, 2, 3, 3, 3, 3, 4], target = 5
#   Output: 0

# Example 3:
#   Input:  arr = [1, 1, 1, 1, 1], target = 1
#   Output: 5

# Difficulty: Easy


def count_occurrences(arr, target):
    # Write your code here
    # Hint: Count = (last occurrence - first occurrence + 1)
    # Use first and last occurrence logic
    pass


# --- Run & Test ---
print(count_occurrences([2, 2, 3, 3, 3, 3, 4], 3))   # expected: 4
print(count_occurrences([2, 2, 3, 3, 3, 3, 4], 5))   # expected: 0
print(count_occurrences([1, 1, 1, 1, 1], 1))         # expected: 5
