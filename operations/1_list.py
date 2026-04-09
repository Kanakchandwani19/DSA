# Python Lists - Operations Practice
# ====================================
# A list is an ordered, mutable collection. You can store anything in it.
# Think of it like a to-do notepad — you can add, remove, reorder items.

# ---------------------------------------------------------
# STORY: You are managing a cricket team's batting order.
# ---------------------------------------------------------

batting_order = ["Rohit", "Shubman", "Virat", "Shreyas", "KL Rahul"]

# Q1. A new player "Hardik" is added at the end of the order.
#     Use .append() to add him.
# batting_order.append(???)
# print(batting_order)
# expected: [..., "Hardik"]

batting_order.append("Hardik")
print(batting_order)

# Q2. "Virat" got injured. Remove him from the list using .remove().
# batting_order.remove(???)
# print(batting_order)

batting_order.remove("Virat")
print(batting_order)

# Q3. An opening batsman "Warner" is added at position 0 (top of the order).
#     Use .insert() to place him at index 0.
# batting_order.insert(???)
# print(batting_order)

batting_order.insert(0,"Warner")
print(batting_order)

# Q4. Print the last player in the order without hardcoding the index.
#     Hint: use negative indexing [-1]
# print(batting_order[???])

print(batting_order[-1])

# Q5. Reverse the batting order (they're now batting from the bottom).
#     Use .reverse()
batting_order.reverse()
print(batting_order)

# Q6. Sort the batting order alphabetically using .sort()
batting_order.sort()
print(batting_order)

# Q7. How many players are currently in the list?
#     Use len()
print(len(batting_order))

# Q8. Slice the first 3 players from the list.
#     Hint: list[start:end]
print(batting_order[0:3])

# Q9. Check if "Virat" is still in the list using 'in' keyword.
print("Virat" in batting_order)

# Q10. Create a copy of the batting order using .copy()
#      Change something in the copy — verify the original is unchanged.
backup = batting_order.copy()
backup.append("Jadeja")
print("Original:", batting_order)
print("Copy:", backup)
