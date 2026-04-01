# Python heapq - Operations Practice
# =====================================
# heapq gives you a min-heap in Python (smallest element always at top).
# It's not a class — it's a module of functions that work on a regular list.
#
# heapq.heappush(heap, val)  → add element
# heapq.heappop(heap)        → remove and return the SMALLEST element
# heap[0]                    → peek at smallest without removing
#
# For MAX heap: negate values (push -val, pop and negate result).
# Used in DSA for: top-K problems, Dijkstra's, merge K sorted lists.

import heapq

# ---------------------------------------------------------
# STORY: You're an ER doctor. Patients arrive with severity scores.
#        Higher severity = treated first (max heap).
#        But heapq is a min heap — so we store negative severity.
# ---------------------------------------------------------

# Q1. Create an empty heap and push patients with their severity.
patients = [(8, "Alice"), (3, "Bob"), (10, "Charlie"), (6, "Diana"), (1, "Eve")]

er = []
# for severity, name in patients:
#     heapq.heappush(er, (-severity, name))   # negate for max heap
# print(er)

# Q2. Who should be treated first? Peek at the top without removing.
# most_critical = er[0]
# print(f"Treat first: {most_critical[1]} (severity: {-most_critical[0]})")

# Q3. Treat the most critical patient — pop from the heap.
# severity, name = heapq.heappop(er)
# print(f"Treating: {name} (severity: {-severity})")
# print(f"Next up: {er[0][1]}")

# Q4. Convert a regular list into a heap in-place using heapq.heapify()
scores = [15, 3, 22, 8, 1, 19]
# heapq.heapify(scores)
# print(scores)          # list is now heap-ordered
# print(scores[0])       # expected: 1 (smallest)

# Q5. Find the 3 largest scores using heapq.nlargest()
# print(heapq.nlargest(3, scores))   # expected: [22, 19, 15]

# Q6. Find the 3 smallest scores using heapq.nsmallest()
# print(heapq.nsmallest(3, scores))  # expected: [1, 3, 8]

# Q7. Classic DSA: Find the Kth largest element using a min heap of size K.
def kth_largest(arr, k):
    pass
    # hint: maintain a heap of size K
    # if heap size exceeds K, pop the smallest
    # at the end, heap[0] is the Kth largest

# print(kth_largest([3, 2, 1, 5, 6, 4], 2))   # expected: 5
# print(kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # expected: 4

# Q8. Merge two sorted lists into one sorted list using heapq.merge()
list1 = [1, 4, 7]
list2 = [2, 3, 8]
# merged = list(heapq.merge(list1, list2))
# print(merged)   # expected: [1, 2, 3, 4, 7, 8]
