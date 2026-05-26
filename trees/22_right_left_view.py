# Right/Left View of Binary Tree

# Problem Statement:
# Given a binary tree, return:
# - Right View: rightmost node at each level
# - Left View: leftmost node at each level

# Examples:
# Example 1:
#   Input:  root = [1,2,3,null,5,null,4]
#   Right View Output: [1, 3, 4]
#   Left View Output: [1, 2, 5]

# Example 2:
#   Input:  root = [1,2,3,4,5,6,7]
#   Right View Output: [1, 3, 7]
#   Left View Output: [1, 2, 4]

# Difficulty: Medium


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def right_view(root):
    # Write your code here
    # Hint: Level order traversal, take last node at each level
    # Or use recursion with level tracking (visit right subtree first)
    pass


def left_view(root):
    # Write your code here
    # Hint: Level order traversal, take first node at each level
    # Or use recursion with level tracking (visit left subtree first)
    pass


# --- Run & Test ---
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.right = TreeNode(5)
root1.right.right = TreeNode(4)
print(right_view(root1))    # expected: [1, 3, 4]
print(left_view(root1))     # expected: [1, 2, 5]
