# Iterative Preorder Traversal of Binary Tree

# Problem Statement:
# Given the root of a binary tree, return the preorder traversal
# (Root → Left → Right) using iteration (no recursion).

# Example:
#        1
#       / \
#      2   3
#     / \
#    4   5
#
#   Output: [1, 2, 4, 5, 3]

# Key Concept:
#   Use an explicit stack to simulate the recursive call stack.
#   Push root, then loop:
#     - Pop a node, add its value to result
#     - Push right child first (so left is processed first)
#     - Push left child


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def iterative_preorder(root):
    # write your code here
    pass


# --- Run & Test ---
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)

print(iterative_preorder(root1))   # expected: [1, 2, 4, 5, 3]

root2 = TreeNode(1)
root2.right = TreeNode(2)
root2.right.right = TreeNode(3)

print(iterative_preorder(root2))   # expected: [1, 2, 3]
