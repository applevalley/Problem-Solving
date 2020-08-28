# 1인 공간이 정확히 K와 맞아떨어져야 한다
# 가로, 세로의 경우를 구하고, K = 3 / 11101인 경우 0을 발견했을 때 앞에서의 111을 인식해야 한다.
# 연속되어야 하기에, K = 3 / 01011같은 경우는 답이 될 수 없다.

import sys
sys.stdin = open('where.txt')

T = int(input())

for test_case in range(1,T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # print(arr)

    ans = 0
    for i in range(N): # 01234
        cnt = 0
        for j in range(N): # 01234
            if j < N-1:
                if arr[i][j] == 1:
                    cnt += 1
                    if cnt != K and arr[i][j+1] == 0:
                        cnt = 0
                    elif cnt == K and arr[i][j+1] == 0:
                        ans += 1
                        cnt = 0
            elif j == N-1:
                if arr[i][j] == 1:
                    cnt += 1

        if cnt == K:
            ans += 1

    for i in range(N): # 01234
        cnt = 0
        for j in range(N): # 01234
            if j < N-1: # 4
                if arr[j][i] == 1:
                    cnt += 1
                    if cnt != K and arr[j+1][i] == 0:
                        cnt = 0
                    elif cnt == K and arr[j+1][i] == 0:
                        ans += 1
                        cnt = 0
            elif j == N-1:
                if arr[j][i] == 1:
                    cnt += 1

        if cnt == K:
            ans += 1

    print("#{} {}".format(test_case, ans))



    # for i in range(len(arr)): # 01234
    #     cnt = 0
    #     for j in range(len(arr[i])): # 01234
    #         if j < len(arr[i])-1:
    #             if arr[j][i] == 1:
    #                 cnt += 1
    # for i in range(len(arr)):
    #     cnt = 0
    #     for j in range(len(arr)):
    #         if arr[j][i] == 1:
    #             cnt += 1
    #         if cnt == K and j == 0:
    #             ans += 1
    #     if cnt == K:
    #         ans += 1

