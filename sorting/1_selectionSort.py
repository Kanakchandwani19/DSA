# Selection sort: finds smallest element
# and puts it at correct position
# It is called Selection Sort because in every pass we select the minimum element.

arr = [13, 19, 24, 56, 9, 8]

n = len(arr)

for i in range(n):

    min = i

    for j in range(i+1, n):
        if arr[j] < arr[min]:
            min = j

    arr[i], arr[min] = arr[min], arr[i]

print(arr)