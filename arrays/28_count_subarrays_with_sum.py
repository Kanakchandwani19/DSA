# Count subarrays with given sum

# Problem Statement:
# Given an array of integers and a target sum, count the number of non-empty subarrays
# that have sum equal to target.

# Examples:
# Example 1:
#   Input:  arr = [1, 1, 1], target = 2
#   Output: 2
#   Explanation: Subarrays are [1,1] and [1,1]

# Example 2:
#   Input:  arr = [1, 2, 3], target = 3
#   Output: 2
#   Explanation: Subarrays are [1,2] and [3]

# Example 3:
#   Input:  arr = [1, -1, 0], target = 0
#   Output: 3
#   Explanation: Subarrays are [1,-1], [0] and [1,-1,0]

# Difficulty: Medium


def count_subarrays_with_sum(arr, target):
    # Write your code here
    # Hint: Use prefix sum and hashmap
    # If (prefix_sum - target) exists in hashmap, add its count to result
    pass


# --- Run & Test ---
print(count_subarrays_with_sum([1, 1, 1], 2))       # expected: 2
print(count_subarrays_with_sum([1, 2, 3], 3))       # expected: 2
print(count_subarrays_with_sum([1, -1, 0], 0))      # expected: 3
