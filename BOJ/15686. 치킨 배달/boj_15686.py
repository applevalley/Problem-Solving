'''
N x N 크기의 배열에 치킨집(2)와 가정집(1)이 있다.
치킨 거리는 집과 가장 가까운 치킨집까지의 거리이고, 거리 계산은 |x1 - x2| + |y1 - y2|다.
모든 집의 치킨 거리의 합은 도시의 치킨 거리이다.
일부 치킨집을 폐업시킨다고 했을 때, 도시의 치킨 거리의 합의 최솟값은 얼마인가?

집은 2N개를 넘지 않고, 반드시 하나는 있다.
치킨집은 M 이하이고 최대 13개이다.

M개만 남기고 폐업시켜야 하는데, 폐업의 기준이 뭘까?
치킨집이 하나만 있다면, 단순히 각 가정집과의 거리만 더해주면 된다. 그런데 치킨집이 두 개 이상이면?

전체 치킨집들에서 폐업을 통해 남겨진 치킨집의 수만큼에 대해사 조합을 통해 치킨집들의 묶음을 만든다.
그 각 묶음에 대해, 한 치킨집에 대한 모든 가정집들의 거리를 계산해 한 가정집에 대한 치킨 거리를 만들어 도시의 치킨 거리를 만든다.
도시의 치킨 거리가 가장 작은 치킨집 묶음을 선택하자!
'''


# 재귀를 시도했다 처참히 실패한 흔적
# 이게 더 이상적인데.. 조건 설정을 다시 고민해보자.

# def comb(n, k):
#     if len(chicken) == k:
#         cnt = []
#         for x, y in chicken:
#             cnt.append([(abs(x - a) + abs(y - b)) for a, b in house])
#
#         temp = []
#         for i in range(len(house)):
#             standard = cnt[0][i]
#             for j in range(1, len(cnt)):
#                 if cnt[j][i] < standard:
#                     standard = cnt[j][i]
#             temp.append(standard)
#
#         chicken_distance.append(sum(temp))
#         return
#
#     if n == k:
#         cnt = []
#         shop = [i for i in range(len(chicken)) if selected[i] == 1]
#         if len(shop) == M:
#             print('uau')
#             distance_list = ([chicken[i] for i in range(len(chicken)) if i in shop])
#             for x, y in distance_list:
#                 cnt.append([(abs(x - a) + abs(y - b)) for a, b in house])
#
#             temp = []
#             for i in range(len(house)):
#                 standard = cnt[0][i]
#                 for j in range(1, len(cnt)):
#                     if cnt[j][i] < standard:
#                         standard = cnt[j][i]
#                 temp.append(standard)
#
#             chicken_distance.append(sum(temp))
#             return
#         else:
#             return
#
#     else:
#         for i in range(len(chicken)):
#             selected[i] = 1
#             comb(n + 1, k)
#             selected[i] = 0


# 일단 통과는 시켰다..

from itertools import combinations

N, M = map(int, input().split())
arr = [list(map(int, (input().split()))) for _ in range(N)]

house = [(i, j) for i in range(N) for j in range(N) if arr[i][j] == 1]
chicken = [(i, j) for i in range(N) for j in range(N) if arr[i][j] == 2]
chicken_comb = list(combinations(chicken, M))
chicken_distance = []

for i in chicken_comb:
    cnt = []
    for x, y in i:
        cnt.append([(abs(x - a) + abs(y - b)) for a, b in house])

    temp = []
    for j in range(len(house)):
        standard = cnt[0][j]
        for k in range(1, len(cnt)):
            if cnt[k][j] < standard:
                standard = cnt[k][j]
        temp.append(standard)

    chicken_distance.append(sum(temp))

print(min(chicken_distance))

