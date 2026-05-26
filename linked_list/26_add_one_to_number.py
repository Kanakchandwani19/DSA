# Add One to a Number Represented by Linked List

# Problem Statement:
# Given a linked list representing a number (head is most significant digit),
# add 1 to it and return the modified linked list.

# Examples:
# Example 1:
#   Input:  1 -> 2 -> 3 -> None (represents 123)
#   Output: 1 -> 2 -> 4 -> None (represents 124)

# Example 2:
#   Input:  9 -> 9 -> 9 -> None (represents 999)
#   Output: 1 -> 0 -> 0 -> 0 -> None (represents 1000)


class Node:
    def __init__(self, data):
        # TODO: Implement node initialization
        self.data = data
        self.next =  None


class LinkedList:
    def __init__(self):
        # TODO: Initialize head
        self.head = None

    def add_one(self):
        """
        Add one to the number represented by linked list
        Time Complexity: O(n)
        Space Complexity: O(1) or O(n) depending on approach
        """
        # TODO: Implement adding one to the number
        #recursion backtracking approach
        def helper(temp):
            if temp is None:
                return 1
            
            carry = helper(temp.next)
            temp.data = temp.data + carry

            if temp.data < 10:
                return 0
            temp.data = 0
            return 1

        carry = helper(self.head)
        if carry == 1:
            newNode = Node(1)
            newNode.next = self.head
            self.head = newNode
        return self.head

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
print("Before adding 1:")
ll1.print_list()  # expected: 1 -> 2 -> 3
ll1.add_one()
print("After adding 1:")
ll1.print_list()  # expected: 1 -> 2 -> 4

ll2 = LinkedList()
ll2.head = Node(9)
ll2.head.next = Node(9)
ll2.head.next.next = Node(9)
print("\nBefore adding 1:")
ll2.print_list()  # expected: 9 -> 9 -> 9
ll2.add_one()
print("After adding 1:")
ll2.print_list()  # expected: 1 -> 0 -> 0 -> 0
