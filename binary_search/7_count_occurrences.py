# Count Occurrences in Sorted Array

# Problem Statement:
# Given a sorted array and a target value, count the number of times the target appears in the array.

# Examples:
# Example 1:
#   Input:  arr = [2, 2, 3, 3, 3, 3, 4], target = 3
#   Output: 4

# Example 2:
#   Input:  arr = [2, 2, 3, 3, 3, 3, 4], target = 5
#   Output: 0

# Example 3:
#   Input:  arr = [1, 1, 1, 1, 1], target = 1
#   Output: 5

# Difficulty: Easy


def count_occurrences(arr, target):
    # Write your code here
    # Hint: Count = (last occurrence - first occurrence + 1)
    # Use first and last occurrence logic
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

        if first == -1:
            return 0

    return last - first + 1


# --- Run & Test ---
print(count_occurrences([2, 2, 3, 3, 3, 3, 4], 3))   # expected: 4
print(count_occurrences([2, 2, 3, 3, 3, 3, 4], 5))   # expected: 0
print(count_occurrences([1, 1, 1, 1, 1], 1))         # expected: 5
