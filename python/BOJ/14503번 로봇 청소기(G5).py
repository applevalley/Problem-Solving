import sys; sys.stdin = open('14503.txt')
# sys.setrecursionlimit(10000)

# 우선 현재 위치 청소 변수 += 1
# 현재 방향 기준 왼쪽부터 차례대로 탐색
# 북일 때 서쪽으로,
# 왼쪽에 청소 안한 공간이 있으면 그 방향으로 회전하고 한칸 전진
# 왼쪽에 청소할 공간이 없으면 그 방향으로 회전하고 처음으로 돌아감
# 네 방향 모두 청소되어있거나 벽이면 방향 유지하고 한칸 후진 처음으로 돌아감
# 네 방향 모두 청소되었고 벽인데 뒤쪽도 벽이라 후진 못하면 동작 종료
# 청소된 칸은 안 간다.(방문표시) 벽은 통과못한다. 테두리는 전부 벽이다.


# 0 1 2 3 / 북동남서
# 3 2 1 0
dx = [-1, 0, 1, 0] # 북동남서
dy = [0, 1, 0, -1]

def dfs(x, y, k):
    global cnt, temp, chk
    temp = 0
    # if chk: return

    if visit[x][y] == 0:
        visit[x][y] = 1
        cnt += 1

    for i in range(4):

        new_k = (k + 3 - i) % 4 # 왼쪽 회전 방향

        tx, ty = x + dx[new_k], y + dy[new_k] # 왼쪽 방향에 청소를 안 한 공간이 있는지 확인
        if 0 <= tx < N and 0 <= ty < M and arr[tx][ty] == 0 and not visit[tx][ty]:
            # cnt += 1
            print(tx, ty, cnt + 1)
            if chk: return
            dfs(tx, ty, new_k)
        else: # 왼쪽에 청소할 공간이 없다면

            temp += 1
    if temp == 4:  # 네 방향 전부 갈 수 없는 경우
        new_direct = (k - 2) % 4
        tx, ty = x + dx[new_direct], y + dy[new_direct]
        if 0 <= tx < N and 0 <= ty < M:
            temp = 0
            if arr[tx][ty] == 1 and visit[tx][ty] == 0: # 뒷 칸마저 벽이라면
                chk += 1
                return cnt # 종료
            else:
                print('--back--')
                print(tx, ty, cnt)
                print('----')
                dfs(tx, ty, k)


N, M = map(int, input().split())
r, c, d = map(int, input().split())
cnt = temp = 0
chk = 0


arr = [list(map(int, input().split())) for _ in range(N)]
visit = [[0] * M for _ in range(N)]
move_list = [0, 1, 2, 3]

dfs(r, c, d)
print(cnt)

for i in visit:
    print(*i)