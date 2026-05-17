# Check if Linked List is Palindrome

# Problem Statement:
# Given a linked list, check if it is a palindrome.
# Approach: Find middle, reverse second half, compare.

# Examples:
# Example 1:
#   Input:  1 -> 2 -> 2 -> 1 -> None
#   Output: True

# Example 2:
#   Input:  1 -> 2 -> 3 -> None
#   Output: False


class Node:
    def __init__(self, data):
        # TODO: Implement node initialization
        pass


class LinkedList:
    def __init__(self):
        # TODO: Initialize head
        pass

    def is_palindrome(self):
        """
        Check if linked list is a palindrome
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement palindrome check
        pass

    def print_list(self):
        # TODO: Implement print functionality
        pass


# --- Run & Test ---
ll1 = LinkedList()
ll1.head = Node(1)
ll1.head.next = Node(2)
ll1.head.next.next = Node(2)
ll1.head.next.next.next = Node(1)
print("List 1:")
ll1.print_list()
print(f"Is palindrome: {ll1.is_palindrome()}")  # expected: True

ll2 = LinkedList()
ll2.head = Node(1)
ll2.head.next = Node(2)
ll2.head.next.next = Node(3)
print("\nList 2:")
ll2.print_list()
print(f"Is palindrome: {ll2.is_palindrome()}")  # expected: False
