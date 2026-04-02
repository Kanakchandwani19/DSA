# Pattern 7 - Right-Aligned Triangle
#
#     *
#    **
#   ***
#  ****
# *****

# Problem Statement:
# Print a right-aligned triangle of stars of height N.
# Each row has leading spaces so the stars are flush to the right.

# Example (N = 5):
#     *
#    **
#   ***
#  ****
# *****

n = 5

for i in range(1, n+1):
    print(" " * (n-i) + "*" * i )


  
