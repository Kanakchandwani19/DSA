# Delete All Occurrences of a Key in Doubly Linked List

# Problem Statement:
# Given a doubly linked list and a key, delete all nodes that have the given key value.

# Examples:
# Example 1:
#   Input:  List = 1 <-> 2 <-> 3 <-> 2 <-> 4 -> None, key = 2
#   Output: 1 <-> 3 <-> 4 -> None

# Example 2:
#   Input:  List = 5 <-> 5 <-> 5 -> None, key = 5
#   Output: None (all nodes deleted)

# Example 3:
#   Input:  List = 10 <-> 20 <-> 30 -> None, key = 40
#   Output: 10 <-> 20 <-> 30 -> None (no change)


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

    def delete_all_occurrences(self, key):
        """
        Delete all nodes with the given key value
        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(1)
        """
        # TODO: Implement deletion of all occurrences
        pass

    def print_forward(self):
        """Print all elements from head to tail"""
        # TODO: Implement forward print functionality
        pass


# --- Run & Test ---

# Example 1: Delete all occurrences of 2
dll1 = DoublyLinkedList()
dll1.head = DoublyNode(1)
dll1.head.next = DoublyNode(2)
dll1.head.next.prev = dll1.head
dll1.head.next.next = DoublyNode(3)
dll1.head.next.next.prev = dll1.head.next
dll1.head.next.next.next = DoublyNode(2)
dll1.head.next.next.next.prev = dll1.head.next.next
dll1.head.next.next.next.next = DoublyNode(4)
dll1.head.next.next.next.next.prev = dll1.head.next.next.next
print("Example 1 - Before:")
dll1.print_forward()  # expected: 1 <-> 2 <-> 3 <-> 2 <-> 4 -> None
dll1.delete_all_occurrences(2)
print("After deleting all 2s:")
dll1.print_forward()  # expected: 1 <-> 3 <-> 4 -> None

# Example 2: Delete all nodes (all same value)
dll2 = DoublyLinkedList()
dll2.head = DoublyNode(5)
dll2.head.next = DoublyNode(5)
dll2.head.next.prev = dll2.head
dll2.head.next.next = DoublyNode(5)
dll2.head.next.next.prev = dll2.head.next
print("\nExample 2 - Before:")
dll2.print_forward()  # expected: 5 <-> 5 <-> 5 -> None
dll2.delete_all_occurrences(5)
print("After deleting all 5s:")
dll2.print_forward()  # expected: None

# Example 3: Key not present
dll3 = DoublyLinkedList()
dll3.head = DoublyNode(10)
dll3.head.next = DoublyNode(20)
dll3.head.next.prev = dll3.head
dll3.head.next.next = DoublyNode(30)
dll3.head.next.next.prev = dll3.head.next
print("\nExample 3 - Before:")
dll3.print_forward()  # expected: 10 <-> 20 <-> 30 -> None
dll3.delete_all_occurrences(40)
print("After deleting all 40s:")
dll3.print_forward()  # expected: 10 <-> 20 <-> 30 -> None
