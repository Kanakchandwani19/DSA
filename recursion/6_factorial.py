# Factorial of a Given Number

# Problem Statement:
# Given a number N, return N! (N factorial) using recursion.
# Factorial: N! = N × (N-1) × (N-2) × ... × 1
# Base case: 0! = 1

# Examples:
# Example 1:
#   Input:  N = 5
#   Output: 120
#   Explanation: 5 × 4 × 3 × 2 × 1 = 120

# Example 2:
#   Input:  N = 0
#   Output: 1
#   Explanation: 0! is defined as 1

# Example 3:
#   Input:  N = 6
#   Output: 720
#   Explanation: 6 × 5 × 4 × 3 × 2 × 1 = 720


def factorial(n):
    if n == 0:
        return 1
    else:
        return n* factorial(n-1)


    

print(factorial(5))   # expected: 120
print(factorial(0))   # expected: 1
print(factorial(6))   # expected: 720
