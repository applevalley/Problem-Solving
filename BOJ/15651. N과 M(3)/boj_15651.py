# 이번엔 중복을 허용한다!

def go():
    if len(A) == M:
        print(' '.join(map(str, A)))
        return

    for i in range(1, N + 1):
        A.append(i)
        go()
        A.pop()

import sys

N, M = map(int, sys.stdin.readline().split())
A = []

go()