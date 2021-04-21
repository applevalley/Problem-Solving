def DFS(x):
    global cnt
    visit[x] = 1
    cnt += 1

    for w in G[x]:
        if w and not visit[w]:
            DFS(w)

computer = int(input())
pair = int(input())
G = [[] for _ in range(computer + 1)]
node = []
visit = [0] * (computer + 1)
cnt = 0

for i in range(pair):
    first, second = map(int, input().split())
    node.extend([first, second])

for i in range(pair):
    first, second = node[2 * i], node[2 * i + 1]
    G[first].append(second)
    G[second].append(first)

DFS(1)
print(cnt - 1) if cnt > 1 else print(cnt)