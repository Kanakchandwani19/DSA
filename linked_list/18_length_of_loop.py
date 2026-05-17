# Length of Loop in Linked List

# Problem Statement:
# Given a linked list with a loop, find the length of the loop.

# Examples:
# Example 1:
#   Input:  1 -> 2 -> 3 -> 4 -> 2 (loop: 2 -> 3 -> 4 -> 2)
#   Output: 3 (loop contains 3 nodes)


class Node:
    def __init__(self, data):
        # TODO: Implement node initialization
        pass


class LinkedList:
    def __init__(self):
        # TODO: Initialize head
        pass

    def length_of_loop(self):
        """
        Find the length of the loop
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement finding loop length
        pass


# --- Run & Test ---
ll1 = LinkedList()
ll1.head = Node(1)
ll1.head.next = Node(2)
ll1.head.next.next = Node(3)
ll1.head.next.next.next = Node(4)
ll1.head.next.next.next.next = ll1.head.next  # Loop: 2->3->4->2
print(f"Length of loop: {ll1.length_of_loop()}")  # expected: 3
