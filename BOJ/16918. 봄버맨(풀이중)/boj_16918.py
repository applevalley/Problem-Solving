# R x C 크기의 직사각형 배열의 각 칸에는 폭탄이 있거나 없다.
# 폭탄이 있는 칸은 3초 뒤에 폭발하고, 폭발하면 인접한 네 방향의 칸도 같이 폭발한다. 다만 연쇄적인 폭발은 없다.
# 봄버맨은 폭탄을 설치한 뒤 다음 1초간 아무것도 하지 않는다.
# 그 다음 1초에는 폭탄이 설치되지 않은 모든 칸에 폭탄을 설치한다.
# 1초 뒤에는 처음 설치한 폭탄이 모두 폭발한다.
# 그 다음 1초에는 폭탄이 설치되지 않는 모든 칸에 폭탄을 설치한다.
# 이 과정이 반복된다
# N초 뒤의 배열은 어떤 상태일까?

# 주어진 N초가 될 때까지 계속 반복문이 돌아가는 형태가 될 것같다.
# 함수에 전해질 배열의 칸을 [x, y, int] 식으로 해서 반복문마다 3번째 요소인 int를 증가시켜서 3인 경우 폭발하게 하는 것이다.

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bomb(x, y, value):
    global cnt

    if cnt <= 1:
        for i in range(R):
            for j in range(C):
                if arr[i][j] == 'O' and timer[i][j] == 0:
                    timer[i][j] = 1
                elif arr[i][j] == 'O' and timer[i][j]:
                    timer[i][j] += 1
    else:
        for i in range(R):
            for j in range(C):
                if arr[i][j] == 'O' and timer[i][j] == 3:
                    arr[tx][ty] = '.'
                    timer[tx][ty] = 0

                    for k in range(4):
                        tx, ty = i + dx[k], j + dy[k]
                        if 0 <= tx < R and 0 <= ty < C and arr[tx][ty] == 'O':
                            arr[tx][ty] = '.'
                            timer[tx][ty] = 0

                elif arr[i][j] == 'O' and timer[i][j] < 3:
                    timer[i][j] += 1

                if cnt % 2 == 0 and arr[i][j] == '.':
                    arr[i][j] = 'O'
                    timer[i][j] = 1




import sys
from collections import deque

R, C, N = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
timer = [[0] * C for _ in range(R)]
cnt = 0
print(*arr)

while cnt < N:
    for i in range(R):
        for j in range(C):
            bomb(i, j, timer[i][j])

    for xx in arr:
        print(*xx)

    cnt += 1