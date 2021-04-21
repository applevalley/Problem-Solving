def DFS(x):
    visited[x] = 1
    for y in range(len(G[x])):
        if G[x][y] and not visited[y]:
            print(y, end=' ')
            DFS(y)

def BFS(x):
    Q = [x]
    visited = [0] * (N + 1)
    visited[x] = 1
    while Q:
        x = Q.pop(0)
        for y in range(len(G[x])):
            if G[x][y] and not visited[y]:
                print(y, end=' ')
                visited[y] = 1
                Q.append(y)

N, M, V = map(int, input().split())
G = [[0] * (N + 1) for _ in range(N + 1)]
node = []
visited = [0] * (N + 1)

for i in range(M):
    first, second = map(int, input().split())
    node.extend([first, second])

for i in range(M):
    first, second = node[2 * i], node[2 * i + 1]
    G[first][second] = 1
    G[second][first] = 1

print(V, end=' ')
DFS(V)
print()
print(V, end=' ')
BFS(V)