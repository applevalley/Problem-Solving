import sys
sys.stdin = open('2606.txt')

def BFS(v):
    global cnt
    Q = []
    Q.append(v)
    visit[v] = 1
    # print(v, end=" ")

    while Q:
        v = Q.pop(0)
        for i in G[v]:
            if not visit[i]:
                Q.append(i)
                visit[i] = visit[v] + 1
                # print(i, end=" ")
                cnt += 1

temp = []
V = int(input())
E = int(input())
cnt = 0
for i in range(E):
    s, e = map(int, input().split())
    temp.extend([s,e])

# print(temp)

G = [[] for _ in range(V+1)]
visit = [0] * (V+1)
for i in range(E):
    x, y = temp[2*i], temp[2*i+1]
    G[x].append(y)
    G[y].append(x)

BFS(1)

# print(G)
# print(temp)
# print(visit)
print(cnt)
