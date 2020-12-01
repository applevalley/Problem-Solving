dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def go(arr):
    x, y, tx, ty = R - 1, 0, R - 1, 0
    dir = 0
    num = 1
    for i in range(C * R):
        x, y = tx, ty
        arr[x][y] = num
        tx, ty = x + dx[dir], y + dy[dir]
        if tx < 0 or tx >= R or ty < 0 or ty >= C or arr[tx][ty] != 0:
            dir = (dir + 1) % 4
            tx, ty = x + dx[dir], y + dy[dir]
        num += 1

C, R = map(int, input().split())
arr = [[0] * C for _ in range(R)]
target = int(input())
number = list(range(1, (C*R + 1)))
go(arr)

# for i in arr:
#     print(*i)

for i in range(R):
    for j in range(C):
        if arr[i][j] == target:
            print(j + 1, R - i)

if target > max(number):
    print(0)