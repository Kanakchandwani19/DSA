# Roman to Integer

# Problem Statement:
# Roman numerals are represented by seven symbols:
# I=1, V=5, X=10, L=50, C=100, D=500, M=1000
# Roman numerals are usually written largest to smallest from left to right.
# However, there are special cases like IV=4, IX=9, XL=40, XC=90, CD=400, CM=900
# Given a roman numeral, convert it to an integer.

# Examples:
# Example 1:
#   Input:  s = "III"
#   Output: 3

# Example 2:
#   Input:  s = "LVIII"
#   Output: 58
#   Explanation: L = 50, V = 5, III = 3

# Example 3:
#   Input:  s = "MCMXCIV"
#   Output: 1994
#   Explanation: M = 1000, CM = 900, XC = 90, IV = 4

# Difficulty: Medium


def roman_to_integer(s):
    # Write your code here
    # Hint: Use a dictionary for roman to integer mapping
    # If current value < next value, subtract current (like IV)
    # Otherwise, add current value
    pass


# --- Run & Test ---
print(roman_to_integer("III"))        # expected: 3
print(roman_to_integer("LVIII"))      # expected: 58
print(roman_to_integer("MCMXCIV"))    # expected: 1994
