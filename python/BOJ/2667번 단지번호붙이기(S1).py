import sys; sys.stdin = open('2667.txt')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# bfs
def bfs(x, y):
    global cnt
    Q = [[x, y]]
    visit[x][y] = cnt
    while Q:
        x, y = Q.pop(0)
        for k in range(4):
            tx, ty = x + dx[k], y + dy[k]
            if 0 <= tx < N and 0 <= ty < N and arr[tx][ty] == 1 and not visit[tx][ty]:
                visit[tx][ty] = cnt
                Q.append([tx, ty])

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
visit = [[0] * N for _ in range(N)]
cnt = 0
house = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and not visit[i][j]:
            cnt += 1
            bfs(i, j)


print(cnt)
for i in range(1, cnt + 1):
    temp = 0
    for j in range(N):
        for k in range(N):
            if visit[j][k] == i:
                temp += 1
    house.append(temp)

house.sort()
for i in house:
    print(i)


# dfs

# def dfs(x, y):
#     global cnt
#     if visit[x][y] == 1: return
#     if cnt == 0:
#         cnt += 1
#     visit[x][y] = 1
#     for i in range(4):
#         tx, ty = x + dx[i], y + dy[i]
#         if 0 <= tx < N and 0 <= ty < N:
#             if arr[tx][ty] == '1' and not visit[tx][ty]:
#                 cnt += 1
#                 dfs(tx, ty)
#
#
# N = int(input())
# arr = [list(input()) for _ in range(N)]
# visit = [[0] * (N) for _ in range(N)]
# res = []
# ans = 0
#
# for i in range(N):
#     for j in range(N):
#         cnt = 0
#         if arr[i][j] == '1':
#             dfs(i,j)
#             if cnt != 0:
#                 ans += 1
#                 res.append(cnt)
#
# print(ans)
#
# for _ in range(len(res)):
#     for i in range(len(res)-1):
#         if res[i] > res[i+1]:
#             res[i], res[i+1] = res[i+1], res[i]
#
# for i in res:
#     print(i)