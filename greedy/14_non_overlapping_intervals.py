# Non-overlapping Intervals

# Problem Statement:
# Given an array of intervals, find the minimum number of intervals you need to remove
# to make the rest of the intervals non-overlapping.

# Examples:
# Example 1:
#   Input:  intervals = [[1,2],[2,3],[3,4],[1,3]]
#   Output: 1
#   Explanation: Remove [1,3] to make rest non-overlapping

# Example 2:
#   Input:  intervals = [[1,2],[1,2],[1,2]]
#   Output: 2

# Example 3:
#   Input:  intervals = [[1,2],[2,3]]
#   Output: 0

# Difficulty: Medium


def non_overlapping_intervals(intervals):
    # Write your code here
    # Hint: Sort by end time
    # Greedily select intervals that end earliest
    # Count overlapping intervals that need to be removed
    pass


# --- Run & Test ---
print(non_overlapping_intervals([[1,2],[2,3],[3,4],[1,3]]))    # expected: 1
print(non_overlapping_intervals([[1,2],[1,2],[1,2]]))          # expected: 2
print(non_overlapping_intervals([[1,2],[2,3]]))                # expected: 0
