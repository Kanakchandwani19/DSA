# Rearrange array elements by sign

# Problem Statement:
# Given an array of integers with equal number of positive and negative integers.
# Rearrange the array such that positive and negative numbers are placed alternatively.
# The order of appearance should be maintained.

# Examples:
# Example 1:
#   Input:  arr = [3, 1, -2, -5, 2, -4]
#   Output: [3, -2, 1, -5, 2, -4]
#   Explanation: Positive numbers are [3, 1, 2] and negatives are [-2, -5, -4]

# Example 2:
#   Input:  arr = [-1, 1]
#   Output: [1, -1]

# Example 3:
#   Input:  arr = [1, 2, -4, -5]
#   Output: [1, -4, 2, -5]

# Difficulty: Medium


def rearrange_by_sign(arr):
    # Write your code here
    # Hint: Create a result array and use two pointers for even and odd indices
    # Place positives at even indices (0, 2, 4...) and negatives at odd indices (1, 3, 5...)
    pass


# --- Run & Test ---
print(rearrange_by_sign([3, 1, -2, -5, 2, -4]))   # expected: [3, -2, 1, -5, 2, -4]
print(rearrange_by_sign([-1, 1]))                  # expected: [1, -1]
print(rearrange_by_sign([1, 2, -4, -5]))          # expected: [1, -4, 2, -5]
