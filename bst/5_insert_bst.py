# Insert a given node in BST

# Problem Statement:
# Given the root of a BST and a value to insert, insert the value into the BST.
# Return the root of the BST after insertion.

# Examples:
# Example 1:
#   Input:  root = [4,2,7,1,3], val = 5
#   Output: [4,2,7,1,3,5]

# Difficulty: Medium


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert_bst(root, val):
    # Write your code here
    # Hint: If root is None, create new node
    # If val < root.data, insert in left subtree
    # If val > root.data, insert in right subtree
    pass


# --- Run & Test ---
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

root = insert_bst(root, 5)
print(root.right.left.data if root.right.left else None)    # expected: 5
