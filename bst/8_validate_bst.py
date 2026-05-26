# Check if a tree is a BST or not

# Problem Statement:
# Given the root of a binary tree, determine if it is a valid BST.

# Examples:
# Example 1:
#   Input:  root = [2,1,3]
#   Output: True

# Example 2:
#   Input:  root = [5,1,4,null,null,3,6]
#   Output: False (3 is less than 5, violates BST property)

# Difficulty: Medium


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def is_valid_bst(root, min_val=float('-inf'), max_val=float('inf')):
    # Write your code here
    # Hint: For each node, maintain valid range [min_val, max_val]
    # For left child: range becomes [min_val, root.data]
    # For right child: range becomes [root.data, max_val]
    pass


# --- Run & Test ---
root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(3)
print(is_valid_bst(root1))    # expected: True

root2 = TreeNode(5)
root2.left = TreeNode(1)
root2.right = TreeNode(4)
root2.right.left = TreeNode(3)
root2.right.right = TreeNode(6)
print(is_valid_bst(root2))    # expected: False
