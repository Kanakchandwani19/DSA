# Jump Game - I

# Problem Statement:
# You are given an array where each element represents your maximum jump length at that position.
# Determine if you can reach the last index starting from the first index.

# Examples:
# Example 1:
#   Input:  arr = [2, 3, 1, 1, 4]
#   Output: True
#   Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index

# Example 2:
#   Input:  arr = [3, 2, 1, 0, 4]
#   Output: False
#   Explanation: You will always arrive at index 3, which has max jump of 0

# Difficulty: Easy


def jump_game_1(arr):
    # Write your code here
    # Hint: Keep track of max reachable index
    # If at any point current index > max reachable, return False
    pass


# --- Run & Test ---
print(jump_game_1([2, 3, 1, 1, 4]))    # expected: True
print(jump_game_1([3, 2, 1, 0, 4]))    # expected: False
