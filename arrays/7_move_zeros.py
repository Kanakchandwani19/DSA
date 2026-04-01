# Move Zeros to End

# Problem Statement:
# Given an array, move all zeros to the end while maintaining the
# relative order of all non-zero elements.
# Do this in-place without using extra space.

# Examples:
# Example 1:
#   Input:  arr = [0, 1, 0, 3, 12]
#   Output: [1, 3, 12, 0, 0]

# Example 2:
#   Input:  arr = [0, 0, 0]
#   Output: [0, 0, 0]

# Example 3:
#   Input:  arr = [1, 2, 3]
#   Output: [1, 2, 3]
#   Explanation: no zeros, nothing changes


def move_zeros(arr):
    # write your code here
    # modify arr in-place
    pass


# --- Run & Test ---
arr1 = [0, 1, 0, 3, 12]
move_zeros(arr1)
print(arr1)   # expected: [1, 3, 12, 0, 0]

arr2 = [0, 0, 0]
move_zeros(arr2)
print(arr2)   # expected: [0, 0, 0]

arr3 = [1, 2, 3]
move_zeros(arr3)
print(arr3)   # expected: [1, 2, 3]
