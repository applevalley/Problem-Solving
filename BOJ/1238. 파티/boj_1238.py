'''
N개의 숫자로 구성된 마을에 한 명씩 산다.
유향 그래프가 주어진다. 올 때와 다시 돌아올 때의 경로는 다를 수 있다.
모든 사람들이 각자의 지점에서 목표 지점까지 왕복할 때 가장 오래 걸린 시간은?

목표지점에 사는 사람을 제외한 모든 사람들의 경우에 대해 다익스트라를 왕복으로 사용할 수 있을까?
최악의 경우 999명에 대해 각각 2번의 다익스트라를 돌려야 한다. 시간 초과 없이 가능할까?

'''

import heapq

def dijkstra_go(start):
    Q = []
    heapq.heappush(Q, (0, start))
    distance[start] = 0

    while Q:
        dist, now = heapq.heappop(Q)
        if distance[now] < dist: continue

        for i in G[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(Q, (cost, i[0]))


def dijkstra_back(start):
    Q = []
    heapq.heappush(Q, (0, start))
    distance[start] = 0

    while Q:
        dist, now = heapq.heappop(Q)
        if distance[now] < dist: continue

        for i in G[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(Q, (cost, i[0]))

N, M, X = map(int, input().split())
G = [[] for _ in range(N + 1)]
temp = 0
maxV = 0

for i in range(M):
    a, b, c = map(int, input().split())
    G[a].append([b, c])


for i in range(1, N + 1):
    distance = [0xffffff] * (N + 1)

    if i == X: continue

    dijkstra_go(i)
    temp = distance[X]

    distance = [0xffffff] * (N + 1)
    dijkstra_back(X)
    temp += distance[i]

    if temp > maxV:
        maxV = temp

print(maxV)
