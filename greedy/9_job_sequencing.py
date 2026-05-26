# Job sequencing Problem

# Problem Statement:
# Given a set of N jobs where each job has a deadline and profit.
# Each job takes 1 unit of time. Only one job can be scheduled at a time.
# Profit is earned only if the job is completed by its deadline.
# Find the maximum profit and the number of jobs done.

# Examples:
# Example 1:
#   Input:  jobs = [[1, 4, 20], [2, 1, 10], [3, 1, 40], [4, 1, 30]]
#           Format: [job_id, deadline, profit]
#   Output: (2, 60)
#   Explanation: Job 3 (profit 40) and Job 1 (profit 20) can be done

# Example 2:
#   Input:  jobs = [[1, 2, 100], [2, 1, 19], [3, 2, 27], [4, 1, 25], [5, 1, 15]]
#   Output: (2, 127)

# Difficulty: Medium


def job_sequencing(jobs):
    # Write your code here
    # Hint: Sort jobs by profit in descending order
    # Use an array to track filled slots
    # For each job, find latest available slot before deadline
    pass


# --- Run & Test ---
print(job_sequencing([[1, 4, 20], [2, 1, 10], [3, 1, 40], [4, 1, 30]]))    # expected: (2, 60)
print(job_sequencing([[1, 2, 100], [2, 1, 19], [3, 2, 27], [4, 1, 25], [5, 1, 15]]))  # expected: (2, 127)
