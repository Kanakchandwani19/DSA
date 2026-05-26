# Stock Buy and Sell

# Problem Statement:
# You are given an array where the ith element is the price of a given stock on day i.
# Find the maximum profit you can achieve by buying on one day and selling on another day in the future.
# If no profit can be made, return 0.

# Examples:
# Example 1:
#   Input:  prices = [7, 1, 5, 3, 6, 4]
#   Output: 5
#   Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5

# Example 2:
#   Input:  prices = [7, 6, 4, 3, 1]
#   Output: 0
#   Explanation: No transaction is done, max profit = 0

# Example 3:
#   Input:  prices = [1, 2, 3, 4, 5]
#   Output: 4
#   Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4

# Difficulty: Medium


def stock_buy_sell(prices):
    # Write your code here
    # Hint: Keep track of minimum price seen so far and maximum profit
    pass


# --- Run & Test ---
print(stock_buy_sell([7, 1, 5, 3, 6, 4]))   # expected: 5
print(stock_buy_sell([7, 6, 4, 3, 1]))      # expected: 0
print(stock_buy_sell([1, 2, 3, 4, 5]))      # expected: 4
