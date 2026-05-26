# Postfix to Infix Conversion

# Problem Statement:
# Convert a postfix expression to infix notation.
# Postfix: AB+
# Infix: (A+B)

# Examples:
# Example 1:
#   Input:  "AB+"
#   Output: "(A+B)"

# Example 2:
#   Input:  "AB+C*"
#   Output: "((A+B)*C)"

# Example 3:
#   Input:  "ABC/-AK/L-*"
#   Output: "((A-(B/C))*((A/K)-L))"

# Difficulty: Easy


def postfix_to_infix(expression):
    # Write your code here
    # Hint: Use a stack, traverse from left to right
    # For operands: push to stack
    # For operators: pop two operands, create infix string (op2 operator op1), push back
    pass


# --- Run & Test ---
print(postfix_to_infix("AB+"))              # expected: "(A+B)"
print(postfix_to_infix("AB+C*"))            # expected: "((A+B)*C)"
print(postfix_to_infix("ABC/-AK/L-*"))      # expected: "((A-(B/C))*((A/K)-L))"
