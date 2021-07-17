# 4개의 톱니바퀴가 순차적으로 돌아간다.
# 시계 또는 반시계 방향으로 톱니바퀴는 매 회전마다 한 칸씩 총 K번 회전한다.
# 회전시킬 톱니바퀴와 회전시킬 방향을 결정하고, 회전할때 서로 맞닿는 극에 따라 연쇄적인 회전이 있을 수 있다.

# 회전시킬 톱니바퀴와 방향을 입력받으면 톱니바퀴를 인자로 하는 함수를 만들어 인접한 톱니바퀴를 조사할 수 있다.
# 회전시킬 톱니바퀴를 기준으로 왼쪽, 오른쪽으로 탐색하며 맞물리는 톱니 (각 톱니바퀴의 [2]와 [6]번 인덱스)를 조사해 서로 값이 다르면
# 해당 톱니바퀴를 회전시켜야 한다. 여기서 기준이 되는 톱니바퀴의 번호 x와 연속적으로 맞물리는 임의의 톱니바퀴 y와의 차를 2로 나눈 나머지를 구했다.
# 나머지가 1이라면 바로 인접해있는 톱니바퀴이기에 기준 톱니바퀴의 회전과 반대 방향이고, 나머지가 0인 경우 기준점으로부터 두 칸의 차이가 있는 것이기에 기준점과 같은 방향이 된다.

# 톱니바퀴가 4개밖에 없고, 회전도 최대 100번이었기에 시간이 많이 걸리지 않았지만 톱니바퀴의 수가 매우 많아지거나, 최대 회전 수가 1만번, 10만번 이상이라면 제한 시간 안에 통과하지 못하겠다는 생각이 들었다.
# 어떻게 하면 조금 더 효율적으로 해결할 수 있을까...?

def turn(x):

    for i in range(x, 4):
        if i == x:
            standard = wheel[i][2]
        else:
            if wheel[i][6] != standard and (i - x) % 2:
                for_reverse.append(i)
                standard = wheel[i][2]
            elif wheel[i][6] != standard and (i - x) % 2 == 0:
                for_straight.append(i)
                standard = wheel[i][2]
            else: break



    for i in range(x, -1, -1):
        if i == x:
            standard = wheel[i][6]
        else:
            if wheel[i][2] != standard and (x - i) % 2:
                for_reverse.append(i)
                standard = wheel[i][6]
            elif wheel[i][2] != standard and (x - i) % 2 == 0:
                for_straight.append(i)
                standard = wheel[i][6]
            else: break


import sys
from collections import deque

wheel = [list(sys.stdin.readline().rstrip()) for _ in range(4)]
K = int(sys.stdin.readline().rstrip())
cnt = 0

for i in range(K):
    for_straight = deque()
    for_reverse = deque()
    target, direction = map(int, sys.stdin.readline().split())
    turn(target - 1)

    if direction == -1:
        for_reverse, for_straight = for_straight, for_reverse
        for_reverse.append(target - 1)
    else:
        for_straight.append(target - 1)

    # print(for_straight)
    # print(for_reverse)
    # print(wheel)
    while for_straight:
        x = for_straight.pop()

        temp = wheel[x].pop(-1)
        wheel[x].insert(0, temp)

    while for_reverse:
        x = for_reverse.pop()

        temp = wheel[x].pop(0)
        wheel[x].append(temp)

    # print(wheel)

for i in range(4):
    if wheel[i][0] == '1':
        cnt += (2 ** i)

print(cnt)