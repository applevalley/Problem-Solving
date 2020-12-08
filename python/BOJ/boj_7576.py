import sys
sys.stdin = open('7576.txt')

# dx = [-1,1,0,0]   # 상하좌우
# dy = [0,0,-1,1]
#
# M, N = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
# temp, cnt, ans = 0, 0, 0
#
# temp = 0
# Q = []
#
# for i in range(N):
#     for j in range(M):
#         if arr[i][j] == 1:
#             Q.append((i,j,0))
# while Q:
#     s, e, ans = Q.pop(0)
#     for i in range(4):
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


from collections import deque

dx = [-1,1,0,0]   # 상하좌우
dy = [0,0,-1,1]

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt, ans = 0, 0
Q = deque()

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            Q.append((i,j,0))
while Q:
    s, e, ans = Q.popleft()
    for i in range(4):
        tx, ty = s + dx[i], e + dy[i]
        if 0 <= tx < N and 0 <= ty < M:
            if arr[tx][ty] == 0:
                arr[tx][ty] = 1
                Q.append((tx,ty, ans+1))
                cnt = ans + 1

def chk(cnt):
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                return -1
    return cnt

print(chk(cnt))