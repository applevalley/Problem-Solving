from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def melt(x, y):
    visited[x][y] = 1
    Q = deque()
    Q.append([x, y])
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            tx, ty = x + dx[i], y + dy[i]
            if 0 <= tx < N and 0 <= ty < M and arr[tx][ty] == 0 and arr[x][y] > 0:
                arr[x][y] -= 1

            if 0 <= tx < N and 0 <= ty < M and not visited[tx][ty]:
                visited[tx][ty] = 1
                Q.append([tx, ty])


N, M = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# while True:


while True:
    visited = [[0] * M for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0 and not visited[i][j]:
                cnt += 1
                melt(i, j)


    for i in arr:
        print(*i)
    for j in visited:
        print(*j)
    print()
