# N x M 사이즈의 미로에서 U, D, L, R의 명령에 따라 이동했을 때 미로의 경계 밖으로 탈출이 가능하게 하는 칸은 몇개일까?
# 탈출 가능한 "칸"이라는 데 주목해야겠다. BFS처럼 큐에 방향을 넣어가는 식의 이동이 아니라 그 칸의 명령을 그대로 따라만 가야 한다.
# 결국 모든 칸에 대해서 탐색을 해야 할 필요가 생긴다. 시간 초과 안날까? DFS로 구성한다면 최대 재귀 깊이를 가볍게 넘어버릴 것 같다.
# N과 M 전부 최대 데이터인 500이라고 가정했을 때, 최대 25,000칸에 대한 탐색을 해야 한다. 시간 제한은 1초다..


# 우선 기본적인 DFS를 만들어보자. 이 방식은 분명 시간 초과가 날 것이다.
# 실제로 시간 초과가 났다.


# 1차 시도
# import sys
# sys.setrecursionlimit(200000)

# dx = [-1, 1, 0, 0]  # UDLR
# dy = [0, 0, -1, 1]
#
# def DFS(x, y):
#     global cnt
#     # print(cnt)
#     visited[x][y] = 1
#     move_number = move_set.index(arr[x][y])
#     tx, ty = x + dx[move_number], y + dy[move_number]
#
#     if 0 > tx or tx >= N or 0 > ty or ty >= M: # 기본 명령 : 0 <= tx < N and 0 <= ty < M
#         cnt += 1
#     elif 0 <= tx < N and 0 <= ty < M and not visited[tx][ty]:
#         DFS(tx, ty)
#
# N, M = map(int, sys.stdin.readline().split())
# arr = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
#
# cnt = 0
# move_set = ['U', 'D', 'L', 'R']
#
# for i in range(N):
#     for j in range(M):
#         visited = [[0] * M for _ in range(N)]
#         DFS(i, j)
#
# print(cnt)



# 생각해보니, 시간을 줄일법한 생각이 들었다.
# 예를 들어, 한 좌표에서 명령을 따라 이동해 미로를 탈출했다.
# 추후에 방문하는 다른 좌표에서, 앞서 탈출한 경로의 지점을 방문한다면, 그 점 역시 탈출이 가능한 점이 되지 않을까?
# 어차피 같은 경로를 따라서 갈 것이기 때문이다.
# 또는 탐색의 시작점이 탈출 경로 중 한 점인 경우, 볼 것도 없이 탈출이 가능한 좌표이다.
# 이 방법의 관건은 탈출이 가능한 좌표를 얼마나 빨리 만나느냐이다.
# 만약 매우 큰 사이즈의 미로에서 탈출 지점이 가장 마지막 좌표라면, 결국 전부 다 순회하게 되는건데 그러면 똑같이 시간초과가 난다.
# 우선 (0, 0)부터 쭉 탐색하면서 방문표시를 새롭게 하고, 탈출한 지점이 나오면 해당 방문 좌표를 별도의 리스트에 담는다.
# 만약 탈출하지 않은 경우 방문표시를 위한 리스트를 초기화한다.

# 2차 시도
# 90% 시간초과 ㅠㅠㅠㅠㅠㅠ
# 혹시 위에서 생각했던 문제(탈출이 가능한 좌표가 배열의 최후반부에만 존재하는 경우)가 원인이었나 싶어서 (0, 0)이 아닌 거꾸로 탐색하는 방법을
# 시도했지만.. 여전히 90%에서 초과가 됬다. 뭔가 다른 방법이 필요하다. BFS로는 어떨까?

