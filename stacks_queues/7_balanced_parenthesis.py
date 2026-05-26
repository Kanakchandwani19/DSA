# Balanced Parenthesis

# Problem Statement:
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
# A string is valid if:
# - Open brackets must be closed by the same type of brackets.
# - Open brackets must be closed in the correct order.

# Examples:
# Example 1:
#   Input:  s = "()"
#   Output: True

# Example 2:
#   Input:  s = "()[]{}"
#   Output: True

# Example 3:
#   Input:  s = "(]"
#   Output: False

# Example 4:
#   Input:  s = "([)]"
#   Output: False

# Example 5:
#   Input:  s = "{[]}"
#   Output: True

# Difficulty: Easy


def balanced_parenthesis(s):
    # Write your code here
    # Hint: Use a stack
    # Push opening brackets onto stack
    # For closing brackets, check if top of stack matches
    pass


# --- Run & Test ---
print(balanced_parenthesis("()"))          # expected: True
print(balanced_parenthesis("()[]{}"))      # expected: True
print(balanced_parenthesis("(]"))          # expected: False
print(balanced_parenthesis("([)]"))        # expected: False
print(balanced_parenthesis("{[]}"))        # expected: True
