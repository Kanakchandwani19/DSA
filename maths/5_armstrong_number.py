# Check if the Number is Armstrong

# Problem Statement:
# A number N is called an Armstrong number if the sum of its digits,
# each raised to the power of the number of digits, equals N itself.
#
# Formula: for a d-digit number, sum of (each digit ^ d) == N

# Examples:
# Example 1:
#   Input:  N = 153
#   Output: True
#   Explanation: 3 digits → 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153 ✓

# Example 2:
#   Input:  N = 9474
#   Output: True
#   Explanation: 4 digits → 9^4 + 4^4 + 7^4 + 4^4 = 6561+256+2401+256 = 9474 ✓

# Example 3:
#   Input:  N = 123
#   Output: False
#   Explanation: 1^3 + 2^3 + 3^3 = 1 + 8 + 27 = 36 ≠ 123


def is_armstrong(n):
    # write your code here
    pass


# --- Run & Test ---
print(is_armstrong(153))   # expected: True
print(is_armstrong(9474))  # expected: True
print(is_armstrong(123))   # expected: False
