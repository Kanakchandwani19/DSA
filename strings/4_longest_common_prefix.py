# Longest Common Prefix

# Problem Statement:
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Examples:
# Example 1:
#   Input:  strs = ["flower", "flow", "flight"]
#   Output: "fl"

# Example 2:
#   Input:  strs = ["dog", "racecar", "car"]
#   Output: ""
#   Explanation: There is no common prefix among the input strings.

# Example 3:
#   Input:  strs = ["interspecies", "interstellar", "interstate"]
#   Output: "inters"

# Difficulty: Easy


def longest_common_prefix(strs):
    # Write your code here
    # Hint: Sort the array and compare only the first and last strings
    # Or iterate character by character for all strings
    pass


# --- Run & Test ---
print(longest_common_prefix(["flower", "flow", "flight"]))                      # expected: "fl"
print(longest_common_prefix(["dog", "racecar", "car"]))                         # expected: ""
print(longest_common_prefix(["interspecies", "interstellar", "interstate"]))    # expected: "inters"
