# Print N to 1 Using Recursion

# Problem Statement:
# Given a number N, print all numbers from N down to 1 using recursion.
# Do NOT use any loop.

# Examples:
# Example 1:
#   Input:  N = 5
#   Output: 5 4 3 2 1

# Example 2:
#   Input:  N = 1
#   Output: 1

# Example 3:
#   Input:  N = 7
#   Output: 7 6 5 4 3 2 1


def print_n_to_1(n):
    if n==0:
        return
    
    print(n)
    print_n_to_1(n-1)


    



print_n_to_1(5)   # expected: 5 4 3 2 1
print("---")
print_n_to_1(1)   # expected: 1
print("---")
print_n_to_1(7)   # expected: 7 6 5 4 3 2 1
