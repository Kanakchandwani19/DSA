# Search in Rotated Sorted Array - I

# Problem Statement:
# There is an integer array nums sorted in ascending order (with distinct values).
# The array is rotated at an unknown pivot index.
# Given the array after rotation and a target value, return the index of target if it is in the array, otherwise return -1.
# You must write an algorithm with O(log n) runtime complexity.

# Examples:
# Example 1:
#   Input:  arr = [4, 5, 6, 7, 0, 1, 2], target = 0
#   Output: 4

# Example 2:
#   Input:  arr = [4, 5, 6, 7, 0, 1, 2], target = 3
#   Output: -1

# Example 3:
#   Input:  arr = [1], target = 0
#   Output: -1

# Difficulty: Medium


def search_rotated_array_1(arr, target):
    # Write your code here
    # Hint: Identify which half is sorted (left or right)
    # If arr[left] <= arr[mid], left half is sorted
    # Check if target lies in sorted half, else search other half
    pass


# --- Run & Test ---
print(search_rotated_array_1([4, 5, 6, 7, 0, 1, 2], 0))   # expected: 4
print(search_rotated_array_1([4, 5, 6, 7, 0, 1, 2], 3))   # expected: -1
print(search_rotated_array_1([1], 0))                     # expected: -1
