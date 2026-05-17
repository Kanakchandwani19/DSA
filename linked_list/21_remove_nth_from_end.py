# Remove Nth Node from the End of Linked List

# Problem Statement:
# Given a linked list, remove the Nth node from the end and return the head.
# Use two-pointer technique with N+1 gap.

# Examples:
# Example 1:
#   Input:  1 -> 2 -> 3 -> 4 -> 5 -> None, N = 2
#   Output: 1 -> 2 -> 3 -> 5 -> None (removed 4)


class Node:
    def __init__(self, data):
        # TODO: Implement node initialization
        pass


class LinkedList:
    def __init__(self):
        # TODO: Initialize head
        pass

    def remove_nth_from_end(self, n):
        """
        Remove Nth node from the end
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement removal of Nth node from end
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
ll1.remove_nth_from_end(2)
print("After removing 2nd node from end:")
ll1.print_list()  # expected: 1 -> 2 -> 3 -> 5 -> None
