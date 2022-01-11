def sum_divide(k, n):
    if dp[k][n]:
        return dp[k][n]

    dp[k][n] = sum_divide(k - 1, n) + sum_divide(k, n - 1)

    return dp[k][n]


N, K = map(int, input().split())
dp = [[1] * (N + 1)] + [[0] * (N + 1) for _ in range(K - 1)]

for i in range(1, K):
    dp[i][0] = 1

# print(dp)
print(sum_divide(K - 1, N) % 1000000000)
# print(dp)