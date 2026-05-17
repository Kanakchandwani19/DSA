# Add One to a Number Represented by Linked List

# Problem Statement:
# Given a linked list representing a number (head is most significant digit),
# add 1 to it and return the modified linked list.

# Examples:
# Example 1:
#   Input:  1 -> 2 -> 3 -> None (represents 123)
#   Output: 1 -> 2 -> 4 -> None (represents 124)

# Example 2:
#   Input:  9 -> 9 -> 9 -> None (represents 999)
#   Output: 1 -> 0 -> 0 -> 0 -> None (represents 1000)


class Node:
    def __init__(self, data):
        # TODO: Implement node initialization
        pass


class LinkedList:
    def __init__(self):
        # TODO: Initialize head
        pass

    def add_one(self):
        """
        Add one to the number represented by linked list
        Time Complexity: O(n)
        Space Complexity: O(1) or O(n) depending on approach
        """
        # TODO: Implement adding one to the number
        pass

    def print_list(self):
        # TODO: Implement print functionality
        pass


# --- Run & Test ---
ll1 = LinkedList()
ll1.head = Node(1)
ll1.head.next = Node(2)
ll1.head.next.next = Node(3)
print("Before adding 1:")
ll1.print_list()  # expected: 1 -> 2 -> 3
ll1.add_one()
print("After adding 1:")
ll1.print_list()  # expected: 1 -> 2 -> 4

ll2 = LinkedList()
ll2.head = Node(9)
ll2.head.next = Node(9)
ll2.head.next.next = Node(9)
print("\nBefore adding 1:")
ll2.print_list()  # expected: 9 -> 9 -> 9
ll2.add_one()
print("After adding 1:")
ll2.print_list()  # expected: 1 -> 0 -> 0 -> 0
