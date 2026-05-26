# Find the Length of the Linked List

# Problem Statement:
# Given a linked list, find and return the total number of nodes in the list.

# Examples:
# Example 1:
#   Input:  List = 1 -> 2 -> 3 -> 4 -> 5 -> None
#   Output: 5

# Example 2:
#   Input:  List = None (empty list)
#   Output: 0

# Example 3:
#   Input:  List = 10 -> None
#   Output: 1


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

    def find_length(self):
        """
        Find the length of the linked list
        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(1)
        """
        # TODO: Implement length calculation
        count = 0
        current = self.head

        while current != None:
            count += 1
            current = current.next 

        return count


    def print_list(self):
        """Print all elements in the linked list"""
        # TODO: Implement print functionality
        curr = self.head
        while curr:
            print(curr.data, end = " -> ")
            curr = curr.next
        print("None")
        


# --- Run & Test ---

# Example 1: Find length of list with multiple nodes
ll1 = LinkedList()
ll1.head = Node(1)
ll1.head.next = Node(2)
ll1.head.next.next = Node(3)
ll1.head.next.next.next = Node(4)
ll1.head.next.next.next.next = Node(5)
print("Example 1:")
ll1.print_list()
print(f"Length: {ll1.find_length()}")  # expected: 5

# Example 2: Find length of empty list
ll2 = LinkedList()
print("\nExample 2:")
ll2.print_list()
print(f"Length: {ll2.find_length()}")  # expected: 0

# Example 3: Find length of single node list
ll3 = LinkedList()
ll3.head = Node(10)
print("\nExample 3:")
ll3.print_list()
print(f"Length: {ll3.find_length()}")  # expected: 1
