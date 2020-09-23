dx = [0,1,0,-1]
dy = [1,0,-1,0]

def go(arr):
    x, y = 0, 0
    nx, ny = 0, 0
    dir = 0  # 0 ~ 3  우 / 하 / 좌 / 상
    num = 1  # 1 ~ (N*N)

    for i in range(N*N):
        x, y = nx, ny
        arr[x][y] = num
        nx, ny = x + dx[dir], y + dy[dir]
        if nx < 0 or nx >= N or ny < 0 or ny >= N or arr[nx][ny] != 0:
        # if 0 <= nx < N and 0 <= ny < N:
            dir = (dir + 1) % 4
            nx, ny = x + dx[dir], y + dy[dir]
        num += 1


for test_case in range(1, int(input())+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    visit = [[0] * N for _ in range(N)]

    go(arr)
    print("#{}".format(test_case))
    for i in arr:
        print(*i)