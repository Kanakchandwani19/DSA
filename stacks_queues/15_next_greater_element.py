# Next Greater Element

# Problem Statement:
# Given an array, for each element find the next greater element in the array.
# The next greater element for an element x is the first greater element on the right side of x.
# If no greater element exists, return -1 for that element.

# Examples:
# Example 1:
#   Input:  arr = [4, 5, 2, 25]
#   Output: [5, 25, 25, -1]
#   Explanation: For 4, next greater is 5. For 5, it's 25. For 2, it's 25. For 25, none exists.

# Example 2:
#   Input:  arr = [13, 7, 6, 12]
#   Output: [-1, 12, 12, -1]

# Example 3:
#   Input:  arr = [1, 3, 2, 4]
#   Output: [3, 4, 4, -1]

# Difficulty: Medium


def next_greater_element(arr):
    # Write your code here
    # Hint: Use a stack, traverse from right to left
    # Pop elements from stack that are smaller than current element
    # Top of stack is the next greater element
    pass


# --- Run & Test ---
print(next_greater_element([4, 5, 2, 25]))    # expected: [5, 25, 25, -1]
print(next_greater_element([13, 7, 6, 12]))   # expected: [-1, 12, 12, -1]
print(next_greater_element([1, 3, 2, 4]))     # expected: [3, 4, 4, -1]
