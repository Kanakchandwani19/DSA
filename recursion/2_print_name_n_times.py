# Print Name N Times Using Recursion

# Problem Statement:
# Given a name (string) and a number N, print the name N times using recursion.
# Do NOT use any loop.

# Examples:
# Example 1:
#   Input:  name = "Nikhil", N = 4
#   Output:
#     Nikhil
#     Nikhil
#     Nikhil
#     Nikhil

# Example 2:
#   Input:  name = "Alice", N = 2
#   Output:
#     Alice
#     Alice

# Example 3:
#   Input:  name = "Bob", N = 0
#   Output:  (nothing printed)


def print_name(name, n):
    if n == 0:
        return
    print(name)
    print_name(name, n-1)
    


    


# --- Run & Test ---
print_name("Nikhil", 4)   # expected: Nikhil printed 4 times
print("---")
print_name("Alice", 2)    # expected: Alice printed 2 times
print("---")
print_name("Bob", 0)      # expected: nothing
