# Search in a Binary Search Tree

# Problem Statement:
# Given the root of a BST and a target value, find the node with that value.
# Return the subtree rooted at that node. If no such node exists, return None.

# Examples:
# Example 1:
#   Input:  root = [4,2,7,1,3], target = 2
#   Output: TreeNode with value 2 (and its subtree)

# Example 2:
#   Input:  root = [4,2,7,1,3], target = 5
#   Output: None

# Difficulty: Easy


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def search_bst(root, target):
    # Write your code here
    # Hint: Use BST property
    # If target < root.data, search left
    # If target > root.data, search right
    # If target == root.data, return root
    pass


# --- Run & Test ---
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

result1 = search_bst(root, 2)
print(result1.data if result1 else None)    # expected: 2

result2 = search_bst(root, 5)
print(result2.data if result2 else None)    # expected: None
