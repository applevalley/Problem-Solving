'''
N x N 크기의 배열 위에 뱀이 돌아다닌다.
(0, 0)에 위치한 뱀은 오른쪽을 향해 쭉 가고, 왼쪽이나 오른쪽으로 이동할 수 있다.
벽에 박거나 본인 몸에 박으면 끝난다. 몇 초만에 끝날까?

우선 방향 잡기가 중요하다. 오른쪽으로 가는 것에서 시작하는데, 여기서 왼쪽이 나오면 오른쪽을 바라보는 기준에서 왼쪽이기 때문에 방향상으로는 위쪽이 된다.
반대로 오른쪽이 나오면 오른쪽에서 오른쪽이기에 아래 방향이 된다. 따라서 벡터를 구성할 때 [상 우 하 좌 ] 처럼 구성해야 하고,
왼쪽이면 -1, 오른쪽이면 +1 한 다음에 그걸 4로 나눈 나머지를 방향 벡터에 넣어줘야 한다.

배열상에서 표시해야 할 정보는 뱀의 몸 길이, 사과이다. 값을 다르게 해서 구분하면 될듯. 사과가 있는 좌표를 만나면, 몸 길이가 늘어난다.
뱀의 길이는 어떻게 표시해야 할까? visit를 만들어 매 회차마다 새로 갱신하면 시간초과가 날 것.
뱀의 길이를 담는 deque를 하나 만들까?
이동할 때 deque에 이동할 좌표를 넣고, 만약 길이가 1이면 0번째 요소를 popleft하면 될 것이다.

'''

import sys
from collections import deque

sys.setrecursionlimit(10000)

dx = [-1, 0, 1, 0] # 상우하좌
dy = [0, 1, 0, -1]

def snake_game(x, y, k):
    global snake_body, cnt, finish
    cnt += 1      # 시간 증가

    if finish: return

    tx, ty = x + dx[k], y + dy[k]      # 뱀의 머리가 이동한 좌표

    if 0 > tx or N <= tx or 0 > ty or N <= ty or arr[tx][ty] == 9:   # 벽을 만났거나, 자기 자신의 몸을 마주친 경우
        finish = True
        return

    if [tx, ty] in apples:    # 사과를 만났다!
        target_apple = apples.index([tx, ty])
        del apples[target_apple]                 # 한 좌표의 사과는 한 번만 먹을 수 있다. 지워주지 않으면 해당 좌표에 올 때마다 계속 먹고, 길이가 계속 늘어날 것이다.
        snake_body.append([tx, ty])   # 뱀의 몸 길이가 1 늘어난다. deque에 tx, ty를 넣어주자.
        arr[tx][ty] = 9               # 뱀이 있다는 표시도 해주자
    else:
        tail_x, tail_y = snake_body.popleft()    # 사과가 없었기에 뱀의 꼬리가 있는 칸을 지워줘야 한다.
        arr[tail_x][tail_y] = 0                  # 꼬리가 있던 칸의 값을 비운다.
        snake_body.append([tx, ty])              # 대신 새롭게 좌표가 하나 들어온다.(뱀 길이는 그대로고, 꼬리 길이를 지웠기에)
        arr[tx][ty] = 9                          # 좌표 표시


    if str(cnt) in second_direction:
        target = second_direction.index(str(cnt))
        if second_direction[target + 1] == 'L':
            snake_game(tx, ty, ((k - 1) % 4))
        elif second_direction[target + 1] == 'D':
            snake_game(tx, ty, ((k + 1) % 4))
    else:
        snake_game(tx, ty, k)


N = int(input())
arr = [[0] * N for _ in range(N)]  # 정사각형 배열
arr[0][0] = 9                      # 배열 내에 뱀이 있는 좌표를 표시
K = int(input())
apples = []  # 사과 좌표를 담을 리스트

for i in range(K):  # 사과 담기
    x, y = map(int, input().split())
    apples.append([x - 1, y - 1])

L = int(input())
second_direction = []
snake_body = deque()               # 뱀의 몸 정보를 담을 deque
snake_body.append([0, 0])
cnt = 0                            # 총 걸린 시간
finish = False

for i in range(L):                 # 길이와 방향 정보를 담는 과정
    second_direction.extend(input().split())

snake_game(0, 0, 1)

print(cnt)