# Sort an array of 0's 1's and 2's

# Problem Statement:
# Given an array containing only 0s, 1s, and 2s, sort the array in ascending order.
# Try to solve it in a single pass without using any sorting algorithm.

# Examples:
# Example 1:
#   Input:  arr = [2, 0, 2, 1, 1, 0]
#   Output: [0, 0, 1, 1, 2, 2]

# Example 2:
#   Input:  arr = [2, 0, 1]
#   Output: [0, 1, 2]

# Example 3:
#   Input:  arr = [0]
#   Output: [0]

# Difficulty: Medium
# Hint: Dutch National Flag Algorithm (3-pointer approach)


def sort_0_1_2(arr):
    # Write your code here
    # Hint: Use three pointers - low, mid, high
    # 0 to low-1: all 0s
    # low to mid-1: all 1s
    # high+1 to n-1: all 2s
    pass


# --- Run & Test ---
arr1 = [2, 0, 2, 1, 1, 0]
sort_0_1_2(arr1)
print(arr1)  # expected: [0, 0, 1, 1, 2, 2]

arr2 = [2, 0, 1]
sort_0_1_2(arr2)
print(arr2)  # expected: [0, 1, 2]

arr3 = [0]
sort_0_1_2(arr3)
print(arr3)  # expected: [0]
