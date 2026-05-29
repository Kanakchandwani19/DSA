# First and Last Occurrence

# Problem Statement:
# Given a sorted array with possible duplicates, find the first and last position of a given target value.
# If target is not found in the array, return [-1, -1].

# Examples:
# Example 1:
#   Input:  arr = [5, 7, 7, 8, 8, 10], target = 8
#   Output: [3, 4]

# Example 2:
#   Input:  arr = [5, 7, 7, 8, 8, 10], target = 6
#   Output: [-1, -1]

# Example 3:
#   Input:  arr = [2, 2, 2, 2], target = 2
#   Output: [0, 3]

# Difficulty: Medium


def first_last_occurrence(arr, target):
    # Write your code here
    # Hint: Use lower bound to find first occurrence
    # Use upper bound - 1 to find last occurrence
    left = 0 
    right = len(arr) - 1
    first = -1
    

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            first = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    left = 0
    right = len(arr) - 1
    last = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            last = mid
            left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return [first, last]




# --- Run & Test ---
print(first_last_occurrence([5, 7, 7, 8, 8, 10], 8))   # expected: [3, 4]
print(first_last_occurrence([5, 7, 7, 8, 8, 10], 6))   # expected: [-1, -1]
print(first_last_occurrence([2, 2, 2, 2], 2))          # expected: [0, 3]
