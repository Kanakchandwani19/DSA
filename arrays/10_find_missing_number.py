# Find the Missing Number

# Problem Statement:
# Given an array of N-1 integers in range [1, N], find the one missing number.
# All integers from 1 to N appear exactly once except one.

# Examples:
# Example 1:
#   Input:  arr = [1, 2, 4, 5], N = 5
#   Output: 3

# Example 2:
#   Input:  arr = [2, 3, 4, 5], N = 5
#   Output: 1
#   Explanation: 1 is missing

# Example 3:
#   Input:  arr = [1, 2, 3, 4], N = 5
#   Output: 5

# Hint: sum of 1 to N = N*(N+1)/2 — subtract the sum of arr from it


def find_missing(arr, n):           ##method 1
    for i in range(1, n+1):
        if i not in arr:
            return i
        
def find_missing(arr, n):           ##method 2
    missing = n * (n+1) // 2
    original = sum(arr)

    return missing - original

# --- Run & Test ---
print(find_missing([1, 2, 4, 5], 5))   # expected: 3
print(find_missing([2, 3, 4, 5], 5))   # expected: 1
print(find_missing([1, 2, 3, 4], 5))   # expected: 5
