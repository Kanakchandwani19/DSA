# Preorder, Inorder, and Postorder Traversal in One Pass

# Problem Statement:
# Given the root of a binary tree, compute preorder, inorder, and postorder
# traversals all in a single pass using one function.
# Return three lists: (preorder, inorder, postorder).

# Example:
#        1
#       / \
#      2   3
#     / \
#    4   5
#
#   Preorder:  [1, 2, 4, 5, 3]
#   Inorder:   [4, 2, 5, 1, 3]
#   Postorder: [4, 5, 2, 3, 1]

# Key Concept:
#   Use a stack of (node, visit_count) pairs.
#   visit_count tracks how many times we've "visited" this node:
#     count == 1 → add to preorder,  push back with count 2, go left
#     count == 2 → add to inorder,   push back with count 3, go right
#     count == 3 → add to postorder, done with this node
#
#   This simulates the 3 moments a node is touched during recursion.


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def all_traversals(root):
    # write your code here
    # return (preorder_list, inorder_list, postorder_list)
    pass


# --- Run & Test ---
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)

pre, ino, post = all_traversals(root1)
print("Preorder: ", pre)    # expected: [1, 2, 4, 5, 3]
print("Inorder:  ", ino)    # expected: [4, 2, 5, 1, 3]
print("Postorder:", post)   # expected: [4, 5, 2, 3, 1]
