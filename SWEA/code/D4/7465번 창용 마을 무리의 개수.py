import sys
sys.stdin = open('7465.txt')

# 그래프 문제!
# 아는 관계를 간선으로 -> 연결된 한 덩어리는 결합 컴포넌트
# 무향 그래프 안에서 몇 개의 결합 컴포넌트가 있는가?

def DFS(v):
    global cnt
    visit[v] = 1
    for w in range(1, N + 1):
        if G[v][w] and not visit[w]:
            DFS(w)
    if [0] * (N + 1) == G[v]:
        cnt += 2
    else:
        cnt += 1


for test_case in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    temp = []
    ans = 1
    cnt = 0

    for i in range(M):
        line = map(int, input().split())
        temp.extend(line)

    # print(temp)
    G = [[0] * (N + 1) for _ in range(N + 1)]
    visit = [0] * (N + 1)
    for i in range(M):
        s, e = temp[2 * i], temp[2 * i + 1]
        G[s][e] = G[e][s] = 1

    for i in range(1, N + 1):
        DFS(i)
        print(cnt)
        if i > 1:
            if cnt != 1:      # cnt가 1이 아닌 -> 간선으로 연결된 정점이 있어 n차례 재귀호출을 한 경우 cnt를 n만큼 올렸고,
                ans += 1      # 1이 아닌 cnt가 있다면 한 무리가 있는 것으로 간주하고 ans를 1 올렸습니다
        cnt = 0

    print("#{} {}".format(test_case, ans))