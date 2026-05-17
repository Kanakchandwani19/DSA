# Reverse a Doubly Linked List

# Problem Statement:
# Given a doubly linked list, reverse it so that the last node becomes the head
# and all next/prev pointers are swapped.

# Examples:
# Example 1:
#   Input:  1 <-> 2 <-> 3 <-> 4 -> None
#   Output: 4 <-> 3 <-> 2 <-> 1 -> None

# Example 2:
#   Input:  10 <-> 20 -> None
#   Output: 20 <-> 10 -> None

# Example 3:
#   Input:  5 -> None
#   Output: 5 -> None


class DoublyNode:
    """DoublyNode class represents a single node in a doubly linked list"""
    def __init__(self, data):
        # TODO: Implement node initialization with data, next, and prev
        pass


class DoublyLinkedList:
    """DoublyLinkedList class to manage nodes"""
    def __init__(self):
        # TODO: Initialize head
        pass

    def reverse(self):
        """
        Reverse the doubly linked list
        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(1)
        """
        # TODO: Implement reverse functionality
        pass

    def print_forward(self):
        """Print all elements from head to tail"""
        # TODO: Implement forward print functionality
        pass


# --- Run & Test ---

# Example 1: Reverse list with multiple nodes
dll1 = DoublyLinkedList()
dll1.head = DoublyNode(1)
dll1.head.next = DoublyNode(2)
dll1.head.next.prev = dll1.head
dll1.head.next.next = DoublyNode(3)
dll1.head.next.next.prev = dll1.head.next
dll1.head.next.next.next = DoublyNode(4)
dll1.head.next.next.next.prev = dll1.head.next.next
print("Example 1 - Before:")
dll1.print_forward()  # expected: 1 <-> 2 <-> 3 <-> 4 -> None
dll1.reverse()
print("After reversing:")
dll1.print_forward()  # expected: 4 <-> 3 <-> 2 <-> 1 -> None

# Example 2: Reverse list with two nodes
dll2 = DoublyLinkedList()
dll2.head = DoublyNode(10)
dll2.head.next = DoublyNode(20)
dll2.head.next.prev = dll2.head
print("\nExample 2 - Before:")
dll2.print_forward()  # expected: 10 <-> 20 -> None
dll2.reverse()
print("After reversing:")
dll2.print_forward()  # expected: 20 <-> 10 -> None

# Example 3: Reverse single node list
dll3 = DoublyLinkedList()
dll3.head = DoublyNode(5)
print("\nExample 3 - Before:")
dll3.print_forward()  # expected: 5 -> None
dll3.reverse()
print("After reversing:")
dll3.print_forward()  # expected: 5 -> None
