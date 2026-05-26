# N meetings in one room

# Problem Statement:
# Given the start and end times of N meetings, find the maximum number of meetings
# that can be accommodated in a single meeting room.
# Only one meeting can be held at a time in the room.

# Examples:
# Example 1:
#   Input:  start = [1, 3, 0, 5, 8, 5], end = [2, 4, 6, 7, 9, 9]
#   Output: 4
#   Explanation: Meetings at times (1,2), (3,4), (5,7), (8,9) can be held

# Example 2:
#   Input:  start = [10, 12, 20], end = [20, 25, 30]
#   Output: 2

# Difficulty: Medium


def n_meetings_one_room(start, end):
    # Write your code here
    # Hint: Sort meetings by end time
    # Greedily select meeting that ends earliest and doesn't overlap
    pass


# --- Run & Test ---
print(n_meetings_one_room([1, 3, 0, 5, 8, 5], [2, 4, 6, 7, 9, 9]))    # expected: 4
print(n_meetings_one_room([10, 12, 20], [20, 25, 30]))                # expected: 2