# import sys
# sys.setrecursionlimit(100000)
#
# dx = [-1, 1, 0, 0]  # UDLR
# dy = [0, 0, -1, 1]
#
# def DFS(x, y):
#     global cnt
#     if (x, y) in escape_list:
#         cnt += 1
#         return
#
#     visited.add((x, y))
#     move_number = move_set.index(arr[x][y])
#     tx, ty = x + dx[move_number], y + dy[move_number]
#
#     if 0 > tx or tx >= N or 0 > ty or ty >= M: # 기본 명령 : 0 <= tx < N and 0 <= ty < M
#         cnt += 1
#     elif 0 <= tx < N and 0 <= ty < M and (tx, ty) not in visited:
#         DFS(tx, ty)
#
# N, M = map(int, sys.stdin.readline().split())
# arr = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
# escape_list = set()
# cnt = 0
# move_set = ['U', 'D', 'L', 'R']
#
# for i in range(N):
#     for j in range(M):
#         visited = set()
#         temp = cnt
#         DFS(i, j)
#         if temp != cnt:
#             escape_list = escape_list | visited
#
# print(cnt)

# 3차 시도
# BFS로 바꾸어보았지만 역시 같은 지점에서 실패

# import sys
# from collections import deque
#
# dx = [-1, 1, 0, 0]  # UDLR
# dy = [0, 0, -1, 1]
#
# def BFS(x, y):
#     global cnt
#     Q = deque()
#     Q.append([x, y])
#     visited.add((x, y))
#
#     while Q:
#         new_x, new_y = Q.popleft()
#         move_number = move_set.index(arr[new_x][new_y])
#         tx, ty = new_x + dx[move_number], new_y + dy[move_number]
#
#         if 0 > tx or tx >= N or 0 > ty or ty >= M: # 기본 명령 : 0 <= tx < N and 0 <= ty < M
#             cnt += 1
#         elif 0 <= tx < N and 0 <= ty < M and (tx, ty) not in visited:
#             visited.add((tx, ty))
#             Q.append(tx, ty)
#
# N, M = map(int, sys.stdin.readline().split())
# arr = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
# escape_list = set()
# cnt = 0
# move_set = ['U', 'D', 'L', 'R']
#
# for i in range(N):
#     for j in range(M):
#         visited = set()
#         temp = cnt
#         BFS(i, j)
#         if temp != cnt:
#             escape_list = escape_list | visited
#
# print(cnt)


# 4차 시도
# 실패했던 지점의 좌표도 저장해두면 어떨까...?

# import sys
# sys.setrecursionlimit(100000)
#
# dx = [-1, 1, 0, 0]  # UDLR
# dy = [0, 0, -1, 1]
#
# def DFS(x, y):
#     global cnt
#     if (x, y) in escape_list:
#         cnt += 1
#         return
#
#     if (x, y) not in escape_list and (x, y) in fail_list:
#         return
#
#     visited.add((x, y))
#     move_number = move_set.index(arr[x][y])
#     tx, ty = x + dx[move_number], y + dy[move_number]
#
#     if 0 > tx or tx >= N or 0 > ty or ty >= M: # 기본 명령 : 0 <= tx < N and 0 <= ty < M
#         cnt += 1
#     elif 0 <= tx < N and 0 <= ty < M and (tx, ty) not in visited:
#         DFS(tx, ty)
#
# N, M = map(int, sys.stdin.readline().split())
# arr = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
# escape_list = set()
# fail_list = set()
# cnt = 0
# move_set = ['U', 'D', 'L', 'R']
#
# for i in range(N):
#     for j in range(M):
#         visited = set()
#         temp = cnt
#         DFS(i, j)
#         if temp != cnt:
#             escape_list = escape_list | visited
#         else:
#             fail_list = fail_list | visited
#
# print(cnt)



