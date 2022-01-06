import sys; sys.stdin = open('1868.txt')


# def BFS(x, y):
#     global mine_cnt
#     Q = [[x, y]]
#     Q_temp = 0
#     while Q:
#         mine_cnt = 0
#
#         x, y = Q.pop(0)
#         if arr[x][y] != '.':
#             continue
#
#         for l in range(8):
#             tx, ty = x + dx[l], y + dy[l]
#             if 0 <= tx < N and 0 <= ty < N:
#                 if arr[tx][ty] == '*':
#                     mine_cnt += 1
#                 elif arr[tx][ty] == '.':
#                     Q.append([tx, ty])
#
#         if mine_cnt:
#             if Q_temp == 0:
#                 Q = []
#                 continue
#             # if Q_temp and arr[x][y] == '.':
#             #     arr[x][y] = mine_cnt
#             #     continue
#             # elif Q_temp == 0:
#             #     Q = []
#
#         else:
#             arr[x][y] = mine_cnt
#         Q_temp += 1
#
#
# dx = [-1, 1, 0, 0, -1, -1, 1, 1] # 상하좌우 좌상 우상 좌하 우하
# dy = [0, 0, -1, 1, -1, 1, -1, 1]
#
# for test_case in range(1, int(input()) + 1):
#     N = int(input())
#     arr = [list(input()) for _ in range(N)]
#     mine_cnt = 0 # 지뢰 카운터
#     cnt = 0 # 클릭 횟수
#
#     for _ in arr:
#         print(*_)
#     print()
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == '.':
#                 BFS(i, j)
#                 # if arr[i][j] != '.':
#                 #     cnt += 1
#                 if i == 0 and j == 3:
#                     for m in arr:
#                         print(*m)
#
#
#
#     # for _ in arr:
#     #     print(*_)
#
#     # print(cnt)
#     #
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == '.':
#                 cnt += 1
#
#     print(cnt)
#
#
#
#

# 수업 코드
from collections import deque

dr = [-1, 1, 0, 0, -1, -1, 1, 1]  # 상하좌우 좌상 우상 좌하 우하
dc = [0, 0, -1, 1, -1, 1, -1, 1]

def BFS(r, c):
    queue = deque()
    queue.append((r, c))
    visited[r][c] = True

    while queue:
        curr_r, curr_c = queue.popleft()
        for i in range(8):
            nr = curr_r + dr[i]
            nc = curr_c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                visited[nr][nc] = True
                if game[nr][nc] == 0:  # 연쇄적으로 클릭이 가능하면
                    queue.append((nr, nc))


def DFS(r, c):
    visited[r][c] = True
    if game[r][c] != 0:
        return

    for i in range(8):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
            DFS(nr, nc)

def mine_check(r, c):
    cnt = 0
    for i in range(8):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nr >= N or nc < 0 or nc >= N: continue
        if game[nr][nc] == '*': cnt += 1
    return cnt

for tc in range(1, int(input()) + 1):
    N = int(input())
    game = [list(input()) for _ in range(N)] #지뢰판

    # 내 주변 지뢰의 수로 2차원 리스트 갱신
    zero_list = []
    for i in range(N):
        for j in range(N):
            if game[i][j] == '.':
                game[i][j] = mine_check(i, j)
            if game[i][j] == 0:
                zero_list.append((i, j))

    ans = 0
    # 주변에 지뢰가 하나도 없는 값들을 먼저 클릭
    visited = [[False] * N for _ in range(N)]

    for r, c in zero_list:
        if visited[r][c]: continue
        BFS(r, c)
        ans += 1

    # 나머지 지뢰가 아닌 칸 클릭
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and game[i][j] != '*':
                ans += 1

    print("#{} {}".format(tc, ans))








