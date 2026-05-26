# Leaders in an Array

# Problem Statement:
# Given an array, find all the leaders in the array.
# An element is a leader if it is greater than all the elements to its right side.
# The rightmost element is always a leader.

# Examples:
# Example 1:
#   Input:  arr = [16, 17, 4, 3, 5, 2]
#   Output: [17, 5, 2]
#   Explanation: 17 > all elements to its right, 5 > 2, and 2 is the last element

# Example 2:
#   Input:  arr = [1, 2, 3, 4, 0]
#   Output: [4, 0]

# Example 3:
#   Input:  arr = [7, 10, 4, 10, 6, 5, 2]
#   Output: [10, 6, 5, 2]

# Difficulty: Medium


def leaders_in_array(arr):
    # Write your code here
    # Hint: Traverse from right to left, keep track of maximum element seen so far
    pass


# --- Run & Test ---
print(leaders_in_array([16, 17, 4, 3, 5, 2]))     # expected: [17, 5, 2]
print(leaders_in_array([1, 2, 3, 4, 0]))          # expected: [4, 0]
print(leaders_in_array([7, 10, 4, 10, 6, 5, 2]))  # expected: [10, 6, 5, 2]
