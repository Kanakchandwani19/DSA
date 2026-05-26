# Implement Queue using LinkedList

# Problem Statement:
# Implement a queue using linked list with the following operations:
# - enqueue(x): Add element x to the rear of the queue
# - dequeue(): Remove and return the element from the front of the queue
# - front(): Return the front element without removing it
# - is_empty(): Check if the queue is empty

# Examples:
# Example 1:
#   queue = QueueUsingLinkedList()
#   queue.enqueue(1)
#   queue.enqueue(2)
#   queue.enqueue(3)
#   print(queue.front())    # Output: 1
#   print(queue.dequeue())  # Output: 1
#   print(queue.front())    # Output: 2

# Difficulty: Easy


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class QueueUsingLinkedList:
    def __init__(self):
        # Write your code here
        # Hint: Initialize front and rear as None
        pass

    def enqueue(self, x):
        # Write your code here
        # Hint: Create new node and add it to rear
        pass

    def dequeue(self):
        # Write your code here
        # Hint: Check if queue is empty, then remove and return front data
        pass

    def front(self):
        # Write your code here
        # Hint: Return front data without removing
        pass

    def is_empty(self):
        # Write your code here
        pass


# --- Run & Test ---
queue = QueueUsingLinkedList()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.front())       # expected: 1
print(queue.dequeue())     # expected: 1
print(queue.front())       # expected: 2
print(queue.is_empty())    # expected: False
queue.dequeue()
queue.dequeue()
print(queue.is_empty())    # expected: True
