# Merge Intervals

# Problem Statement:
# Given an array of intervals, merge all overlapping intervals.

# Examples:
# Example 1:
#   Input:  intervals = [[1,3],[2,6],[8,10],[15,18]]
#   Output: [[1,6],[8,10],[15,18]]

# Example 2:
#   Input:  intervals = [[1,4],[4,5]]
#   Output: [[1,5]]

# Difficulty: Medium


def merge_intervals(intervals):
    # Write your code here
    # Hint: Sort intervals by start time
    # Iterate and merge if current start <= previous end
    pass


# --- Run & Test ---
print(merge_intervals([[1,3],[2,6],[8,10],[15,18]]))    # expected: [[1,6],[8,10],[15,18]]
print(merge_intervals([[1,4],[4,5]]))                    # expected: [[1,5]]
