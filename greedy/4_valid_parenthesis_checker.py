# Valid Parenthesis Checker

# Problem Statement:
# Given a string of '(' and ')', and '*' where '*' can be treated as '(' or ')' or empty string.
# Check if the string is valid (all parentheses are properly matched).

# Examples:
# Example 1:
#   Input:  s = "()"
#   Output: True

# Example 2:
#   Input:  s = "(*)"
#   Output: True
#   Explanation: * can be treated as )

# Example 3:
#   Input:  s = "(*))"
#   Output: True

# Difficulty: Medium


def valid_parenthesis_checker(s):
    # Write your code here
    # Hint: Use greedy approach
    # Maintain min and max possible open brackets count
    # For '(': increment both
    # For ')': decrement both
    # For '*': decrement min, increment max
    pass


# --- Run & Test ---
print(valid_parenthesis_checker("()"))        # expected: True
print(valid_parenthesis_checker("(*)"))       # expected: True
print(valid_parenthesis_checker("(*))"))      # expected: True
