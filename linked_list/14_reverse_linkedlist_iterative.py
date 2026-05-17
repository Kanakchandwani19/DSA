# Reverse a LinkedList [Iterative]

# Problem Statement:
# Given a singly linked list, reverse it iteratively.

# Examples:
# Example 1:
#   Input:  1 -> 2 -> 3 -> 4 -> 5 -> None
#   Output: 5 -> 4 -> 3 -> 2 -> 1 -> None

# Example 2:
#   Input:  1 -> 2 -> None
#   Output: 2 -> 1 -> None

# Example 3:
#   Input:  1 -> None
#   Output: 1 -> None


class Node:
    def __init__(self, data):
        # TODO: Implement node initialization
        pass


class LinkedList:
    def __init__(self):
        # TODO: Initialize head
        pass

    def reverse_iterative(self):
        """
        Reverse the linked list iteratively
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement iterative reverse
        pass

    def print_list(self):
        # TODO: Implement print functionality
        pass


# --- Run & Test ---
ll1 = LinkedList()
ll1.head = Node(1)
ll1.head.next = Node(2)
ll1.head.next.next = Node(3)
ll1.head.next.next.next = Node(4)
ll1.head.next.next.next.next = Node(5)
print("Before:")
ll1.print_list()  # expected: 1 -> 2 -> 3 -> 4 -> 5 -> None
ll1.reverse_iterative()
print("After:")
ll1.print_list()  # expected: 5 -> 4 -> 3 -> 2 -> 1 -> None
