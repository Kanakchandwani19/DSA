# Top View of Binary Tree

# Problem Statement:
# Given a binary tree, return the top view of the tree.
# Top view means when you look at the tree from the top, the nodes you will see.

# Examples:
# Example 1:
#   Input:  root = [1,2,3,4,5,6,7]
#           Tree:       1
#                     /   \
#                    2     3
#                   / \   / \
#                  4   5 6   7
#   Output: [4, 2, 1, 3, 7]

# Example 2:
#   Input:  root = [1,2,3,null,4,5,6]
#   Output: [2, 1, 3, 6]

# Difficulty: Medium


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def top_view(root):
    # Write your code here
    # Hint: Use vertical order traversal concept
    # For each vertical column, store only the first node encountered (top-most)
    # Use level order traversal with column tracking
    pass


# --- Run & Test ---
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)
root1.right.left = TreeNode(6)
root1.right.right = TreeNode(7)
print(top_view(root1))    # expected: [4, 2, 1, 3, 7]
