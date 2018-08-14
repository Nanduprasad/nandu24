def smallest(arr,n):
    min = arr[0]
    for i in range(1, n):
        if arr[i] < min:
            min = arr[i]
    return min
arr = [10, 1, 2, 3, 24]
n = len(arr)
Ans = smallest(arr,n)
print (Ans)
