# 나이트는 수직으로 2칸을 가고서 수평으로 한 칸을 가거나, 수평으로 2칸을 가고서 수직으로 한 칸을 갈 수 있다.
# 특정한 좌표로 이동하기 위한 최소의 이동 횟수는 얼마일까?

# 우선 나이트의 이동을 정의해주어야 한다.
# 현재의 특정 좌표에서 이동이 가능하다는 전제 하에, 나이트가 이동할 수 있는 경우의 수는 8가지이다.
# 나이트의 현재 위치를 큐에 넣고, 8방향에 맞춰 계속 이동을 시킨다.
# 이렇게 가다보면 나이트는 목표 좌표에 여러번 도달할 것이다.
# 도착한 시점에서의 이동 횟수를 비교해 가장 작은 값이 답이 된다.

# 방문처리는 필요할까?
# 만약 특정 좌표를 다녀갔다는 표시를 하지 않는다면 무한히 나이트는 돌아다닐 것이다.
# 체스판의 범위 안에 있고, 방문하지 않은 경우 체스판과 같은 사이즈의 visited 배열의 해당 좌표에 방문 횟수의 값을 넣어준다.

# 체스판의 길이는 4에서 최대 300
# 시간 제한은 1초

# 생각보다 시간이 오래 걸렸다.
# 큐를 deque로 변경하고, sys를 통해 입력을 받아오게 수정했음에도 꽤 시간이 많이 걸리는 것을 보면 코드의 문제인것같다.
# 효율성을 더 올릴 수 있는 방법을 생각해봐야겠다.

import sys
from collections import deque

dx = [-1, -2, -2, -1, 1, 2, 2, 1]   # 한 위치에서 나이트가 이동할 수 있는 경우
dy = [-2, -1, 1, 2, -2, -1, 1, 2]

def BFS(x, y):
    global ans

    visited = [[0] * chess_length for _ in range(chess_length)]
    Q = deque()
    Q.append([x, y])

    while Q:
        x, y = Q.popleft()
        for i in range(8):
            tx, ty = x + dx[i], y + dy[i]
            if 0 <= tx < chess_length and 0 <= ty < chess_length and not visited[tx][ty]:
                Q.append([tx, ty])
                visited[tx][ty] = visited[x][y] + 1

                if tx == target_x and ty == target_y:
                    ans = min(ans, visited[tx][ty])

for test_case in range(int(sys.stdin.readline().rstrip())):
    chess_length = int(sys.stdin.readline().rstrip())
    chess_board = [[0] * chess_length for _ in range(chess_length)]
    knight_x, knight_y = map(int, sys.stdin.readline().split())
    target_x, target_y = map(int, sys.stdin.readline().split())
    ans = 10e9

    if knight_x == target_x and knight_y == target_y:
        print(0)
        continue

    BFS(knight_x, knight_y)

    print(ans)