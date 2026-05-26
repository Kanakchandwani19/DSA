# Construct a BST from a preorder traversal

# Problem Statement:
# Given an array representing the preorder traversal of a BST, construct the BST.

# Examples:
# Example 1:
#   Input:  preorder = [8, 5, 1, 7, 10, 12]
#   Output: BST with root 8

# Difficulty: Medium


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def construct_bst_from_preorder(preorder):
    # Write your code here
    # Hint: First element is root
    # Elements smaller than root go to left subtree
    # Elements larger than root go to right subtree
    # Use recursion with range bounds
    pass


# Helper to print inorder (for verification)
def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.data] + inorder(root.right)


# --- Run & Test ---
preorder = [8, 5, 1, 7, 10, 12]
root = construct_bst_from_preorder(preorder)
print(inorder(root))    # expected: [1, 5, 7, 8, 10, 12] (sorted order)
