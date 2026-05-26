# Quick Sort: FASTEST
# USING OF PIVOT ELEMENT

def quickSort(arr):

    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]

    left = []
    right = []

    for i in range(1, len(arr)):

        if arr[i] < pivot:
            left.append(arr[i])

        else:
            right.append(arr[i])

    left = quickSort(left)
    right = quickSort(right)

    return left + [pivot] + right

arr = [12,45,34,23,78,99]

print(quickSort(arr))