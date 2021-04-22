dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(x, y):
    global cnt
    Q = [[x, y]]
    visit[x][y] = 1
    cnt += 1
    while Q:
        x, y = Q.pop(0)
        for i in range(4):
            tx, ty = x + dx[i], y + dy[i]
            if 0 <= tx < M and 0 <= ty < N and arr[tx][ty] == 0 and not visit[tx][ty]:
                Q.append([tx, ty])
                visit[tx][ty] = 1
                cnt += 1

M, N, K = map(int, input().split())
arr = [[0] * N for _ in range(M)]
visit = [[0] * N for _ in range(M)]
cnt = 0
space = []

for i in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(x1, x2):
        for k in range(y1, y2):
            arr[k][j] = 1

for i in range(M):
    for j in range(N):
        cnt = 0
        if arr[i][j] == 0 and not visit[i][j]:
            BFS(i, j)
            space.append(cnt)

space.sort()

print(len(space))
for i in space:
    print(i, end=' ')