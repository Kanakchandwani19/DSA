# Postorder Traversal Using 1 Stack (Iterative)

# Problem Statement:
# Given the root of a binary tree, return the postorder traversal
# (Left → Right → Root) using iteration with only 1 stack (no recursion).
# This is harder than the 2-stack version.

# Example:
#        1
#       / \
#      2   3
#     / \
#    4   5
#
#   Output: [4, 5, 2, 3, 1]

# Key Concept:
#   Track the previously visited node to know whether you're coming
#   back from the left or right subtree.
#
#   Algorithm:
#     Use a `prev` pointer (last node visited).
#     Go as far left as possible.
#     At each node, check:
#       - If right child exists and was NOT the last visited → go right
#       - Otherwise → visit this node (it's safe to process now)


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def postorder_1stack(root):
    # write your code here
    pass


# --- Run & Test ---
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)

print(postorder_1stack(root1))   # expected: [4, 5, 2, 3, 1]

root2 = TreeNode(1)
root2.right = TreeNode(2)
root2.right.right = TreeNode(3)

print(postorder_1stack(root2))   # expected: [3, 2, 1]
