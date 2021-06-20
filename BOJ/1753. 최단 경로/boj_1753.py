# 방향 그래프가 주어졌을 때, 시작점에서 다른 모든 정점으로의 최단 경로는?

# 가중치가 음의 정수가 아니다! 다익스트라를 사용해볼 수 있다.

import heapq
import sys

def dijkstra(start):
    Q = []
    heapq.heappush(Q, (0, start))
    dist[start] = 0

    while Q:
        shortest, node = heapq.heappop(Q)

        if dist[node] < shortest: continue

        for i in arr[node]:
            cost = shortest + i[1]
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(Q, (cost, i[0]))

V, E = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline().rstrip())
arr = [[] for i in range(V + 1)]
dist = [0xffffff] * (V + 1)

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    arr[u].append([v, w])

dijkstra(start)

for i in range(1, V + 1):
    if dist[i] == 0xffffff:
        print('INF')
    else:
        print(dist[i])