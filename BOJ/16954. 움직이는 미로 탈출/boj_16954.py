'''
체스판은 8 x 8이고 모든 칸은 벽이거나 빈칸이거나
캐릭터는 좌측 하단 끝에 있고, 우측 상단 끝으로 이동해야 한다.
1초마다 벽은 아래로 한 칸씩 내려오고, 가장 아래 칸보다 내려가면 사라지게 된다.
캐릭터는 인접 8방향으로 이동하거나 멈출 수 있다. 벽으로는 이동 못 한다.
캐릭터는 벽보다 먼저 이동한다. 벽이 캐릭터 위치로 오면 캐릭터는 더 이상 못 움직인다.
캐릭터는 우측 상단 끝으로 이동할 수 있나? 있으면 1, 없으면 0
--
인접 8방향에 멈추는 경우까지 해서 방향 벡터 리스트는 총 9개로 구성된다.
시작점인 좌측 하단 끝에서부터 BFS를 돌리면 어떻게 될까? => (8 * 8) ** 9 ......? 맞나?
여튼 시간초과난다. 그러면 어떻게 시간을 줄일 수 있나?(갈 수 없는 경로를 차단)

시작 좌표부터 방문하게 되는 모든 9가지 새로운 좌표에 있어 해당 좌표가 체스판을 벗어나지 않았거나,
해당 좌표의 x축 한 칸 위에 벽이 있지 않은 경우(캐릭터 이동 이후 벽이 내려오면서 겹쳐지는 경우)가 아니라면 이동할 수 있다.
이 경우 해당 정보를 큐에 넣어준다!

방문 정보는 어떻게 해야 하지...?
별도의 방문 처리가 없다면 계속 왔다갔다하면서 시간 초과날수도 있다.
그런데
'''

from collections import deque

dx = [-1, 1, 0, 0, -1, 1, -1, 1, 0]           # 상/하/좌/우/좌상/좌하/우상/우하/제자리
dy = [0, 0, -1, 1, -1, -1, 1, 1, 0]


def BFS(x, y):
    Q = deque()
    Q.append([x, y])
    cnt = 0

    while Q:
        visited = [[0] * 8 for _ in range(8)]

        for _ in range(len(Q)):
            x, y = Q.popleft()

            if chess_board[x][y] == '#': continue
            if x == 0 and y == 7: return 1

            for i in range(9):
                tx, ty = x + dx[i], y + dy[i]
                if 0 <= tx < 8 and 0 <= ty < 8 and chess_board[tx][ty] == '.' and not visited[tx][ty]:
                    visited[tx][ty] = 1
                    Q.append([tx, ty])

        chess_board.pop()
        chess_board.appendleft(['.', '.', '.', '.', '.', '.', '.', '.'])

        cnt += 1
        if cnt > 8:
            return 1

    return 0


chess_board = deque([list(input().strip()) for _ in range(8)])
print(BFS(7, 0))

# def BFS(x, y, k):
#     Q = deque()
#     Q.append([x, y, []])
#     cnt = 0
#
#     while Q:
#         x, y, visited = Q.popleft()
#         column = [[a, y] for a in range(x) if chess_board[a][y] == '#']
#         if x == 0 or not column or cnt > 7:
#             k = 1
#             break
#
#         for i in range(9):
#             tx, ty = x + dx[i], y + dy[i]
#             if 0 <= tx < 8 and 0 <= ty < 8:
#                 # if [tx, ty] not in wall_list and tx and chess_board[tx - 1][ty] == '.' and [tx, ty] not in visited:
#                 if [tx, ty] not in wall_list and (tx and [tx - 1, ty] not in wall_list):
#                     if i == 9:
#                         Q.append([tx, ty, visited])
#                     elif i != 9 and [tx, ty] not in visited:
#                         visited.append([tx, ty])
#                         Q.append([tx, ty, visited])
#
#         for i in range(len(wall_list)):
#             wall_x, wall_y = wall_list.popleft()
#             if wall_x == 7: continue
#
#             wall_list.append([wall_x + 1, wall_y])
#
#         print(wall_list)
#         cnt += 1
#
#     return 1 if k else 0



