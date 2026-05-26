# Insert Interval

# Problem Statement:
# Given a set of non-overlapping intervals sorted by start time, insert a new interval.
# Merge if necessary and return the result as a sorted list of intervals.

# Examples:
# Example 1:
#   Input:  intervals = [[1,3],[6,9]], newInterval = [2,5]
#   Output: [[1,5],[6,9]]

# Example 2:
#   Input:  intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
#   Output: [[1,2],[3,10],[12,16]]

# Difficulty: Medium


def insert_interval(intervals, new_interval):
    # Write your code here
    # Hint: Three parts
    # 1. Add all intervals that end before new interval starts
    # 2. Merge all overlapping intervals
    # 3. Add all intervals that start after new interval ends
    pass


# --- Run & Test ---
print(insert_interval([[1,3],[6,9]], [2,5]))                             # expected: [[1,5],[6,9]]
print(insert_interval([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))       # expected: [[1,2],[3,10],[12,16]]
