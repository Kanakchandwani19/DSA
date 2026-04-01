# Iterative Inorder Traversal of Binary Tree

# Problem Statement:
# Given the root of a binary tree, return the inorder traversal
# (Left → Root → Right) using iteration (no recursion).

# Example:
#        1
#       / \
#      2   3
#     / \
#    4   5
#
#   Output: [4, 2, 5, 1, 3]

# Key Concept:
#   Use an explicit stack.
#   Keep going left as far as possible, pushing nodes onto the stack.
#   When you can't go left, pop a node, record it, then move to its right child.
#
#   Algorithm:
#     current = root
#     while current is not None OR stack is not empty:
#       go left until None, pushing each node
#       pop node, add to result
#       move to right child


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def iterative_inorder(root):
    # write your code here
    pass


# --- Run & Test ---
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)

print(iterative_inorder(root1))   # expected: [4, 2, 5, 1, 3]

root2 = TreeNode(1)
root2.right = TreeNode(2)
root2.right.right = TreeNode(3)

print(iterative_inorder(root2))   # expected: [1, 2, 3]
