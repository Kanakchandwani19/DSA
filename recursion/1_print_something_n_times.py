# Understand Recursion by Printing Something N Times

# Problem Statement:
# Given a number N, print "Hello" N times using recursion.
# Do NOT use any loop — solve it recursively.

# Key Concept:
#   - A recursive function calls itself with a smaller input
#   - It must have a base case to stop (otherwise infinite recursion)
#   - Base case here: when N == 0, stop

# Examples:
# Example 1:
#   Input:  N = 3
#   Output:
#     Hello
#     Hello
#     Hello

# Example 2:
#   Input:  N = 1
#   Output:
#     Hello

# Example 3:
#   Input:  N = 0
#   Output:  (nothing printed)


def print_n_times(n):
    if n==0:
        return 
    
    print("Hello")
    print_n_times(n-1)

# --- Run & Test ---
print_n_times(3)   # expected: Hello printed 3 times
print("---")
print_n_times(1)   # expected: Hello printed 1 time
print("---")
print_n_times(0)   # expected: nothing
