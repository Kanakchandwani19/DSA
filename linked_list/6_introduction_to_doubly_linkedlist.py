# Introduction to Doubly Linked List

# Problem Statement:
# A doubly linked list is a linear data structure where each node contains
# data and two pointers: one to the next node and one to the previous node.
# Implement a basic DoublyNode class and create a simple doubly linked list.

# Examples:
# Example 1:
#   Create a doubly linked list: None <- 1 <-> 2 <-> 3 <-> 4 -> None
#   Visual representation:
#   None <- [1] <-> [2] <-> [3] <-> [4] -> None

# Example 2:
#   Create a doubly linked list: None <- 10 <-> 20 <-> 30 -> None
#   Visual representation:
#   None <- [10] <-> [20] <-> [30] -> None


class DoublyNode:
    """DoublyNode class represents a single node in a doubly linked list"""
    def __init__(self, data):
        # TODO: Implement node initialization with data, next, and prev
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    """DoublyLinkedList class to manage nodes"""
    def __init__(self):
        # TODO: Initialize head
        self.head = None
        self.tail = None

    def print_forward(self):
        """Print all elements from head to tail"""
        # TODO: Implement forward print functionality
        curr = self.head

        while curr:
            print(curr.data, end = " -> ")
            curr = curr.next

        print("None")



    def print_backward(self):
        """Print all elements from tail to head"""
        # TODO: Implement backward print functionality
        curr = self.tail

        while curr:
            print(curr.data, end = " -> ")
            curr = curr.prev

        print("None")

    def append(self, data):
        """Add a node at the end of the doubly linked list"""
        # TODO: Implement append functionality
        new_node = DoublyNode(data)

        if self.head == None:
            self.head = new_node
            self.tail = new_node

            return
        
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node


# --- Run & Test ---

# Example 1: Create a doubly linked list 1 <-> 2 <-> 3 <-> 4
dll1 = DoublyLinkedList()
dll1.append(1)
dll1.append(2)
dll1.append(3)
dll1.append(4)
print("Example 1 - Forward:")
dll1.print_forward()  # expected: 1 <-> 2 <-> 3 <-> 4 -> None
print("Example 1 - Backward:")
dll1.print_backward()  # expected: 4 <-> 3 <-> 2 <-> 1 -> None

# Example 2: Create a doubly linked list 10 <-> 20 <-> 30
dll2 = DoublyLinkedList()
dll2.append(10)
dll2.append(20)
dll2.append(30)
print("\nExample 2 - Forward:")
dll2.print_forward()  # expected: 10 <-> 20 <-> 30 -> None
print("Example 2 - Backward:")
dll2.print_backward()  # expected: 30 <-> 20 <-> 10 -> None

# Example 3: Empty doubly linked list
dll3 = DoublyLinkedList()
print("\nExample 3 (Empty List) - Forward:")
dll3.print_forward()  # expected: None
print("Example 3 (Empty List) - Backward:")
dll3.print_backward()  # expected: None
