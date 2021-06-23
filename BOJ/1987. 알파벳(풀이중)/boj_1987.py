# R x C 사이즈의 공간이 있고, 좌상단에 말이 있다.
# 인접한 4방향으로 이동하는데, 이동한 좌표에 있는 알파벳은 그 동안 지나온 알파벳과는 달라야 한다.
# 좌상단까지 포함했을 때, 최대 몇 칸까지 갈 수 있는가?

# 시간초과ㅠ

import sys
sys.setrecursionlimit(100000)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def DFS(x, y):
    global cnt
#
    alpha.add(arr[x][y])
    visited[x][y] = 1
    cnt = max(cnt, len(alpha))

    for i in range(4):
        tx, ty = x + dx[i], y + dy[i]
        if 0 <= tx < R and 0 <= ty < C and arr[tx][ty] not in alpha and not visited[tx][ty]:
            DFS(tx, ty)
            alpha.remove(arr[tx][ty])
            visited[tx][ty] = 0


R, C = map(int, sys.stdin.readline().split())
arr = [sys.stdin.readline().rstrip() for _ in range(R)]
alpha = set()
visited = [[0] * C for _ in range(R)]
cnt = 1

DFS(0, 0)

print(cnt)









# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# from collections import deque
#
# def BFS(x, y):
#     Q = deque()
#     Q.append([x, y])
#
#     while Q:
#         x, y = Q.popleft()
#         for i in range(4):
#             tx, ty = x + dx[i], y + dy[i]
#             if 0 <= tx < R and 0 <= ty < C and arr[tx][ty] not in alpha:
#                 Q.append([tx, ty])
#                 alpha.append(arr[tx][ty])
#
# R, C = map(int, input().split())
# arr = [input() for _ in range(R)]
# alpha = [arr[0][0]]
#
# BFS(0, 0)
# print(alpha)
