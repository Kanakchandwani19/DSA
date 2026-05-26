# Delete a node in BST

# Problem Statement:
# Given the root of a BST and a key, delete the node with that key in the BST.
# Return the root of the BST after deletion.

# Examples:
# Example 1:
#   Input:  root = [5,3,6,2,4,null,7], key = 3
#   Output: [5,4,6,2,null,null,7] or [5,2,6,null,4,null,7]

# Difficulty: Medium


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def delete_bst(root, key):
    # Write your code here
    # Hint: Three cases:
    # 1. Node is leaf: simply remove it
    # 2. Node has one child: replace node with child
    # 3. Node has two children: find inorder successor (smallest in right subtree),
    #    copy its value to node, delete successor
    pass


# --- Run & Test ---
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)

root = delete_bst(root, 3)
# Tree structure should be valid BST after deletion
