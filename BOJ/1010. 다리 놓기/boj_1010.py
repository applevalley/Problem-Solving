'''
강을 기점으로 N개의 포인트과 M개의 포인트가 있음 (N <= M)
한 사이트에는 하나의 다리만 연결된다
N개 사이트 개수만큼 다리를 지으려 한다(..!)
경우의 수는?

설명이 복잡하지만, 다시 돌려 보면 M개 중에서 N개를 선택하는 조합을 구하면 될듯
'''


import sys

input = sys.stdin.readline
test_case = int(input())

for _ in range(test_case):
    N, M = map(int, input().split())
    dp = [[0 for _ in range(30)] for _ in range(30)]
    bridge_list = [i for i in range(1, M + 1)]

    for i in range(30):
        dp[i][i] = 1
        dp[i][0] = 1

    for i in range(2, 30):
        for j in range(1, 30):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

    print(dp[M][N])
