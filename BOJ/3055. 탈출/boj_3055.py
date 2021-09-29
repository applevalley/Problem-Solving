'''
R x C 크기의 배열에 고슴도치 S가 있다.
고슴도치는 .으로 표시된 빈 공간을 통해서만 D에 위치한 비버의 굴로 도망쳐야하는데,
*으로 표시된 물이 인접한 방향으로 퍼져나간다. 물과 고슴도치 전부 X로 표시된 돌은 건너거나 물을 퍼트릴 수 없다.
탈출할 수 있다면 필요한 최소 시간을, 탈출 불가능하다면 kaktus를 출력하자.

고슴도치와 비버는 딱 하나만 오지만, 물은 여러 군데서 퍼질 수 있다.

비버의 집(목표 지점)의 좌표를 저장해놓고, 모든 경우에서 물 - 고슴도치의 순서로 비교한다.
고슴도치의 visit 좌표에 탈출 좌표의 값이 있다면 탈출한거고, 아니라면 익사한 것
'''

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
visited_water = [[0] * C for _ in range(R)]
visited_man = [[0] * C for _ in range(R)]
for_hedgehog, for_water = 0xffffff, 0xffffff
act_list = deque()

for i in range(R):
    for j in range(C):
        if arr[i][j] == 'D':
            target_x, target_y = i, j
        elif arr[i][j] == '*':
            act_list.append([i, j, 0])
        elif arr[i][j] == 'S':
            start_x, start_y = i, j

act_list.append([start_x, start_y, 1])

while act_list:
    x, y, k = act_list.popleft()

    for i in range(4):
        tx, ty = x + dx[i], y + dy[i]
        if 0 <= tx < R and 0 <= ty < C and arr[tx][ty] != 'X' and arr[tx][ty] != 'D' and k == 0 and not visited_water[tx][ty]:
            act_list.append([tx, ty, 0])
            visited_water[tx][ty] = visited_water[x][y] + 1

        if 0 <= tx < R and 0 <= ty < C and arr[tx][ty] != 'X' and arr[tx][ty] != '*' and k == 1 and not visited_man[tx][ty] and not visited_water[tx][ty]:
            act_list.append([tx, ty, 1])
            visited_man[tx][ty] = visited_man[x][y] + 1


if visited_man[target_x][target_y]:
    print(visited_man[target_x][target_y])
else:
    print('KAKTUS')