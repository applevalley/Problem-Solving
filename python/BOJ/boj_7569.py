import sys
sys.stdin = open('7569.txt')
# from collections import deque
#
# M, N, H = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N*H)]
# cnt, ans = 0, 0
# Q = deque()
#
# dx = [-1,1,0,0,N,-N]   # 상하좌우앞뒤
# dy = [0,0,-1,1,0,0]
#
# for i in range(N*H):
#     for j in range(M):
#         if arr[i][j] == 1:
#             Q.append((i,j,0))
# while Q:
#     s, e, ans = Q.popleft()
#     for i in range(6):
#         tx, ty = s + dx[i], e + dy[i]
#         if 0 <= tx < N and 0 <= ty < M:
#             if arr[tx][ty] == 0:
#                 arr[tx][ty] = 1
#                 Q.append((tx,ty, ans+1))
#                 cnt = ans + 1
#
# def chk(cnt):
#     for i in range(N):
#         for j in range(M):
#             if arr[i][j] == 0:
#                 return -1
#     return cnt
#
# print(chk(cnt))
# #
#
from collections import deque

M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
cnt, ans = 0, 0
Q = deque()

dx = [-1,1,0,0,0,0]   # 상하좌우앞뒤
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,1,-1]

for k in range(H):
    for i in range(N):
        for j in range(M):
            if arr[k][i][j] == 1:
                Q.append((i,j,k,0))
while Q:
    s, e, m, ans = Q.popleft()
    for i in range(6):
        tx, ty, tz = s + dx[i], e + dy[i], m + dz[i]
        if 0 <= tx < N and 0 <= ty < M and 0 <= tz < H:
            if arr[tz][tx][ty] == 0:
                arr[tz][tx][ty] = 1
                Q.append((tx,ty,tz, ans+1))
                cnt = ans + 1

def chk(cnt):
    for k in range(H):
        for i in range(N):
            for j in range(M):
                if arr[k][i][j] == 0:
                    return -1
    return cnt

print(chk(cnt))


# -1 -1
# -1 -1
# 여기서 -1 나와야하는데 0이 나온다다

