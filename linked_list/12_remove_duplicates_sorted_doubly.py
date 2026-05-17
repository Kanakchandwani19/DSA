# Remove Duplicates from Sorted Doubly Linked List

# Problem Statement:
# Given a sorted doubly linked list, remove all duplicate nodes,
# keeping only the first occurrence of each value.

# Examples:
# Example 1:
#   Input:  1 <-> 1 <-> 2 <-> 3 <-> 3 <-> 4 -> None
#   Output: 1 <-> 2 <-> 3 <-> 4 -> None

# Example 2:
#   Input:  1 <-> 1 <-> 1 <-> 1 -> None
#   Output: 1 -> None

# Example 3:
#   Input:  1 <-> 2 <-> 3 -> None
#   Output: 1 <-> 2 <-> 3 -> None (no duplicates)


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

    def remove_duplicates(self):
        """
        Remove duplicate nodes from sorted doubly linked list
        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(1)
        """
        # TODO: Implement remove duplicates functionality
        pass

    def print_forward(self):
        """Print all elements from head to tail"""
        # TODO: Implement forward print functionality
        pass


# --- Run & Test ---

# Example 1: Remove duplicates from list with several duplicates
dll1 = DoublyLinkedList()
dll1.head = DoublyNode(1)
dll1.head.next = DoublyNode(1)
dll1.head.next.prev = dll1.head
dll1.head.next.next = DoublyNode(2)
dll1.head.next.next.prev = dll1.head.next
dll1.head.next.next.next = DoublyNode(3)
dll1.head.next.next.next.prev = dll1.head.next.next
dll1.head.next.next.next.next = DoublyNode(3)
dll1.head.next.next.next.next.prev = dll1.head.next.next.next
dll1.head.next.next.next.next.next = DoublyNode(4)
dll1.head.next.next.next.next.next.prev = dll1.head.next.next.next.next
print("Example 1 - Before:")
dll1.print_forward()  # expected: 1 <-> 1 <-> 2 <-> 3 <-> 3 <-> 4 -> None
dll1.remove_duplicates()
print("After removing duplicates:")
dll1.print_forward()  # expected: 1 <-> 2 <-> 3 <-> 4 -> None

# Example 2: All nodes are duplicates
dll2 = DoublyLinkedList()
dll2.head = DoublyNode(1)
dll2.head.next = DoublyNode(1)
dll2.head.next.prev = dll2.head
dll2.head.next.next = DoublyNode(1)
dll2.head.next.next.prev = dll2.head.next
dll2.head.next.next.next = DoublyNode(1)
dll2.head.next.next.next.prev = dll2.head.next.next
print("\nExample 2 - Before:")
dll2.print_forward()  # expected: 1 <-> 1 <-> 1 <-> 1 -> None
dll2.remove_duplicates()
print("After removing duplicates:")
dll2.print_forward()  # expected: 1 -> None

# Example 3: No duplicates
dll3 = DoublyLinkedList()
dll3.head = DoublyNode(1)
dll3.head.next = DoublyNode(2)
dll3.head.next.prev = dll3.head
dll3.head.next.next = DoublyNode(3)
dll3.head.next.next.prev = dll3.head.next
print("\nExample 3 - Before:")
dll3.print_forward()  # expected: 1 <-> 2 <-> 3 -> None
dll3.remove_duplicates()
print("After removing duplicates:")
dll3.print_forward()  # expected: 1 <-> 2 <-> 3 -> None
