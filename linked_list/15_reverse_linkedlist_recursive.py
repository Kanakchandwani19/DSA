# Reverse a LinkedList [Recursive]

# Problem Statement:
# Given a singly linked list, reverse it recursively.

# Examples:
# Example 1:
#   Input:  1 -> 2 -> 3 -> 4 -> 5 -> None
#   Output: 5 -> 4 -> 3 -> 2 -> 1 -> None


class Node:
    def __init__(self, data):
        # TODO: Implement node initialization
        pass


class LinkedList:
    def __init__(self):
        # TODO: Initialize head
        pass

    def reverse_recursive(self, head):
        """
        Reverse the linked list recursively
        Time Complexity: O(n)
        Space Complexity: O(n) due to recursion stack
        """
        # TODO: Implement recursive reverse
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
ll1.print_list()
ll1.head = ll1.reverse_recursive(ll1.head)
print("After:")
ll1.print_list()