'''      
.......*...*.*...***..**....*.......*..*..*..*...*.**.*.**..
.*....***.**...*.......*..**.*.........**..*.**..*......*.**
........*.*.*...*****.....*..*.*....*.*.*.**.**..*......*..*
**.*.**.****..*...*.....*...*.......**....*..........***.*.*
.......*.**..*.***......*.***..*.***.*.***.....**..*.**.**..
*....*......*..*..**.......**........*..*.*.....*.**.**.*...
*.....*....**.*...*.....***..*.....***.**....*...*......***.
..*...*..*.*.*.******......*..*.*..*..*.*.........*...**.**.
*..*.*..*.*...***..*....*.*..**...*........*.......*.*...*..
*.****..*......*..**.*.****.....*..*.....**...**.*..*..**..*
......**..*.....*...*..*.*....*.*.....*..*..............*..*
.*..**.*..*..******.*****.*...*.*.*..*....*..**.*..*...*....
**..*....*............*......*.***..*.**..**....*...*.......
..*.*.....*...*.*...**....*...**.**.*.*..**...*.......**....
......*..*.*****..**..*...*....*...*.**......***..*...**.*.*
**...*.*....*.......**.*.*.*..***..*.*..........*..*.**.*...
....*...*....*....*.*.....*.*...*.*...***..*...*..*...*..**.
...*.....*.....**.....*...*.............**..*.*.*..*......*.
*..*................*..*.*.*.**.*...*...*..*.*.*....*.**..**
.*..*.*......*.**.*..*....***.......**.**.***...*..*.....*..
..*........*..*.***........***...**.*..**..****..**..*.**.*.
...*...*..*.***....*.*.....**....*.*.*.*.*..........*.....**
*.*........*...**..*.*...*............*..*.....*..*......*..
*........*..**.**..**.**...**..*...*.....*.*..*.........**.*
...*.**....*.*.........*...*....*....*..*.*.....*....**.....
....**...*...*.***..*...**....**.*..*......*.....***....*.**
**.*.*...*.*...**..**...*.**..*.*..*...*.*...*.*.......*....
...**...*..*....*.***..*.**.*......*.*.*.......*.**.*..*.*..
....*.*.*.***....*.***..**....*.....*.....*.***...*..*....*.
*..........*...*.........*.*........**...*..**......*...*..*
*.*.**..*.....****...*.........*.*.*..**..***.*...*.*..*....
.....*.**..*.*....*.**....*.*....**.*.*...**.*....*.*.***.*.
.....*.......**.**.**.****...**.*.....*.*..*..**.*.........*
*.****.*.*.....*...*..*.*..*...*.**.**.****..*.....*....*..*
**....**..*.....*.*...**..**.....*..****.***......***.***...
**.....***..*......*.**....***..*.*..**.**..**.....*.**.**.*
.*..*....*....*..****..*.*..*..*....**......*..*...**..*..**
.*........*.......*..****.*....*......................*.*.**
*.*....*.***...**....**..**.......*..*....***.*..*......**..
...*.....**..**.****.....*...*.*................*.*....***..
*.**..........*.**...**..*.***..*.*..*.....**.....*.*.....**
.*....**...**..**.*..*....*...*...*..*..*.**..*.*....**.....
.***............*..*....**..*****....*.......*.*....***....*
.*..*.*...*..*..*..*.*.*...*.*....*.**......***.*.*...**...*
*.*...**....*..**..*.*..*...*.....**....**...*.......**..*..
*.*.***..*.*..**...*....***....*.*.*..*.**.*.*.*..**.*.***..
.........*.*..*****.**.....*.*.*.*....*..*..*......**.*...*.
*..**.***........*****...*..**..*..*..*..**...**.....*.*..**
*.....*.*...........**.*..*.*.........**..***.**............
...........***..*..***...**..**.*.*..**.*.**..*.*..*....*...
*...**.....*..***...*.**.*.....*.....*......*.........*.*.*.
..**..*.*...*.**.......*****....*.*..*....**....**..*.*...**
..*...*.**.**.....*.*.**.......*...*...*....*.*..**.*.*.*...
*....*.*......*....**.*....*****.**.**....*.......**..*.....
..*.***....*......*..*..*......****....*.*.*..**..*...*....*
.*.*.....*.....*.*.*...*.*....**..**.*....**...*....***.*...
.......****...**.*...*.*.*.......*..**.*...*...*.....*.....*
....*.*..*.*.*...*.*..**..*.....*.***......**..*.*.*.*.*..*.
....*.....*.*..**.....*..*.*..*..*..........*..*...*...*....
**.*****.......***..*......*.*.*..............*.........**..


'''