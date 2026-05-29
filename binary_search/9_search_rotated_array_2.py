# Search in Rotated Sorted Array - II

# Problem Statement:
# Similar to Search in Rotated Sorted Array I, but the array may contain duplicates.
# Given the array after rotation and a target value, return true if target is in the array, false otherwise.

# Examples:
# Example 1:
#   Input:  arr = [2, 5, 6, 0, 0, 1, 2], target = 0
#   Output: True

# Example 2:
#   Input:  arr = [2, 5, 6, 0, 0, 1, 2], target = 3
#   Output: False

# Example 3:
#   Input:  arr = [1, 0, 1, 1, 1], target = 0
#   Output: True

# Difficulty: Medium


def search_rotated_array_2(arr, target):
    # Write your code here
    # Hint: Similar to version I, but handle duplicates
    # When arr[left] == arr[mid] == arr[right], shrink search space by moving pointers
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return True
        
        if arr[mid] == arr[left] == arr[right]:
            left += 1
            right -= 1

        elif arr[left] <= arr[mid]:

            if arr[left] <= target < arr[mid]:
                right = mid - 1

            else:
                left = mid + 1

        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1

            else:
                right = mid -1

    return False





# --- Run & Test ---
print(search_rotated_array_2([2, 5, 6, 0, 0, 1, 2], 0))   # expected: True
print(search_rotated_array_2([2, 5, 6, 0, 0, 1, 2], 3))   # expected: False
print(search_rotated_array_2([1, 0, 1, 1, 1], 0))         # expected: True
