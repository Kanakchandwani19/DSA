# Middle of a LinkedList [Tortoise-Hare Method]

# Problem Statement:
# Given a singly linked list, find the middle node. If there are two middle nodes,
# return the second middle node. Use the slow-fast pointer (tortoise-hare) technique.

# Examples:
# Example 1:
#   Input:  1 -> 2 -> 3 -> 4 -> 5 -> None
#   Output: 3 (middle node)

# Example 2:
#   Input:  1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
#   Output: 4 (second middle node)

# Example 3:
#   Input:  1 -> None
#   Output: 1


class Node:
    """Node class represents a single node in a linked list"""
    def __init__(self, data):
        # TODO: Implement node initialization
        pass


class LinkedList:
    """LinkedList class to manage nodes"""
    def __init__(self):
        # TODO: Initialize head
        pass

    def find_middle(self):
        """
        Find the middle node using tortoise-hare (slow-fast pointer) method
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement find middle functionality
        pass

    def print_list(self):
        """Print all elements in the linked list"""
        # TODO: Implement print functionality
        pass


# --- Run & Test ---

# Example 1: Odd number of nodes
ll1 = LinkedList()
ll1.head = Node(1)
ll1.head.next = Node(2)
ll1.head.next.next = Node(3)
ll1.head.next.next.next = Node(4)
ll1.head.next.next.next.next = Node(5)
print("Example 1:")
ll1.print_list()
middle = ll1.find_middle()
print(f"Middle node: {middle.data if middle else None}")  # expected: 3

# Example 2: Even number of nodes
ll2 = LinkedList()
ll2.head = Node(1)
ll2.head.next = Node(2)
ll2.head.next.next = Node(3)
ll2.head.next.next.next = Node(4)
ll2.head.next.next.next.next = Node(5)
ll2.head.next.next.next.next.next = Node(6)
print("\nExample 2:")
ll2.print_list()
middle = ll2.find_middle()
print(f"Middle node: {middle.data if middle else None}")  # expected: 4

# Example 3: Single node
ll3 = LinkedList()
ll3.head = Node(1)
print("\nExample 3:")
ll3.print_list()
middle = ll3.find_middle()
print(f"Middle node: {middle.data if middle else None}")  # expected: 1
