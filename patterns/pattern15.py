# Pattern 15 - Hourglass (Sandglass)
#
# * * * * *
#  * * * *
#   * * *
#    * *
#     *
#    * *
#   * * *
#  * * * *
# * * * * *

# Problem Statement:
# Print an hourglass pattern of height (2*N - 1) rows.
# Top half: stars decrease from N to 1, with increasing leading spaces.
# Bottom half: mirror of top half (stars increase from 2 to N).

# Example (N = 5):
# * * * * *
#  * * * *
#   * * *
#    * *
#     *
#    * *
#   * * *
#  * * * *
# * * * * *


def hourglass(n):
    for i in range(n,0,-1):
        print(" " * (n-i) + "* " * i)

    for i in range(1, n+1):
        print(" " * (n-i) + "* " * i)


hourglass(5)
