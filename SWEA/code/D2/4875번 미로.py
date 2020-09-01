import sys
sys.stdin = open('maze.txt')

def maze(x, y):
    # print(x, y)
    global res
    visited[x][y] = 1       # 좌표 방문체크
    dx = [-1, 1, 0, 0]      # 상하좌우 탐색
    dy = [0, 0, -1, 1]

    for i in range(4):
        tx, ty = x + dx[i], y + dy[i]
        if 0 <= tx < N and 0 <= ty < N:     # 배열을 벗어나지 않게끔 제한을 두었습니다.
            if arr[tx][ty] == '0' and not visited[tx][ty]:   # 전체 배열 arr의 tx,ty값이 0이면서 방문하지 않았을 때
                maze(tx, ty)                                 # 재귀를 수행합니다.
            if arr[tx][ty] == '3':                           # arr의 tx,ty값이 3일 때(미로를 탈출할 수 있을 때)
                res += 1                                     # 탈출을 위한 조건으로 res 변수에 값을 지정했습니다.
                break
        if res == 1:
            break


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]                   # 방문을 확인하기 위한 배열
    res = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':                            # arr의 i,j가 2일 때(미로의 시작 지점일 때)
                maze(i,j)                                   # 함수를 호출합니다.
                if res == 1:                                # 탈출할 수 있다면
                    print("#{} {}".format(test_case, '1'))  # 1입니다.
                else:
                    print("#{} {}".format(test_case, '0'))