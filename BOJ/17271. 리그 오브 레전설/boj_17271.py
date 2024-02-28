
import sys
sys.setrecursionlimit(100000)

def calc(N):
    if dp[N]:
        return dp[N]
    else:
        dp[N] = (calc(N - 1) + calc(N - M)) % 1000000007
    return dp[N]

N, M = map(int, input().split())
if N < M:
    print(1)
elif N == M:
    print(2)
else:
    dp = ([1] * M) + ([0] * (N - M + 1))
    calc(N)
    print(dp[N])