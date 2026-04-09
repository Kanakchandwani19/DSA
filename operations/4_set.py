# Python Sets - Operations Practice
# ====================================
# A set is an unordered collection of UNIQUE elements.
# No duplicates allowed. Great for membership checks and set math.
# Think of it like a guest list — each name appears only once.

# ---------------------------------------------------------
# STORY: Two college clubs are comparing their member lists.
# ---------------------------------------------------------

coding_club = {"Nikhil", "Ananya", "Rohan", "Priya", "Kanak"}
robotics_club = {"Rohan", "Kanak", "Deepak", "Sara", "Priya"}

# Q1. Add "Raj" to the coding club using .add()
coding_club.add("Raj")
print(coding_club)

# Q2. Try adding "Nikhil" again — sets ignore duplicates.
coding_club.add("Nikhil")
print(coding_club)   # size should not increase

# Q3. Remove "Ananya" from the coding club using .remove()
#     (raises error if not found — use .discard() to avoid error)
coding_club.remove("Ananya")
print(coding_club)

# Q4. Who is in BOTH clubs? (Intersection)
#     Use & operator or .intersection()
print(coding_club.intersection(robotics_club))
# both = coding_club & robotics_club
# print("In both clubs:", both)
# print(coding_club & robotics_club)


# Q5. Who is in EITHER club? (Union — combined list, no duplicates)
#     Use | operator or .union()
print(coding_club | robotics_club)


# Q6. Who is ONLY in the coding club (not in robotics)?
#     Use - operator or .difference()
# only_coding = coding_club - robotics_club
# print("Only in coding:", only_coding)
print(coding_club - robotics_club)

# Q7. Who is in one club but NOT both? (Symmetric Difference)
#     Use ^ operator or .symmetric_difference()
# exclusive = coding_club ^ robotics_club
# print("Exclusive members:", exclusive)
print(coding_club ^ robotics_club)

# Q8. Is "Priya" in the coding club? Use 'in' keyword.
print("Priya" in coding_club)

# Q9. How many members does each club have?
print(len(coding_club))
print(len(robotics_club))

# Q10. Are the clubs completely separate (no common members)?
#      Use .isdisjoint()
print(coding_club.isdisjoint(robotics_club))   # False — they share members

# Q11. A list has duplicates. Use a set to remove them.
attendance = ["Nikhil", "Rohan", "Nikhil", "Priya", "Rohan", "Kanak", "Priya"]
unique_attendance = set(attendance)
print(unique_attendance)
print("Unique count:", len(unique_attendance))
