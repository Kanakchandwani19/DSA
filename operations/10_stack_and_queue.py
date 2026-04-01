# Stack and Queue in Python
# ===========================
# Stack and Queue are not built-in types — they're patterns built on top of
# list or deque. Understanding how to implement them is fundamental to DSA.
#
# STACK  → Last In First Out (LIFO) — like a pile of plates
#           push = append()    pop = pop()    peek = list[-1]
#
# QUEUE  → First In First Out (FIFO) — like a ticket counter line
#           enqueue = append()   dequeue = popleft()   peek = deque[0]
#           Use deque, NOT list (list.pop(0) is O(N), deque.popleft() is O(1))

from collections import deque

# =============================================================
# PART 1 — STACK
# STORY: You're building a browser's Back button feature.
#        Each page visited is pushed. Back = pop the last page.
# =============================================================

browser_history = []   # using list as a stack

# Q1. Visit three pages — push them onto the stack using .append()
# browser_history.append("google.com")
# browser_history.append("youtube.com")
# browser_history.append("github.com")
# print(browser_history)

# Q2. User presses Back — pop the last visited page using .pop()
# last = browser_history.pop()
# print(f"Going back from: {last}")
# print(f"Now on: {browser_history[-1]}")

# Q3. Peek at the current page (top of stack) without popping.
# print(browser_history[-1])

# Q4. Is the history empty?
# print(len(browser_history) == 0)

# Q5. Classic stack problem: Check if brackets are balanced.
#     Valid: "()[]{}"   "([])"
#     Invalid: "(]"     "([)]"
def is_balanced(s):
    pass
    # hint: push opening brackets, pop when closing bracket found
    # check if popped bracket matches the closing one

# print(is_balanced("()[]{}"))   # expected: True
# print(is_balanced("([)]"))     # expected: False
# print(is_balanced("{[]}"))     # expected: True


# =============================================================
# PART 2 — QUEUE
# STORY: A movie ticket counter — first person in line gets served first.
# =============================================================

ticket_queue = deque()

# Q6. People join the line — enqueue using .append()
# ticket_queue.append("Nikhil")
# ticket_queue.append("Ananya")
# ticket_queue.append("Rohan")
# print(ticket_queue)

# Q7. Serve the first person in line — dequeue using .popleft()
# served = ticket_queue.popleft()
# print(f"Served: {served}")
# print(f"Next in line: {ticket_queue[0]}")

# Q8. Peek at who's next without removing.
# print(ticket_queue[0])

# Q9. How many people are waiting?
# print(len(ticket_queue))

# Q10. Classic queue problem: implement a "hot potato" game.
#      Players sit in a circle. Pass the potato N times.
#      The player holding it after N passes is eliminated.
#      Repeat until one player remains.
def hot_potato(players, num):
    queue = deque(players)
    # while more than 1 player:
    #   rotate the potato num times (use rotate or popleft+append)
    #   eliminate the player now holding it
    # return the winner
    pass

# print(hot_potato(["Nikhil", "Ananya", "Rohan", "Priya", "Kanak"], 7))
