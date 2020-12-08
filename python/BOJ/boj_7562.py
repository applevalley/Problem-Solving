from collections import deque

dx = [-1, -2, -2, -1, 1, 2, 2, 1]   # 나이트가 움직일 수 있는 8방향
dy = [-2, -1, 1, 2, -2, -1, 1, 2]

def go(a,b):
    visit[a][b] = 1
    Q = deque()
    Q.append((a,b))
    while Q:
        x1,y1 = Q.popleft()
        if x1 == x and y1 == y:
            print(visit[x][y] - 1)    # 위에서 visit[a][b] = 1을 줘서 하나를 빼자
        for i in range(8):
            tx, ty = x1 + dx[i], y1 + dy[i]
            if 0 <= tx < N and 0 <= ty < N and not visit[tx][ty]:
                visit[tx][ty] = visit[x1][y1] + 1  # 1씩 늘려가면서 해를 찾는다
                Q.append((tx,ty))


for test_case in range(int(input())):
    N = int(input())
    i,j = map(int, input().split())  # 현재 위치
    x,y = map(int, input().split())  # 타겟
    arr = [[0] * N for _ in range(N)]
    visit = [[0] * N for _ in range(N)]
    arr[i][j] = 1

    if i == x and j == y:   # 위치가 같다면 0
        print(0)
    else:
        go(i,j)