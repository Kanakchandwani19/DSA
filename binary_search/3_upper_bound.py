# Upper Bound

# Problem Statement:
# Given a sorted array and a target value, find the index of the first element that is strictly greater than target.
# If no such element exists, return the length of the array.

# Examples:
# Example 1:
#   Input:  arr = [1, 2, 2, 3], target = 2
#   Output: 3
#   Explanation: First element > 2 is at index 3

# Example 2:
#   Input:  arr = [1, 2, 2, 3], target = 0
#   Output: 0

# Example 3:
#   Input:  arr = [1, 2, 2, 3], target = 5
#   Output: 4

# Difficulty: Easy


def upper_bound(arr, target):
    # Write your code here
    # Hint: Similar to lower bound
    # Keep moving left when arr[mid] > target
    left = 0
    right = len(arr)-1
    current = len(arr)

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] > target:
            current = mid
            right = mid - 1

        else:
            left = mid + 1

    return current


# --- Run & Test ---
print(upper_bound([1, 2, 2, 3], 2))   # expected: 3
print(upper_bound([1, 2, 2, 3], 0))   # expected: 0
print(upper_bound([1, 2, 2, 3], 5))   # expected: 4
