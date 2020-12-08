T = int(input())
arr = list(map(int, input().split()))
for i in range(T):
    for j in range(len(arr)-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(arr[0], arr[-1])
