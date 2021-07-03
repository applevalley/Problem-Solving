# 1번부터 N번까지 도시와 M개의 단방향 도로(노드)가 존재하며 모든 거리는 1
# 특정 도시 X부터 출발해 도달 가능한 도시 중 최단 거리가 정확히 K인 모든 도시들의 번호를 출력

# 메모리...초과?
# 인접행렬로 접근한 방식이 잘못된것같다.
# 어떻게 저장하지..?

# import sys
# from collections import deque

# def BFS(x):
#     Q = deque()
#     Q.append(x)

#     while Q:
#         x = Q.popleft()

#         for w in range(1, N + 1):
#             if node[x][w] == 1 and not visit[w]:
#                 Q.append(w)
#                 visit[w] = visit[x] + 1

# N, M, K, X = map(int, input().split())

# node = [[0] * (N + 1) for _ in range(N + 1)]
# visit = [0] * (N + 1)
# check = False

# for i in range(M):
#     start, arrive = map(int, sys.stdin.readline().split())
#     node[start][arrive] = 1

# BFS(X)

# print(visit.index(K))
# print('--')
# for i in range(1, N + 1):
#     if visit[i] == K:
#         print(i)
#         check = True

# if not check:
#     print(-1)


# 거리 계산을 visited로 하지 않고 x_count라는 별도의 인자로 변경했다!
# visited는 방문 처리만 해준다. 통과!

import sys
from collections import deque

def BFS(x):
    Q = deque()
    Q.append([x, 0])
    visit[x] = True

    while Q:
        x, x_count = Q.popleft()
        if x_count == K:
            ans.append(x)
        for w in edge_list[x]:
            if not visit[w]:
                Q.append([w, x_count + 1])
                visit[w] = True

N, M, K, X = map(int, input().split())
edge_list = [[] for _ in range(N + 1)]
visit = [0] * (N + 1)
ans = []

for i in range(M):
    start, arrive = map(int, sys.stdin.readline().split())
    edge_list[start].append(arrive)

BFS(X)

if ans:
    ans.sort()
    for i in ans:
        print(i)
else:
    print(-1)