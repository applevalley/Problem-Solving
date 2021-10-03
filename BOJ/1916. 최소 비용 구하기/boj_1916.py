'''
A에서 B로 가는 최소 비용은?
기본 다익스트라로 해결 가능할 것 같다.
'''

import heapq

def dijkstra(start):
    Q = []
    heapq.heappush(Q, (0, start))
    distance[start] = 0

    while Q:
        dist, now = heapq.heappop(Q)
        if distance[now] < dist: continue

        for i in G[now]:
            cost = dist + i[1]
            if  cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(Q, (cost, i[0]))

N = int(input())
M = int(input())
G = [[] for _ in range(N + 1)]
distance = [0xffffff] * (N + 1)

for i in range(M):
    a, b, c = map(int, input().split())
    G[a].append([b, c])

start, target = map(int, input().split())

dijkstra(start)
print(distance[target])


# N = 3 M = 6
# 1 2 3
# 1 3 4
# 2 3 2
#
#
#