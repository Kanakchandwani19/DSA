# Find the Number that Appears Once (Others Appear Twice)

# Problem Statement:
# Given an array where every element appears exactly twice except for one,
# find that single element.
# Solve it in O(N) time and O(1) space.

# Examples:
# Example 1:
#   Input:  arr = [2, 2, 1]
#   Output: 1

# Example 2:
#   Input:  arr = [4, 1, 2, 1, 2]
#   Output: 4

# Example 3:
#   Input:  arr = [1]
#   Output: 1

# Hint: XOR of a number with itself is 0, XOR of a number with 0 is itself.
#       XOR all elements — pairs cancel out, leaving the single element.


def single_number(arr):
    # write your code here
    pass


# --- Run & Test ---
print(single_number([2, 2, 1]))          # expected: 1
print(single_number([4, 1, 2, 1, 2]))   # expected: 4
print(single_number([1]))               # expected: 1
