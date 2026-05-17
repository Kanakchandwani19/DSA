# Delete the Middle Node of Linked List

# Problem Statement:
# Given a linked list, delete the middle node.
# If there are two middle nodes, delete the second one.

# Examples:
# Example 1:
#   Input:  1 -> 2 -> 3 -> 4 -> 5 -> None
#   Output: 1 -> 2 -> 4 -> 5 -> None (deleted 3)


class Node:
    def __init__(self, data):
        # TODO: Implement node initialization
        pass


class LinkedList:
    def __init__(self):
        # TODO: Initialize head
        pass

    def delete_middle(self):
        """
        Delete the middle node
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement deletion of middle node
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
ll1.delete_middle()
print("After deleting middle:")
ll1.print_list()  # expected: 1 -> 2 -> 4 -> 5 -> None
