# Prefix to Infix Conversion

# Problem Statement:
# Convert a prefix expression to infix notation.
# Prefix: +AB
# Infix: (A+B)

# Examples:
# Example 1:
#   Input:  "+AB"
#   Output: "(A+B)"

# Example 2:
#   Input:  "*+ABC"
#   Output: "((A+B)*C)"

# Example 3:
#   Input:  "*-A/BC-/AKL"
#   Output: "((A-(B/C))*((A/K)-L))"

# Difficulty: Medium


def prefix_to_infix(expression):
    # Write your code here
    # Hint: Use a stack, traverse from right to left
    # For operands: push to stack
    # For operators: pop two operands, create infix string (op1 operator op2), push back
    pass


# --- Run & Test ---
print(prefix_to_infix("+AB"))              # expected: "(A+B)"
print(prefix_to_infix("*+ABC"))            # expected: "((A+B)*C)"
print(prefix_to_infix("*-A/BC-/AKL"))      # expected: "((A-(B/C))*((A/K)-L))"
