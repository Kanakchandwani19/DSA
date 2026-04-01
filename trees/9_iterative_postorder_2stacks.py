# Postorder Traversal Using 2 Stacks (Iterative)

# Problem Statement:
# Given the root of a binary tree, return the postorder traversal
# (Left → Right → Root) using iteration with 2 stacks (no recursion).

# Example:
#        1
#       / \
#      2   3
#     / \
#    4   5
#
#   Output: [4, 5, 2, 3, 1]

# Key Concept:
#   Stack 1 drives traversal (like preorder but Right before Left).
#   Stack 2 collects results in reverse postorder.
#
#   Algorithm:
#     Push root to stack1.
#     While stack1 not empty:
#       Pop from stack1, push to stack2.
#       Push left child to stack1, then right child.
#     Result = stack2 popped in order (reverse of what was pushed).


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def postorder_2stacks(root):
    # write your code here
    pass


# --- Run & Test ---
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)

print(postorder_2stacks(root1))   # expected: [4, 5, 2, 3, 1]

root2 = TreeNode(1)
root2.right = TreeNode(2)
root2.right.right = TreeNode(3)

print(postorder_2stacks(root2))   # expected: [3, 2, 1]
