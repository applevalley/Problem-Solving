T = int(input())
cnt = 0
arr = list(map(int, input().split()))

for i in range(T):
    cnt += (arr[i]/max(arr)) * 100

print(cnt/T)