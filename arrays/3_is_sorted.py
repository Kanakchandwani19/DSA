# Check if the Array is Sorted

# Problem Statement:
# Given an array of N integers, check whether the array is sorted
# in non-decreasing order (ascending, duplicates allowed).
# Return True if sorted, False otherwise.

# Examples:
# Example 1:
#   Input:  arr = [1, 2, 3, 4, 5]
#   Output: True

# Example 2:
#   Input:  arr = [1, 2, 2, 4, 5]
#   Output: True
#   Explanation: duplicates are allowed in non-decreasing order

# Example 3:
#   Input:  arr = [5, 4, 3, 2, 1]
#   Output: False

# Example 4:
#   Input:  arr = [1]
#   Output: True
#   Explanation: single element is always sorted


def is_sorted(arr):
    # write your code here
    pass


# --- Run & Test ---
print(is_sorted([1, 2, 3, 4, 5]))   # expected: True
print(is_sorted([1, 2, 2, 4, 5]))   # expected: True
print(is_sorted([5, 4, 3, 2, 1]))   # expected: False
print(is_sorted([1]))               # expected: True
