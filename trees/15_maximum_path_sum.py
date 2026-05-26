# Maximum Path Sum

# Problem Statement:
# Given the root of a binary tree, return the maximum path sum of any non-empty path.
# A path is any sequence of nodes where each pair of adjacent nodes has an edge.
# A node can only appear in the sequence at most once.
# The path does not need to pass through the root.

# Examples:
# Example 1:
#   Input:  root = [1,2,3]
#           Tree:     1
#                   /   \
#                  2     3
#   Output: 6
#   Explanation: Path is 2 -> 1 -> 3

# Example 2:
#   Input:  root = [-10,9,20,null,null,15,7]
#           Tree:     -10
#                    /    \
#                   9     20
#                        /  \
#                       15   7
#   Output: 42
#   Explanation: Path is 15 -> 20 -> 7

# Difficulty: Medium


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def maximum_path_sum(root):
    # Write your code here
    # Hint: For each node, max path through that node = node.data + left_sum + right_sum
    # Use a helper function that returns max path sum going down from node
    # Keep a global variable to track maximum path sum
    pass


# --- Run & Test ---
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
print(maximum_path_sum(root1))    # expected: 6

root2 = TreeNode(-10)
root2.left = TreeNode(9)
root2.right = TreeNode(20)
root2.right.left = TreeNode(15)
root2.right.right = TreeNode(7)
print(maximum_path_sum(root2))    # expected: 42
