# Deletion of the Head of Linked List

# Problem Statement:
# Given a linked list, delete the head node and return the new head.
# This operation should have O(1) time complexity.

# Examples:
# Example 1:
#   Input:  List = 1 -> 2 -> 3 -> 4 -> None
#   Output: 2 -> 3 -> 4 -> None

# Example 2:
#   Input:  List = 5 -> None
#   Output: None (empty list)

# Example 3:
#   Input:  List = None (empty list)
#   Output: None (no change)


class Node:
    """Node class represents a single node in a linked list"""
    def __init__(self, data):
        # TODO: Implement node initialization
        self.data = data
        self.next = None


class LinkedList:
    """LinkedList class to manage nodes"""
    def __init__(self):
        # TODO: Initialize head
        self.head = None

    def delete_head(self):
        """
        Delete the head node of the linked list
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        # TODO: Implement deletion of head
        if self.head == None:
            return None
        self.head = self.head.next

    def print_list(self):
        """Print all elements in the linked list"""
        # TODO: Implement print functionality
        curr = self.head
        while curr:
            print(curr.data, end = " -> ")
            curr =  curr.next
        print("None")


# --- Run & Test ---

# Example 1: Delete head from list with multiple nodes
ll1 = LinkedList()
ll1.head = Node(1)
ll1.head.next = Node(2)
ll1.head.next.next = Node(3)
ll1.head.next.next.next = Node(4)
print("Example 1 - Before:")
ll1.print_list()  # expected: 1 -> 2 -> 3 -> 4 -> None
ll1.delete_head()
print("After deleting head:")
ll1.print_list()  # expected: 2 -> 3 -> 4 -> None

# Example 2: Delete head from single node list
ll2 = LinkedList()
ll2.head = Node(5)
print("\nExample 2 - Before:")
ll2.print_list()  # expected: 5 -> None
ll2.delete_head()
print("After deleting head:")
ll2.print_list()  # expected: None

# Example 3: Delete head from empty list
ll3 = LinkedList()
print("\nExample 3 - Before:")
ll3.print_list()  # expected: None
ll3.delete_head()
print("After deleting head:")
ll3.print_list()  # expected: None
