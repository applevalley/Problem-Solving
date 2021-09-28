# N x M 형태의 직사각형 2차원 배열에 바이러스가 퍼진다.
# 이 바이러스는 인접한 4방향으로 퍼져나간다. 0은 빈 칸, 1은 벽, 2는 바이러스다.
# 새로 세울 수 있는 벽은 총 3개이다. 벽 3개를 잘 활용해서 바이러스가 퍼지는 영역을 최소화하자!
# 바이러스로부터 안전한 안전 영역의 최댓값은?

# 벽의 크기는 최대 8이다. 데이터의 크기가 크지 않다!
# 그러면 모든 0에 대해서 3개씩 조합을 해가지고 매번 벽을 세워서 돌리면 되나?
# 과연 그런 방식이 시간초과 없이 돌아가긴 할까..?

# 오늘도 라이브러리에 의존해버리고 말았다. 이런 습관 고쳐야 해..

import copy
from collections import deque
from itertools import combinations

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def wall(first, second, third):
    global cnt

    new_arr = copy.deepcopy(arr)     # 원본 배열에서 바이러스를 퍼트리고 다시 돌리는 것보다 매번마다 새 복사본 배열에서 진행하는게 구현이 편하기에 생성
    Q = deque()
    new_arr[first[0]][first[1]] = 1       # 새로 세울 벽 3개에 대해 새 복사본 배열에서 벽으로 처리해준다.
    new_arr[second[0]][second[1]] = 1
    new_arr[third[0]][third[1]] = 1

    for i in range(0, N):
        for j in range(0, M):
            if new_arr[i][j] == 2:        # 바이러스의 좌표를 덱에 넣고
                Q.append([i, j])

    while Q:                              # 바이러스를 퍼트린다
        x, y = Q.popleft()
        for i in range(4):
            tx, ty = x + dx[i], y + dy[i]
            if 0 <= tx < N and 0 <= ty < M and new_arr[tx][ty] == 0:
                Q.append([tx, ty])
                new_arr[tx][ty] = 2

    safe_area = [[x, y] for x in range(0, N) for y in range(0, M) if new_arr[x][y] == 0]   # 안전 영역에 속하는 좌표들

    if cnt < len(safe_area):         # 최댓값으로 바꾸기
        cnt = len(safe_area)


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
construction_for_wall = [[x, y] for x in range(0, N) for y in range(0, M) if arr[x][y] == 0]   # 벽 후보들
target = list(combinations(construction_for_wall, 3))           # 조합

for x, y, z in target:
    wall(x, y, z)

print(cnt)
