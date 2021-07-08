# pypy3로만 통과ㅠ 최적화가 더 필요하다.

# 빙산은 바닷물과 접하는 부분(인접하는 방향의 좌표값이 0인 경우) 1씩 녹아내린다.
# 언제 빙산이 두 덩어리 이상으로 분리될까?

# 모든 빙산을 순회하며 바닷물과 인접하는 만큼 녹게 하는 한 사이클을 거쳐야 한다는 생각이 들었다.
# 여기서 생각해봐야했던 것은 매 사이클마다 빙산에 대한 정보가 필요한가?라는 것이었다.
# 단순히 빙산이 0과 접하는 경우에 1씩 차감되게끔 만든다면 아래와 같은 문제가 있을 수 있다.

# 0 0 0 0       0 0 0 0         0 0 0 0         0 0 0 0
# 0 1 3 0   ->  0 0 3 0    ->   0 0 0 0   ->    0 0 0 0
# 0 0 4 0       0 0 4 0         0 0 4 0         0 0 0 0
# 0 0 0 0       0 0 0 0         0 0 0 0         0 0 0 0

# (0, 0)부터 순차적으로 값이 1 이상인 빙산에 대해 차감을 수행할 때, 앞 좌표의 빙산이 전부 녹아내려(0이 되는 경우)버리면
# 그 다음 좌표의 빙산은 앞서 녹아내린 빙산의 좌표까지 차감해버린다는 것이다.
# 사실 위의 경우 한 번의 사이클이 돌았을 때 아래와 같은 모양이 나와야 할 것이다.

# 0 0 0 0
# 0 0 1 0
# 0 0 1 0
# 0 0 0 0

# 따라서 매 사이클마다 빙산의 위치를 기록하게 해 해당 위치의 좌표는 0이 되더라도 계산에서 제외시켜야 할 필요가 있었다.
# 이를 통해 pypy3에서 통과는 할 수 있었지만, 파이썬에는 여전히 시간초과가 났다.
# 아마 매 회차마다 빙산의 정보를 저장한다는 부분에서 효율성에 대한 문제가 있지 않을까라는 생각이 든다.
# 어떻게 시간을 더 아낄 수 있을까..
# 회차마다 빙산을 찾기 위한 N x M 만큼의 연산이 돌고 있는 것도 시간에 큰 영향을 주고 있다.
# 위 2가지를 해결해낸다면, 파이썬으로도 문제가 없을 것이라고 생각된다.


import sys
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
            if 0 <= tx < N and 0 <= ty < M and arr[tx][ty] == 0 and arr[x][y] > 0 and not visited[tx][ty]:
                arr[x][y] -= 1

            if 0 <= tx < N and 0 <= ty < M and arr[tx][ty] > 0 and not visited[tx][ty]:
                visited[tx][ty] = 1
                Q.append([tx, ty])


N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
ans = 0

while True:
    visited = [[0] * M for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0 and not visited[i][j]:
                cnt += 1
                melt(i, j)

    if cnt > 1:
        break
    elif cnt == 0:
        ans = 0
        break
    ans += 1

print(ans)