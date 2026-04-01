# Reverse an Array Using Recursion

# Problem Statement:
# Given an array, reverse it in-place using recursion.
# Do NOT use any built-in reverse function or extra array.

# Examples:
# Example 1:
#   Input:  [1, 2, 3, 4, 5]
#   Output: [5, 4, 3, 2, 1]

# Example 2:
#   Input:  [1, 2, 3]
#   Output: [3, 2, 1]

# Example 3:
#   Input:  [7]
#   Output: [7]
#   Explanation: single element, stays the same

# Hint: use two pointers — left and right — and swap, then recurse inward


def reverse_array(arr, left, right):
    # write your code here
    pass


# --- Run & Test ---
arr1 = [1, 2, 3, 4, 5]
reverse_array(arr1, 0, len(arr1) - 1)
print(arr1)   # expected: [5, 4, 3, 2, 1]

arr2 = [1, 2, 3]
reverse_array(arr2, 0, len(arr2) - 1)
print(arr2)   # expected: [3, 2, 1]

arr3 = [7]
reverse_array(arr3, 0, len(arr3) - 1)
print(arr3)   # expected: [7]
