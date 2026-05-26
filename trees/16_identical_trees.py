# Check if two trees are identical or not

# Problem Statement:
# Given the roots of two binary trees p and q, check if they are identical.
# Two binary trees are identical if they are structurally identical and the nodes have the same value.

# Examples:
# Example 1:
#   Input:  p = [1,2,3], q = [1,2,3]
#   Output: True

# Example 2:
#   Input:  p = [1,2], q = [1,null,2]
#   Output: False

# Example 3:
#   Input:  p = [1,2,1], q = [1,1,2]
#   Output: False

# Difficulty: Medium


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def is_identical(p, q):
    # Write your code here
    # Hint: Use recursion
    # Base cases:
    # - If both are None, return True
    # - If one is None, return False
    # - If values don't match, return False
    # Recursive case: check left and right subtrees
    pass


# --- Run & Test ---
p1 = TreeNode(1)
p1.left = TreeNode(2)
p1.right = TreeNode(3)

q1 = TreeNode(1)
q1.left = TreeNode(2)
q1.right = TreeNode(3)
print(is_identical(p1, q1))    # expected: True

p2 = TreeNode(1)
p2.left = TreeNode(2)

q2 = TreeNode(1)
q2.right = TreeNode(2)
print(is_identical(p2, q2))    # expected: False
