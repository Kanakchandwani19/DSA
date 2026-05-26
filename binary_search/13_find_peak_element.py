# Find Peak Element

# Problem Statement:
# A peak element is an element that is strictly greater than its neighbors.
# Given a 0-indexed integer array, find a peak element and return its index.
# If the array contains multiple peaks, return the index to any of the peaks.
# You must write an algorithm that runs in O(log n) time.

# Examples:
# Example 1:
#   Input:  arr = [1, 2, 3, 1]
#   Output: 2
#   Explanation: 3 is a peak element

# Example 2:
#   Input:  arr = [1, 2, 1, 3, 5, 6, 4]
#   Output: 5
#   Explanation: Both 2 and 6 are peaks, index 5 (value 6) is valid

# Example 3:
#   Input:  arr = [1, 2, 3, 4, 5]
#   Output: 4
#   Explanation: 5 is a peak element

# Difficulty: Medium


def find_peak_element(arr):
    # Write your code here
    # Hint: Use binary search
    # If arr[mid] < arr[mid+1], peak is in right half
    # Otherwise, peak is in left half (including mid)
    pass


# --- Run & Test ---
print(find_peak_element([1, 2, 3, 1]))           # expected: 2
print(find_peak_element([1, 2, 1, 3, 5, 6, 4]))  # expected: 1 or 5
print(find_peak_element([1, 2, 3, 4, 5]))        # expected: 4
