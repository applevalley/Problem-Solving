# N x N 크기의 공간에 M마리의 물고기와 귀여운 아기 상어가 있다.
# 각 공간에는 최대 1마리의 물고기가 있을 수 있다.
# 아기 상어와 물고기는 모두 자연수인 크기를 가지는데, 아기 상어는 초기 크기가 2이다.
# 상어는 1초마다 4방향으로 인접한 한 칸을 이동하는데, 자신보다 큰 물고기가 있는 칸은 갈 수 없다.
# 상어는 자신보다 작은 물고기만 먹을 수 있고, 같은 크기의 경우 먹지는 못할 뿐 그 공간을 지날 수는 있다.
# 더 이상 먹을 물고기가 없다면 엄마를 부른다. 먹을 수 있는 물고기가 있으면 그 물고기를 먹으러 간다.
# 먹을 물고기가 둘 이상인 경우, 상어의 위치로부터 가까운 물고기를 먹는데,
# 거리가 같은 고기가 여럿 있다면 그 중에서 상단에 있는 것을 먹고, 상단인 고기가 둘 이상이라면 그 중 왼쪽에 있는 물고기를 먹는다.
# 상어는 자신의 크기와 같은 수의 물고기들을 먹을 때마다 크기가 1 커진다. 초기 크기는 2이기에 2마리 먹어야 크기가 3이 된다.
# 아기 상어는 몇초만에 엄마를 부를까?

# 0은 빈 칸, 1 ~ 6은 칸에 있는 물고기의 크기, 9는 상어의 초기 위치이다.

# 우선 맵을 둘러보며 어떤 물고기를 먹을 수 있을지 판단해야 한다.
# 먹을 수 있는 고기가 여럿 있는 경우, 그 중 도달하기까지 거리가 가장 짧은 물고기를 먹어야 한다.

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

import sys
from collections import deque


def bfs(x, y, arr):
    global ans, shark_size, shark_x, shark_y

    # if not arr: return

    temp = 0

    while True:
        if not arr: return
        arr.sort(key=lambda x: ((abs(shark_x - x[0]) + abs(shark_y - x[1])), x[0], x[1]))
        # arr.popleft()
        fish_x, fish_y, value = arr.pop(0)
        Q = deque()
        Q.append([x, y])
        visit = [[0] * N for _ in range(N)]
        check = False
        # visit[x][y] = 1
        while Q:
            x, y = Q.popleft()

            for i in range(4):
                tx, ty = x + dx[i], y + dy[i]
                if 0 <= tx < N and 0 <= ty < N and aqua[tx][ty] <= shark_size and not visit[tx][ty]:
                    Q.append([tx, ty])
                    visit[tx][ty] = visit[x][y] + 1

                    if tx == fish_x and ty == fish_y and aqua[tx][ty] < shark_size:
                        temp += 1
                        eaten.add((tx, ty))
                        ans += visit[tx][ty]
                        aqua[shark_x][shark_y] = 0
                        x, y = tx, ty
                        shark_x, shark_y = tx, ty
                        aqua[shark_x][shark_y] = 9
                        check = True
                        break
            if check == True: break


        if temp == shark_size:
            temp = 0
            shark_size += 1
            return

N = int(sys.stdin.readline())
aqua = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
eaten = set()

shark_size = 2
ans = 0

while True:
    fishes = []
    for i in range(N):
        for j in range(N):
            if 0 < aqua[i][j] < shark_size and (i, j) not in eaten:
                fishes.append([i, j, aqua[i][j]])
            elif aqua[i][j] == 9:
                shark_x, shark_y = i, j

    if not fishes: break

    bfs(shark_x, shark_y, fishes)


print(ans)
