# N개의 문자열로 이루어진 집합 S
# M개의 문자열 중 집합 S에 포함된 것은 몇 개일까?

# N, M은 최대 10,000까지 올 수 있다.
# M개의 각 문자열들에 대해 N에 포함되는지를 검사한다면 O(M)의 복잡도를 가지지 않을까?
# 리스트가 아닌 집합의 containment 메서드는 O(1)의 복잡도를 가지기 때문이다.

import sys

N, M = map(int, sys.stdin.readline().split())
standard = set(sys.stdin.readline().rstrip() for _ in range(N))
target = [sys.stdin.readline().rstrip() for _ in range(M)]
cnt = 0

for i in target:
    if i in standard:
        cnt += 1

print(cnt)
