# Next Smaller Element

# Problem Statement:
# Given an array, for each element find the next smaller element in the array.
# The next smaller element for an element x is the first smaller element on the right side of x.
# If no smaller element exists, return -1 for that element.

# Examples:
# Example 1:
#   Input:  arr = [4, 5, 2, 25]
#   Output: [2, 2, -1, -1]
#   Explanation: For 4, next smaller is 2. For 5, it's 2. For 2 and 25, none exists.

# Example 2:
#   Input:  arr = [13, 7, 6, 12]
#   Output: [7, 6, -1, -1]

# Example 3:
#   Input:  arr = [4, 3, 2, 1]
#   Output: [3, 2, 1, -1]

# Difficulty: Medium


def next_smaller_element(arr):
    # Write your code here
    # Hint: Similar to Next Greater Element, but pop elements greater than current
    # Use a stack, traverse from right to left
    stack = []
    result= []

    for i in range(len(arr) - 1, -1, -1):

        while stack and stack [-1] >= arr[i]:
            stack.pop()

        if not stack:
            result.append(-1)

        else:
            result.append(stack[-1])

        stack.append(arr[i])

    return result[::-1]


# --- Run & Test ---
print(next_smaller_element([4, 5, 2, 25]))    # expected: [2, 2, -1, -1]
print(next_smaller_element([13, 7, 6, 12]))   # expected: [7, 6, -1, -1]
print(next_smaller_element([4, 3, 2, 1]))     # expected: [3, 2, 1, -1]
