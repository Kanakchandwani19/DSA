# Infix to Postfix Conversion

# Problem Statement:
# Convert an infix expression to postfix notation.
# Infix: A + B
# Postfix: A B +
#
# Operators: +, -, *, /, ^
# Precedence: ^ > *, / > +, -
# Associativity: ^ is right-to-left, others are left-to-right

# Examples:
# Example 1:
#   Input:  "A+B"
#   Output: "AB+"

# Example 2:
#   Input:  "A+B*C"
#   Output: "ABC*+"

# Example 3:
#   Input:  "(A+B)*C"
#   Output: "AB+C*"

# Example 4:
#   Input:  "A+B*C-D"
#   Output: "ABC*+D-"

# Difficulty: Medium


def infix_to_postfix(expression):
    # Write your code here
    # Hint: Use a stack for operators
    # For operands: add directly to result
    # For '(': push to stack
    # For ')': pop until '(' is found
    # For operators: pop operators with higher/equal precedence, then push current
    pass


# --- Run & Test ---
print(infix_to_postfix("A+B"))          # expected: "AB+"
print(infix_to_postfix("A+B*C"))        # expected: "ABC*+"
print(infix_to_postfix("(A+B)*C"))      # expected: "AB+C*"
print(infix_to_postfix("A+B*C-D"))      # expected: "ABC*+D-"
