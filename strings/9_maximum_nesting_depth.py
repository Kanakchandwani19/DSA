# Maximum Nesting Depth of the Parentheses

# Problem Statement:
# A string is a valid parentheses string if it is empty, can be written as AB (A concatenated with B),
# or can be written as (A), where A and B are valid parentheses strings.
# The nesting depth of a valid parentheses string is the maximum number of nested parentheses.
# Given a valid parentheses string s, return the nesting depth of s.

# Examples:
# Example 1:
#   Input:  s = "(1+(2*3)+((8)/4))+1"
#   Output: 3
#   Explanation: Digit 8 is inside of 3 nested parentheses

# Example 2:
#   Input:  s = "(1)+((2))+(((3)))"
#   Output: 3

# Example 3:
#   Input:  s = "1+(2*3)/(2-1)"
#   Output: 1

# Difficulty: Medium


def maximum_nesting_depth(s):
    # Write your code here
    # Hint: Keep track of current depth and maximum depth
    # Increment depth for '(', decrement for ')'
    pass


# --- Run & Test ---
print(maximum_nesting_depth("(1+(2*3)+((8)/4))+1"))    # expected: 3
print(maximum_nesting_depth("(1)+((2))+(((3)))"))      # expected: 3
print(maximum_nesting_depth("1+(2*3)/(2-1)"))          # expected: 1
