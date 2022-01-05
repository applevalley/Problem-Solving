def go():
    Q = []
    for i in range(1, N + 1):
        if visit[i] == 0:
            Q.append(i)
    while Q:
        v = Q.pop(0)
        res.append(v)
        for w in range(1, N + 1):
            if G[v][w]:
                visit[w] -= 1
                if visit[w] == 0:
                    Q.append(w)


for test_case in range(1, 11):
    N, M = map(int, input().split())
    temp = list(map(int, input().split()))

    G = [[0] * (N + 1) for _ in range(N + 1)]
    visit = [0] * (N + 1)
    res = []

    for i in range(M):
        s, e = temp[2 * i], temp[2 * i + 1]
        G[s][e] = 1
        visit[e] += 1

    go()

    print("#{}".format(test_case), end=" ")
    for i in res:
        print(i, end=" ")
    print()