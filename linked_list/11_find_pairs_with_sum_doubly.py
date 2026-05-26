# Find Pairs with Given Sum in Doubly Linked List

# Problem Statement:
# Given a sorted doubly linked list and a target sum, find all pairs of nodes
# whose data sum equals the target. Use two-pointer technique.

# Examples:
# Example 1:
#   Input:  List = 1 <-> 2 <-> 3 <-> 4 <-> 5 -> None, target = 5
#   Output: [(1, 4), (2, 3)]

# Example 2:
#   Input:  List = 1 <-> 2 <-> 3 <-> 4 -> None, target = 10
#   Output: [] (no pairs found)

# Example 3:
#   Input:  List = 1 <-> 2 <-> 4 <-> 5 <-> 6 <-> 8 -> None, target = 7
#   Output: [(1, 6), (2, 5)]


class DoublyNode:
    """DoublyNode class represents a single node in a doubly linked list"""
    def __init__(self, data):
        # TODO: Implement node initialization with data, next, and prev
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    """DoublyLinkedList class to manage nodes"""
    def __init__(self):
        # TODO: Initialize head
        self.head = None
        self.tail = None

    def find_pairs_with_sum(self, target):
        """
        Find all pairs with given sum using two-pointer technique
        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(1) excluding output array
        """
        # TODO: Implement find pairs functionality
        if not self.head or not self.head.next:
            return []
        left = self.head
        right = self.head

        while right.next:
            right = right.next

        pairs = []

        while left != right and right.next != left:
            current_sum = left.data + right.data

            if current_sum == target:
                pairs.append((left.data , right.data))

                left = left.next
                right = right.prev

            elif current_sum < target:
                left = left.next

            else:
                right = right.prev

        return pairs




    def print_forward(self):
        """Print all elements from head to tail"""
        # TODO: Implement forward print functionality
        curr = self.head

        while curr:
            print(curr.data, end = " -> ")
            curr = curr.next

        print("None")


# --- Run & Test ---

# Example 1: Find pairs with sum 5
dll1 = DoublyLinkedList()
dll1.head = DoublyNode(1)
dll1.head.next = DoublyNode(2)
dll1.head.next.prev = dll1.head
dll1.head.next.next = DoublyNode(3)
dll1.head.next.next.prev = dll1.head.next
dll1.head.next.next.next = DoublyNode(4)
dll1.head.next.next.next.prev = dll1.head.next.next
dll1.head.next.next.next.next = DoublyNode(5)
dll1.head.next.next.next.next.prev = dll1.head.next.next.next
print("Example 1:")
dll1.print_forward()
print(f"Pairs with sum 5: {dll1.find_pairs_with_sum(5)}")  # expected: [(1, 4), (2, 3)]

# Example 2: No pairs found
dll2 = DoublyLinkedList()
dll2.head = DoublyNode(1)
dll2.head.next = DoublyNode(2)
dll2.head.next.prev = dll2.head
dll2.head.next.next = DoublyNode(3)
dll2.head.next.next.prev = dll2.head.next
dll2.head.next.next.next = DoublyNode(4)
dll2.head.next.next.next.prev = dll2.head.next.next
print("\nExample 2:")
dll2.print_forward()
print(f"Pairs with sum 10: {dll2.find_pairs_with_sum(10)}")  # expected: []

# Example 3: Multiple pairs
dll3 = DoublyLinkedList()
dll3.head = DoublyNode(1)
dll3.head.next = DoublyNode(2)
dll3.head.next.prev = dll3.head
dll3.head.next.next = DoublyNode(4)
dll3.head.next.next.prev = dll3.head.next
dll3.head.next.next.next = DoublyNode(5)
dll3.head.next.next.next.prev = dll3.head.next.next
dll3.head.next.next.next.next = DoublyNode(6)
dll3.head.next.next.next.next.prev = dll3.head.next.next.next
dll3.head.next.next.next.next.next = DoublyNode(8)
dll3.head.next.next.next.next.next.prev = dll3.head.next.next.next.next
print("\nExample 3:")
dll3.print_forward()
print(f"Pairs with sum 7: {dll3.find_pairs_with_sum(7)}")  # expected: [(1, 6), (2, 5)]
