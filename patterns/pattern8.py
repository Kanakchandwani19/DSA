# Pattern 8 - Pyramid (Centered Triangle)
#
#     *
#    ***
#   *****
#  *******
# *********

# Problem Statement:
# Print a centered pyramid of stars of height N.
# Row i has (2*i - 1) stars and appropriate leading spaces.

# Example (N = 5):
#     *
#    ***
#   *****
#  *******
# *********

n=5

for i in range(1, n+1): 
    print(" " * (n-i) + "*" * (2*i-1))
