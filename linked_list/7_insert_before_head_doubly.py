# Insert Node Before Head in Doubly Linked List

# Problem Statement:
# Given a doubly linked list, insert a new node with given data at the beginning (before head).
# This operation should have O(1) time complexity.

# Examples:
# Example 1:
#   Input:  List = 2 <-> 3 <-> 4 -> None, data = 1
#   Output: 1 <-> 2 <-> 3 <-> 4 -> None

# Example 2:
#   Input:  List = None (empty list), data = 5
#   Output: 5 -> None

# Example 3:
#   Input:  List = 10 -> None, data = 20
#   Output: 20 <-> 10 -> None


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

    def insert_before_head(self, data):
        """
        Insert a new node at the beginning of the doubly linked list
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        # TODO: Implement insertion before head
        pass

    def print_forward(self):
        """Print all elements from head to tail"""
        # TODO: Implement forward print functionality
        pass


# --- Run & Test ---

# Example 1: Insert before head of existing list
dll1 = DoublyLinkedList()
dll1.head = DoublyNode(2)
dll1.head.next = DoublyNode(3)
dll1.head.next.prev = dll1.head
dll1.head.next.next = DoublyNode(4)
dll1.head.next.next.prev = dll1.head.next
print("Example 1 - Before:")
dll1.print_forward()  # expected: 2 <-> 3 <-> 4 -> None
dll1.insert_before_head(1)
print("After inserting 1 before head:")
dll1.print_forward()  # expected: 1 <-> 2 <-> 3 <-> 4 -> None

# Example 2: Insert before head of empty list
dll2 = DoublyLinkedList()
print("\nExample 2 - Before:")
dll2.print_forward()  # expected: None
dll2.insert_before_head(5)
print("After inserting 5 before head:")
dll2.print_forward()  # expected: 5 -> None

# Example 3: Multiple insertions before head
dll3 = DoublyLinkedList()
dll3.insert_before_head(10)
print("\nExample 3:")
dll3.print_forward()  # expected: 10 -> None
dll3.insert_before_head(20)
dll3.print_forward()  # expected: 20 <-> 10 -> None
dll3.insert_before_head(30)
dll3.print_forward()  # expected: 30 <-> 20 <-> 10 -> None
