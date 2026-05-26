# Sort a Linked List of 0's, 1's and 2's

# Problem Statement:
# Given a linked list containing only 0s, 1s, and 2s, sort it in a single pass.
# Use the Dutch National Flag algorithm approach.

# Examples:
# Example 1:
#   Input:  1 -> 2 -> 0 -> 1 -> 0 -> 2 -> None
#   Output: 0 -> 0 -> 1 -> 1 -> 2 -> 2 -> None


class Node:
    def __init__(self, data):
        # TODO: Implement node initialization
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        # TODO: Initialize head
        self.head = None

    def sort_012(self):
        """
        Sort linked list containing 0s, 1s, and 2s
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement sorting of 0s, 1s, and 2s
        zero = 0
        one = 0
        two = 0

        current = self.head

        while current:
            if current.data == 0:
                zero += 1

            elif current.data == 1:
                one += 1

            else:
                two += 1

            current = current.next

        current = self.head

        while current:

            if zero > 0:
                current.data = 0
                zero -= 1

            elif one > 0:
                current.data = 1
                one -= 1

            else:
                current.data = 2
                two -= 1

            current = current.next



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
ll1.head.next.next = Node(0)
ll1.head.next.next.next = Node(1)
ll1.head.next.next.next.next = Node(0)
ll1.head.next.next.next.next.next = Node(2)
print("Before sorting:")
ll1.print_list()
ll1.sort_012()
print("After sorting:")
ll1.print_list()  # expected: 0 -> 0 -> 1 -> 1 -> 2 -> 2 -> None
