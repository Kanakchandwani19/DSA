# Longest Subarray with Given Sum K (Positives Only)

# Problem Statement:
# Given an array of positive integers and a target sum K,
# find the length of the longest contiguous subarray whose sum equals K.
# Return 0 if no such subarray exists.

# Examples:
# Example 1:
#   Input:  arr = [1, 2, 3, 1, 1, 1], K = 3
#   Output: 3
#   Explanation: subarray [1, 1, 1] has sum 3 and length 3

# Example 2:
#   Input:  arr = [1, 2, 3, 4, 5], K = 9
#   Output: 3
#   Explanation: subarray [2, 3, 4] has sum 9 and length 3

# Example 3:
#   Input:  arr = [5, 5, 5], K = 10
#   Output: 2
#   Explanation: subarray [5, 5] has sum 10

# Example 4:
#   Input:  arr = [1, 2, 3], K = 100
#   Output: 0

# Hint: use sliding window — expand right pointer, shrink left when sum > K


def longest_subarray_sum_k(arr, k):
    # write your code here
    pass


# --- Run & Test ---
print(longest_subarray_sum_k([1, 2, 3, 1, 1, 1], 3))   # expected: 3
print(longest_subarray_sum_k([1, 2, 3, 4, 5], 9))       # expected: 3
print(longest_subarray_sum_k([5, 5, 5], 10))             # expected: 2
print(longest_subarray_sum_k([1, 2, 3], 100))            # expected: 0
