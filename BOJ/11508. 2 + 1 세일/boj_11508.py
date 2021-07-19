# 3개를 한 번에 산다면 가장 싼 하나는 무료이다. 그 외는 정가를 지불한다.
# N개를 살 때 필요한 최소비용은?

# 배열에서 임의의 값 3개를 묶을 때, 작은 값보다는 최대한 큰 값에 가까운 값 하나를 배제할 수 있게 구성해야 한다.
# 그래야 작은 값을 배제한 경우와 비교했을 떄 전체의 합이 더 작게 나오게 된다.
# 따라서 큰 순서로 정렬을 한 뒤, 3개씩 묶어가며 그 중에서 가장 작은 값을 계산에서 제외해야 한다.

import sys
N = int(sys.stdin.readline())
thing = [int(sys.stdin.readline()) for _ in range(N)]
cnt = 0
two_plus_one = []

thing.sort(reverse=True)

for i in thing:
    if len(two_plus_one) != 3:
        two_plus_one.append(i)
        if len(two_plus_one) == 3:
            cnt += (sum(two_plus_one) - min(two_plus_one))
            two_plus_one = []

if two_plus_one:
    cnt += sum(two_plus_one)

print(cnt)