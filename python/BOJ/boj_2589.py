from collections import deque

import sys
sys.stdin = open('2589.txt')

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def go(x,y):
    global cnt
    visit = [[0] * M for _ in range(N)]    # visit를 함수 호출마다 새로 만든다.
    visit[x][y] = 1
    Q = deque()
    Q.append((x,y))
    while Q:
        x1, y1 = Q.popleft()
        for i in range(4):
            tx, ty = x1 + dx[i], y1 + dy[i]
            if 0 <= tx < N and 0 <= ty < M and not visit[tx][ty]:
                if G[tx][ty] == 0:
                    visit[tx][ty] = visit[x1][y1] + 1    # 거리 계산
                    Q.append((tx,ty))
                    if cnt < visit[tx][ty]:   # 기준값과 비교
                        cnt = visit[tx][ty]   # 새로운 기준값
    res.append(cnt)        # 이렇게 하면 각 좌표에서의 거리가 res에 담기게 된다.

N, M = map(int, input().split())
arr = [input() for _ in range(N)]   # 입력받을 배열
G = [[0] * M for _ in range(N)]
cnt = 0
res = []

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'W':      # 바다이면 해당 좌표에 숫자를 저장한다.
            G[i][j] = 2


for i in range(N):
    for j in range(M):
        cnt = 0
        if G[i][j] == 0:       # G의 좌표값이 비어있을 때(=육지일 때)
            go(i,j)

print(max(res) - 1)  # 위에서 시작 지점의 visit 좌표도 1을 추가하기 때문에 1을 빼준다.