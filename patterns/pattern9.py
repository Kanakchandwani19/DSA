# Pattern 9 - Inverted Pyramid
#
# *********
#  *******
#   *****
#    ***
#     *

# Problem Statement:
# Print an inverted centered pyramid of stars of height N.
# First row has (2*N - 1) stars, each subsequent row decreases by 2.

# Example (N = 5):
# *********
#  *******
#   *****
#    ***
#     *

n=5 

for i in range(n,0,-1):
    print(" " * (n-i) + "*" * (2*i-1))
