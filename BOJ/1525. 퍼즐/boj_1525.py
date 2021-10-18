'''
0이면 빈 칸이고 인접한 칸 중에 0이 있으면 그 수를 옮길 수 있다.
3번 이내의 이동으로
1 2 3
4 5 6
7 8 0
이렇게 만들 수 있어야 한다. 이게 가능할까? 가능하다면 이동에 걸린 최소 횟수를, 3번으로 안 된다면 -1을 출력하자.

모든 좌표에 대해 델타를 통한 DFS를 한다면 시간 초과가 날 것이다.
한 번의 이동에서 0을 제외한 8번의 숫자가 움직일 수 있다. 그러면 그 때마다 배열을 새로 복사하나? 문제의 메모리 제한은 32mb로 매우 작다.
배열을 새로 만드는게 아닌 기존 배열 상에서, 혹은 복사된 배열상에서만 돌아가게끔 해야 한다는거다.
'''

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS():
    Q = deque()
    Q.append(number)
    move[number] = 0

    while Q:
        puzzle = Q.popleft()
        if puzzle == 123456789:
            return move[puzzle]

        s = str(puzzle)
        target = s.find('9')
        x, y = target // 3, target % 3

        for i in range(4):
            tx, ty = x + dx[i], y + dy[i]
            if 0 <= tx < 3 and 0 <= ty < 3:
                idx = (tx * 3) + ty
                moved = list(s)
                moved[target], moved[idx] = moved[idx], moved[target]
                changed = int(''.join(moved))

                if not move.get(changed):
                    move[changed] = move[puzzle] + 1
                    Q.append(changed)
    return -1

number = ''
move = dict()

for i in range(3):
    number += input().replace(' ', '')

number = int(number.replace('0', '9'))

print(BFS())

















# arr = [list(map(int, input().split())) for _ in range(3)]
# correct = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
# Q = deque()
# temp = 0
#
# while temp < 3:
#     Q = deque()
#     for i in range(3):
#         for j in range(3):
#             if arr[i][j]:
#                 Q.append(i, j, deepcopy(arr))
#
#     while Q:
#         x, y, arr = Q.popleft()
#         if arr == correct: break
#
#         for i in range(4):
#             tx, ty = x + dx[i], y + dy[i]
#             if 0 <= tx < 3 and 0 <= ty < 3 and arr[tx][ty] == 0:
#                 arr[x][y], arr[tx][ty] = arr[tx][ty], arr[x][y]
#                 Q.append(tx, ty, arr)
#
#
#     temp += 1