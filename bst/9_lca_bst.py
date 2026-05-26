# Lowest Common Ancestor (LCA) in BST

# Problem Statement:
# Given a BST and two nodes p and q, find their lowest common ancestor.
# The LCA is the lowest node that has both p and q as descendants.

# Examples:
# Example 1:
#   Input:  root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
#   Output: 6

# Example 2:
#   Input:  root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
#   Output: 2

# Difficulty: Medium


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def lca_bst(root, p, q):
    # Write your code here
    # Hint: Use BST property
    # If both p and q are smaller than root, LCA is in left subtree
    # If both p and q are larger than root, LCA is in right subtree
    # Otherwise, root is the LCA
    pass


# --- Run & Test ---
root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)

print(lca_bst(root, 2, 8).data)    # expected: 6
print(lca_bst(root, 2, 4).data)    # expected: 2
