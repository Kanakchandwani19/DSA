# Minimum number of platforms required for a railway

# Problem Statement:
# Given arrival and departure times of all trains that reach a railway station,
# find the minimum number of platforms required so that no train waits.

# Examples:
# Example 1:
#   Input:  arrival = [900, 940, 950, 1100, 1500, 1800]
#           departure = [910, 1200, 1120, 1130, 1900, 2000]
#   Output: 3
#   Explanation: At time 1100, trains 2, 3, 4 are at station

# Example 2:
#   Input:  arrival = [900, 1100, 1235], departure = [1000, 1200, 1240]
#   Output: 1

# Difficulty: Medium


def minimum_platforms(arrival, departure):
    # Write your code here
    # Hint: Sort both arrays
    # Use two pointers to track arrivals and departures
    # Count platforms needed and track maximum
    pass


# --- Run & Test ---
print(minimum_platforms([900, 940, 950, 1100, 1500, 1800],
                       [910, 1200, 1120, 1130, 1900, 2000]))    # expected: 3
print(minimum_platforms([900, 1100, 1235], [1000, 1200, 1240])) # expected: 1
