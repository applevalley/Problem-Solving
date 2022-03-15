'''
벽을 부수자!
n x m 사이즈의 2차원 배열이 있고, 0은 갈 수 있는 곳, 1은 없는 곳이다.
(1, 1)에서 (n, m)까지 이동하는데, 최단 경로로 가야 한다!
시작 지점과 끝 지점 역시 경로에 포함되며, k개만큼의 벽을 부수는 것이 허락된다.
탈출할 수 있다면 최단 경로를, 불가능하다면 -1을 출력하자!

또 다시 bfs의 시간이 왔다!
deque에 x 좌표와 y 좌표 값을 넣되, 부술 수 있는 벽의 잔여 횟수인 k`와 현재까지 이동한 거리인 distance를 추가로 포함시킨다.
따라서 deque의 각 요소 안에는 총 4개의 int 값이 있는 것이다.
인접한 4방향으로 탐색을 수행하며, 갈 수 없는 곳(값이 1)이지만 k`가 0이 아니라면, k`를 1 차감하고 해당 좌표를 deque에 추가시킨다!
매 방문마다 n x m 사이즈의 visited에 이동한 횟수를 남기게 되는데... 모든 좌표에 있어 새롭게 최솟값으로 갱신을 하면 그 또한 많은 연산을 일으킬 지도 모른다.
그렇다고 방문한 좌표에 방문 처리를 하지 않으면 무한 루프에 빠질 우려가 있기에 방문하는 좌표는 방문 처리를 하고, (n, m) 위치에서만 최솟값 비교를 해보자!
'''


from collections import deque

dx = [-1, 1, 0, 0]            # 상하좌우
dy = [0, 0, -1, 1]

def BFS(x, y, k, dist):
    Q = deque()
    Q.append([x, y, k, dist])
    visited[x][y][k] = 0
    value = 0xffff

    while Q:
        x, y, k, dist = Q.popleft()
        if x == N - 1 and y == M - 1:
            value = min(value, dist)
            continue

        for i in range(4):
            tx, ty = x + dx[i], y + dy[i]
            if 0 <= tx < N and 0 <= ty < M and not visited[tx][ty][k]:

                if arr[tx][ty] == '0':
                    visited[tx][ty][k] = dist + 1
                    Q.append([tx, ty, k, dist + 1])
                elif k < K:
                    visited[tx][ty][k + 1] = dist + 1
                    Q.append([tx, ty, k + 1, dist + 1])

    if value == 0xffff:
        return -1
    else:
        return value + 1

    return -1

N, M, K = map(int, input().split())
arr = [list(input()) for _ in range(N)]
visited = [[[0] * M for _ in range(N)] for _ in range(K + 1)]

print(BFS(0, 0, 0, 0))