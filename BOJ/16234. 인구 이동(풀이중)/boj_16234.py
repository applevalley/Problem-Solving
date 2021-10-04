'''
국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면 국경선을 공유한다.
공유된 국경선을 통해 이동이 가능한 나라들을 연합으로 보고, 각 칸의 인구 수를 (연합의 인구 수 / 칸의 개수)로 바꿔준다. 이 과정이 1회다.
몇 회동안 인구 이동이 일어나는가?

모든 좌표에 대해 상하좌우로 4번 확인한다. 기준 좌표 (x, y)와 벡터로 만들어진 대상 좌표(tx, ty)에 대해 두 값의 차가 L부터 R 사이라면 연합에 포함시키고, 해당 좌표값을 변수에 더해준다.
이렇게 한 번의 순회에서 대상 좌표들을 전부 구해 저장한다. 좌표를 탐색하면서 값을 누적시킨 변수를 활용해 인구 이동을 해나간다.
'''

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(x, y):
    global ans, check

    Q = deque()
    Q.append([x, y])
    visited[x][y] = 1
    temp = arr[x][y]
    connected = [[x, y]]

    while Q:
        print(Q)
        print(visited)
        print(connected)
        x, y = Q.popleft()
        for i in range(4):
            tx, ty = x + dx[i], y + dy[i]
            if 0 <= tx < N and 0 <= ty < N and L <= abs(arr[x][y] - arr[tx][ty]) <= R and not visited[tx][ty] and [tx, ty] not in connected:
                Q.append([tx, ty])
                visited[tx][ty] = 1
                temp += arr[tx][ty]
                connected.append([tx, ty])

    for x, y in connected:
        arr[x][y] = int(temp / len(connected))

    ans += 1
    check = True

N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0

while True:
    visited = [[0] * N for _ in range(N)]
    check = False
    # for _ in arr:
    #     print(*_)
    #
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                BFS(i, j)

print(ans)
