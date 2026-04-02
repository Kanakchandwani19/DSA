# Pattern 11 - Hollow Square
#
# * * * * *
# *       *
# *       *
# *       *
# * * * * *

# Problem Statement:
# Print a hollow square of stars of size N x N.
# Only the border cells contain *, interior cells are spaces.

# Example (N = 5):
# * * * * *
# *       *
# *       *
# *       *
# * * * * *

n=5

for i in range(n):
    for j in range(n):
        print("*" if i==0 or i==n-1 or j==0 or j==n-1 else " ", end=" ")
    print()

