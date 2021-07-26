# 동시에 움직이는 N대의 크레인 각각은 1분에 박스를 하나씩 배에 실을 수 있다.
# 각 크레인에는 무게 제한이 있어 그보다 더 무거운 박스는 움직일 수 없다. 모든 박스를 배로 옮기는데 걸리는 시간의 최솟값은?

# 크레인과 박스 숫자에 대한 제한을 별도로 언급하고 있지 않다. 따라서 나올 수 있는 모든 경우는 다음과 같다.
# 박스와 크레인이 전부 존재한다.
# 박스만 없다.
# 크레인만 없다.
# 여기서 박스 또는 크레인이 아예 없거나, 크레인의 최대 무게를 초과하는 박스 x가 있는 경우는 배에 모든 박스를 실을 수 없다.

# 제일 무거운 박스를 무게 제한이 가장 여유로운 크레인이 들 수 있게 해야 한다.
# 크레인과 박스들을 내림차순으로 정렬한 뒤, 크레인의 수만큼 박스들을 순회한다.

# 9 8 5
# 8 7 6 3

# 위와 같은 경우 한 박스에 한 크레인으로 대칭시켜나가다 보면 크레인 5 - 박스 6을 만난다. 다만 박스의 무게가 더 크기에 크레인 5로는 옮길 수 없다.
# 이런 경우 다음 박스인 3과 크레인 5를 매칭시켜야 하고, 만약 박스가 8 7 6으로 끝이라면 다음 1초에서야 작업을 마무리할 수 있다.

# 시간 제한이 2초여서 시간 초과가 나더라도 퍼센티지는 어느 정도 올라갈 거라고 생각했는데 1%에서 이미 시간초과가 났다.
# 생각보다 데이터가 많은 모양이다. 여기서 더 줄이려면 어떻게 해야하지..

# import sys
# from collections import deque
#
# N = int(sys.stdin.readline().rstrip())
# cranes = list(map(int, sys.stdin.readline().split()))
# M = int(sys.stdin.readline().rstrip())
# boxes = list(map(int, sys.stdin.readline().split()))
# boxes_Q = deque()                        # 박스를 하나씩 꺼내야 하기에 연산을 줄이기 위해 리스트 대신 deque를 활용하기로 함
# timer = 0
#
# cranes.sort(reverse=True)
# boxes.sort(reverse=True)
# boxes_Q.extend(boxes)
#
# while True:
#
#     if not cranes or not boxes_Q:          # 처음부터 크레인이나 박스 자체가 없는 경우
#         if not timer:                      # -1
#             timer = -1
#         break                              # 안에 조건문을 따로 둔 것은 박스 deque에서 모든 요소가 pop된 경우를 고려한 것
#
#     if cranes[0] < boxes_Q[0]:             # 박스 무게가 크레인보다 큰 경우
#         timer = -1                       # -1
#         break
#
#     for i in range(N):
#         if not boxes_Q:                  # 모든 박스가 다 옮겨진 경우 빠져나올 것
#             timer += 1
#             break
#
#         if cranes[i] >= boxes_Q[0]:      # 박스를 크레인과 비교해가면서 하나씩 차감
#             boxes_Q.popleft()
#             continue
#         else:                            # i번째 박스가 i번째 크레인보다 큰 경우
#             for j in range(len(boxes_Q)):      # 시간을 절약하기 위해 다른 박스를 찾아주자
#                 if cranes[i] >= boxes_Q[j]:    # 대신 옮겨줄 박스를 찾았다면
#                     boxes_Q.pop(j)             # 해당 박스를 배에 옮겨준 뒤
#                     break                      # 빠져나올 것
#
#     else:                                # 모든 크레인을 순회하고 난 경우 카운터를 초기화하고, 1초를 추가한다
#         timer += 1
#
#         if not boxes_Q: break
#
# print(timer)





# 2차 시도
# 입력을 받아서 역순으로 정렬하는 것까지는 동일하다.
# 시도중...

import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
cranes = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().rstrip())
boxes = list(map(int, sys.stdin.readline().split()))
boxes_Q = deque()                        # 박스를 하나씩 꺼내야 하기에 연산을 줄이기 위해 리스트 대신 deque를 활용하기로 함
timer = 0

cranes.sort(reverse=True)
boxes.sort(reverse=True)
boxes_Q.extend(boxes)

if not cranes or not boxes_Q:  # 처음부터 크레인이나 박스 자체가 없는 경우
    timer = -1

if cranes[0] < boxes_Q[0]:  # 박스 무게가 크레인보다 큰 경우
    timer = -1  # -1

for i in range((max(N, M) // min(N, M)) + 1):
    if timer == -1: break

    for j in range(N):
        if cranes[j] >= boxes_Q[0]:
            boxes_Q.popleft()

    timer += 1

if boxes_Q:
    timer = -1

print(timer)