# Preorder Traversal of Binary Tree (Recursive)

# Problem Statement:
# Given the root of a binary tree, return the preorder traversal
# of its nodes' values.
#
# Preorder means: Root → Left → Right

# Example:
#        1
#       / \
#      2   3
#     / \
#    4   5
#
#   Preorder: [1, 2, 4, 5, 3]

# Example 2:
#    1
#     \
#      2
#       \
#        3
#   Preorder: [1, 2, 3]


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preorder(root, result=None):
    # write your code here
    # hint: visit root first, then recurse left, then recurse right
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
preorder(root1, result1)
print(result1)   # expected: [1, 2, 4, 5, 3]

# Tree 2: only right children
root2 = TreeNode(1)
root2.right = TreeNode(2)
root2.right.right = TreeNode(3)

result2 = []
preorder(root2, result2)
print(result2)   # expected: [1, 2, 3]
