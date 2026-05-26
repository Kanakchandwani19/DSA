# Search Insert Position

# Problem Statement:
# Given a sorted array and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.

# Examples:
# Example 1:
#   Input:  arr = [1, 3, 5, 6], target = 5
#   Output: 2

# Example 2:
#   Input:  arr = [1, 3, 5, 6], target = 2
#   Output: 1

# Example 3:
#   Input:  arr = [1, 3, 5, 6], target = 7
#   Output: 4

# Difficulty: Easy


def search_insert_position(arr, target):
    # Write your code here
    # Hint: This is same as finding lower bound
    pass


# --- Run & Test ---
print(search_insert_position([1, 3, 5, 6], 5))   # expected: 2
print(search_insert_position([1, 3, 5, 6], 2))   # expected: 1
print(search_insert_position([1, 3, 5, 6], 7))   # expected: 4
