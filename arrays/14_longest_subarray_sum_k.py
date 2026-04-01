# Longest Subarray with Sum K (Positives and Negatives)

# Problem Statement:
# Given an array that may contain positive numbers, negative numbers, and zeros,
# find the length of the longest contiguous subarray whose sum equals K.
# Return 0 if no such subarray exists.

# Examples:
# Example 1:
#   Input:  arr = [1, -1, 5, -2, 3], K = 3
#   Output: 4
#   Explanation: subarray [1, -1, 5, -2] has sum 3 and length 4

# Example 2:
#   Input:  arr = [-2, -1, 2, 1], K = 1
#   Output: 2
#   Explanation: subarray [2, -1] or [-1, 2] each has sum 1, length 2

# Example 3:
#   Input:  arr = [1, 2, 3], K = 6
#   Output: 3
#   Explanation: entire array sums to 6

# Example 4:
#   Input:  arr = [1, 2, 3], K = 10
#   Output: 0

# Hint: use prefix sum + hashmap
#       if prefix_sum - K exists in the map, a subarray with sum K was found


def longest_subarray_sum_k(arr, k):
    # write your code here
    pass


# --- Run & Test ---
print(longest_subarray_sum_k([1, -1, 5, -2, 3], 3))   # expected: 4
print(longest_subarray_sum_k([-2, -1, 2, 1], 1))       # expected: 2
print(longest_subarray_sum_k([1, 2, 3], 6))             # expected: 3
print(longest_subarray_sum_k([1, 2, 3], 10))            # expected: 0
