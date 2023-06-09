import sys


def move(x, y):

    for i in range(N):
        for j in range(N):
            if i == N - 1 and j == N - 1:
                break

            distance = arr[i][j]
            if 0 <= distance + j < N:
                dp[i][distance + j] += dp[i][j]
            if 0 <= i + distance < N:
                dp[i + distance][j] += dp[i][j]


input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

move(0, 0)
print(dp[N - 1][N - 1])