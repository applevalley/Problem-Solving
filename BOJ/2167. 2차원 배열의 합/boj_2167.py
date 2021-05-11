# 시간이 너무 오래 걸린다 ㅠㅠㅠ
# 값을 저장해놓거나, 배열에 대한 접근을 다르게 해야 할 필요가 있어보인다. 

import sys

def calc(a, b, c, d):
    global memo
    cnt = 0
    for i in range((a - 1), c):
        for j in range((b - 1), d):
            cnt += arr[i][j]
    memo[(a, b, c, d)] = cnt
    print(cnt)


N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
K = int(input())
memo = {}

for i in range(K):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    if (x1, y1, x2, y2) in memo:
        print(memo[(x1, y1, x2, y2)])
    else:
        calc(x1, y1, x2, y2)