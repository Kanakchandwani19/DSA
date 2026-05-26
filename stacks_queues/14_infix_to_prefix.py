# Infix to Prefix Conversion

# Problem Statement:
# Convert an infix expression to prefix notation.
# Infix: A + B
# Prefix: +AB
#
# Operators: +, -, *, /, ^
# Precedence: ^ > *, / > +, -

# Examples:
# Example 1:
#   Input:  "A+B"
#   Output: "+AB"

# Example 2:
#   Input:  "A+B*C"
#   Output: "+A*BC"

# Example 3:
#   Input:  "(A+B)*C"
#   Output: "*+ABC"

# Example 4:
#   Input:  "A+B*C-D"
#   Output: "-+A*BCD"

# Difficulty: Medium


def infix_to_prefix(expression):
    # Write your code here
    # Hint:
    # 1. Reverse the infix expression
    # 2. Replace '(' with ')' and vice versa
    # 3. Convert to postfix
    # 4. Reverse the result
    pass


# --- Run & Test ---
print(infix_to_prefix("A+B"))          # expected: "+AB"
print(infix_to_prefix("A+B*C"))        # expected: "+A*BC"
print(infix_to_prefix("(A+B)*C"))      # expected: "*+ABC"
print(infix_to_prefix("A+B*C-D"))      # expected: "-+A*BCD"
