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
def precedence(op):
    if op == '^':
        return 3

    elif op == '*' or op == '/':
        return 2

    elif op == '+' or op == '-':
        return 1

    return 0


def infix_to_postfix(exp):
    # Write your code here
    # Hint:
    # 1. Reverse the infix expression
    # 2. Replace '(' with ')' and vice versa
    # 3. Convert to postfix
    # 4. Reverse the result

    stack = []
    result = ""

    for ch in exp:

        if ch.isalnum():
            result += ch

        elif ch == '(':
            stack.append(ch)

        elif ch == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()

            stack.pop()

        else:
            while (stack and stack[-1] != '(' and precedence(stack[-1]) >= precedence(ch)):
                result += stack.pop()

            stack.append(ch)

    while stack:
        result += stack.pop()

    return result 

def infix_to_prefix(expression):

    expression = expression[::-1]

    temp = ""

    for ch in expression:
        if ch == '(':
            temp += ')'

        elif ch == ')':
            temp += '('

        else:
            temp += ch

    postfix = infix_to_postfix(temp)

    return postfix[::-1]

    


# --- Run & Test ---
print(infix_to_prefix("A+B"))          # expected: "+AB"
print(infix_to_prefix("A+B*C"))        # expected: "+A*BC"
print(infix_to_prefix("(A+B)*C"))      # expected: "*+ABC"
print(infix_to_prefix("A+B*C-D"))      # expected: "-+A*BCD"
