# Delete Head of Doubly Linked List

# Problem Statement:
# Given a doubly linked list, delete the head node and return the new head.
# This operation should have O(1) time complexity.

# Examples:
# Example 1:
#   Input:  List = 1 <-> 2 <-> 3 <-> 4 -> None
#   Output: 2 <-> 3 <-> 4 -> None

# Example 2:
#   Input:  List = 5 -> None
#   Output: None (empty list)

# Example 3:
#   Input:  List = None (empty list)
#   Output: None (no change)


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

    def delete_head(self):
        """
        Delete the head node of the doubly linked list
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        # TODO: Implement deletion of head
        if self.head == None:
            return None
        self.head = self.head.next


    def print_forward(self):
        """Print all elements from head to tail"""
        # TODO: Implement forward print functionality
        curr = self.head

        while curr:
            print(curr.data, end = " -> ")
            curr = curr.next

        print("None")


# --- Run & Test ---

# Example 1: Delete head from list with multiple nodes
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
dll1.delete_head()
print("After deleting head:")
dll1.print_forward()  # expected: 2 <-> 3 <-> 4 -> None

# Example 2: Delete head from single node list
dll2 = DoublyLinkedList()
dll2.head = DoublyNode(5)
print("\nExample 2 - Before:")
dll2.print_forward()  # expected: 5 -> None
dll2.delete_head()
print("After deleting head:")
dll2.print_forward()  # expected: None

# Example 3: Delete head from empty list
dll3 = DoublyLinkedList()
print("\nExample 3 - Before:")
dll3.print_forward()  # expected: None
dll3.delete_head()
print("After deleting head:")
dll3.print_forward()  # expected: None
