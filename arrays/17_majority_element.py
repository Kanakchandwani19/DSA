# Majority Element - I

# Problem Statement:
# Given an array of N integers, find the element that appears more than N/2 times.
# The majority element always exists in the array.

# Examples:
# Example 1:
#   Input:  arr = [3, 2, 3]
#   Output: 3

# Example 2:
#   Input:  arr = [2, 2, 1, 1, 1, 2, 2]
#   Output: 2

# Example 3:
#   Input:  arr = [1, 1, 1, 1]
#   Output: 1

# Difficulty: Easy
# Hint: Moore's Voting Algorithm


def majority_element(arr):
    # Write your code here
    # Hint: Use two variables - candidate and count
    # If count becomes 0, pick current element as new candidate
    pass


# --- Run & Test ---
print(majority_element([3, 2, 3]))                  # expected: 3
print(majority_element([2, 2, 1, 1, 1, 2, 2]))      # expected: 2
print(majority_element([1, 1, 1, 1]))               # expected: 1
