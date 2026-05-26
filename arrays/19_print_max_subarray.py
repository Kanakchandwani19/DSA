# Print subarray with maximum subarray sum (Extended Kadane's)

# Problem Statement:
# Given an array of integers, find the contiguous subarray with the largest sum.
# Print the start and end indices of that subarray along with the sum.

# Examples:
# Example 1:
#   Input:  arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
#   Output: Subarray: [4, -1, 2, 1], Sum: 6

# Example 2:
#   Input:  arr = [1]
#   Output: Subarray: [1], Sum: 1

# Example 3:
#   Input:  arr = [5, 4, -1, 7, 8]
#   Output: Subarray: [5, 4, -1, 7, 8], Sum: 23

# Difficulty: Medium


def print_max_subarray(arr):
    # Write your code here
    # Hint: Extension of Kadane's algorithm
    # Keep track of start and end indices along with current and max sum
    pass


# --- Run & Test ---
print_max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# expected: Subarray: [4, -1, 2, 1], Sum: 6

print_max_subarray([1])
# expected: Subarray: [1], Sum: 1

print_max_subarray([5, 4, -1, 7, 8])
# expected: Subarray: [5, 4, -1, 7, 8], Sum: 23
