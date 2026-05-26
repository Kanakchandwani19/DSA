# Boundary Traversal

# Problem Statement:
# Given a binary tree, return the boundary nodes in anti-clockwise order starting from the root.
# The boundary includes:
# 1. Left boundary (excluding leaf nodes)
# 2. All leaf nodes (left to right)
# 3. Right boundary (excluding leaf nodes, in reverse order)

# Examples:
# Example 1:
#   Input:  root = [1,2,3,4,5,6,7]
#           Tree:       1
#                     /   \
#                    2     3
#                   / \   / \
#                  4   5 6   7
#   Output: [1, 2, 4, 5, 6, 7, 3]

# Difficulty: Medium


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def boundary_traversal(root):
    # Write your code here
    # Hint: Three separate functions
    # 1. Add left boundary (go left, if not possible go right)
    # 2. Add leaf nodes (inorder traversal)
    # 3. Add right boundary in reverse (go right, if not possible go left)
    pass


# --- Run & Test ---
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)
root1.right.left = TreeNode(6)
root1.right.right = TreeNode(7)
print(boundary_traversal(root1))    # expected: [1, 2, 4, 5, 6, 7, 3]
