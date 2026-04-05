# Pattern 12 - Floyd's Triangle
#
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

# Problem Statement:
# Print Floyd's Triangle with N rows.
# Fill consecutive numbers row by row, starting from 1.
# Row i contains exactly i numbers.

# Example (N = 5):
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

n=5
num = 1

for i in range(1, n+1):
    for j in range(1, i+1):
        print(num, end=" ")
        num = num +1
    print()


