# Lower Bound

# Problem Statement:
# Given a sorted array and a target value, find the index of the first element that is greater than or equal to target.
# If no such element exists, return the length of the array.

# Examples:
# Example 1:
#   Input:  arr = [1, 2, 2, 3], target = 2
#   Output: 1
#   Explanation: First element >= 2 is at index 1

# Example 2:
#   Input:  arr = [1, 2, 2, 3], target = 0
#   Output: 0

# Example 3:
#   Input:  arr = [1, 2, 2, 3], target = 5
#   Output: 4

# Difficulty: Easy


def lower_bound(arr, target):
    # Write your code here
    # Hint: Modify binary search
    # Keep moving left when arr[mid] >= target
    # Store the answer and continue searching in left half
    pass


# --- Run & Test ---
print(lower_bound([1, 2, 2, 3], 2))   # expected: 1
print(lower_bound([1, 2, 2, 3], 0))   # expected: 0
print(lower_bound([1, 2, 2, 3], 5))   # expected: 4
