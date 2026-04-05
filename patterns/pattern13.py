# Pattern 13 - Pascal's Triangle
#
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1

# Problem Statement:
# Print Pascal's Triangle with N rows.
# Each element is the sum of the two elements directly above it.
# The edges of every row are always 1.
#
# Formula: element at row r, col c = C(r, c) = r! / (c! * (r-c)!)

# Example (N = 5):
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1

# 1
# 1 1
# 1 2 1


def pascals_triangle(n):
    # list = [0] * n
    # list[0] = 1
    # 
    matrix = [[0 for j in range(n + 1)] for i in range(n)]

    matrix[0][1] = 1

    for i in range(1,n):  # i=1
        for j in range(1,i+2):  #j=1
            matrix[i][j] = matrix[i-1][j-1] + matrix[i-1][j]  # matrix[1][1] = matrix[0][0] + matrix[0][1] = 1


    
    for i in range(n):
        temp = []
        for j in range(n+1):
            if matrix[i][j] > 0: 
                temp.append(matrix[i][j])
        print(' '.join(str(x) for x in temp))

pascals_triangle(10)
