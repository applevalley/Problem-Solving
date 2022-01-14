def ascend(x):

    # 반복문으로 구성하는 경우

    # if x < 3:
    #     return dp[x]
    #
    # for i in range(3, N + 1):
    #     dp[i] = max(dp[i - 3] + stairs[i - 2] + stairs[i - 1], dp[i - 2] + stairs[i - 1])

    # 재귀로 하는 경우
    # x가 0나 2가 되는 경우 다음 호출에서 음수값이 전달 인자로 전해지고 인덱스 에러를 유발하기에 추가 조건이 필요

    if x < 1:
        return 0

    if dp[x]:
        return dp[x]

    dp[x] = max(ascend(x - 3) + stairs[x - 2] + stairs[x - 1], ascend(x - 2) + stairs[x - 1])

    return dp[x]


N = int(input())
stairs = [int(input()) for _ in range(N)]
dp = [0] * (N + 1)
dp[1] = stairs[0]

if N > 1:
    dp[2] = max(stairs[0] + stairs[1], stairs[1])

print(ascend(N))
