# Implement Stack using Arrays

# Problem Statement:
# Implement a stack using arrays with the following operations:
# - push(x): Push element x onto stack
# - pop(): Remove and return the element on top of the stack
# - peek(): Return the top element without removing it
# - is_empty(): Check if the stack is empty
# - size(): Return the number of elements in the stack

# Examples:
# Example 1:
#   stack = Stack()
#   stack.push(1)
#   stack.push(2)
#   stack.push(3)
#   print(stack.peek())  # Output: 3
#   print(stack.pop())   # Output: 3
#   print(stack.size())  # Output: 2

# Difficulty: Easy


class Stack:
    def __init__(self):
        # Write your code here
        # Hint: Initialize an empty list to store elements
        self.stack = []

    def push(self, x):
        # Write your code here
        # Hint: Append element to the end of list
        self.stack.append(x)


    def pop(self):
        # Write your code here
        # Hint: Check if stack is empty, then remove and return last element
        if self.is_empty():
            return "Stack is empty"

        return self.stack.pop()

    def peek(self):
        # Write your code here
        # Hint: Return last element without removing
        if self.is_empty():
                    return "Stack is empty"

        return self.stack[-1]

    def is_empty(self):
        # Write your code here
        return len(self.stack) == 0

    def size(self):
        # Write your code here
        return len(self.stack )


# --- Run & Test ---
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.peek())       # expected: 3
print(stack.pop())        # expected: 3
print(stack.size())       # expected: 2
print(stack.is_empty())   # expected: False
stack.pop()
stack.pop()
print(stack.is_empty())   # expected: True
