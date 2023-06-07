from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def make_waterpool(x, y, idx):
    Q = deque()
    Q.append([x, y])
    possible = deque()
    possible.append([x, y])
    is_overflow = False
    temp_cnt = 0
    minimum = 0xffffff

    while Q:
        x, y = Q.popleft()

        if x == 0 or x == N - 1 or y == 0 or y == M - 1:
            is_overflow = True

        for _ in range(4):
            tx, ty = x + dx[_], y + dy[_]
            if 0 <= tx < N and 0 <= ty < M:
                if not visited[tx][ty] and arr[tx][ty] == idx:
                    visited[tx][ty] = 1
                    Q.append([tx, ty])
                    possible.append([tx, ty])

                if arr[tx][ty] < idx:
                    is_overflow = True

                if arr[tx][ty] > idx:
                    minimum = min(minimum, arr[tx][ty])

    if not is_overflow:
        temp_cnt += len(possible) * (minimum - idx)
        while possible:
            x, y = possible.popleft()
            arr[x][y] = minimum
            visited[x][y] = 0

    return temp_cnt


N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
maximum = max([max(i) for i in arr])
cnt = 0

for i in range(1, maximum + 1):
    for j in range(N):
        for k in range(M):
            if arr[j][k] == i and not visited[j][k]:
                visited[j][k] = 1
                cnt += make_waterpool(j, k, i)

print(cnt)