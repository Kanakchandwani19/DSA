# Pattern 14 - Butterfly Pattern
#
# *       *
# **     **
# ***   ***
# **** ****
# *********
# **** ****
# ***   ***
# **     **
# *       *

# Problem Statement:
# Print a butterfly pattern of height (2*N - 1) rows.
# Top half: left stars increase, right stars mirror, spaces decrease.
# Bottom half: mirror of top half.
# Total width of each row = 2*N - 1.

# Example (N = 5):
# *       *
# **     **
# ***   ***
# **** ****
# *********
# **** ****
# ***   ***
# **     **
# *       *

n=5

for i in range(1, n+1):
    print("*" *i + " "* (2*(n-i)) + "*" *i)

for i in range(n-1,0,-1):
    print("*"*i + " "* (2*(n-i)) + "*" *i)
