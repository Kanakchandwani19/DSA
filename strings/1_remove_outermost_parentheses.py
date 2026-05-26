# Remove Outermost Parentheses

# Problem Statement:
# A valid parentheses string is either empty, "()" + A + ")" where A is valid, or A + B where both A and B are valid.
# Given a valid parentheses string s, remove the outermost parentheses of every primitive string in the primitive decomposition of s.
# Return the result.

# Examples:
# Example 1:
#   Input:  s = "(()())(())"
#   Output: "()()()"
#   Explanation: The input is "(()())" + "(())", outermost removed gives "()()" + "()"

# Example 2:
#   Input:  s = "(()())(())(()(()))"
#   Output: "()()()()(())"

# Example 3:
#   Input:  s = "()()"
#   Output: ""
#   Explanation: The input is "()" + "()", removing outer parentheses gives "" + ""

# Difficulty: Medium


def remove_outermost_parentheses(s):
    # Write your code here
    # Hint: Use a counter to track balance
    # Add to result only when counter > 1 for '(' and counter > 0 after decrement for ')'
    pass


# --- Run & Test ---
print(remove_outermost_parentheses("(()())(())"))               # expected: "()()()"
print(remove_outermost_parentheses("(()())(())(()(()))"))      # expected: "()()()()(())"
print(remove_outermost_parentheses("()()"))                     # expected: ""
