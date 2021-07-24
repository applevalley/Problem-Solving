# PT 한 번에 기구를 최대 2개까지 쓸 수가 있다. PT를 할 때마다 이전에 사용하지 않은 기구를 쓰려고 한다.
# 다만 기구를 한 번 사용할 때마다 일정 수치만큼의 근손실이 일어난다고 한다.(???)
# PT를 한 번 받을 때, 근손실의 최솟값은 얼마일까? 기구를 2개 사용했을 때의 근손실은 각 기구의 근손실의 합이다.

# 정렬을 해준 뒤 배열을 순회하며 가장 작은 값과 가장 큰 값의 합들을 비교해가며 합을 구했다.
# 사실 문제를 완전히 이해하지 못해서 다시 풀어봐야 할 문제이다.
# PT를 한 번 받을 때의 근손실이 M을 넘지 않도록 한다는데, M에 대한 추가적인 정보가 없다. 단순히 M의 최솟값을 구해야 한다.
# 그렇다면 기구가 홀수라면 내림차순으로 정렬해 앞에서부터 두 기구를 사용한다면 마지막 남은 기구는 근손실 수치가 가장 작은 값이고,
# 가장 작은 기구 하나의 근손실 수치 M이 한 번의 PT로 일어나는 근손실 수치 M의 최솟값이 되어야 한다.
# 근손실 수치 M에 대해 정확한 이해가 필요하다..

import sys
N = int(sys.stdin.readline().rstrip())
health = list(map(int, sys.stdin.readline().split()))
health.sort()

if len(health) % 2:
    max_value = health[-1]
    health = health[:-1]
    odd_sum = [sum([health[i], (health[-i - 1])]) for i in range(0, N // 2)]
    if max(odd_sum) > max_value:
        print(max(odd_sum))
    else:
        print(max_value)

else:
    even_sum = [sum([health[i], (health[-i - 1])]) for i in range(0, N // 2)]
    print(max(even_sum))
