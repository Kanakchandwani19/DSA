# Implement Queue using Arrays

# Problem Statement:
# Implement a queue using arrays with the following operations:
# - enqueue(x): Add element x to the rear of the queue
# - dequeue(): Remove and return the element from the front of the queue
# - front(): Return the front element without removing it
# - is_empty(): Check if the queue is empty
# - size(): Return the number of elements in the queue

# Examples:
# Example 1:
#   queue = Queue()
#   queue.enqueue(1)
#   queue.enqueue(2)
#   queue.enqueue(3)
#   print(queue.front())    # Output: 1
#   print(queue.dequeue())  # Output: 1
#   print(queue.size())     # Output: 2

# Difficulty: Easy


class Queue:
    def __init__(self):
        # Write your code here
        # Hint: Initialize an empty list to store elements
        self.queue = []

    def enqueue(self, x):
        # Write your code here
        # Hint: Append element to the end of list
        self.queue.append(x)

    def dequeue(self):
        # Write your code here
        # Hint: Check if queue is empty, then remove and return first element
        if self.is_empty():
            return "Queue is Empty"

        return self.queue.pop(0)

    def front(self):
        # Write your code here
        # Hint: Return first element without removing
        if self.is_empty():
            return "Queue is Empty"

        return self.queue[0]

    def is_empty(self):
        # Write your code here
        return len(self.queue) == 0

    def size(self):
        # Write your code here
        return len(self.queue)


# --- Run & Test ---
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.front())       # expected: 1
print(queue.dequeue())     # expected: 1
print(queue.size())        # expected: 2
print(queue.is_empty())    # expected: False
queue.dequeue()
queue.dequeue()
print(queue.is_empty())    # expected: True
