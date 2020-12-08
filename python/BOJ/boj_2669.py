arr = [[0] * 100 for _ in range(100)]
cnt = 0

for i in range(4):
    square = list(map(int, input().split()))
    for j in range(square[0], square[2]):
        for k in range(square[1], square[3]):
            arr[j][k] = 1

# for _ in arr:
#     print(*_)

for i in range(100):
    for j in range(100):
        if arr[i][j]:
            cnt += 1

print(cnt)