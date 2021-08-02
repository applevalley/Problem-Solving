# 1번 문제와 동일하다. 다만 모든 수열은 오름차순이어야 한다는 조건이 들어갔다.

def go():
    if len(A) == M:
        for j in range(len(A) - 1):
            if A[j] >= A[j + 1]:
                break
        else:
            print(' '.join(map(str, A)))

    for i in range(1, N + 1):
        if i not in A:
            A.append(i)
            go()
            A.pop()

import sys

N, M = map(int, sys.stdin.readline().split())
A = []

go()