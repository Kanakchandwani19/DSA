# Candy

# Problem Statement:
# There are n children standing in a line, each with a rating.
# You need to give candies to children following these rules:
# 1. Each child must have at least one candy
# 2. Children with higher rating get more candies than their neighbors
# Find the minimum number of candies you need.

# Examples:
# Example 1:
#   Input:  ratings = [1, 0, 2]
#   Output: 5
#   Explanation: Give candies [2, 1, 2]

# Example 2:
#   Input:  ratings = [1, 2, 2]
#   Output: 4
#   Explanation: Give candies [1, 2, 1]

# Difficulty: Hard


def candy(ratings):
    # Write your code here
    # Hint: Two pass approach
    # Left to right: ensure child with higher rating than left neighbor gets more
    # Right to left: ensure child with higher rating than right neighbor gets more
    pass


# --- Run & Test ---
print(candy([1, 0, 2]))      # expected: 5
print(candy([1, 2, 2]))      # expected: 4
