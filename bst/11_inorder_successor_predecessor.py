# Inorder Successor/Predecessor in BST

# Problem Statement:
# Given a BST and a node, find its inorder successor and predecessor.
# - Inorder Successor: The node with the smallest value greater than the given node's value
# - Inorder Predecessor: The node with the largest value smaller than the given node's value

# Examples:
# Example 1:
#   Input:  root = [5,3,7,2,4,6,8], node = 4
#   Successor Output: 5
#   Predecessor Output: 3

# Difficulty: Medium


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder_successor(root, node):
    # Write your code here
    # Hint:
    # If node has right subtree: successor is leftmost node in right subtree
    # Otherwise: successor is the ancestor where we last took a left turn
    pass


def inorder_predecessor(root, node):
    # Write your code here
    # Hint:
    # If node has left subtree: predecessor is rightmost node in left subtree
    # Otherwise: predecessor is the ancestor where we last took a right turn
    pass


# --- Run & Test ---
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(8)

node = root.left.right  # Node with value 4
succ = inorder_successor(root, node)
pred = inorder_predecessor(root, node)
print(succ.data if succ else None)    # expected: 5
print(pred.data if pred else None)    # expected: 3
