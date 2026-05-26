# Find Min/Max in BST

# Problem Statement:
# Given the root of a BST, find the minimum and maximum values.

# Examples:
# Example 1:
#   Input:  root = [5,3,7,2,4,6,8]
#   Min Output: 2
#   Max Output: 8

# Difficulty: Easy


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def find_min(root):
    # Write your code here
    # Hint: Minimum is the leftmost node
    pass


def find_max(root):
    # Write your code here
    # Hint: Maximum is the rightmost node
    pass


# --- Run & Test ---
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(8)

print(find_min(root))    # expected: 2
print(find_max(root))    # expected: 8
