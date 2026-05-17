# Sort a Linked List of 0's, 1's and 2's

# Problem Statement:
# Given a linked list containing only 0s, 1s, and 2s, sort it in a single pass.
# Use the Dutch National Flag algorithm approach.

# Examples:
# Example 1:
#   Input:  1 -> 2 -> 0 -> 1 -> 0 -> 2 -> None
#   Output: 0 -> 0 -> 1 -> 1 -> 2 -> 2 -> None


class Node:
    def __init__(self, data):
        # TODO: Implement node initialization
        pass


class LinkedList:
    def __init__(self):
        # TODO: Initialize head
        pass

    def sort_012(self):
        """
        Sort linked list containing 0s, 1s, and 2s
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement sorting of 0s, 1s, and 2s
        pass

    def print_list(self):
        # TODO: Implement print functionality
        pass


# --- Run & Test ---
ll1 = LinkedList()
ll1.head = Node(1)
ll1.head.next = Node(2)
ll1.head.next.next = Node(0)
ll1.head.next.next.next = Node(1)
ll1.head.next.next.next.next = Node(0)
ll1.head.next.next.next.next.next = Node(2)
print("Before sorting:")
ll1.print_list()
ll1.sort_012()
print("After sorting:")
ll1.print_list()  # expected: 0 -> 0 -> 1 -> 1 -> 2 -> 2 -> None
