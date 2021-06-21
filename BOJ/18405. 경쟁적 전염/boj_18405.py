# N x N 사이즈의 시험관에는 1~K번까지의 바이러스가 있고, 1초마다 4방향으로 전염된다.
# 다만 바이러스는 그 번호가 작은 순서대로 전염되기 시작한다. 이미 전염된 곳은 다른 번호의 바이러스에 추가적으로 전염되지 않는다.
# S초 이후의 (X, Y) 좌표의 값은? 바이러스가 없다면 0을 출력한다.

# N과 K는 각각 최대 200, 1000까지 올 수 있고, S는 최대 10000까지 올 수 있다.
# 따라서 단순히 S까지 매 회차마다 반복문을 통해 전체 리스트에서 바이러스의 좌표를 하나씩 추적해 4방향으로 전염시키는 것은 시간초과가 발생하게 된다.
# 초기 상태에서의 바이러스 좌표를 가지는 리스트와 전염이 되면서 퍼져나가는 좌표의 리스트를 따로 만들어 관리하면 어떨까?
# 시간 제한은 1초이다.

import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]  # 상하좌우
dy = [0, 0, -1, 1]

def BFS(z, x, y):
    Q = deque()
    Q.append([x, y])  # 좌표 입력
    visit[x][y] = 1   # 방문처리

    while Q:
        x, y = Q.popleft()

        for i in range(4):
            tx, ty = x + dx[i], y + dy[i]
            # tx, ty가 N x N 범위 안에 있고, 원본 배열에서의 좌표 값이 0이며, 아직 방문하지 않은 경우
            if 0 <= tx < N and 0 <= ty < N and arr[tx][ty] == 0 and not visit[tx][ty]:
                arr[tx][ty] = z        # 바이러스가 전염되었다! 값을 넣어주자
                infect_map.append([arr[tx][ty], tx, ty])     # 전염 리스트에 추가

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]    # 초기 배열
visit = [[0] * N for _ in range(N)]
S, X, Y = map(int, input().split())
cnt = 0

initial_map = []     # 초기 배열에서의 바이러스 정보를 입력해주기 위한 리스트

for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:
            initial_map.append([arr[i][j], i, j])

initial_map.sort()   # 정렬해주는 이유는 바이러스는 작은 순서부터 전염되기 때문이다. ex) [[1, 0, 0], [2, 1, 1]]
infect_map = []      # 감염 좌표 정보를 담기 위한 리스트

for i in range(S):
    if i == 0:       # 0초일 경우 아직 감염된 곳은 없다. 처음으로 바이러스가 있는 좌표들을 순회한다.
        for c, a, b in initial_map:
            BFS(c, a, b)
    else:            #  0초가 아닌 경우
        infect_map.sort()                        # 감염된 좌표를 담고 있는 리스트 역시 바이러스의 번호를 위해 정렬해준다.
        search_map = infect_map[:]               # 깊은 복사를 위한 슬라이싱
        infect_map = []                          # 리스트를 초기화하지 않는다면 좌표가 계속 쌓여나갈 것이다.
        for c, a, b in search_map:
            BFS(c, a, b)

print(arr[X - 1][Y - 1])                         # 좌표는 (0, 0)부터 시작하기에 1씩 빼주자