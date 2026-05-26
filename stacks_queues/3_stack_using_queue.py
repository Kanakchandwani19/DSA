# Implement Stack using Queue

# Problem Statement:
# Implement a stack using only queue operations.
# The implemented stack should support all the functions of a normal stack (push, pop, top, empty).
# You can use only standard queue operations (enqueue, dequeue, front, is_empty).

# Examples:
# Example 1:
#   stack = StackUsingQueue()
#   stack.push(1)
#   stack.push(2)
#   print(stack.top())   # Output: 2
#   print(stack.pop())   # Output: 2
#   print(stack.empty()) # Output: False

# Difficulty: Easy


from collections import deque

class StackUsingQueue:
    def __init__(self):
        # Write your code here
        # Hint: Use one or two queues
        pass

    def push(self, x):
        # Write your code here
        # Hint: After adding element, rotate the queue so that new element is at front
        # Example: Add x, then move all previous elements to back
        pass

    def pop(self):
        # Write your code here
        # Hint: Remove and return front element from queue
        pass

    def top(self):
        # Write your code here
        # Hint: Return front element without removing
        pass

    def empty(self):
        # Write your code here
        pass


# --- Run & Test ---
stack = StackUsingQueue()
stack.push(1)
stack.push(2)
print(stack.top())      # expected: 2
print(stack.pop())      # expected: 2
print(stack.empty())    # expected: False
print(stack.pop())      # expected: 1
print(stack.empty())    # expected: True
