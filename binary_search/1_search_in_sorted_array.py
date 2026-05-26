# Search X in sorted array

# Problem Statement:
# Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return -1. You must write an algorithm with O(log n) runtime complexity.

# Examples:
# Example 1:
#   Input:  arr = [-1, 0, 3, 5, 9, 12], target = 9
#   Output: 4

# Example 2:
#   Input:  arr = [-1, 0, 3, 5, 9, 12], target = 2
#   Output: -1

# Example 3:
#   Input:  arr = [5], target = 5
#   Output: 0

# Difficulty: Easy


def binary_search(arr, target):
    # Write your code here
    # Hint: Use two pointers left and right
    # Calculate mid = (left + right) // 2
    # If arr[mid] == target, return mid
    # If arr[mid] < target, search right half
    # If arr[mid] > target, search left half
    pass


# --- Run & Test ---
print(binary_search([-1, 0, 3, 5, 9, 12], 9))   # expected: 4
print(binary_search([-1, 0, 3, 5, 9, 12], 2))   # expected: -1
print(binary_search([5], 5))                     # expected: 0
