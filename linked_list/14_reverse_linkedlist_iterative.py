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
        self.data = data
        self.next  = None
        self.prev = None


class LinkedList:
    def __init__(self):
        # TODO: Initialize head
        self.head = None

    def reverse_iterative(self):
        """
        Reverse the linked list iteratively
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement iterative reverse
        current = self.head
        prev_node = None

        while current:
            next_node = current.next

            current.next = prev_node
            current.prev = next_node

            prev_node = current
            current = next_node

        self.head = prev_node


    def print_list(self):
        # TODO: Implement print functionality
        curr = self.head

        while curr:
            print(curr.data, end = " -> ")
            curr = curr.next

        print("None")


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
