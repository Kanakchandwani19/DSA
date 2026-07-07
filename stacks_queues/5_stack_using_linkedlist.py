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
        self.top = None
        self.count = 0

    def push(self, x):
        # Write your code here
        # Hint: Create new node and make it the new head
        new_node = Node(x)

        new_node.next = self.top
        self.top = new_node

        self.count += 1

    def pop(self):
        # Write your code here
        # Hint: Check if stack is empty, then remove and return head data
        if self.is_empty():
            return "Empty"

        removed = self.top.data
        self.top = self.top.next

        self.count -= 1

        return removed

    def peek(self):
        # Write your code here
        # Hint: Return head data without removing
        if self.is_empty():
            return "Empty"

        return self.top.data

    def is_empty(self):
        # Write your code here
        return self.top is None


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
