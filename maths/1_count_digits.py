# Count all Digits of a Number

# Problem Statement:
# Given a number N, count the number of digits in N.

# Examples:
# Example 1:
#   Input:  N = 12345
#   Output: 5
#   Explanation: 1, 2, 3, 4, 5 — five digits

# Example 2:
#   Input:  N = 7
#   Output: 1
#   Explanation: only one digit

# Example 3:
#   Input:  N = 1000
#   Output: 4


def count_digits(n):
    count = 0
    while n>0:
        n = n // 10
        count += 1
    return count


# --- Run & Test ---
print(count_digits(12345))   # expected: 5
print(count_digits(7))       # expected: 1
print(count_digits(1000))    # expected: 4
