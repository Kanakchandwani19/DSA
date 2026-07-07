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
def precedence(op):

    if op == '+' or op == '-':
        return 1

    elif op == '*' or op == '/':
        return 2

    elif op == '^':
        return 3 

    return 0


def infix_to_postfix(expression):
    # Write your code here
    # Hint: Use a stack for operators
    # For operands: add directly to result
    # For '(': push to stack
    # For ')': pop until '(' is found
    # For operators: pop operators with higher/equal precedence, then push current
    
    stack = []
    result = ""

    for ch in expression:

        if ch.isalnum():
            result += ch

        elif ch == '(':
            stack.append(ch)

        elif ch == ')':

            while stack and stack[-1] != '(':
                result += stack.pop()

            stack.pop()

        else:
            while (stack and precedence(stack[-1]) >= precedence(ch)):
                result += stack.pop()

            stack.append(ch)

    while stack:
        result += stack.pop()

    return result


    


# --- Run & Test ---
print(infix_to_postfix("A+B"))          # expected: "AB+"
print(infix_to_postfix("A+B*C"))        # expected: "ABC*+"
print(infix_to_postfix("(A+B)*C"))      # expected: "AB+C*"
print(infix_to_postfix("A+B*C-D"))      # expected: "ABC*+D-"
