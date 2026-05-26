# Next Permutation

# Problem Statement:
# Given an array of integers, find the next lexicographically greater permutation.
# If such arrangement is not possible, rearrange it to the lowest possible order (sorted in ascending order).
# The replacement must be in-place and use only constant extra memory.

# Examples:
# Example 1:
#   Input:  arr = [1, 2, 3]
#   Output: [1, 3, 2]

# Example 2:
#   Input:  arr = [3, 2, 1]
#   Output: [1, 2, 3]

# Example 3:
#   Input:  arr = [1, 1, 5]
#   Output: [1, 5, 1]

# Difficulty: Medium


def next_permutation(arr):
    # Write your code here
    # Hint:
    # 1. Find the break point (index where arr[i] < arr[i+1]) from right to left
    # 2. Find the smallest element greater than arr[break_point] from right
    # 3. Swap them
    # 4. Reverse the elements after break_point
    pass


# --- Run & Test ---
arr1 = [1, 2, 3]
next_permutation(arr1)
print(arr1)  # expected: [1, 3, 2]

arr2 = [3, 2, 1]
next_permutation(arr2)
print(arr2)  # expected: [1, 2, 3]

arr3 = [1, 1, 5]
next_permutation(arr3)
print(arr3)  # expected: [1, 5, 1]
