import sys
sys.stdin = open('cont.txt')

# for test_case in range(1,11):
#
#     def BFS(v):
#         Q = []
#         Q.append(v)
#         visit[v] = 1
#         # print(v, end=" ")
#         while Q:
#             v = Q.pop(0)
#             for w in G[v]:
#                 if not visit[w]:
#                     Q.append(w)
#                     visit[w] = visit[v] + 1
#                     # print(w, end=" ")
#         # print(visit)
#
#
#     V, E = map(int, input().split())
#     data = list(map(int, input().split()))
#
#     # print(length, start)
#     # print(data)
#
#     G = [[] for _ in range(V+1)]
#     visit = [0] * (V+1)
#
#     for i in range(V//2):
#         s, e = data[2*i], data[2*i+1]
#         G[s].append(e)
#         # G[e].append(s)
#
#     BFS(E)
#     # print(G)
#     # print(visit)
#
#     max = 0
#     for i in range(len(visit)):
#         if visit[i] >= max:
#             max = visit[i]
#             max_idx = i
#
#     print(visit)
#     print("#{} {}".format(test_case, max_idx))


# 라이브 강의 코드

for tc in range(1,11):
    N, s = map(int, input().split())
    arr = list(map(int, input().split()))
    G = [[0] * 101 for _ in range(101)]  # 정점번호 1 ~ 100
    for i in range(0, N, 2):          # arr[i] ---> arr[i+1]
        G[arr[i]][arr[i+1]] = 1

    visit = [0] * 101
    Q = [s]
    visit[s] = 1

    while Q:
        v = Q.pop(0)
        for w in range(1, 101):
            if G[v][w] and not visit[w]:
                visit[w] = visit[v] + 1
                Q.append(w)

    ans = 1
    for i in range(2, 101):
        if visit[ans] <= visit[i]:
            ans = i
    print(ans)