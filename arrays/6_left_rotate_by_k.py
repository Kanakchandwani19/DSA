# Left Rotate Array by K Places

# Problem Statement:
# Given an array of N elements and a number K, rotate the array to the
# left by K positions. Elements shifted off the front wrap around to the end.

# Examples:
# Example 1:
#   Input:  arr = [1, 2, 3, 4, 5], K = 2
#   Output: [3, 4, 5, 1, 2]

# Example 2:
#   Input:  arr = [1, 2, 3, 4, 5], K = 0
#   Output: [1, 2, 3, 4, 5]

# Example 3:
#   Input:  arr = [1, 2, 3, 4, 5], K = 5
#   Output: [1, 2, 3, 4, 5]
#   Explanation: rotating by N is the same as no rotation

# Hint: K = K % N handles cases where K >= N


def left_rotate_by_k(arr, k):
    
    

# --- Run & Test ---
arr1 = [1, 2, 3, 4, 5]
left_rotate_by_k(arr1, 2)
print(arr1)   # expected: [3, 4, 5, 1, 2]

arr2 = [1, 2, 3, 4, 5]
left_rotate_by_k(arr2, 0)
print(arr2)   # expected: [1, 2, 3, 4, 5]

arr3 = [1, 2, 3, 4, 5]
left_rotate_by_k(arr3, 5)
print(arr3)   # expected: [1, 2, 3, 4, 5]
