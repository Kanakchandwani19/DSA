# Shortest Job First

# Problem Statement:
# Given an array of job burst times, calculate the average waiting time
# using Shortest Job First (SJF) scheduling algorithm.

# Examples:
# Example 1:
#   Input:  bt = [4, 3, 7, 1, 2]
#   Output: 4
#   Explanation: Order: 1,2,3,4,7. Waiting times: 0,1,3,6,10. Average = 20/5 = 4

# Example 2:
#   Input:  bt = [1, 2, 3, 4]
#   Output: 2.5

# Difficulty: Medium


def shortest_job_first(bt):
    # Write your code here
    # Hint: Sort the burst times
    # Calculate waiting time for each job (sum of all previous burst times)
    # Return average waiting time
    pass


# --- Run & Test ---
print(shortest_job_first([4, 3, 7, 1, 2]))    # expected: 4.0
print(shortest_job_first([1, 2, 3, 4]))        # expected: 2.5
