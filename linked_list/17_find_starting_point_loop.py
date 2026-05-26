# Find the Starting Point of Loop in Linked List

# Problem Statement:
# Given a linked list with a loop, find the starting node of the loop.
# Use Floyd's algorithm to detect loop, then find the starting point.

# Examples:
# Example 1:
#   Input:  1 -> 2 -> 3 -> 4 -> 2 (loop starts at node 2)
#   Output: Node with data 2


class Node:
    def __init__(self, data):
        # TODO: Implement node initialization
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        # TODO: Initialize head
        self.head = None

    def find_loop_start(self):
        """
        Find the starting node of the loop
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement finding loop start
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                slow = self.head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next

                return slow
            
        return None

# --- Run & Test ---
ll1 = LinkedList()
ll1.head = Node(1)
ll1.head.next = Node(2)
ll1.head.next.next = Node(3)
ll1.head.next.next.next = Node(4)
ll1.head.next.next.next.next = ll1.head.next  # Loop starts at 2
start = ll1.find_loop_start()
print(f"Loop starts at: {start.data if start else None}")  # expected: 2
