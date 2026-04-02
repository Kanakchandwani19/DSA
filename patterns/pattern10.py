# Pattern 10 - Diamond
#
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *

# Problem Statement:
# Print a full diamond of stars with height (2*N - 1) rows.
# Top half is a pyramid, bottom half is an inverted pyramid.

# Example (N = 5):
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *


n=5

for i in range(1, n+1):
    print(" " * (n-i) + "*" * (2*i-1))

for i in range(n-1,0,-1):
    print(" " * (n-i) + "*" * (2*i-1))
