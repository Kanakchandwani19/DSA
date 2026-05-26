# Sort Characters by Frequency

# Problem Statement:
# Given a string s, sort it in decreasing order based on the frequency of the characters.
# The frequency of a character is the number of times it appears in the string.
# Return the sorted string. If there are multiple answers, return any of them.

# Examples:
# Example 1:
#   Input:  s = "tree"
#   Output: "eert" or "eetr"
#   Explanation: 'e' appears twice, 'r' and 't' both appear once

# Example 2:
#   Input:  s = "cccaaa"
#   Output: "aaaccc" or "cccaaa"

# Example 3:
#   Input:  s = "Aabb"
#   Output: "bbAa" or "bbaA"

# Difficulty: Easy


def sort_characters_by_frequency(s):
    # Write your code here
    # Hint: Use a dictionary/Counter to count frequency
    # Sort by frequency in descending order
    # Build result string
    pass


# --- Run & Test ---
print(sort_characters_by_frequency("tree"))      # expected: "eert" or "eetr"
print(sort_characters_by_frequency("cccaaa"))    # expected: "aaaccc" or "cccaaa"
print(sort_characters_by_frequency("Aabb"))      # expected: "bbAa" or "bbaA"
