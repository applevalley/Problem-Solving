'''
5 x 5 공간의 2차원 배열에 인접한 모든 방향으로 순회하며 7개의 요소를 순회했을 때, S(다솜파)가 4개 이상 포함된 그룹의 수를 구하면?

0 ~ 24에서 7가지 요소를 가지는 모든 조합을 만들자.
각 조합에 대해 7개의 요소들이 서로 연결되어있는지, 그 중 S(다솜파)가 넷 이상인지를 검사한다.
'''

from itertools import combinations
from collections import deque
from copy import deepcopy

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def check(x, y):
    global dasom, cnt

    copied_visit = deepcopy(visited)
    copied_visit[x][y] = 1
    connected = 1

    Q = deque()
    Q.append([x, y])
    while Q:
        x, y = Q.popleft()
        if arr[x][y] == 'S':
            dasom += 1

        for i in range(4):
            tx, ty = x + dx[i], y + dy[i]
            if 0 <= tx < 5 and 0 <= ty < 5 and copied_visit[tx][ty] == 0 and [tx, ty] in for_point:
                Q.append([tx, ty])
                copied_visit[tx][ty] = 1
                connected += 1

    if connected == 7 and dasom >= 4:
        cnt += 1


arr = [list(input()) for _ in range(5)]
visited = [[0] * 5 for _ in range(5)]
possible_comb = list(combinations(list(i for i in range(25)), 7))
cnt = 0

for i in possible_comb:
    for_point = [[item // 5, item % 5] for item in i]
    dasom = 0
    check(for_point[0][0], for_point[0][1])

print(cnt)