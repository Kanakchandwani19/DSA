# Fibonacci Number

# Problem Statement:
# Given a number N, return the Nth Fibonacci number using recursion.
# Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# Definition:
#   fib(0) = 0
#   fib(1) = 1
#   fib(N) = fib(N-1) + fib(N-2)  for N > 1

# Examples:
# Example 1:
#   Input:  N = 0
#   Output: 0

# Example 2:
#   Input:  N = 1
#   Output: 1

# Example 3:
#   Input:  N = 6
#   Output: 8
#   Explanation: sequence → 0, 1, 1, 2, 3, 5, 8  → 6th index = 8

# Example 4:
#   Input:  N = 10
#   Output: 55


def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return(fibonacci(n-1) + fibonacci(n-2))



# --- Run & Test ---
print(fibonacci(0))    # expected: 0
print(fibonacci(1))    # expected: 1
print(fibonacci(6))    # expected: 8
print(fibonacci(10))   # expected: 55
