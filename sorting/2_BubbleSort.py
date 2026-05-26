# bubble sort : Push biggest element to end
#             Repeatedly compare adjacent elements
# and swap if they are in wrong order


arr  = [4,2,1,3]

n = len(arr)

for i in range(n):
    for j in range(0, n-i-1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(arr)
