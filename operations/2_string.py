# Python Strings - Operations Practice
# ======================================
# Strings are immutable sequences of characters.
# Think of them like a printed ticket — you can read it, slice it,
# but you cannot change a character in place.

# ---------------------------------------------------------
# STORY: You're building a username validator for an app.
# ---------------------------------------------------------

username = "  NikhilCodes42  "

# Q1. The username has extra spaces. Clean it using .strip()
# clean = username.strip()
# print(clean)
# expected: "NikhilCodes42"

hey = username.strip()
print(hey)

# Q2. Convert the username to all lowercase (for case-insensitive comparison).
#     Use .lower()
print(hey.lower())

# Q3. Convert to all uppercase.
#     Use .upper()
print(hey.upper())

# Q4. Check if the username starts with "Nikhil" using .startswith()
print(hey.startswith("Nikhil"))

# Q5. Check if the username ends with "42" using .endswith()
print(hey.endswith("42"))

# Q6. Replace "42" with "99" in the username using .replace()
print(hey.replace("42", "99"))

# Q7. Find the index of "Codes" inside the username using .find()
#     Returns -1 if not found.
print(hey.find("Codes"))

# Q8. Split this sentence into a list of words using .split()
sentence = "Python is easy to learn"
# expected: ["Python", "is", "easy", "to", "learn"]

words = sentence.split()
print(words)

# Q9. Join the words back into a sentence using " ".join()
joined = " ".join(words)
print(joined)

# Q10. Count how many times the letter "o" appears in the sentence.
#      Use .count()
print(sentence.count("o"))

# Q11. Check if the username has only alphanumeric characters using .isalnum()
print(hey.isalnum())   # should be True

# Q12. Reverse the string using slicing.
#      Hint: string[::-1]
print(hey[::-1])

# Q13. Format a welcome message using f-string.
name = "Nikhil"
score = 99
print(f"Welcome {name}, your score is {score}!")
