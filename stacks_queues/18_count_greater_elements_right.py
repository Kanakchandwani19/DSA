# Number of Greater Elements to the Right

# Problem Statement:
# Given an array, for each element count how many elements to its right are greater than it.

# Examples:
# Example 1:
#   Input:  arr = [3, 4, 2, 7, 5, 8, 10, 6]
#   Output: [5, 4, 4, 3, 2, 1, 0, 0]
#   Explanation: For 3, there are 5 greater elements to right (4,7,5,8,10)

# Example 2:
#   Input:  arr = [5, 4, 3, 2, 1]
#   Output: [0, 0, 0, 0, 0]

# Example 3:
#   Input:  arr = [1, 2, 3, 4, 5]
#   Output: [4, 3, 2, 1, 0]

# Difficulty: Medium


def count_greater_elements_right(arr):
    # Write your code here
    # Hint: Traverse from right to left
    # For each element, count elements in remaining array that are greater
    # Can use a sorted data structure or merge sort approach
    n = len(arr)
    result = []

    for i in range(n):
        count = 0

        for j in range(i+1, n):
            if arr[j] > arr[i]:

                count += 1

        result.append(count)

    return result

        


# --- Run & Test ---
print(count_greater_elements_right([3, 4, 2, 7, 5, 8, 10, 6]))   # expected: [5, 4, 4, 3, 2, 1, 0, 0]
print(count_greater_elements_right([5, 4, 3, 2, 1]))             # expected: [0, 0, 0, 0, 0]
print(count_greater_elements_right([1, 2, 3, 4, 5]))             # expected: [4, 3, 2, 1, 0]
