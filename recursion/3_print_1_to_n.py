# Print 1 to N Using Recursion

# Problem Statement:
# Given a number N, print all numbers from 1 to N in order using recursion.
# Do NOT use any loop.

# Examples:
# Example 1:
#   Input:  N = 5
#   Output: 1 2 3 4 5

# Example 2:
#   Input:  N = 1
#   Output: 1

# Example 3:
#   Input:  N = 10
#   Output: 1 2 3 4 5 6 7 8 9 10


def print_1_to_n(n):
    if n==0:
        return
    
    print_1_to_n(n-1)
    print(n)



# --- Run & Test ---
print_1_to_n(5)    # expected: 1 2 3 4 5
print("---")
print_1_to_n(1)    # expected: 1
print("---")
print_1_to_n(10)   # expected: 1 2 3 4 5 6 7 8 9 10
