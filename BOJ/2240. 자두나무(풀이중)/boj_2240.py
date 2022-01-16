'''
T초동안 떨어지는 자두를 W번만 움직여 받아내자!
자두의 위치 초기값은 1
W은 1부터 30까지 -> 최소 한 번은 움직일 수 있다.
하지만 꼭 움직여야만 한다는 조건은 없다
4 1
1
2
1
1
이런 경우 움직이면 손해다.

큐를 만들고, 현재 몇 초인지, 나무의 위치, 얻은 자두의 수, 잔여 이동 횟수를 하나의 리스트로 묶어 큐에 저장한다!
그 뒤 잔여 이동 횟수에 따라 위치를 바꾸는 경우 / 바꾸지 않고 그대로 가는 경우를 전부 추가해 비교한다.
자두의 위치를 담은 정보 리스트 plums의 끝까지 전부 순회한 경우, 얻은 자두의 수를 비교해 최댓값으로 카운터를 갱신해나간다!

DFS식으로 하면 W의 횟수에 큰 영향을 받을 수도 있을 것 같다.
이동하거나, 이동하지 않거나로 경우의 수가 2 ** w만큼 나뉘게 되는데, 최악의 경우 2 ** 30가지의 경우의 수가 있고, 이건 1억이 훌쩍 넘어간다.
'''

# 1 BFS식으로 진행한 풀이 -> 메모리 초과..>!
# 이동한 경우, 아닌 경우로 나눠서 매 횟수마다 2개의 경우의 수가 큐에 초과되다 보니 메모리가 초과된 모양이다..


# from collections import deque
#
# def plum_hunt(remain_move_count):
#     Q = deque()
#     answer = 0                                                # 최종적으로 얻은 자두의 수를 나타낼 변수
#
#     # 초기에 큐에 들어갈 상황은 다음과 같다. 초기 위치값인 1번 나무 아래 서서 시작하거나, 또는 이동 횟수를 1 차감하고 2번 나무 아래에서 시작하거나
#     Q.append([0, 1, 0, remain_move_count])
#     Q.append([0, 2, 0, remain_move_count - 1])
#
#     while Q:
#         time, location, plum_count, remain_move_count = Q.popleft()        # 진행 시간, 나무 위치, 얻은 자두의 수, 잔여 이동 횟수
#
#         # 마지막 자두가 떨어지는 순간
#         if time == T - 1:
#             if plums[time] == location:                # 획득할 수 있다면(같은 위치라면) 자두 획득 횟수에 1을 더한 값을 가지고 최댓값을 비교 후 갱신
#                 answer = max(answer, plum_count + 1)
#             else:
#                 answer = max(answer, plum_count)
#             continue
#
#         # 자두를 얻을 수 있는 경우
#         if plums[time] == location:
#             if remain_move_count > 0:      # 잔여 횟수가 아직 남은 경우
#                 if location == 1:
#                     Q.append([time + 1, 2, plum_count + 1, remain_move_count - 1])
#                 else:
#                     Q.append([time + 1, 1, plum_count + 1, remain_move_count - 1])
#             # 잔여 횟수가 남아있더라도, 이번 시점에 이동하지 않은 경우도 고려해야 한다.
#             Q.append([time + 1, location, plum_count + 1, remain_move_count])
#         # 자두를 얻을 수 없는 경우
#         else:
#             if remain_move_count > 0:
#                 if location == 1:
#                     Q.append([time + 1, 2, plum_count, remain_move_count - 1])
#                 else:
#                     Q.append([time + 1, 1, plum_count, remain_move_count - 1])
#
#             Q.append([time + 1, location, plum_count, remain_move_count])
#
#     # 큐가 비게 될 때까지 전부 순회하면서 갱신된 최종 answer의 값이 가장 자두를 많이 획득할 수 있는 경우이다.
#     return answer
#
# T, W = map(int, input().split())
# plums = [int(input()) for _ in range(T)]
#
# print(plum_hunt(W))



# def plum_hunt():
#     if

T, W = map(int, input().split())
plums = [0] + [int(input()) for _ in range(T)]
print(plums)
dp = [[0]*(W+1) for _ in range(T+1)]

for i in range(1, T + 1):
    if plums[i] == 1:
        dp[i][0] = dp[i - 1][0] + 1
    else:
        dp[i][0] = dp[i - 1][0]

    for j in range(1, W + 1):
        if j > 1:
            break

        if plums[i] == 1 and j % 2 == 0:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + 1
        elif plums[i] == 2 and j % 2 == 1:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1])

print(dp)
print(max(dp[-1]))