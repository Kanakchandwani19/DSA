# Rotate matrix by 90 degrees

# Problem Statement:
# Given an n x n 2D matrix, rotate it by 90 degrees clockwise in-place.

# Examples:
# Example 1:
#   Input:  matrix = [[1,2,3],
#                     [4,5,6],
#                     [7,8,9]]
#   Output: [[7,4,1],
#            [8,5,2],
#            [9,6,3]]

# Example 2:
#   Input:  matrix = [[5,1,9,11],
#                     [2,4,8,10],
#                     [13,3,6,7],
#                     [15,14,12,16]]
#   Output: [[15,13,2,5],
#            [14,3,4,1],
#            [12,6,8,9],
#            [16,7,10,11]]

# Difficulty: Medium


def rotate_matrix(matrix):
    # Write your code here
    # Hint: Two steps:
    # 1. Transpose the matrix (swap matrix[i][j] with matrix[j][i])
    # 2. Reverse each row
    pass


# --- Run & Test ---
matrix1 = [[1,2,3],
           [4,5,6],
           [7,8,9]]
rotate_matrix(matrix1)
print(matrix1)
# expected: [[7,4,1], [8,5,2], [9,6,3]]

matrix2 = [[5,1,9,11],
           [2,4,8,10],
           [13,3,6,7],
           [15,14,12,16]]
rotate_matrix(matrix2)
print(matrix2)
# expected: [[15,13,2,5], [14,3,4,1], [12,6,8,9], [16,7,10,11]]
