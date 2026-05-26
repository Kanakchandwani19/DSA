# Insertion sort: first element is already sorted
# Then we take elements one by one and insert them at the correct place.

arr = [12, 34, 56, 23, 16, 55]

n = len(arr)

for i in range(1, n):
    current = arr[i]

    j = i -1
    while j>=0 and arr[j] > current:
        arr[j+1] = arr[j]
        j = j-1
    arr[j+1] = current

print(arr)
