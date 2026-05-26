# Symmetric Binary Tree

# Problem Statement:
# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# Examples:
# Example 1:
#   Input:  root = [1,2,2,3,4,4,3]
#           Tree:       1
#                     /   \
#                    2     2
#                   / \   / \
#                  3   4 4   3
#   Output: True

# Example 2:
#   Input:  root = [1,2,2,null,3,null,3]
#   Output: False

# Difficulty: Medium


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def is_symmetric(root):
    # Write your code here
    # Hint: Create a helper function to check if two subtrees are mirrors
    # Two trees are mirrors if:
    # - Both roots have same value
    # - Left subtree of left tree is mirror of right subtree of right tree
    # - Right subtree of left tree is mirror of left subtree of right tree
    pass


# --- Run & Test ---
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(2)
root1.left.left = TreeNode(3)
root1.left.right = TreeNode(4)
root1.right.left = TreeNode(4)
root1.right.right = TreeNode(3)
print(is_symmetric(root1))    # expected: True

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(2)
root2.left.right = TreeNode(3)
root2.right.right = TreeNode(3)
print(is_symmetric(root2))    # expected: False
