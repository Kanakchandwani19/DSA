# Left Rotate Array by One

# Problem Statement:
# Given an array of N elements, rotate it to the left by one position.
# The first element moves to the end.

# Examples:
# Example 1:
#   Input:  arr = [1, 2, 3, 4, 5]
#   Output: [2, 3, 4, 5, 1]

# Example 2:
#   Input:  arr = [3]
#   Output: [3]
#   Explanation: single element, no change

# Example 3:
#   Input:  arr = [5, 10, 15]
#   Output: [10, 15, 5]


def left_rotate_by_one(arr):
    # write your code here
    # modify arr in-place
    pass


# --- Run & Test ---
arr1 = [1, 2, 3, 4, 5]
left_rotate_by_one(arr1)
print(arr1)   # expected: [2, 3, 4, 5, 1]

arr2 = [3]
left_rotate_by_one(arr2)
print(arr2)   # expected: [3]

arr3 = [5, 10, 15]
left_rotate_by_one(arr3)
print(arr3)   # expected: [10, 15, 5]
