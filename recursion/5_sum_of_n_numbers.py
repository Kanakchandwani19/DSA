# Sum of First N Numbers

# Problem Statement:
# Given a number N, return the sum of all numbers from 1 to N using recursion.
# Do NOT use any loop or formula directly — solve it recursively.

# Examples:
# Example 1:
#   Input:  N = 5
#   Output: 15
#   Explanation: 1 + 2 + 3 + 4 + 5 = 15

# Example 2:
#   Input:  N = 1
#   Output: 1

# Example 3:
#   Input:  N = 10
#   Output: 55
#   Explanation: 1 + 2 + ... + 10 = 55


def sum(n):
    if n==0:
        return 0
    else:
        return sum(n-1) + n
    



print(sum(1))    # expected: 1
print(sum(5))    # expected: 15
print(sum(10))   # expected: 55
