# Print the matrix in spiral manner

# Problem Statement:
# Given an m x n matrix, return all elements of the matrix in spiral order.

# Examples:
# Example 1:
#   Input:  matrix = [[1,2,3],
#                     [4,5,6],
#                     [7,8,9]]
#   Output: [1,2,3,6,9,8,7,4,5]

# Example 2:
#   Input:  matrix = [[1,2,3,4],
#                     [5,6,7,8],
#                     [9,10,11,12]]
#   Output: [1,2,3,4,8,12,11,10,9,5,6,7]

# Example 3:
#   Input:  matrix = [[1]]
#   Output: [1]

# Difficulty: Medium


def spiral_matrix(matrix):
    # Write your code here
    # Hint: Use four pointers: top, bottom, left, right
    # Traverse: left to right, top to bottom, right to left, bottom to top
    # Shrink boundaries after each direction
    pass


# --- Run & Test ---
print(spiral_matrix([[1,2,3],
                     [4,5,6],
                     [7,8,9]]))
# expected: [1,2,3,6,9,8,7,4,5]

print(spiral_matrix([[1,2,3,4],
                     [5,6,7,8],
                     [9,10,11,12]]))
# expected: [1,2,3,4,8,12,11,10,9,5,6,7]

print(spiral_matrix([[1]]))
# expected: [1]
