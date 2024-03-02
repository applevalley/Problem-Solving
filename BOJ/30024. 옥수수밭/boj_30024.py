import sys
import heapq

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
input = sys.stdin.readline

N, M = map(int, input().split())
corn_map = [[0] * (M + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
corn_value_list = []
visited = [[False] * (M + 1) for _ in range(N + 1)]
K = int(input())

for i in range(1, N + 1):
    for j in range(1, M + 1):
        if i == 1 or i == N or j == 1 or j == M:
            heapq.heappush(corn_value_list, (-corn_map[i][j], [i, j, corn_map[i][j]]))
            visited[i][j] = True


if K == 1:
    only_one = heapq.heappop(corn_value_list)
    print(only_one[1][0], only_one[1][1])
else:
    while K:
        various_one = heapq.heappop(corn_value_list)
        visited[various_one[1][0]][various_one[1][1]] = True
        print(various_one[1][0], various_one[1][1])
        K -= 1

        if K and len(corn_value_list):
            for _ in range(4):
                tx, ty = various_one[1][0] + dx[_], various_one[1][1] + dy[_]
                if 1 <= tx <= N and 1 <= ty <= M and not visited[tx][ty]:
                    heapq.heappush(corn_value_list, (-corn_map[tx][ty], [tx, ty, corn_map[tx][ty]]))
                    visited[tx][ty] = True