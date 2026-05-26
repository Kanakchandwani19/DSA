# Find the Intersection Point of Y Linked List

# Problem Statement:
# Given two linked lists that intersect at some node, find the intersection node.
# Use the two-pointer approach.

# Examples:
# Example 1:
#   List A: 1 -> 2 -> 3 \
#                        -> 6 -> 7 -> None
#   List B: 4 -> 5 ------/
#   Output: Node with data 6


class Node:
    def __init__(self, data):
        # TODO: Implement node initialization
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        # TODO: Initialize head
        self.head = None

    @staticmethod
    def find_intersection(head1, head2):
        """
        Find the intersection point of two linked lists
        Time Complexity: O(m + n)
        Space Complexity: O(1)
        """
        # TODO: Implement finding intersection point

        def collisionPoint(t1, t2, d):
            while d:
                d -= 1
                t1 = t1.next

            while t1 != t2:
                t1 = t1.next
                t2 = t2.next

            return t1

        t1 = head1
        n1 = 0 
        
        while t1 != None:
            n1 += 1
            t1 = t1.next

        t2 = head2
        n2 = 0

        while t2 != None:
            n2 += 1
            t2 = t2.next

        if n1 < n2:
            return collisionPoint(head2, head1, n2-n1)
        else:
            return collisionPoint(head1, head2, n1-n2)


# --- Run & Test ---
# Create intersection
common = Node(6)
common.next = Node(7)

# List 1: 1 -> 2 -> 3 -> 6 -> 7
ll1 = LinkedList()
ll1.head = Node(1)
ll1.head.next = Node(2)
ll1.head.next.next = Node(3)
ll1.head.next.next.next = common

# List 2: 4 -> 5 -> 6 -> 7
ll2 = LinkedList()
ll2.head = Node(4)
ll2.head.next = Node(5)
ll2.head.next.next = common

intersection = LinkedList.find_intersection(ll1.head, ll2.head)
print(f"Intersection at: {intersection.data if intersection else None}")  # expected: 6
