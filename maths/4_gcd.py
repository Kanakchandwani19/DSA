# GCD of Two Numbers

# Problem Statement:
# Given two numbers A and B, find their Greatest Common Divisor (GCD).
# GCD is the largest number that divides both A and B without a remainder.

# Examples:
# Example 1:
#   Input:  A = 12, B = 8
#   Output: 4
#   Explanation: divisors of 12 → 1,2,3,4,6,12
#                divisors of 8  → 1,2,4,8
#                largest common → 4

# Example 2:
#   Input:  A = 9, B = 6
#   Output: 3

# Example 3:
#   Input:  A = 100, B = 75
#   Output: 25


def gcd(a, b):
    while b!=0:
        (a,b) = (b,a%b)
    return a


  

print(gcd(12, 8))     # expected: 4
print(gcd(9, 6))      # expected: 3
print(gcd(100, 75))   # expected: 25
