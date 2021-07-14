# 매 초마다 불은 인접한 4방향으로 퍼져가고, 벽에는 불이 붙지 않는다.
# 사람 역시 인접한 방향으로 이동할 수 있고, 벽을 뚫고 나갈 수 없으며, 불과 마찬가지로 한 동작에는 1초가 걸린다.
# 불이 옮겨졌거나 불이 붙으려 하는 칸으로는 이동할 수 없다.
# 따라서 행동의 우선 순위는 사람보다 불이 앞선다는 것을 생각해낼 수 있다!
# 탈출까지는 몇 초가 걸릴까?

# 인접한 방향 좌표를 큐에 넣어가며 탐색하기 위해 BFS를 이용해야겠다.
# 생각해볼 부분은 불이 하나만 있지 않다는 것이다. 가장 큰 배열의 크기는 1000 x 1000인데, 이 중 불이 몇 개까지 존재하는지는 알 수 없다.
# 불은 사람보다 앞서기 때문에, 모든 불이 각자 행동을 마치고 난 후에야 사람이 이동할 수 있다.
# 불들이 퍼져나가는 부분을 어떻게 효율적으로 풀어낼 수 있을까?

# 우선 배열을 순회하며 불과 사람의 위치를 확인한 후 각각 deque에 넣어준다.
# 만약 사람의 시작 위치가 모서리인 경우 1초만에 탈출이 가능할 것이다.
# 따라서 해당 경우에는 바로 1을 출력하고 테스트케이스를 빠져나와 불필요한 연산을 줄여준다.
# 그 외의 모든 경우에는 사람과 불에 있어 각각 BFS를 수행한다.
# 사람 BFS의 경우에, 모서리에 도착한 경우(탈출이 가능한 경우) 그 지점에서의 visit 배열에 기록된 값을 확인한다.
# 만약 불이 배열 상에 존재하지 않았거나, 불보다 더 빨리 도착한 경우(불 visit > 사람 visit) 확실하게 탈출하게 된다.
# 다만 탈출 가능 경로가 하나가 아닐 수 있기 때문에 탈출한 경우의 시간을 기록하고, 그 중 최솟값을 출력한다.


import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS_fire(arr):
    while arr:
        x, y = arr.popleft()
        for i in range(4):
            tx, ty = x + dx[i], y + dy[i]
            if 0 <= tx < h and 0 <= ty < w and area[tx][ty] != '#' and not visited_for_fire[tx][ty]:
                visited_for_fire[tx][ty] = visited_for_fire[x][y] + 1
                arr.append([tx, ty])

def BFS_man(arr):
    while arr:
        x, y = arr.popleft()
        for i in range(4):
            tx, ty = x + dx[i], y + dy[i]
            if 0 <= tx < h and 0 <= ty < w and area[tx][ty] not in ['#', '*'] and not visited_for_man[tx][ty]:
                visited_for_man[tx][ty] = visited_for_man[x][y] + 1
                arr.append([tx, ty])
                if tx == 0 or tx == h - 1 or ty == 0 or ty == w - 1:
                    if visited_for_fire[tx][ty] == 0 or visited_for_man[tx][ty] < visited_for_fire[tx][ty]:
                        exit.append(visited_for_man[tx][ty])

for test_case in range(int(sys.stdin.readline().rstrip())):
    w, h = map(int, sys.stdin.readline().split())
    area = [list(sys.stdin.readline().rstrip()) for _ in range(h)]
    visited_for_fire = [[0] * w for _ in range(h)]
    visited_for_man = [[0] * w for _ in range(h)]
    exit = []
    fire_list = deque()
    man = deque()
    exit_switch = False

    for i in range(h):
        for j in range(w):
            if area[i][j] == '*':
                fire_list.append([i, j])
                visited_for_fire[i][j] = 1
            elif area[i][j] == '@':
                man.append([i, j])
                visited_for_man[i][j] = 1
                if i == 0 or i == h - 1 or j == 0 or j == w - 1:
                    exit_switch = True

    if exit_switch == True:
        print(1)
        continue

    BFS_fire(fire_list)
    BFS_man(man)

    if exit:
        print(min(exit))
    else:
        print("IMPOSSIBLE")