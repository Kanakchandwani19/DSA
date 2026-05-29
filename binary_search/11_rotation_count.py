# Find how many times array has been rotated

# Problem Statement:
# Given a sorted array that has been rotated, find the number of times it has been rotated.
# Note: The number of rotations is equal to the index of the minimum element.

# Examples:
# Example 1:
#   Input:  arr = [4, 5, 6, 7, 0, 1, 2]
#   Output: 4
#   Explanation: Array was rotated 4 times (minimum element 0 is at index 4)

# Example 2:
#   Input:  arr = [3, 4, 5, 1, 2]
#   Output: 3

# Example 3:
#   Input:  arr = [1, 2, 3, 4, 5]
#   Output: 0
#   Explanation: Array is not rotated

# Difficulty: Easy


def rotation_count(arr):
    # Write your code here
    # Hint: Find the index of minimum element
    # Use same approach as finding minimum in rotated array
    pass

    left = 0
    right = len(arr) - 1

    while left < right:
        mid = (left + right) // 2

        if arr[mid] > arr[right]:
            left = mid +1

        else:
            right = mid

    return left


# --- Run & Test ---
print(rotation_count([4, 5, 6, 7, 0, 1, 2]))   # expected: 4
print(rotation_count([3, 4, 5, 1, 2]))         # expected: 3
print(rotation_count([1, 2, 3, 4, 5]))         # expected: 0
