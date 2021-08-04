# 블록 사이 고이는 빗물의 총량을 구하자!
# 2차원의 가로 세로 W, H가 주어진다.(1 ~ 500)
# 그 뒤에는 0 이상 H 이하인 블록의 높이들이 W개 주어진다. 빈 공간은 없다!

# 특정 위치로부터 시작한 블록이 자신과 높이가 같거나, 더 높은 블록을 만날 때까지 그 사이의 공간에 빗물이 고이게 된다.
# 빗물이 고인 공간을 찾아내면, 그 공간을 누적해 더하고, 블록의 시작점을 갱신해준다. 그 다음 블록부터 다시 비교해나간다.

# 시간 제한은 1초
# 가장 왼쪽부터 끝까지 차례대로 순회한다면, 기본적으로 O(N)이다. 거기다 내부에서 추가 연산이 들어갔을 때, O(N^2)정도까지도 갈 것으로 보인다.
# 하지만 길이의 최댓값이 500이기에 1초 안에 충분히 들어오지 않을까?


# import sys
# H, W = map(int, sys.stdin.readline().split())
# block = list(map(int, sys.stdin.readline().split()))
# ans = 0     # 빗물을 받을 변수
# pool = []
# standard = 0
#
#
# for i in range(W):
#     if i == 0 and block[i]:       # 첫 블록은 그 값이 0이 아닌 이상 비교의 기준이 되는 첫 블록
#         standard = block[i]
#         continue
#
#     if not standard and block[i]: # 현재 블록이 높이를 가지고 있고, 앞선 블록이 0이라 기준 블록이 존재하지 않았을 때
#         standard = block[i]
#         continue
#
#     if standard and standard > block[i] and i < (W - 1):   # 기준 블록이 존재하고, 그 이후의 블록의 높이가 기준 블록보다 낮은 경우
#         pool.append(block[i])       # 물이 고일 수 있는 공간이기에 별도로 저장한다.
#     elif standard and (standard <= block[i] or i == W - 1): # 기준 블록이 존재하고, 그 이후에 만난 블록이 기준 블록의 높이와 같거나 큰 경우
#         if pool:
#             ans += sum([min(standard, block[i]) - j for j in pool if min(standard, block[i]) - j > 0])   # 빗물을 담을 경계인 두 블록 중 낮은 높이의 블록이 기준이 되어야 함
#             pool = []                                                 # 빗물을 담았기에 초기화
#             standard = block[i]
#             continue
#
#         if standard <= block[i]:
#             standard = block[i]
#         # else:
#         #     standard = max(standard, block[i])                            # 기준 블록의 높이 갱신
#
# print(ans)


# 문제의 조건을 다시 생각했다.
# 양쪽에 더 높은 블록이 존재할 때, 그 사이에는 빗물이 고인다.
# 반복문을 돌면서 현재 블록의 왼쪽 값중 최대 높이, 오른쪽 값중 최대 높이를 구해 그 두 값중 작은 값이 현재 위치의 블록보다 크면,
# 작은 값 - 현재 높이를 더해나간다.
# 당연히 어떤 경우에도 첫 블록과 마지막 블록은 물이 안 고인다! 양쪽의 최대 높이(기준)이 되거나, 무시되거나 둘 중 하나이기 때문이다.


import sys

H, W = map(int, sys.stdin.readline().split())
block = list(map(int, sys.stdin.readline().split()))
ans = 0

for i in range(1, W - 1):
    left_side = max(block[:i])
    right_side = max(block[i + 1:])
    standard = min(left_side, right_side)

    if standard > block[i]:
        ans += standard - block[i]

print(ans)