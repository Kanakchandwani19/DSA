# Prefix to Postfix Conversion

# Problem Statement:
# Convert a prefix expression to postfix notation.
# Prefix: +AB
# Postfix: AB+

# Examples:
# Example 1:
#   Input:  "+AB"
#   Output: "AB+"

# Example 2:
#   Input:  "*+ABC"
#   Output: "AB+C*"

# Example 3:
#   Input:  "*-A/BC-/AKL"
#   Output: "ABC/-AK/L-*"

# Difficulty: Medium


def prefix_to_postfix(expression):
    # Write your code here
    # Hint: Use a stack, traverse from right to left
    # For operands: push to stack
    # For operators: pop two operands, create postfix string (op1 op2 operator), push back
    stack = []

    for ch in reversed(expression):

        if ch.isalnum():
            stack.append(ch)

        else:
            op1 = stack.pop()
            op2 = stack.pop()

            new_exp = op1 + op2 + ch
            stack.append(new_exp)

    return stack[-1]




# --- Run & Test ---
print(prefix_to_postfix("+AB"))              # expected: "AB+"
print(prefix_to_postfix("*+ABC"))            # expected: "AB+C*"
print(prefix_to_postfix("*-A/BC-/AKL"))      # expected: "ABC/-AK/L-*"
