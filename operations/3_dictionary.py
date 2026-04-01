# Python Dictionaries - Operations Practice
# ==========================================
# A dictionary stores key-value pairs. Like a real dictionary:
# word (key) → meaning (value). Keys must be unique.

# ---------------------------------------------------------
# STORY: You're building a student report card system.
# ---------------------------------------------------------

report_card = {
    "Nikhil": 88,
    "Ananya": 95,
    "Rohan": 72,
    "Priya": 91
}

# Q1. Get Nikhil's marks using the key.
# print(report_card[???])

# Q2. Add a new student "Kanak" with marks 85.
# report_card[???] = ???
# print(report_card)

# Q3. Rohan studied hard. Update his marks to 80.
# report_card[???] = ???
# print(report_card)

# Q4. Remove "Ananya" from the report card using .pop()
#     .pop() also returns the removed value — print it.
# removed = report_card.pop(???)
# print("Removed:", removed)
# print(report_card)

# Q5. Check if "Priya" is in the report card using 'in'.
# print(??? in report_card)

# Q6. Print all student names (keys) using .keys()
# print(report_card.keys())

# Q7. Print all marks (values) using .values()
# print(report_card.values())

# Q8. Print each student's name and marks using .items() in a loop.
# for name, marks in report_card.???():
#     print(f"{name}: {marks}")

# Q9. Get "Deepak"'s marks safely — if not found, return 0.
#     Use .get() with a default value.
# print(report_card.get(???, ???))

# Q10. Find the student with the highest marks.
#      Hint: use max() with key= parameter
# topper = max(report_card, key=lambda student: report_card[student])
# print("Topper:", topper)

# Q11. How many students are in the report card?
# print(len(report_card))

# Q12. Create a copy of the report card and add 5 bonus marks to everyone.
#      Do NOT modify the original.
# bonus_card = report_card.copy()
# for student in bonus_card:
#     bonus_card[student] += 5
# print("Original:", report_card)
# print("With bonus:", bonus_card)
