# Sort Linked List

# Problem Statement:
# Given a linked list, sort it using merge sort algorithm.
# Merge sort is preferred for linked lists due to O(1) space complexity.

# Examples:
# Example 1:
#   Input:  4 -> 2 -> 1 -> 3 -> None
#   Output: 1 -> 2 -> 3 -> 4 -> None


class Node:
    def __init__(self, data):
        # TODO: Implement node initialization
        pass


class LinkedList:
    def __init__(self):
        # TODO: Initialize head
        pass

    def sort_list(self):
        """
        Sort the linked list using merge sort
        Time Complexity: O(n log n)
        Space Complexity: O(log n) for recursion stack
        """
        # TODO: Implement merge sort
        pass

    def print_list(self):
        # TODO: Implement print functionality
        pass


# --- Run & Test ---
ll1 = LinkedList()
ll1.head = Node(4)
ll1.head.next = Node(2)
ll1.head.next.next = Node(1)
ll1.head.next.next.next = Node(3)
print("Before sorting:")
ll1.print_list()
ll1.sort_list()
print("After sorting:")
ll1.print_list()  # expected: 1 -> 2 -> 3 -> 4 -> None
