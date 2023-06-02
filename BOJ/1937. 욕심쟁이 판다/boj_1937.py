import sys
sys.setrecursionlimit(100000)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def check_route(x, y):
    if dp[x][y]:
        return dp[x][y]
    else:
        dp[x][y] = 1

    for _ in range(4):
        tx, ty = x + dx[_], y + dy[_]

        if 0 <= tx < N and 0 <= ty < N and forest[tx][ty] > forest[x][y]:
            dp[x][y] = max(dp[x][y], check_route(tx, ty) + 1)
            
    return dp[x][y]


input = sys.stdin.readline
N = int(input())
forest = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
ans = 0

for i in range(N):
    for j in range(N):
        ans = max(ans, check_route(i, j))

print(ans)