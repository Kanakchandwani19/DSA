# Maximum Depth in Binary Tree

# Problem Statement:
# Given the root of a binary tree, return its maximum depth.
# The maximum depth is the number of nodes along the longest path from the root node
# down to the farthest leaf node.

# Examples:
# Example 1:
#   Input:  root = [3,9,20,null,null,15,7]
#           Tree:     3
#                   /   \
#                  9    20
#                      /  \
#                     15   7
#   Output: 3

# Example 2:
#   Input:  root = [1,null,2]
#   Output: 2

# Difficulty: Medium


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def maximum_depth(root):
    # Write your code here
    # Hint: Use recursion
    # Base case: if root is None, return 0
    # Recursive case: return 1 + max(left_depth, right_depth)
    pass


# --- Run & Test ---
root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(7)
print(maximum_depth(root1))    # expected: 3

root2 = TreeNode(1)
root2.right = TreeNode(2)
print(maximum_depth(root2))    # expected: 2
