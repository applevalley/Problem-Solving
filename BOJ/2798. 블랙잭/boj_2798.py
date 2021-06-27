N, M = map(int,input().split())
numbers = list(map(int, input().split()))
max_v = 0

for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            cnt = numbers[i] + numbers[j] + numbers[k]
            if cnt > M: continue
            else:
                max_v = max(cnt, max_v)

print(max_v)