# N명을 키 순서대로 정렬한 뒤 K개로 나누어야 한다.
# 한 그룹에는 반드시 사람이 있어야 하고, 같은 그룹에 속한다면 서로 인접해야 한다.
# 비용은 그룹 내에서 가장 큰 사람과 작은 사람간의 차이다. 총 비용의 최솟값은?

# 1 3 5 6 10 이렇게 5명이 3그룹을 만들어야 한다면
# 1 3 / 5 6 / 10 이렇게 만들 수 있다.
# 그룹에 속하려면 인접해야 하기에, n과 n + 1번 인원의 큰 값-작은 값의 차를 리스트에 저장하고,
# 이를 오름차순 정렬해 K - 1개까지 꺼내면 최솟값이 된다.

# 인원은 이미 정렬된 상태로 주어진다.

import sys
N, K = map(int, sys.stdin.readline().split())
children = list(map(int, sys.stdin.readline().split()))
sub = []
cnt = 0

for i in range(1, N):
    sub.append(children[i] - children[i - 1])

sub.sort()

for i in range(N - K):
    cnt += sub[i]

print(cnt)