# Kth Smallest and Largest element in BST

# Problem Statement:
# Given the root of a BST and an integer k, return the kth smallest/largest value in the BST.

# Examples:
# Example 1:
#   Input:  root = [5,3,6,2,4,null,null,1], k = 3
#   Kth Smallest Output: 3
#   Kth Largest Output: 5

# Difficulty: Medium


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def kth_smallest(root, k):
    # Write your code here
    # Hint: Inorder traversal of BST gives sorted order
    # Return kth element in inorder traversal
    pass


def kth_largest(root, k):
    # Write your code here
    # Hint: Reverse inorder traversal (right-root-left) gives descending order
    # Return kth element in reverse inorder
    pass


# --- Run & Test ---
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left.left = TreeNode(1)

print(kth_smallest(root, 3))    # expected: 3
print(kth_largest(root, 3))     # expected: 4
