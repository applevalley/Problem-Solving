import sys
sys.stdin = open('1012.txt')
sys.setrecursionlimit(50000)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def find(x,y):
    global cnt
    if visit[x][y] == 1: return
    if cnt == 0:
        cnt += 1
    visit[x][y] = 1
    for i in range(4):
        tx, ty = x + dx[i], y + dy[i]
        if 0 <= tx < N and 0 <= ty < M:
            if arr[tx][ty] == 1 and not visit[tx][ty]:
                cnt += 1
                find(tx, ty)

T = int(input())

for test_case in range(1, T+1):
    temp = []
    res = 0
    N,M,K = map(int, input().split())
    for i in range(K):
        x, y = map(int, input().split())
        temp.extend([x,y])
    arr = [[0] * (M) for _ in range(N)]
    visit = [[0] * M for _ in range(N)]
    # print(temp)

    for i in range(K):
        s, e = temp[2*i], temp[2*i+1]
        arr[s][e] = 1

    # for i in arr:
    #     print(*i)

    for i in range(N):
        for j in range(M):
            cnt = 0
            if arr[i][j] == 1:
                find(i,j)
                if cnt != 0:
                    res += 1
    print(res)