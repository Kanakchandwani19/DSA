# Introduction to Trees

# What is a Tree?
#   A tree is a non-linear hierarchical data structure made up of nodes.
#   Unlike arrays or linked lists (linear), trees branch out.

# Key Terminology:
#   Root       - the topmost node (no parent)
#   Node       - each element in the tree
#   Edge       - connection between two nodes
#   Parent     - a node with children
#   Child      - a node with a parent
#   Leaf       - a node with no children
#   Height     - longest path from root to a leaf
#   Depth      - distance of a node from the root
#   Subtree    - a node and all its descendants

# Visual Example:
#
#          1          <- root (depth 0)
#        /   \
#       2     3       <- depth 1
#      / \     \
#     4   5     6    <- depth 2 (4, 5, 6 are leaves)
#
#   Height of tree = 2
#   Parent of 4 = 2
#   Children of 1 = [2, 3]
#   Leaves = [4, 5, 6]

# Why Trees?
#   - Represent hierarchical data (file systems, org charts, HTML DOM)
#   - Faster search than arrays: O(log N) for balanced trees
#   - Used in databases (B-trees), compilers (parse trees), networking

# Types of Trees:
#   Binary Tree              - each node has at most 2 children
#   Binary Search Tree (BST) - left < root < right
#   AVL Tree                 - self-balancing BST
#   Heap                     - used in priority queues
#   Trie                     - used for string problems

# Traversal Types (covered in upcoming files):
#   Preorder    : Root -> Left -> Right
#   Inorder     : Left -> Root -> Right
#   Postorder   : Left -> Right -> Root
#   Level Order : level by level, left to right (BFS)

print("Tree concepts loaded. Move on to 2_binary_tree_representation.py")
