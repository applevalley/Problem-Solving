import sys; sys.stdin = open('11724.txt')
# sys.setrecursionlimit(10000) 제출할 때에는 한도를 늘려주어야 했다.

# 무향 그래프가 주어졌을 때 연결 요소의 개수를 구하기
# 자꾸 시간 초과가 나서 pypy3로 제출해 통과했는데, input을 sys.stdin.readline()으로 바꾸니 파이썬으로도 통과되었다.
# pypy3으로도 돌려본 결과 시간은 절반 가량 빨랐지만 메모리 사용량이 2배 가량 더 많았다.

# dfs

def dfs(x):
    visit[x] = 1
    for w in G[x]:  # 정점의 간선을 전부 
        if not visit[w]:
            dfs(w)

# bfs

def bfs(x):
    Q = [x]
    visit[x] = 1
    while Q:
        x = Q.pop(0)
        for w in G[x]:
            if not visit[w]:
                visit[w] = 1
                Q.append(w)

N, M = map(int, sys.stdin.readline().split()) # 정점, 간선의 수
lines = [] # 간선들을 저장할 배열
visit = [0] * (N + 1) # 방문표시
cnt = 0  # 연결 요소의 개수를 세기 위한 변수

if N == 1:   # 만약 정점이 1개라면, 간선이 존재할 수 없다. 0을 출력하고 종료한다.
    print(0)
else:
    for i in range(M):
        a, b = map(int, sys.stdin.readline().split())
        lines.append([a, b])   # 간선들을 배열에 저장한다.

    G = [[] * (N + 1) for _ in range(N + 1)]   # 인접리스트

    for i in range(M):
        u, v = lines[i][0], lines[i][1]
        G[v].append(u)
        G[u].append(v)  # 무향 그래프이기 때문에 u->v / v->u 추가

    for i in range(1, N + 1):
        if not visit[i]:  # 방문하지 않은 정점이라면 탐색한다
            bfs(i)
            cnt += 1

    print(cnt)