#
#
#
# import sys
# from collections import deque
#
# dx = [-1, 1, 0, 0]  # UDLR
# dy = [0, 0, -1, 1]
#
#
# def BFS(x, y):
#     global cnt
#     Q = deque()
#     Q.append([x, y])
#     escape_list = set()
#     escape_list.add((x, y))
#     visited[x][y] = 1
#
#     while Q:
#         new_x, new_y = Q.popleft()
#         if check[x][y]:
#             for a, b in escape_list:
#                 check[a][b] = 1
#             cnt += 1
#             return
#
#         move_number = move_set.index(arr[new_x][new_y])
#         tx, ty = new_x + dx[move_number], new_y + dy[move_number]
#
#
#         # if 0 > tx or tx >= N or 0 > ty or ty >= M:
#         if (not (0 <= tx < N)) or (not (0 <= ty < M)):
#             for a, b in escape_list:
#                 check[a][b] = 1
#             cnt += 1
#         elif check[tx][ty] == -1:
#             for a, b in escape_list:
#                 check[a][b] = -1
#             return
#         elif not visited[tx][ty]:
#             visited[tx][ty] = 1
#             escape_list.add((tx, ty))
#             Q.append((tx, ty))
#
#     for a, b in escape_list:
#         check[a][b] = -1
#     return
#
# N, M = map(int, sys.stdin.readline().split())
# arr = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
# visited = [[0] * M for _ in range(N)]
# check = [[0] * M for _ in range(N)]
# cnt = 0
# move_set = ['U', 'D', 'L', 'R']
#
# for i in range(N):
#     for j in range(M):
#         if check[i][j] == -1:
#             continue
#         elif check[i][j]:
#             cnt += 1
#             continue
#
#         BFS(i, j)
#
# print(cnt)
#
# #
# import collections
# import sys
# from collections import deque


# def bfs(y, x):
#     global cnt
#     q = deque([(y, x)])
#
#     # dp에 탈출할 수 있는 여부를 표시하기 위한 course
#     course = set()
#     course.add((y, x))
#     # 방문 체크
#     # visited = [[0] * m for _ in range(n)]
#     visited[y][x] = 1
#     while q:
#         y, x = q.popleft()
#         # 탈출할 수 있는 곳이면 여태까지 방문했던 곳을 dp에 표시
#         if dp[y][x]:
#             for value in course:
#                 dp[value[0]][value[1]] = 1
#             cnt += 1
#             return
#         # 조건에 따라 움직임
#         if area[y][x] == 'U':
#             y -= 1
#         elif area[y][x] == 'R':
#             x += 1
#         elif area[y][x] == 'D':
#             y += 1
#         else:
#             x -= 1
#
#         # 탈출 했다면 방문한 곳을 dp에 표시
#         if (not (0 <= y < n)) or (not (0 <= x < m)):
#             for value in course:
#                 dp[value[0]][value[1]] = 1
#             cnt += 1
#         # 탈출 불가능 하다면 방문한 곳을 dp에 표시
#         elif (dp[y][x] == -1):
#             for value in course:
#                 dp[value[0]][value[1]] = -1
#             return
#         # 아니면 다음 과정
#         elif not visited[y][x]:
#             visited[y][x] = 1
#             course.add((y, x))
#             q.append((y, x))
#     # 여기까지 왔으면 탈출 불가능하므로 dp에 표시
#     for value in course:
#         dp[value[0]][value[1]] = -1
#     return
#
#
# n, m = map(int, sys.stdin.readline().split())
# area = [sys.stdin.readline() for _ in range(n)]
# dp = [[0] * m for _ in range(n)]
# visited = [[0] * m for _ in range(n)]
# cnt = 0
# for i in range(n):
#     for j in range(m):
#         # 탈출할 수 없는 곳인지?
#         if (dp[i][j] == -1):
#             continue
#         # 탈출할 수 있는 곳인지?
#         elif dp[i][j]:
#             cnt += 1
#             continue
#
#         # 둘 다 아니면
#         bfs(i, j)
# print(cnt)


import sys
from collections import deque

dx = [-1, 1, 0, 0]  # UDLR
dy = [0, 0, -1, 1]

