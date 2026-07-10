# Next Greater Element - 2

# Problem Statement:
# Given a circular array (the next element of the last element is the first element),
# find the next greater element for every element.
# If it doesn't exist, return -1 for that number.

# Examples:
# Example 1:
#   Input:  arr = [1, 2, 1]
#   Output: [2, -1, 2]
#   Explanation: For first 1, NGE is 2. For 2, no element is greater (circular). For second 1, NGE is 2.

# Example 2:
#   Input:  arr = [1, 2, 3, 4, 3]
#   Output: [2, 3, 4, -1, 4]

# Example 3:
#   Input:  arr = [5, 4, 3, 2, 1]
#   Output: [-1, 5, 5, 5, 5]

# Difficulty: Medium


def next_greater_element_2(arr):
    # Write your code here
    # Hint: Since array is circular, traverse the array twice (use modulo)
    # Use a stack similar to NGE-1
    n = len(arr)
    result = [-1] *n
    stack = []

    for i in range(2 * n-1, -1, -1):

        index = i % n

        while stack and stack[-1] <= arr[index]:
            stack.pop()

        if i <n :
            if stack:
                result[index] = stack[-1]

        stack.append(arr[index])

    return result





# --- Run & Test ---
print(next_greater_element_2([1, 2, 1]))         # expected: [2, -1, 2]
print(next_greater_element_2([1, 2, 3, 4, 3]))   # expected: [2, 3, 4, -1, 4]
print(next_greater_element_2([5, 4, 3, 2, 1]))   # expected: [-1, 5, 5, 5, 5]
