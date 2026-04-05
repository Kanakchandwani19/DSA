# Print all Divisors

# Problem Statement:
# Given a number N, print all its divisors in ascending order.
# A divisor of N is any number that divides N without leaving a remainder.

# Examples:
# Example 1:
#   Input:  N = 12
#   Output: [1, 2, 3, 4, 6, 12]

# Example 2:
#   Input:  N = 7
#   Output: [1, 7]
#   Explanation: 7 is prime, only divisors are 1 and itself

# Example 3:
#   Input:  N = 36
#   Output: [1, 2, 3, 4, 6, 9, 12, 18, 36]


def print_divisors(n):
    div = []

    for i in range(1,n + 1):
        if n%i == 0:
            div.append(i)

    return div
    


# --- Run & Test ---
print(print_divisors(12))   # expected: [1, 2, 3, 4, 6, 12]
print(print_divisors(7))    # expected: [1, 7]
print(print_divisors(36))   # expected: [1, 2, 3, 4, 6, 9, 12, 18, 36]
