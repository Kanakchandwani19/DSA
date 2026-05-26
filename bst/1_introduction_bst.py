# Introduction to Binary Search Tree (BST)

# Problem Statement:
# A Binary Search Tree is a binary tree with the following properties:
# - The left subtree of a node contains only nodes with keys less than the node's key
# - The right subtree of a node contains only nodes with keys greater than the node's key
# - Both left and right subtrees must also be binary search trees

# Create a simple BST and verify its properties.

# Difficulty: Easy


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def is_bst(root, min_val=float('-inf'), max_val=float('inf')):
    # Write your code here
    # Hint: For each node, check if its value is within valid range
    # For left subtree: max value should be node.data
    # For right subtree: min value should be node.data
    pass


# --- Run & Test ---
# Valid BST:
#        5
#       / \
#      3   7
#     / \
#    2   4
root1 = TreeNode(5)
root1.left = TreeNode(3)
root1.right = TreeNode(7)
root1.left.left = TreeNode(2)
root1.left.right = TreeNode(4)
print(is_bst(root1))    # expected: True

# Invalid BST:
#        5
#       / \
#      3   7
#     / \
#    2   6  (6 should not be in left subtree of 5)
root2 = TreeNode(5)
root2.left = TreeNode(3)
root2.right = TreeNode(7)
root2.left.left = TreeNode(2)
root2.left.right = TreeNode(6)
print(is_bst(root2))    # expected: False
