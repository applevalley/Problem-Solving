# n개의 요소가 담긴 수열 a에서 두 요소를 더했을 때 그 값이 자연수 x가 되는 쌍의 합은 몇 개일까?
# 요소의 숫자 n의 개수는 1 <= n <= 100000 이지만 수열 a의 두 요소 ai, aj에서 i < j의 관계가 있기 때문에
# 요소 n은 최소 2부터 시작한다고 생각해볼 수 있다.

# 최대 입력 가능한 n이 100000이고, 시간 제한은 1초이기에 단순한 O(n^2)의 복잡도는 당연히 시간초과가 날 것이다.
# 정렬을 하지 않고 부분집합으로 구하려고 했지만 시간초과가 났다.
# 투 포인터로 해결할 수 있는 문제라는 것을 알게 되었고, 해당 이론을 찾아본 뒤 코드를 완성하였다.

import sys

N = int(input())
arr = list(map(int, sys.stdin.readline().split()))
x = int(input())
arr.sort()                   # 투 포인터를 사용하려면 정렬이 필수!
start, end = 0, N - 1
res = 0

while start < end:
    temp = arr[start] + arr[end]
    if temp == x: res += 1
    if temp < x:             # temp가 x보다 작다면 temp의 값을 키워야 한다.
        start += 1           # start의 인덱스를 올려 temp가 더 큰 값을 가지게 한다.
        continue
    end -= 1                 # 위의 조건에 해당되지 않았다면 temp가 x보다 큰 것이다. end를 감소시켜 temp를 줄인다.

print(res)

# import sys
#
# N = int(input())
# arr = list(map(int, sys.stdin.readline().split()))
# x = int(input())
# cnt = 0
#
# arr.sort()
# print(arr)
#
# for i in range(N - 1):
#     start = arr[i]
#     if start > x: continue
#
#     for j in range(i + 1, N):
#         end = arr[j]
#         if start + end == x:
#             cnt += 1
#
# print(cnt)
# 정렬을 해주지 않고 수열 자체의 부분집합들을 구해 각각의 부분집합들의 요소들을 전부 더해 비교해볼수는 없을까?
# 아쉽게도 재귀의 깊이가 너무 깊어졌다. 부분집합으로는 어려울 것 같다.

# import sys
# sys.setrecursionlimit(100000)
#
# N = int(input())
# arr = list(map(int, sys.stdin.readline().split()))
# x = int(input())
#
# length = len(arr)
# A = [0] * length
# ans = 0
#
# def powerset(n, k):
#     global ans
#     if n == k:                         # 모든 선택이 끝난 상황
#         cnt = 0
#         if A.count(1) == 2:            # 리스트 A에 1이 2번 들어있다면, 해당 부분집합은 2개의 요소로 구성되어 있을 것이다.
#             for i in range(n):
#                 if A[i] == 1:
#                     cnt += arr[i]
#
#             if cnt == x:               # 이 두 요소의 합이 자연수 x과 같다면, 숫자를 하나 올려준다
#                 ans += 1
#     else:
#         A[k] = 1                       # 매 시도마다 각 요소를 선택하거나, 하지 않으며 부분집합을 만들어나간다.
#         powerset(n, k+1)
#         A[k] = 0
#         powerset(n, k+1)
#
# powerset(length, 0)
# print(ans)