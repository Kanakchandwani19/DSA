# Segregate Odd and Even Nodes in Linked List

# Problem Statement:
# Given a linked list, segregate odd and even nodes such that all odd nodes
# come before even nodes, maintaining relative order.

# Examples:
# Example 1:
#   Input:  1 -> 2 -> 3 -> 4 -> 5 -> None
#   Output: 1 -> 3 -> 5 -> 2 -> 4 -> None


class Node:
    def __init__(self, data):
        # TODO: Implement node initialization
        pass


class LinkedList:
    def __init__(self):
        # TODO: Initialize head
        pass

    def segregate_odd_even(self):
        """
        Segregate odd and even nodes
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement odd-even segregation
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
ll1.segregate_odd_even()
print("After:")
ll1.print_list()  # expected: 1 -> 3 -> 5 -> 2 -> 4 -> None
