# Inorder Traversal of Binary Tree (Recursive)

# Problem Statement:
# Given the root of a binary tree, return the inorder traversal
# of its nodes' values.
#
# Inorder means: Left → Root → Right
# Note: Inorder traversal of a BST gives elements in sorted order.

# Example:
#        1
#       / \
#      2   3
#     / \
#    4   5
#
#   Inorder: [4, 2, 5, 1, 3]

# Example 2:
#    1
#     \
#      2
#       \
#        3
#   Inorder: [1, 2, 3]


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder(root, result=None):
    # write your code here
    # hint: recurse left first, then visit root, then recurse right
    pass


# --- Run & Test ---
# Tree 1:
#        1
#       / \
#      2   3
#     / \
#    4   5
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)

result1 = []
inorder(root1, result1)
print(result1)   # expected: [4, 2, 5, 1, 3]

# Tree 2:
root2 = TreeNode(1)
root2.right = TreeNode(2)
root2.right.right = TreeNode(3)

result2 = []
inorder(root2, result2)
print(result2)   # expected: [1, 2, 3]
