# Kadane's Algorithm - Maximum Subarray Sum

# Problem Statement:
# Given an array of integers, find the contiguous subarray with the largest sum.
# Return the sum of that subarray.

# Examples:
# Example 1:
#   Input:  arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
#   Output: 6
#   Explanation: [4, -1, 2, 1] has the largest sum = 6

# Example 2:
#   Input:  arr = [1]
#   Output: 1

# Example 3:
#   Input:  arr = [5, 4, -1, 7, 8]
#   Output: 23

# Difficulty: Medium


def kadanes_algorithm(arr):
    # Write your code here
    # Hint: Keep track of current sum and maximum sum
    # If current sum becomes negative, reset it to 0
    pass


# --- Run & Test ---
print(kadanes_algorithm([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # expected: 6
print(kadanes_algorithm([1]))                               # expected: 1
print(kadanes_algorithm([5, 4, -1, 7, 8]))                  # expected: 23
