# String to Integer (atoi)

# Problem Statement:
# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.
# The algorithm:
# 1. Read and ignore leading whitespace
# 2. Check if next character is '-' or '+' (determines sign)
# 3. Read digits until non-digit character or end of input
# 4. Convert digits to integer
# 5. Clamp the integer to 32-bit range [-2^31, 2^31 - 1]

# Examples:
# Example 1:
#   Input:  s = "42"
#   Output: 42

# Example 2:
#   Input:  s = "   -42"
#   Output: -42

# Example 3:
#   Input:  s = "4193 with words"
#   Output: 4193

# Example 4:
#   Input:  s = "words and 987"
#   Output: 0

# Difficulty: Medium


def string_to_integer(s):
    # Write your code here
    # Hint: Handle whitespace, sign, digits, and overflow
    # INT_MAX = 2^31 - 1 = 2147483647
    # INT_MIN = -2^31 = -2147483648
    pass


# --- Run & Test ---
print(string_to_integer("42"))                  # expected: 42
print(string_to_integer("   -42"))              # expected: -42
print(string_to_integer("4193 with words"))     # expected: 4193
print(string_to_integer("words and 987"))       # expected: 0
