# Diameter of Binary Tree

# Problem Statement:
# Given the root of a binary tree, return the length of the diameter of the tree.
# The diameter is the length of the longest path between any two nodes in a tree.
# This path may or may not pass through the root.
# The length of a path is represented by the number of edges between nodes.

# Examples:
# Example 1:
#   Input:  root = [1,2,3,4,5]
#           Tree:     1
#                   /   \
#                  2     3
#                 / \
#                4   5
#   Output: 3
#   Explanation: Path is [4,2,1,3] or [5,2,1,3]

# Example 2:
#   Input:  root = [1,2]
#   Output: 1

# Difficulty: Easy


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def diameter_binary_tree(root):
    # Write your code here
    # Hint: For each node, diameter = left_height + right_height
    # Use a helper function to calculate height and update diameter
    pass


# --- Run & Test ---
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)
print(diameter_binary_tree(root1))    # expected: 3

root2 = TreeNode(1)
root2.left = TreeNode(2)
print(diameter_binary_tree(root2))    # expected: 1
