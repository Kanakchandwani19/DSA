# Zig Zag or Spiral Traversal

# Problem Statement:
# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values.
# (i.e., from left to right, then right to left for the next level and alternate between).

# Examples:
# Example 1:
#   Input:  root = [3,9,20,null,null,15,7]
#           Tree:     3
#                   /   \
#                  9    20
#                      /  \
#                     15   7
#   Output: [[3], [20,9], [15,7]]

# Example 2:
#   Input:  root = [1]
#   Output: [[1]]

# Difficulty: Medium


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def zigzag_traversal(root):
    # Write your code here
    # Hint: Use level order traversal (BFS) with a flag to track direction
    # Alternate the direction at each level
    # Or reverse the list for alternate levels
    pass


# --- Run & Test ---
root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(7)
print(zigzag_traversal(root1))    # expected: [[3], [20, 9], [15, 7]]

root2 = TreeNode(1)
print(zigzag_traversal(root2))    # expected: [[1]]
