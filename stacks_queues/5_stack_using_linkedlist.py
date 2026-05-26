# Implement Stack using LinkedList

# Problem Statement:
# Implement a stack using linked list with the following operations:
# - push(x): Push element x onto stack
# - pop(): Remove and return the element on top of the stack
# - peek(): Return the top element without removing it
# - is_empty(): Check if the stack is empty

# Examples:
# Example 1:
#   stack = StackUsingLinkedList()
#   stack.push(1)
#   stack.push(2)
#   stack.push(3)
#   print(stack.peek())  # Output: 3
#   print(stack.pop())   # Output: 3
#   print(stack.pop())   # Output: 2

# Difficulty: Easy


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class StackUsingLinkedList:
    def __init__(self):
        # Write your code here
        # Hint: Initialize head as None
        pass

    def push(self, x):
        # Write your code here
        # Hint: Create new node and make it the new head
        pass

    def pop(self):
        # Write your code here
        # Hint: Check if stack is empty, then remove and return head data
        pass

    def peek(self):
        # Write your code here
        # Hint: Return head data without removing
        pass

    def is_empty(self):
        # Write your code here
        pass


# --- Run & Test ---
stack = StackUsingLinkedList()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.peek())       # expected: 3
print(stack.pop())        # expected: 3
print(stack.pop())        # expected: 2
print(stack.is_empty())   # expected: False
stack.pop()
print(stack.is_empty())   # expected: True
