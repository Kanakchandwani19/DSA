# Postorder Traversal of Binary Tree (Recursive)

# Problem Statement:
# Given the root of a binary tree, return the postorder traversal
# of its nodes' values.
#
# Postorder means: Left → Right → Root
# Used when you need to process children before the parent
# (e.g. deleting a tree, evaluating expression trees).

# Example:
#        1
#       / \
#      2   3
#     / \
#    4   5
#
#   Postorder: [4, 5, 2, 3, 1]

# Example 2:
#    1
#     \
#      2
#       \
#        3
#   Postorder: [3, 2, 1]


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def postorder(root, result=None):
    # write your code here
    # hint: recurse left, then right, then visit root last
    pass


# --- Run & Test ---
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)

result1 = []
postorder(root1, result1)
print(result1)   # expected: [4, 5, 2, 3, 1]

root2 = TreeNode(1)
root2.right = TreeNode(2)
root2.right.right = TreeNode(3)

result2 = []
postorder(root2, result2)
print(result2)   # expected: [3, 2, 1]
