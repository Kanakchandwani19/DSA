# Insertion at the Head of Linked List

# Problem Statement:
# Given a linked list, insert a new node with given data at the beginning (head) of the list.
# This operation should have O(1) time complexity.

# Examples:
# Example 1:
#   Input:  List = 2 -> 3 -> 4 -> None, data = 1
#   Output: 1 -> 2 -> 3 -> 4 -> None

# Example 2:
#   Input:  List = None (empty list), data = 5
#   Output: 5 -> None

# Example 3:
#   Input:  List = 10 -> None, data = 20
#   Output: 20 -> 10 -> None


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

    def insert_at_head(self, data):
        """
        Insert a new node at the beginning of the linked list
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        # TODO: Implement insertion at head
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

        

    def print_list(self):
        """Print all elements in the linked list"""
        # TODO: Implement print functionality
        curr = self.head 
        while curr:
            print(curr.data, end = " -> ")
            curr = curr.next
        print("None")


# --- Run & Test ---

# Example 1: Insert at head of existing list
ll1 = LinkedList()
ll1.head = Node(2)
ll1.head.next = Node(3)
ll1.head.next.next = Node(4)
print("Example 1 - Before:")
ll1.print_list()  # expected: 2 -> 3 -> 4 -> None
ll1.insert_at_head(1)
print("After inserting 1 at head:")
ll1.print_list()  # expected: 1 -> 2 -> 3 -> 4 -> None

# Example 2: Insert at head of empty list
ll2 = LinkedList()
print("\nExample 2 - Before:")
ll2.print_list()  # expected: None
ll2.insert_at_head(5)
print("After inserting 5 at head:")
ll2.print_list()  # expected: 5 -> None

# Example 3: Multiple insertions at head
ll3 = LinkedList()
ll3.insert_at_head(10)
print("\nExample 3:")
ll3.print_list()  # expected: 10 -> None
ll3.insert_at_head(20)
ll3.print_list()  # expected: 20 -> 10 -> None
ll3.insert_at_head(30)
ll3.print_list()  # expected: 30 -> 20 -> 10 -> None
