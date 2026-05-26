# Detect a Loop in Linked List

# Problem Statement:
# Given a linked list, detect if there is a cycle/loop in it.
# Use Floyd's Cycle Detection Algorithm (Tortoise-Hare).

# Examples:
# Example 1:
#   Input:  1 -> 2 -> 3 -> 4 -> 2 (loop back to node 2)
#   Output: True

# Example 2:
#   Input:  1 -> 2 -> 3 -> None
#   Output: False


class Node:
    def __init__(self, data):
        # TODO: Implement node initialization
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        # TODO: Initialize head
        self.head = None

    def detect_loop(self):
        """
        Detect if there is a loop using Floyd's cycle detection
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement loop detection
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
            
        return False
            
        


# --- Run & Test ---
# Example with loop
ll1 = LinkedList()
ll1.head = Node(1)
ll1.head.next = Node(2)
ll1.head.next.next = Node(3)
ll1.head.next.next.next = Node(4)
ll1.head.next.next.next.next = ll1.head.next  # Create loop
print("Has loop:", ll1.detect_loop())  # expected: True

# Example without loop
ll2 = LinkedList()
ll2.head = Node(1)
ll2.head.next = Node(2)
ll2.head.next.next = Node(3)
print("Has loop:", ll2.detect_loop())  # expected: False
