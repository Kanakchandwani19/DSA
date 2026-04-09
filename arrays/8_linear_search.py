# Linear Search

# Problem Statement:
# Given an array of N elements and a target value, return the index
# of the target if found, otherwise return -1.
# Search from left to right (linear scan).

# Examples:
# Example 1:
#   Input:  arr = [3, 4, 1, 7, 5], target = 7
#   Output: 3
#   Explanation: 7 is at index 3

# Example 2:
#   Input:  arr = [3, 4, 1, 7, 5], target = 10
#   Output: -1
#   Explanation: 10 is not in the array

# Example 3:
#   Input:  arr = [5], target = 5
#   Output: 0


def linear_search(arr, target):
    for i in range(len(arr)):
      if arr[i] == target:
         return i
      
    return -1


# --- Run & Test ---
print(linear_search([3, 4, 1, 7, 5], 7))    # expected: 3
print(linear_search([3, 4, 1, 7, 5], 10))   # expected: -1
print(linear_search([5], 5))                 # expected: 0
