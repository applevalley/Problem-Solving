# 최대 층 수는 F층이고, 현재 S층에서 G층으로 가야 한다.
# 올라갈 때는 U층씩, 내려갈 때는 D층씩 내려간다.
# 버튼을 몇 번을 눌러야 G층에 도달할까?

# 우선 무조건 계단을 타야 하는 상황은 아래와 같다.
# 1. 목표 층보다 현재 층이 더 높은데 내려가는 버튼이 없을 때
# 2. 목표 층보다 현재 층이 더 낮은데 올라가는 버튼이 없을 때

# 현재 층이 목표 층보다 높다면(낮다면), 내려가는(올라가는)버튼을 누르기 시작한다.
# 만약 목표 층을 지나가버린다면, 되돌아간 뒤 반대 방향의 버튼을 누른다.
# 재귀로 가능할까?

# 최대 높이는 100만층이고, 시간 제한은 1초이다.
# 재귀로 하려면 탈출 조건을 자세히 줘야 할 것으로 보인다...

# 재귀로 하면 시간 복잡도가 지수 수준으로 올라갈 수 있다고 하여 BFS로 다시 풀어보기로 하였다.
import sys
sys.setrecursionlimit(10 ** 6)


def up(start, goal):
    global cnt, check_stair, finish
    if check_stair:
        cnt = 'use the stairs'
        return
    if finish: return

    if start == goal:
        finish = True
        return

    if start > goal:
        if not finish:
            cnt += 1
            up((start - D), goal)
        else:
            return

    if not finish:
        cnt += 1
        up((start + U), goal)

    return


def down(start, goal):
    global cnt, check_stair, finish
    if check_stair:
        cnt = 'use the stairs'
        return
    if finish: return

    if start == goal:
        finish = True
        return

    if start > goal or start > F:
        if not finish:
            cnt += 1
            down((start + U), goal)
        else:
            return

    if not finish:
        cnt += 1
        down((start - D), goal)


F, S, G, U, D = map(int, input().split())
cnt = 0
check_stair = False
finish = False

if S > G and not D or S < G and not U:
    check_stair = True

if S < G:
    up(S, G)
else:
    down(S, G)

print(cnt)
