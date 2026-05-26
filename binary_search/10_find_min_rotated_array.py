# Find Minimum in Rotated Sorted Array

# Problem Statement:
# Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
# Given the rotated array, return the minimum element of this array.
# You must write an algorithm with O(log n) runtime complexity.

# Examples:
# Example 1:
#   Input:  arr = [3, 4, 5, 1, 2]
#   Output: 1
#   Explanation: The original array was [1,2,3,4,5] rotated 3 times.

# Example 2:
#   Input:  arr = [4, 5, 6, 7, 0, 1, 2]
#   Output: 0

# Example 3:
#   Input:  arr = [11, 13, 15, 17]
#   Output: 11

# Difficulty: Medium


def find_min_rotated_array(arr):
    # Write your code here
    # Hint: The minimum element is the only element whose previous is greater
    # Use binary search: if arr[mid] > arr[right], min is in right half
    pass


# --- Run & Test ---
print(find_min_rotated_array([3, 4, 5, 1, 2]))       # expected: 1
print(find_min_rotated_array([4, 5, 6, 7, 0, 1, 2])) # expected: 0
print(find_min_rotated_array([11, 13, 15, 17]))      # expected: 11
