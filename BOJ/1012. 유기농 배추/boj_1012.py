dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def BFS(x, y):
    global cnt
    cnt += 1
    Q = [[x, y]]
    visit[x][y] = 1

    while Q:
        x, y = Q.pop(0)
        for i in range(4):
            tx, ty = x + dx[i], y + dy[i]
            if 0 <= tx < N and 0 <= ty < M and arr[tx][ty] == 1 and not visit[tx][ty]:
                visit[tx][ty] = 1
                Q.append([tx, ty])

for test_case in range(int(input())):
    M, N, K = map(int, input().split())
    arr = [[0] * M for _ in range(N)]
    visit = [[0] * M for _ in range(N)]
    cnt = 0

    for i in range(K):
        x, y = map(int, input().split())
        arr[y][x] = 1

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and not visit[i][j]:
                BFS(i, j)

    print(cnt)