'''
M x N 사이즈의 배열이 있다.
인접한 4방향에 대해 항상 좌표 값이 더 낮은 지점으로만 이동해 (0,0)부터 (M - 1, N - 1)까지 도달할 수 있는 경우의 수는?

재귀를 활용한 DFS로 구할 수 있지 않을까?
데이터의 최대 크기는 500 x 500이기에 (M x N) * 4 면 연산 횟수가 최대 100만일 거라고 생각했지만 계산이 잘못되었다.
한 번 재귀가 이뤄질 때마다 4방향의 탐색이 발생한다. 총 횟수는 4의 25만 제곱이 된다. 엄청 많다!

각 칸의 값은 10000 이하의 자연수다. 따라서 dp의 값을 0으로 초기화하면 좌표 값이 0인 곳을 방문했을 때 문제가 생길 수 있다.
따라서 초기 값은 문제 조건에 맞지 않는 음수 값으로 준다!

(x,y)가 (M - 1, N - 1)인 경우 카운터를 증가시킨다.
'''

import sys
sys.setrecursionlimit(5000)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def DFS(x, y):
    if x == M - 1 and y == N - 1:
        return 1

    if dp[x][y] != -1:
        return dp[x][y]
    dp[x][y] = 0

    for i in range(4):
        tx, ty = x + dx[i], y + dy[i]
        if 0 <= tx < M and 0 <= ty < N and arr[x][y] > arr[tx][ty]:
            dp[x][y] += DFS(tx, ty)    # 경로의 개수

    return dp[x][y]


M, N = map(int, input().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)]

print(DFS(0, 0))
