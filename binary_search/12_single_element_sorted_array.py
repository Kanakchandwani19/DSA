# Single Element in a Sorted Array

# Problem Statement:
# You are given a sorted array consisting of only integers where every element appears exactly twice,
# except for one element which appears exactly once.
# Return the single element that appears only once.
# Your solution must run in O(log n) time and O(1) space.

# Examples:
# Example 1:
#   Input:  arr = [1, 1, 2, 3, 3, 4, 4, 8, 8]
#   Output: 2

# Example 2:
#   Input:  arr = [3, 3, 7, 7, 10, 11, 11]
#   Output: 10

# Example 3:
#   Input:  arr = [1]
#   Output: 1

# Difficulty: Medium


def single_element_sorted_array(arr):
    # Write your code here
    # Hint: Before the single element, pairs start at even indices
    # After the single element, pairs start at odd indices
    # Use binary search to find the transition point
    pass


# --- Run & Test ---
print(single_element_sorted_array([1, 1, 2, 3, 3, 4, 4, 8, 8]))   # expected: 2
print(single_element_sorted_array([3, 3, 7, 7, 10, 11, 11]))      # expected: 10
print(single_element_sorted_array([1]))                           # expected: 1
