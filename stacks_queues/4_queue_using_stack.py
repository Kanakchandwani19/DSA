# Implement Queue using Stack

# Problem Statement:
# Implement a queue using only stack operations.
# The implemented queue should support all the functions of a normal queue (enqueue, dequeue, front, empty).
# You can use only standard stack operations (push, pop, peek, is_empty).

# Examples:
# Example 1:
#   queue = QueueUsingStack()
#   queue.enqueue(1)
#   queue.enqueue(2)
#   print(queue.front())    # Output: 1
#   print(queue.dequeue())  # Output: 1
#   print(queue.empty())    # Output: False

# Difficulty: Easy


class QueueUsingStack:
    def __init__(self):
        # Write your code here
        # Hint: Use two stacks - one for enqueue, one for dequeue
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x):
        # Write your code here
        # Hint: Simply push to the first stack
        self.stack1.append(x)


    def dequeue(self):
        # Write your code here
        # Hint: If second stack is empty, transfer all elements from first stack
        # Then pop from second stack
        if self.empty():
            return "Empty"

        if not self.stack2:

            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()
                
    

    def front(self):
        # Write your code here
        # Hint: Similar to dequeue, but peek instead of pop
        if self.empty():
            return "Empty"

        if not self.stack2:

            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2[-1]

    def empty(self):
        # Write your code here
        # Hint: Queue is empty when both stacks are empty
        return (len(self.stack1) == 0 and len(self.stack2) == 0)


# --- Run & Test ---
queue = QueueUsingStack()
queue.enqueue(1)
queue.enqueue(2)
print(queue.front())       # expected: 1
print(queue.dequeue())     # expected: 1
print(queue.empty())       # expected: False
print(queue.dequeue())     # expected: 2
print(queue.empty())       # expected: True
