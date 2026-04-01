# Binary Tree Representation in Python

# A Binary Tree is a tree where every node has at most 2 children:
#   - left child
#   - right child

# How to represent a node:
#   Each node stores:
#     - data  : the value
#     - left  : reference to left child (or None)
#     - right : reference to right child (or None)


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Building a tree manually:
#
#        1
#       / \
#      2   3
#     / \
#    4   5
#
# We create each node and connect them via .left and .right

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Accessing nodes:
print("Root:", root.data)                    # 1
print("Root's left child:", root.left.data)  # 2
print("Root's right child:", root.right.data) # 3
print("Root's left->left:", root.left.left.data)  # 4
print("Root's left->right:", root.left.right.data) # 5
print("Root's right->left:", root.right.left)  # None (no child)
