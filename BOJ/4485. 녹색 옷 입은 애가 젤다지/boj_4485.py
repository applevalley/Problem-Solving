'''
최단 경로를 구하자! 다익스트라를 사용한다.
최단 경로라는 걸 생각하지 못했을 때는 DFS를 이용했지만, 당연하게도 시간초과가 났다.
기존 인접 리스트 형태에서 사용했던 다익스트라 알고리즘을 인접 행렬로 변형했다.
'''

import heapq

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dijkstra(N, arr, distance):
    q = []
    heapq.heappush(q, (0, 0, 0))
    distance[0][0] = 0

    while q:
        dist, x, y = heapq.heappop(q)
        if distance[x][y] < dist: continue

        for i in range(4):
            tx, ty = x + dx[i], y + dy[i]
            if 0 <= tx < N and 0 <= ty < N:
                cost = dist + arr[tx][ty]
                if distance[tx][ty] > cost:
                    distance[tx][ty] = cost
                    heapq.heappush(q, (cost, tx, ty))

    return distance[N - 1][N - 1] + arr[0][0]

cnt = 0

while True:
    cnt += 1
    N = int(input())
    if N == 0: break

    arr = [list(map(int, input().split())) for _ in range(N)]
    distance = [[0xffffffff] * (N) for _ in range(N)]

    print(f'Problem {cnt}: {dijkstra(N, arr, distance)}')
