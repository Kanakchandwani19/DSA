# Set Matrix Zeroes

# Problem Statement:
# Given an m x n matrix, if an element is 0, set its entire row and column to 0.
# Do it in-place.

# Examples:
# Example 1:
#   Input:  matrix = [[1,1,1],
#                     [1,0,1],
#                     [1,1,1]]
#   Output: [[1,0,1],
#            [0,0,0],
#            [1,0,1]]

# Example 2:
#   Input:  matrix = [[0,1,2,0],
#                     [3,4,5,2],
#                     [1,3,1,5]]
#   Output: [[0,0,0,0],
#            [0,4,5,0],
#            [0,3,1,0]]

# Difficulty: Medium


def set_matrix_zeroes(matrix):
    # Write your code here
    # Hint: Use the first row and first column as markers
    # Use an extra variable to track if first row/column should be zero
    pass


# --- Run & Test ---
matrix1 = [[1,1,1],
           [1,0,1],
           [1,1,1]]
set_matrix_zeroes(matrix1)
print(matrix1)
# expected: [[1,0,1], [0,0,0], [1,0,1]]

matrix2 = [[0,1,2,0],
           [3,4,5,2],
           [1,3,1,5]]
set_matrix_zeroes(matrix2)
print(matrix2)
# expected: [[0,0,0,0], [0,4,5,0], [0,3,1,0]]
