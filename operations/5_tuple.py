# Python Tuples - Operations Practice
# ======================================
# A tuple is like a list BUT immutable — once created, it cannot be changed.
# Use tuples when data should NOT change: coordinates, RGB colors, DB records.
# Tuples are faster than lists and can be used as dictionary keys.

# ---------------------------------------------------------
# STORY: You're storing GPS coordinates of city landmarks.
#        Coordinates must NEVER change — perfect for tuples.
# ---------------------------------------------------------

gateway = (18.9220, 72.8347)   # (latitude, longitude)
eiffel  = (48.8584, 2.2945)
everest = (27.9881, 86.9250)

# Q1. Print the latitude of the Gateway of India.
#     Use index 0.
# print(gateway[???])

# Q2. Unpack the eiffel tuple into two variables: lat and lon.
# lat, lon = ???
# print(f"Eiffel: lat={lat}, lon={lon}")

# Q3. Try changing the latitude of gateway — what happens?
# gateway[0] = 99.9999   # uncomment and observe the TypeError

# Q4. How many elements are in the everest tuple?
# print(len(???))

# Q5. Check if 72.8347 is in the gateway tuple using 'in'.
# print(??? in gateway)

# Q6. Tuples can be used as dictionary keys (lists cannot).
#     Create a dict that maps coordinates to landmark names.
# landmarks = {
#     (18.9220, 72.8347): "Gateway of India",
#     (48.8584, 2.2945) : "Eiffel Tower",
#     (27.9881, 86.9250): "Mount Everest"
# }
# print(landmarks[(48.8584, 2.2945)])   # expected: Eiffel Tower

# Q7. Concatenate gateway and eiffel into one tuple using +
# combined = gateway + eiffel
# print(combined)

# Q8. A function returning multiple values actually returns a tuple.
#     Write a function that returns (min, max) of a list.
def min_max(arr):
    pass   # return (min(arr), max(arr))

# result = min_max([3, 1, 9, 4, 7])
# low, high = result
# print(f"Min: {low}, Max: {high}")   # expected: Min: 1, Max: 9

# Q9. Convert the gateway tuple to a list, modify it, convert back.
# temp = list(gateway)
# temp[0] = 0.0
# new_gateway = tuple(temp)
# print(new_gateway)

# Q10. Create a tuple with a single element — tricky syntax!
# single = (42,)   # comma is required, otherwise it's just an int
# print(type(single))    # <class 'tuple'>
# print(type((42)))      # <class 'int'>  -- NOT a tuple
