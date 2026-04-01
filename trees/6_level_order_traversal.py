# Level Order Traversal (BFS) of Binary Tree

# Problem Statement:
# Given the root of a binary tree, return the level order traversal
# of its nodes' values — i.e., from left to right, level by level.
# Return a list of lists, where each inner list contains one level.

# Example:
#        1
#       / \
#      2   3
#     / \   \
#    4   5   6
#
#   Output: [[1], [2, 3], [4, 5, 6]]

# Example 2:
#    1
#     \
#      2
#       \
#        3
#   Output: [[1], [2], [3]]

# Key Concept:
#   Use a queue (collections.deque).
#   Start with root in the queue.
#   For each level: process all nodes currently in the queue,
#   add their children to the queue for the next level.


from collections import deque


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def level_order(root):
    # write your code here
    pass


# --- Run & Test ---
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)
root1.right.right = TreeNode(6)

print(level_order(root1))   # expected: [[1], [2, 3], [4, 5, 6]]

root2 = TreeNode(1)
root2.right = TreeNode(2)
root2.right.right = TreeNode(3)

print(level_order(root2))   # expected: [[1], [2], [3]]
