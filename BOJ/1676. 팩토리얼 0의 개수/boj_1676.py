def facto(x):
    if dp[x]:
        return dp[x]
    else:
        dp[x] = x * facto(x - 1)

    return dp[x]


N = int(input())
dp = [0] * (N + 1)
dp[0] = 1
result = str(facto(N))
cnt = 0

for i in range(len(result) - 1, -1, -1):
    if result[i] == '0':
        cnt += 1
    else:
        break

print(cnt)