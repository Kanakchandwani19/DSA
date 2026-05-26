# Merge Sort:
# Divide and conquer

def mergeSort(arr):
    
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2

    left = arr[:mid]
    right = arr[mid:]

    left = mergeSort(left)
    right = mergeSort(right)

    return merge(left, right)

def merge(left, right):

    result = []
     
    i=0
    j=0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result += [left[i]]
            i += 1

        else:
            result += [right[j]]
            j+=1

    while i < len(left):
        result += [left[i]]
        i += 1

    while j < len(right):
        result += [right[j]]
        j += 1

    return result

arr = [34, 45, 12, 23, 11]

sorted_array= mergeSort(arr)

print(sorted_array)


