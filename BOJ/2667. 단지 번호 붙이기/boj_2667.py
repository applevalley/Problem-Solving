dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def BFS(x, y):
    global cnt, temp
    cnt += 1
    Q = [[x, y]]
    visit[x][y] = cnt

    while Q:
        x, y = Q.pop(0)
        for i in range(4):
            tx, ty = x + dx[i], y + dy[i]
            if 0 <= tx < N and 0 <= ty < N and not visit[tx][ty] and arr[tx][ty] == "1":
                visit[tx][ty] = cnt
                Q.append([tx, ty])
                temp += 1


N = int(input())
arr = [list(input()) for _ in range(N)]
visit = [[0] * N for _ in range(N)]
cnt = 0
temp = 1
house = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == '1' and not visit[i][j]:
            BFS(i, j)
            house.append(temp)
            temp = 1

print(cnt)

house.sort()

for i in house:
    print(i)