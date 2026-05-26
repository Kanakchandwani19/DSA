# Bottom View of Binary Tree

# Problem Statement:
# Given a binary tree, return the bottom view of the tree.
# Bottom view means when you look at the tree from the bottom, the nodes you will see.

# Examples:
# Example 1:
#   Input:  root = [1,2,3,4,5,6,7]
#           Tree:       1
#                     /   \
#                    2     3
#                   / \   / \
#                  4   5 6   7
#   Output: [4, 2, 6, 3, 7]

# Example 2:
#   Input:  root = [20,8,22,5,3,null,25]
#   Output: [5, 8, 3, 22, 25]

# Difficulty: Medium


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def bottom_view(root):
    # Write your code here
    # Hint: Similar to top view
    # For each vertical column, store the last node encountered (bottom-most)
    # Use level order traversal with column tracking and overwrite values
    pass


# --- Run & Test ---
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)
root1.right.left = TreeNode(6)
root1.right.right = TreeNode(7)
print(bottom_view(root1))    # expected: [4, 2, 6, 3, 7]
