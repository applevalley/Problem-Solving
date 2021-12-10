import sys
sys.setrecursionlimit(1000000)

def facto(x):
    if dp[x]:
        return dp[x]

    dp[x] = x * facto(x - 1)

    return dp[x]


dp = [0] * 1000001
dp[0], dp[1] = 0, 1
time_limit = 10 ** 8

for test_case in range(int(input())):
    S, N, T, L = map(str, input().split())

    if S == "O(N)":
        temp = int(N) * int(T)
    elif S == "O(N^2)":
        temp = (int(N) ** 2) * int(T)
    elif S == "O(N^3)":
        temp = (int(N) ** 3) * int(T)
    elif S == "O(2^N)":
        temp = (2 ** int(N)) * int(T)
    elif S == "O(N!)":
        if int(N) > 20:
            print("TLE!")
            continue
        temp = (facto(int(N))) * int(T)

    print("May Pass.") if temp <= int(L) * time_limit else print("TLE!")