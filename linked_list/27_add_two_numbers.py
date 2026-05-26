# Add Two Numbers Represented by Linked Lists

# Problem Statement:
# Given two linked lists representing two non-negative integers,
# where digits are stored in reverse order, add them and return the sum as a linked list.

# Examples:
# Example 1:
#   Input:  L1 = 2 -> 4 -> 3 (represents 342)
#           L2 = 5 -> 6 -> 4 (represents 465)
#   Output: 7 -> 0 -> 8 (represents 807)

# Example 2:
#   Input:  L1 = 9 -> 9 -> 9 (represents 999)
#           L2 = 1 (represents 1)
#   Output: 0 -> 0 -> 0 -> 1 (represents 1000)


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
    def add_two_numbers(l1, l2):
        """
        Add two numbers represented by linked lists
        Time Complexity: O(max(m, n))
        Space Complexity: O(max(m, n))
        """
        # TODO: Implement adding two numbers
        newNode = Node(0)   #create a dummy node
        current = newNode

        carry = 0 

        while l1 or l2 or carry:
            total = carry

            if l1:
                total += l1.data
                l1 = l1.next

            if l2:
                total += l2.data
                l2 = l2.next

            digit = total % 10
            carry = total // 10

            current.next = Node(digit)

            current = current.next

        return newNode.next

    def print_list(self):
        # TODO: Implement print functionality
        curr = self.head

        while curr:
            print(curr.data, end = " -> ")
            curr = curr.next
        print("None")


# --- Run & Test ---
# Example 1: 342 + 465 = 807
ll1 = LinkedList()
ll1.head = Node(2)
ll1.head.next = Node(4)
ll1.head.next.next = Node(3)

ll2 = LinkedList()
ll2.head = Node(5)
ll2.head.next = Node(6)
ll2.head.next.next = Node(4)

print("Number 1:")
ll1.print_list()
print("Number 2:")
ll2.print_list()

result = LinkedList()
result.head = LinkedList.add_two_numbers(ll1.head, ll2.head)
print("Sum:")
result.print_list()  # expected: 7 -> 0 -> 8

# Example 2: 999 + 1 = 1000
ll3 = LinkedList()
ll3.head = Node(9)
ll3.head.next = Node(9)
ll3.head.next.next = Node(9)

ll4 = LinkedList()
ll4.head = Node(1)

print("\nNumber 1:")
ll3.print_list()
print("Number 2:")
ll4.print_list()

result2 = LinkedList()
result2.head = LinkedList.add_two_numbers(ll3.head, ll4.head)
print("Sum:")
result2.print_list()  # expected: 0 -> 0 -> 0 -> 1
