'''
미세먼지의 확산이 먼저
인접 4방향으로 퍼지고, 인접 방향이 공기청정기거나 배열을 벗어나면 안 퍼짐
확산되는 양은 int(기준 좌표값 / 5)
4방향으로 돌고 난 뒤 기준 좌표의 값을 기존 값 - ((기존 값 / 5) * 확산된 횟수)로 수정

그 뒤 공기청정기가 돈다
위 청정기는 반시계방향 (우 -> 상 -> 좌 -> 하)
아래 청정기는 시계방향 (우 -> 하 -> 좌 -> 상)
바람이 흘러간 칸은 미세먼지가 지워진다.
방향 전환은 어떻게 하나?
처음 우측으로 갈 때, r x c 사이즈에서 c - 1까지 가면 위 아래에 따라 옮겨간다.
반시계라면 0, c - 1, 시계라면 r - 1, c - 1까지 가면 방향을 전환한다.
반시계라면 0, 0, 시계라면 r - 1, 0까지 가면 방향을 전환한다.
그 뒤로는 각자의 청정기 위치 (좌표 값이 -1)까지 간다. -1에 도착하면 다음 이동은 위의 것을 반복한다.

이걸 반복하는게 1초다.
공기청정기는 이동하지 않을 것이다! 바람만 돈다.
우선 둘 다 arr은 공유해야 할 것이다.
while 루프를 줘서 주어진 시간만큼 먼지 확산, 공기청정기 작동을 시킨다.
먼지의 확산은 미세먼지가 있는 칸 전체에서 일어나기에, 매 작동마다 이를 확인해야 하는데...
루프마다 O(RC)로 배열을 순회하면 무조건 시간초과가 난다. 배열은 최대 50 x 50까지 가능하고, 시간은 1000까지다.

그래서 어떻게 하나?
우선 본격적으로 루프에 들어가기 전, 배열에 먼지 좌표를 전부 담는다.
그리고 매 초마다 해당 배열을 전부 순회하면서, 새로 먼지가 확산된 좌표를 배열에 추가하고, 그 배열을 return한다!
이러면 먼지 위치 정보들은 그대로 있을 것이고, 새로 전체 r x c 사이즈 탐색을 할 필요가 없어진다.

청정기는 2개가 있고, 윗 청정기와 아랫 청정기를 별도의 함수로 돌린다.
방향 회전을 하는 기준이 필요하기에, 청정기 위치의 좌표를 별도로 보관해둔다.
청정기 바람이 한 칸씩 이동할 것이고, 만약 그 좌표값에 먼지가 있다면 그 값을 0으로 비워야 한다.
다만 이걸 배열 안에서 remove를 하면 시간 복잡도가 증가해버릴 것이다.

아예 먼지 위치를 리스트가 아닌 집합으로 담으면 어떨까? 어차피 먼지 위치들에 있어 순서는 딱히 상관이 없다. 어차피 다 돌 것이기 때문이다.
그러면 비워진 칸이 있으면, 차집합 연산으로 복잡도를 줄일 수 있지 않을까?
'''


import sys
from copy import deepcopy
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def spread(dirt, copied_arr):
    global arr

    while dirt:
        x, y = dirt.popleft()
        copied_arr[x][y] = arr[x][y]

        for i in range(4):
            tx, ty = x + dx[i], y + dy[i]
            if tx < 0 or ty < 0 or tx >= R or ty >= C: continue
            if arr[tx][ty] == -1 or [tx, ty] in dirt: continue
            



R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) * C for _ in range(R)]
dirt = deque([[i, j] for i in range(R) for j in range(C) if arr[i][j] > 0])
cleaner = deque([[i, j] for i in range(R) for j in range(C) if arr[i][j] == -1])

while T > 0:
    copied_arr = deepcopy(arr)
    spread(dirt, copied_arr)