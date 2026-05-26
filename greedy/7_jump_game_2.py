# Jump Game II

# Problem Statement:
# You are given an array where each element represents your maximum jump length at that position.
# Find the minimum number of jumps required to reach the last index.
# Assume you can always reach the last index.

# Examples:
# Example 1:
#   Input:  arr = [2, 3, 1, 1, 4]
#   Output: 2
#   Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index

# Example 2:
#   Input:  arr = [2, 3, 0, 1, 4]
#   Output: 2

# Difficulty: Medium


def jump_game_2(arr):
    # Write your code here
    # Hint: Use greedy approach with two pointers (current end and farthest)
    # Count jumps when you reach current end
    pass


# --- Run & Test ---
print(jump_game_2([2, 3, 1, 1, 4]))    # expected: 2
print(jump_game_2([2, 3, 0, 1, 4]))    # expected: 2
