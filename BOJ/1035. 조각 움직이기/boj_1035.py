import sys
from collections import deque
from itertools import permutations, combinations

dx_for_check = [-1, 1, 0, 0]
dy_for_check = [0, 0, -1, 1]


def is_connected(temp_arr):
    q = deque()
    q.append([temp_arr[0][0], temp_arr[0][1]])
    q_map = [[0 for _ in range(5)] for _ in range(5)]
    for x, y in temp_arr:
        q_map[x][y] = 1
    q_visit = [[0 for _ in range(5)] for _ in range(5)]
    q_visit[temp_arr[0][0]][temp_arr[0][1]] = 1
    cnt = 1
    while q:
        x, y = q.popleft()

        for _ in range(4):
            nx, ny = x + dx_for_check[_], y + dy_for_check[_]
            if 0 <= nx < 5 and 0 <= ny < 5 and q_map[nx][ny] and not q_visit[nx][ny]:
                q_visit[nx][ny] = 1
                cnt += 1
                q.append([nx, ny])

    if cnt == piece_count:
        return True
    else:
        return False

input = sys.stdin.readline
arr = [list(input()) for _ in range(5)]
arr_for_perm = [[x, y] for x in range(5) for y in range(5)]
piece_check = [[x, y] for x in range(5) for y in range(5) if arr[x][y] == '*']
piece_count = len(piece_check)
check_list = list(combinations(arr_for_perm, piece_count))
ans = 0xffffff

if piece_count == 1:
    print(0)
else:
    for i in check_list:
        if is_connected(i):
            temp_list = list(permutations(i, piece_count))
            for j in temp_list:
                chk = 0
                for k in range(piece_count):
                    chk += (abs(j[k][0] - piece_check[k][0]) + abs(j[k][1] - piece_check[k][1]))
                ans = min(ans, chk)
    print(ans)