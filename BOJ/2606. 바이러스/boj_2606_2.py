# dfs, bfs 2가지 풀이

import sys
from collections import deque


def bfs(x):
    Q = deque()
    Q.append(x)
    visited[x] = 1
    count = 0
    while Q:
        x = Q.popleft()
        for w in arr[x]:
            if not visited[w]:
                Q.append(w)
                visited[w] = 1
                count += 1
    return count


def dfs(x, k):
    global ans
    visited[x] = 1

    for w in arr[x]:
        if not visited[w]:
            ans += 1
            dfs(w, k + 1)


input = sys.stdin.readline
N = int(input())
visited = [0] * (N + 1)
arr = [[] for _ in range(N + 1)]
M = int(input())
for _ in range(M):
    start, end = map(int, input().split())
    arr[start].append(end)
    arr[end].append(start)

print(bfs(1))

ans = 0
visited = [0] * (N + 1)
dfs(1, 0)
print(ans)