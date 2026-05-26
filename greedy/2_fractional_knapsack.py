# Fractional Knapsack

# Problem Statement:
# Given weights and values of n items, put these items in a knapsack of capacity W
# to get the maximum total value in the knapsack.
# You can take fractions of items (unlike 0/1 knapsack).

# Examples:
# Example 1:
#   Input:  values = [60, 100, 120], weights = [10, 20, 30], capacity = 50
#   Output: 240.0
#   Explanation: Take all of item 3 (value 120), all of item 2 (value 100), and 2/3 of item 1 (value 40)

# Example 2:
#   Input:  values = [60, 100], weights = [10, 20], capacity = 15
#   Output: 160.0
#   Explanation: Take all of item 2 (100) and half of item 1 (30)

# Difficulty: Medium


def fractional_knapsack(values, weights, capacity):
    # Write your code here
    # Hint: Calculate value/weight ratio for each item
    # Sort items by ratio in descending order
    # Greedily take items with highest ratio first
    pass


# --- Run & Test ---
print(fractional_knapsack([60, 100, 120], [10, 20, 30], 50))    # expected: 240.0
print(fractional_knapsack([60, 100], [10, 20], 15))             # expected: 160.0
