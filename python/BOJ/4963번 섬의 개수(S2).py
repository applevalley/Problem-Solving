import sys;sys.stdin = open('4963.txt')

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def bfs(x, y):
    Q = [[x, y]]
    visited[x][y] = 1
    while Q:
        x, y = Q.pop(0)
        for k in range(8):
            tx, ty = x + dx[k], y + dy[k]
            if 0 <= tx < h and 0 <= ty < w and arr[tx][ty] == 1 and not visited[tx][ty]: # 섬이면서 방문한 적이 없어야 한다.
                visited[tx][ty] = 1
                Q.append([tx, ty])

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0: break # 종료조건 - 마지막으로 0이 2개 입력되는 순간 탈출
    arr = [list(map(int, input().split())) for _ in range(h)] # 그래프
    visited = [[0] * w for _ in range(h)]
    cnt = 0

    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                cnt += 1 # 섬의 개수를 누적

    print(cnt)
