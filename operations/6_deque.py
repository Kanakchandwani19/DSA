# Python Deque - Operations Practice
# =====================================
# deque (double-ended queue) from the collections module.
# Unlike a list, deque supports O(1) append and pop from BOTH ends.
# List pop(0) is O(N) — deque popleft() is O(1). Big deal in DSA!
#
# Use deque for: BFS, sliding window, implementing queues/stacks.

from collections import deque

# ---------------------------------------------------------
# STORY: You're managing a printer queue at a college lab.
#        New jobs join the back. The printer processes from the front.
#        VIP jobs can be added to the front (priority).
# ---------------------------------------------------------

printer_queue = deque(["Assignment1.pdf", "Resume.pdf", "Notes.pdf"])

# Q1. A new job "Project.pdf" joins at the back using .append()
# printer_queue.append(???)
# print(printer_queue)

# Q2. The printer finishes the first job — remove from the front using .popleft()
# finished = printer_queue.popleft()
# print("Printed:", finished)
# print(printer_queue)

# Q3. A professor's "Exam.pdf" is urgent — add to the FRONT using .appendleft()
# printer_queue.appendleft(???)
# print(printer_queue)

# Q4. The last job "Notes.pdf" is cancelled — remove from the back using .pop()
# printer_queue.pop()
# print(printer_queue)

# Q5. How many jobs are in the queue?
# print(len(printer_queue))

# Q6. Peek at the front job without removing it (index 0).
# print(printer_queue[0])

# Q7. Rotate the queue by 1 — moves the last element to the front.
#     Use .rotate(1)
# printer_queue.rotate(1)
# print(printer_queue)

# Q8. Convert the deque back to a list.
# jobs_list = list(printer_queue)
# print(jobs_list)

# Q9. Create a deque with a max size of 3 (older items auto-removed).
#     Use deque(maxlen=3)
# limited = deque(maxlen=3)
# limited.append("A")
# limited.append("B")
# limited.append("C")
# limited.append("D")   # "A" gets removed automatically
# print(limited)   # expected: deque(['B', 'C', 'D'], maxlen=3)

# Q10. Use deque to implement BFS on a simple graph.
#      (This is the most common DSA use of deque)
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6],
    4: [],
    5: [],
    6: []
}

def bfs(start):
    visited = []
    queue = deque([start])
    seen = set([start])
    # write your code here
    # while queue has elements:
    #   popleft a node, add to visited
    #   add its unvisited neighbors to queue
    pass

# print(bfs(1))   # expected: [1, 2, 3, 4, 5, 6]
