# Longest Consecutive Sequence in an Array

# Problem Statement:
# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
# The algorithm must run in O(n) time complexity.

# Examples:
# Example 1:
#   Input:  arr = [100, 4, 200, 1, 3, 2]
#   Output: 4
#   Explanation: The longest consecutive sequence is [1, 2, 3, 4]. Length is 4.

# Example 2:
#   Input:  arr = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
#   Output: 9
#   Explanation: The longest consecutive sequence is [0,1,2,3,4,5,6,7,8]. Length is 9.

# Example 3:
#   Input:  arr = [9, 1, 4, 7, 3, 2, 8, 5, 6]
#   Output: 9

# Difficulty: Medium


def longest_consecutive_sequence(arr):
    # Write your code here
    # Hint: Use a set for O(1) lookup
    # For each number, check if it's the start of a sequence (num-1 not in set)
    # Then count consecutive numbers
    pass


# --- Run & Test ---
print(longest_consecutive_sequence([100, 4, 200, 1, 3, 2]))            # expected: 4
print(longest_consecutive_sequence([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))   # expected: 9
print(longest_consecutive_sequence([9, 1, 4, 7, 3, 2, 8, 5, 6]))      # expected: 9
