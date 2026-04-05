# Check for Prime Number

# Problem Statement:
# Given a number N, determine whether it is a prime number.
# A prime number is greater than 1 and has no divisors other than 1 and itself.

# Examples:
# Example 1:
#   Input:  N = 7
#   Output: True
#   Explanation: divisors of 7 are only 1 and 7

# Example 2:
#   Input:  N = 12
#   Output: False
#   Explanation: 12 is divisible by 2, 3, 4, 6

# Example 3:
#   Input:  N = 1
#   Output: False
#   Explanation: 1 is not considered a prime number

# Example 4:
#   Input:  N = 2
#   Output: True
#   Explanation: 2 is the smallest prime number


def is_prime(n):
    if n<=1:
        return False

    for i in range(2,n):
        if n%i == 0:
            return False
    return True

# --- Run & Test ---
print(is_prime(7))    # expected: True
print(is_prime(12))   # expected: False
print(is_prime(1))    # expected: False
print(is_prime(2))    # expected: True
