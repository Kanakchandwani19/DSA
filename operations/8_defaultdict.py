# Python defaultdict - Operations Practice
# ==========================================
# defaultdict from collections is like a regular dict BUT it never raises
# KeyError — it auto-creates a default value for missing keys.
#
# defaultdict(list)  → missing key returns []
# defaultdict(int)   → missing key returns 0
# defaultdict(set)   → missing key returns set()
#
# Extremely useful in DSA for: graph adjacency lists, grouping, frequency maps.

from collections import defaultdict

# ---------------------------------------------------------
# STORY: You're building a school timetable system.
#        Each subject maps to a list of students enrolled.
# ---------------------------------------------------------

# Without defaultdict you'd write:
#   if subject not in timetable:
#       timetable[subject] = []
#   timetable[subject].append(student)
#
# With defaultdict(list) — just append directly, no check needed!

timetable = defaultdict(list)

enrollments = [
    ("Math", "Nikhil"), ("Science", "Ananya"), ("Math", "Rohan"),
    ("English", "Priya"), ("Science", "Nikhil"), ("Math", "Priya"),
    ("English", "Rohan")
]

# Q1. Fill the timetable by looping through enrollments.
#     For each (subject, student), append student to timetable[subject].
# for subject, student in enrollments:
#     timetable[???].append(???)
# print(dict(timetable))
# expected: {'Math': ['Nikhil', 'Rohan', 'Priya'], 'Science': [...], 'English': [...]}

# Q2. Access a subject that no one enrolled in — no KeyError!
# print(timetable["Physics"])   # expected: []

# Q3. Use defaultdict(int) to count word frequency (like Counter but manual).
sentence = "the cat sat on the mat the cat"
word_freq = defaultdict(int)
# for word in sentence.split():
#     word_freq[???] += 1
# print(dict(word_freq))

# Q4. Use defaultdict(set) to build a graph (no duplicate edges).
edges = [(1, 2), (1, 3), (2, 4), (3, 4), (1, 2)]   # (1,2) appears twice
graph = defaultdict(set)
# for u, v in edges:
#     graph[u].add(v)
#     graph[v].add(u)
# print(dict(graph))
# expected: {1: {2, 3}, 2: {1, 4}, 3: {1, 4}, 4: {2, 3}}  — no duplicate edge

# Q5. Group anagrams using defaultdict(list).
#     Key = sorted word, value = list of original words.
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
groups = defaultdict(list)
# for word in words:
#     key = "".join(sorted(word))
#     groups[???].append(???)
# print(list(groups.values()))

# Q6. Convert a defaultdict back to a regular dict for clean output.
# clean = dict(timetable)
# print(clean)
