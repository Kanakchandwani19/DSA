# Floor and Ceil in a BST

# Problem Statement:
# Given a BST and a key, find floor and ceil of the key.
# Floor: Largest value <= key
# Ceil: Smallest value >= key

# Examples:
# Example 1:
#   Input:  root = [8,4,12,2,6,10,14], key = 5
#   Floor Output: 4
#   Ceil Output: 6

# Difficulty: Easy


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def floor_bst(root, key):
    # Write your code here
    # Hint: If root.data > key, go left
    # If root.data <= key, this could be floor, but check right for larger value
    pass


def ceil_bst(root, key):
    # Write your code here
    # Hint: If root.data < key, go right
    # If root.data >= key, this could be ceil, but check left for smaller value
    pass


# --- Run & Test ---
root = TreeNode(8)
root.left = TreeNode(4)
root.right = TreeNode(12)
root.left.left = TreeNode(2)
root.left.right = TreeNode(6)
root.right.left = TreeNode(10)
root.right.right = TreeNode(14)

print(floor_bst(root, 5))    # expected: 4
print(ceil_bst(root, 5))     # expected: 6
