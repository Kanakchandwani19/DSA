# Introduction to Singly LinkedList

# Problem Statement:
# A singly linked list is a linear data structure where each element (node) contains
# data and a reference (pointer) to the next node in the sequence.
# Implement a basic Node class and create a simple linked list.

# Examples:
# Example 1:
#   Create a linked list: 1 -> 2 -> 3 -> 4 -> None
#   Visual representation:
#   [1] -> [2] -> [3] -> [4] -> None

# Example 2:
#   Create a linked list: 10 -> 20 -> 30 -> None
#   Visual representation:
#   [10] -> [20] -> [30] -> None


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

    def print_list(self):
        """Print all elements in the linked list"""
        # TODO: Implement print functionality
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")
        


    def append(self, data):
        """Add a node at the end of the linked list"""
        # TODO: Implement append functionality
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return 
         
        curr = self.head
        while curr.next != None :
            curr = curr.next 
        curr.next = new_node

# if self.head == None:     #check empty list
#             return 

#   if self.head.next == None:      #single node case
#             self.head = None
#             return
        

# --- Run & Test ---

# Example 1: Create a linked list 1 -> 2 -> 3 -> 4
ll1 = LinkedList()
ll1.append(1)
ll1.append(2)
ll1.append(3)
ll1.append(4)
print("Example 1:")
ll1.print_list()  # expected: 1 -> 2 -> 3 -> 4 -> None

# Example 2: Create a linked list 10 -> 20 -> 30
ll2 = LinkedList()
ll2.append(10)
ll2.append(20)
ll2.append(30)
print("\nExample 2:")
ll2.print_list()  # expected: 10 -> 20 -> 30 -> None

# Example 3: Empty linked list
ll3 = LinkedList()
print("\nExample 3 (Empty List):")
ll3.print_list()  # expected: None
