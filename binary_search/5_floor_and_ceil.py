# Floor and Ceil in Sorted Array

# Problem Statement:
# Given a sorted array and a target value:
# - Floor: Largest element in array that is <= target
# - Ceil: Smallest element in array that is >= target
# Return both floor and ceil. If not found, return -1.

# Examples:
# Example 1:
#   Input:  arr = [1, 2, 8, 10, 10, 12, 19], target = 5
#   Output: (2, 8)
#   Explanation: Floor is 2, Ceil is 8

# Example 2:
#   Input:  arr = [1, 2, 8, 10, 10, 12, 19], target = 10
#   Output: (10, 10)

# Example 3:
#   Input:  arr = [1, 2, 8, 10, 10, 12, 19], target = 0
#   Output: (-1, 1)

# Difficulty: Easy


def floor_and_ceil(arr, target):
    # Write your code here
    # Hint: Floor is the largest element <= target
    # Ceil is the smallest element >= target (lower bound)
    pass


# --- Run & Test ---
print(floor_and_ceil([1, 2, 8, 10, 10, 12, 19], 5))   # expected: (2, 8)
print(floor_and_ceil([1, 2, 8, 10, 10, 12, 19], 10))  # expected: (10, 10)
print(floor_and_ceil([1, 2, 8, 10, 10, 12, 19], 0))   # expected: (-1, 1)
