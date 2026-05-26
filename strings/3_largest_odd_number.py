# Largest Odd Number in a String

# Problem Statement:
# You are given a string num, representing a large integer.
# Return the largest-valued odd integer (as a string) that is a non-empty substring of num.
# If no odd integer exists, return an empty string "".
# A substring is a contiguous sequence of characters within a string.

# Examples:
# Example 1:
#   Input:  num = "52"
#   Output: "5"
#   Explanation: The only non-empty substrings are "5", "2", and "52". "5" is the only odd number.

# Example 2:
#   Input:  num = "4206"
#   Output: ""
#   Explanation: There are no odd numbers in "4206".

# Example 3:
#   Input:  num = "35427"
#   Output: "35427"
#   Explanation: "35427" is already an odd number.

# Difficulty: Easy


def largest_odd_number(num):
    # Write your code here
    # Hint: A number is odd if its last digit is odd
    # Traverse from right to left and find the first odd digit
    pass


# --- Run & Test ---
print(largest_odd_number("52"))       # expected: "5"
print(largest_odd_number("4206"))     # expected: ""
print(largest_odd_number("35427"))    # expected: "35427"
