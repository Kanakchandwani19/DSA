# Check for Balanced Binary Tree

# Problem Statement:
# Given a binary tree, determine if it is height-balanced.
# A height-balanced binary tree is one where the left and right subtrees of every node
# differ in height by no more than 1.

# Examples:
# Example 1:
#   Input:  root = [3,9,20,null,null,15,7]
#           Tree:     3
#                   /   \
#                  9    20
#                      /  \
#                     15   7
#   Output: True

# Example 2:
#   Input:  root = [1,2,2,3,3,null,null,4,4]
#   Output: False

# Difficulty: Medium


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def is_balanced(root):
    # Write your code here
    # Hint: Use a helper function that returns height and balance status
    # If difference between left and right height > 1, tree is not balanced
    # Use -1 to indicate unbalanced tree
    pass


# --- Run & Test ---
root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(7)
print(is_balanced(root1))    # expected: True

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.left.left = TreeNode(3)
root2.left.left.left = TreeNode(4)
print(is_balanced(root2))    # expected: False
