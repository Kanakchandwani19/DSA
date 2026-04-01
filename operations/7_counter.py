# Python Counter - Operations Practice
# =======================================
# Counter from collections is a dict subclass for counting hashable objects.
# It turns frequency counting from 5 lines into 1 line.
# Extremely common in DSA problems involving frequencies, anagrams, top-K.

from collections import Counter

# ---------------------------------------------------------
# STORY: You're analyzing votes in a school election.
# ---------------------------------------------------------

votes = [
    "Alice", "Bob", "Alice", "Charlie", "Bob", "Alice",
    "Charlie", "Bob", "Alice", "Charlie", "Charlie", "Bob"
]

# Q1. Count votes for each candidate in one line using Counter.
# vote_count = Counter(???)
# print(vote_count)
# expected: Counter({'Alice': 4, 'Bob': 4, 'Charlie': 4}) — adjust based on above

# Q2. How many votes did "Alice" get?
# print(vote_count[???])

# Q3. Who are the top 2 candidates? Use .most_common(2)
# print(vote_count.most_common(???))

# Q4. Access a candidate that doesn't exist — Counter returns 0, not KeyError.
# print(vote_count["Diana"])   # expected: 0

# Q5. Counter works on strings too — count character frequency.
word = "programming"
# char_count = Counter(???)
# print(char_count)

# Q6. Check if two strings are anagrams using Counter.
#     Two words are anagrams if their character counts are equal.
def are_anagrams(s1, s2):
    pass   # return Counter(s1) == Counter(s2)

# print(are_anagrams("listen", "silent"))   # expected: True
# print(are_anagrams("hello", "world"))     # expected: False

# Q7. Add two Counters together using + (combines counts).
week1 = Counter({"Alice": 3, "Bob": 2})
week2 = Counter({"Alice": 1, "Bob": 3, "Charlie": 4})
# total = week1 + week2
# print(total)   # expected: Counter({'Charlie': 4, 'Bob': 5, 'Alice': 4})

# Q8. Subtract one Counter from another using - (keeps only positive counts).
# diff = week2 - week1
# print(diff)

# Q9. Find the least common candidate using .most_common()[:-2:-1]
#     (last element of most_common is the least common)
# print(vote_count.most_common()[:-2:-1])

# Q10. Convert Counter back to a regular dict.
# regular_dict = dict(vote_count)
# print(regular_dict)