def find(x, y):
    global cnt

    if (x, y) in success: return

    Q = deque()
    Q.append([x, y])
    visit = [[0] * m for _ in range(n)]
    visit[x][y] = 1
    move_number = move_set.index(area[x][y])           # 구석 칸에 위치한 명령(방향)을 인식
    tx, ty = x + dx[move_number], y + dy[move_number]  # 방향에 맞게 위치를 조정

    if not (0 <= tx < n) or not (0 <= ty < m):         # 미로를 탈출했을까?
        success.add((x, y))                            # 탈출했다면 해당 좌표를 탈출 리스트에 추가하고
        cnt += 1                                       # 탈출 가능한 칸의 수를 추가해주자

        # 해당 구석 좌표로 탈출이 가능한 것을 확인했다.
        # 이제 인접한 방향의 좌표들을 확인해나갈 차례이다! 만약 인접한 좌표의 명령이 탈출이 가능한 구석 좌표이거나,
        # 해당 구석 좌표를 향해 갈 수 있는 곳이라면 구석이 아닌 그 좌표도 역시 탈출할 수 있는 좌표가 된다.
        # (좌표를 따라 가면 탈출이 가능한 구석 좌표를 만날 것이고, 그러면 탈출이 가능하기 때문에)
        while Q:
            Q_x, Q_y = Q.popleft() # 1 3

            for k in range(4):  # k = 1
                new_tx, new_ty = Q_x + dx[k], Q_y + dy[k] # x, y = 2 3
                if 0 <= new_tx < n and 0 <= new_ty < m:   # 인접한 방향 중 구석이 아닌 경우
                    target_number = move_set.index(area[new_tx][new_ty]) # num = 0
                    target_x, target_y = new_tx + dx[target_number], new_ty + dy[target_number] #

                    if target_x == Q_x and target_y == Q_y:
                        success.add((target_x, target_y))
                        cnt += 1
                        # visit[new_tx][new_ty] = 1
                        Q.append([target_x, target_y])

    # else:
    #     Q = deque()
    #     Q.append([tx, ty])
    #     while Q:
    #         tx, ty = Q.popleft()
    #         visit[tx][ty] = 1
    #         move_number = move_set.index(area[tx][ty])
    #         new_tx, new_ty = tx + dx[move_number], ty + dy[move_number]
    #
    #         if not (0 <= new_tx < n) or not (0 <= new_ty < m) and not visit[new_tx][new_ty]:
    #             success.add((x, y))
    #             cnt += 1
    #             return

            # if 0 <= new_tx < n and 0 <= new_ty < m and not visit[new_tx][new_ty]:



        # elif 0 < tx < n - 1 and 0 < ty < m - 1 and [tx, ty] not in check: # and not visit[tx][ty]:
        #     check.append([tx, ty])


n, m = map(int, sys.stdin.readline().split())
area = [sys.stdin.readline() for _ in range(n)]
visit = [[0] * m for _ in range(n)]
corner = []
check = deque()
success = set()
failed = set()
cnt = 0
move_set = ['U', 'D', 'L', 'R']

# 구석 좌표만 따로 모아주는 과정
for i in range(n):
    for j in range(m):
        if i == 0 or i == n - 1:
            corner.append([i, j]) #, [area[i][j]]])
        elif j == 0 and area[i][j] not in corner or j == m - 1 and area[i][j] not in corner:
            corner.append([i, j])


# 구석 좌표들을 대상으로 검사
for i, j in corner:
    find(i, j)
#
# if check:
#     while check:
#         new_x, new_y = check.popleft()
#         visit[new_x][new_y] = 1
#
#         for i in range(4):
#             new_tx, new_ty = new_x + dx[i], new_y + dy[i]
#
#             if (new_tx, new_ty) in success and (new_x, new_y) not in success:
#                 success.add((new_x, new_y))
#                 cnt += 1
#
#             if 0 < new_tx < n - 1 and 0 < new_ty < m - 1 and not visit[new_tx][new_ty]:
#                 check.append([new_tx, new_ty])


print(cnt)
