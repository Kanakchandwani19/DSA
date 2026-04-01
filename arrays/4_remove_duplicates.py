# Remove Duplicates from Sorted Array

# Problem Statement:
# Given a sorted array, remove duplicates in-place so each element appears
# only once. Return the count of unique elements.
# The first K elements of the array should contain the unique values in order.
# (You don't need to worry about elements beyond index K-1.)

# Examples:
# Example 1:
#   Input:  arr = [1, 1, 2, 2, 3]
#   Output: 3  (unique elements: [1, 2, 3, ...])

# Example 2:
#   Input:  arr = [1, 1, 1, 1]
#   Output: 1  (unique elements: [1, ...])

# Example 3:
#   Input:  arr = [1, 2, 3, 4]
#   Output: 4  (unique elements: [1, 2, 3, 4])


def remove_duplicates(arr):
    # write your code here
    # modify arr in-place and return count of unique elements
    pass


# --- Run & Test ---
arr1 = [1, 1, 2, 2, 3]
k = remove_duplicates(arr1)
print(k, arr1[:k])   # expected: 3 [1, 2, 3]

arr2 = [1, 1, 1, 1]
k = remove_duplicates(arr2)
print(k, arr2[:k])   # expected: 1 [1]

arr3 = [1, 2, 3, 4]
k = remove_duplicates(arr3)
print(k, arr3[:k])   # expected: 4 [1, 2, 3, 4]
