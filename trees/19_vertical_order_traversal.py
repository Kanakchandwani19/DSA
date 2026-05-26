# Vertical Order Traversal

# Problem Statement:
# Given the root of a binary tree, return the vertical order traversal of its nodes' values.
# For each node at position (row, col), its left and right children will be at positions
# (row + 1, col - 1) and (row + 1, col + 1) respectively.
# The root is at position (0, 0).

# Examples:
# Example 1:
#   Input:  root = [3,9,20,null,null,15,7]
#   Output: [[9], [3, 15], [20], [7]]

# Example 2:
#   Input:  root = [1,2,3,4,5,6,7]
#   Output: [[4], [2], [1, 5, 6], [3], [7]]

# Difficulty: Medium


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def vertical_order_traversal(root):
    # Write your code here
    # Hint: Use a hash map with column as key
    # Do level order traversal and track (node, row, col)
    # For left child: col - 1, for right child: col + 1
    pass


# --- Run & Test ---
root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(7)
print(vertical_order_traversal(root1))    # expected: [[9], [3, 15], [20], [7]]
