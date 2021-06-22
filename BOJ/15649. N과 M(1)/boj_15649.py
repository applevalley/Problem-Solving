# 자연수 N과 M이 주어졌을 때, 1부터 N까지의 자연수 중 중복 없이 M개를 고른 수열을 구하자!

# 중복 없이 골라야 한다. [1, 2]와 [2, 1]은 별개이다.
# 백트래킹에 대한 이해가 조금 더 필요하다!

N, M = map(int, input().split())
numbers = [i for i in range(1, N + 1)]
ans = [0] * N

# 라이브러리를 쓰면 편하지
# from itertools import permutations
#
# ans = list(permutations(numbers, M))
#
# for i in ans:
#     for j in i:
#         print(j, end=' ')
#     print()
# #

# 재귀를 이용해 직접 구해보자
def ans(numbers):
    n = len(numbers)
    pick = []

    def recursion():
        if len(pick) == M:
            for j in pick:
                print(j, end=' ')
            print()
            return

        for i in range(1, n + 1):
            if i not in pick:
                pick.append(i)
                recursion()
                pick.pop()

    recursion()

ans(numbers)
