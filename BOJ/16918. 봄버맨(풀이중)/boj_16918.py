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

def bomb():
    global cnt
    Q = deque()

    # 초기값, 또는 1초인 경우
    if cnt <= 1:
        for i in range(R):
            for j in range(C):
                if arr[i][j] == 'O':
                    timer[i][j] += 1
    else:
        for i in range(R):
            for j in range(C):
                if arr[i][j] == 'O' and timer[i][j] == 3:           # 3초가 되어 폭발할 좌표인 경우 모아서 따로 처리해준다.
                    Q.append([i, j])                                # 여기서 바로 처리하면 폭발하지 않는 좌표가 생겨버리기 때문

                elif arr[i][j] == 'O' and timer[i][j] < 3:          # 폭탄이 있는 좌표이면서 3초가 경과하지 않은 경우
                    timer[i][j] += 1

                if cnt % 2 == 0 and arr[i][j] == '.':               # 폭탄 심기
                    arr[i][j] = 'O'
                    timer[i][j] = 1
        while Q:
            x, y = Q.popleft()
            arr[x][y] = '.'
            timer[x][y] = 0

            for k in range(4):
                tx, ty = x + dx[k], y + dy[k]
                if 0 <= tx < R and 0 <= ty < C and arr[tx][ty] == 'O':
                    arr[tx][ty] = '.'
                    timer[tx][ty] = 0




import sys
from collections import deque

R, C, N = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
timer = [[0] * C for _ in range(R)]    # 폭탄 시간 계산을 위한 리스트 / 폭탄이 설치된 후 숫자를 올리기 시작해 3초가 되면 폭발한다
cnt = 0

# 왜 N + 1을 해야 제대로 동작하는지 이해가 되지 않는다. 어딘가 잘못 짠 곳이 있다는건데...
while cnt < N + 1:
    bomb()
    cnt += 1

for x in arr:
    print(*x)