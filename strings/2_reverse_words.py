# Reverse words in a given string

# Problem Statement:
# Given a string s, reverse the order of words in the string.
# Words are separated by spaces. Return the string with words in reverse order.
# Note: Handle multiple spaces between words properly.

# Examples:
# Example 1:
#   Input:  s = "the sky is blue"
#   Output: "blue is sky the"

# Example 2:
#   Input:  s = "  hello world  "
#   Output: "world hello"

# Example 3:
#   Input:  s = "a good   example"
#   Output: "example good a"

# Difficulty: Medium


def reverse_words(s):
    # Write your code here
    # Hint: Split by spaces, filter empty strings, reverse the list, join with space
    pass


# --- Run & Test ---
print(reverse_words("the sky is blue"))      # expected: "blue is sky the"
print(reverse_words("  hello world  "))      # expected: "world hello"
print(reverse_words("a good   example"))     # expected: "example good a"
