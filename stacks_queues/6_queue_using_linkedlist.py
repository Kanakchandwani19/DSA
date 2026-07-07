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
        self.front_node = None
        self.rear_node = None
        self.count = 0

    def enqueue(self, x):
        # Write your code here
        # Hint: Create new node and add it to rear
        new_node = Node(x)

        if self.is_empty():

            self.front_node = new_node
            self.rear_node = new_node

        else:
            self.rear_node.next = new_node
            self.rear_node = new_node

        self.count += 1


    def dequeue(self):
        # Write your code here
        # Hint: Check if queue is empty, then remove and return front data
        if self.is_empty():
            return "Empty"

        removed = self.front_node.data

        self.front_node = self.front_node.next

        self.count -= 1

        if self.front_node is None:
            self.rear_node = None

        return removed

    def front(self):
        # Write your code here
        # Hint: Return front data without removing
        if self.is_empty():
            return "Empty"

        return self.front_node.data

    def is_empty(self):
        # Write your code here
        return self.front_node is None


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
