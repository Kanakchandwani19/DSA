# Search in Linked List

# Problem Statement:
# Given a linked list and a target value, search for the target in the list.
# Return True if the value exists, False otherwise.
# Alternatively, return the index (0-based) of the target, or -1 if not found.

# Examples:
# Example 1:
#   Input:  List = 1 -> 2 -> 3 -> 4 -> 5 -> None, target = 3
#   Output: True (or index = 2)

# Example 2:
#   Input:  List = 10 -> 20 -> 30 -> None, target = 40
#   Output: False (or index = -1)

# Example 3:
#   Input:  List = None (empty list), target = 5
#   Output: False (or index = -1)


class Node:
    """Node class represents a single node in a linked list"""
    def __init__(self, data):
        # TODO: Implement node initialization
        self.data = data
        self.next = None


class LinkedList:
    """LinkedList class to manage nodes"""
    def __init__(self):
        # TODO: Initialize head
        self.head = None

    def search(self, target):
        """
        Search for a target value in the linked list
        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(1)
        Returns: True if found, False otherwise
        """
        # TODO: Implement search functionality (return True/False)
        current = self.head

        while current != None:
            if current.data == target:
                return True
            current = current.next

        return False

    def search_index(self, target):
        """
        Search for a target value and return its index
        Returns: index of target (0-based), or -1 if not found
        """
        # TODO: Implement search functionality (return index)
        current = self.head
        curr_index = 0

        while current != None:
            if current.data == target:
                return curr_index

            current = current.next
            curr_index += 1
        return -1            

    def print_list(self):
        """Print all elements in the linked list"""
        # TODO: Implement print functionality
        curr = self.head
        while curr:
            print(curr.data, end = " -> ")
            curr = curr.next
        print("None")



# --- Run & Test ---

# Example 1: Search in list with target present
ll1 = LinkedList()
ll1.head = Node(1)
ll1.head.next = Node(2)
ll1.head.next.next = Node(3)
ll1.head.next.next.next = Node(4)
ll1.head.next.next.next.next = Node(5)
print("Example 1:")
ll1.print_list()
print(f"Search for 3: {ll1.search(3)}")  # expected: True
print(f"Index of 3: {ll1.search_index(3)}")  # expected: 2

# Example 2: Search in list with target not present
ll2 = LinkedList()
ll2.head = Node(10)
ll2.head.next = Node(20)
ll2.head.next.next = Node(30)
print("\nExample 2:")
ll2.print_list()
print(f"Search for 40: {ll2.search(40)}")  # expected: False
print(f"Index of 40: {ll2.search_index(40)}")  # expected: -1

# Example 3: Search in empty list
ll3 = LinkedList()
print("\nExample 3:")
ll3.print_list()
print(f"Search for 5: {ll3.search(5)}")  # expected: False
print(f"Index of 5: {ll3.search_index(5)}")  # expected: -1
