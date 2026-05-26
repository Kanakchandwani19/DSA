# Implement Min Stack

# Problem Statement:
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# Implement the MinStack class:
# - push(x): Push element x onto stack
# - pop(): Remove the element on top of the stack
# - top(): Get the top element
# - get_min(): Retrieve the minimum element in the stack in O(1) time

# Examples:
# Example 1:
#   min_stack = MinStack()
#   min_stack.push(-2)
#   min_stack.push(0)
#   min_stack.push(-3)
#   print(min_stack.get_min())  # Output: -3
#   min_stack.pop()
#   print(min_stack.top())      # Output: 0
#   print(min_stack.get_min())  # Output: -2

# Difficulty: Easy


class MinStack:
    def __init__(self):
        # Write your code here
        # Hint: Use two stacks - one for elements, one for minimum values
        pass

    def push(self, x):
        # Write your code here
        # Hint: Push to main stack
        # Push to min stack if x is less than or equal to current min
        pass

    def pop(self):
        # Write your code here
        # Hint: Pop from main stack
        # Pop from min stack if popped value equals current min
        pass

    def top(self):
        # Write your code here
        pass

    def get_min(self):
        # Write your code here
        # Hint: Return top of min stack
        pass


# --- Run & Test ---
min_stack = MinStack()
min_stack.push(-2)
min_stack.push(0)
min_stack.push(-3)
print(min_stack.get_min())   # expected: -3
min_stack.pop()
print(min_stack.top())       # expected: 0
print(min_stack.get_min())   # expected: -2
