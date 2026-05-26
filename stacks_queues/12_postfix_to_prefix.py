# Postfix to Prefix Conversion

# Problem Statement:
# Convert a postfix expression to prefix notation.
# Postfix: AB+
# Prefix: +AB

# Examples:
# Example 1:
#   Input:  "AB+"
#   Output: "+AB"

# Example 2:
#   Input:  "AB+C*"
#   Output: "*+ABC"

# Example 3:
#   Input:  "ABC/-AK/L-*"
#   Output: "*-A/BC-/AKL"

# Difficulty: Medium


def postfix_to_prefix(expression):
    # Write your code here
    # Hint: Use a stack, traverse from left to right
    # For operands: push to stack
    # For operators: pop two operands, create prefix string (operator op2 op1), push back
    pass


# --- Run & Test ---
print(postfix_to_prefix("AB+"))              # expected: "+AB"
print(postfix_to_prefix("AB+C*"))            # expected: "*+ABC"
print(postfix_to_prefix("ABC/-AK/L-*"))      # expected: "*-A/BC-/AKL"
