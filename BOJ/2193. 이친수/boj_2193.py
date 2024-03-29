


def calc(x):
    if dp[x]:
        return dp[x]

    dp[x] = calc(x - 1) + calc(x - 2)

    return dp[x]


N = int(input())
dp = [0] * 90
dp[0], dp[1] = 1, 1

if N < 2:
    print(1)
else:
    print(calc(N - 1))