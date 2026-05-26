# Lemonade Change

# Problem Statement:
# At a lemonade stand, each lemonade costs $5.
# Customers are standing in a queue and each pays with a $5, $10, or $20 bill.
# You must provide correct change to each customer (initially you have no money).
# Return true if you can provide change to every customer, false otherwise.

# Examples:
# Example 1:
#   Input:  bills = [5, 5, 5, 10, 20]
#   Output: True
#   Explanation: Collect 5,5,5. Give back 5 to customer with 10. Give back 10+5 to customer with 20.

# Example 2:
#   Input:  bills = [5, 5, 10, 10, 20]
#   Output: False
#   Explanation: Cannot give change to last customer

# Example 3:
#   Input:  bills = [5, 5, 10]
#   Output: True

# Difficulty: Easy


def lemonade_change(bills):
    # Write your code here
    # Hint: Keep count of $5 and $10 bills
    # For $10 bill: give back one $5
    # For $20 bill: give back one $10 and one $5, or three $5 bills
    pass


# --- Run & Test ---
print(lemonade_change([5, 5, 5, 10, 20]))     # expected: True
print(lemonade_change([5, 5, 10, 10, 20]))    # expected: False
print(lemonade_change([5, 5, 10]))            # expected: True
