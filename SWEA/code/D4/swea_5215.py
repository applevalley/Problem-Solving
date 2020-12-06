import sys; sys.stdin = open('5215.txt')


# for문

# for test_case in range(1, int(input()) + 1):
#     N, L = map(int, input().split())
#
#     score, calorie = [], []
#
#     for _ in range(N):
#         s, c = map(int, input().split())
#         score.append(s)
#         calorie.append(c)
#
#     ans = 0
#     for i in range(1 << N):
#         sum_score = sum_calorie = 0
#         for j in range(N):
#             if i & (1 << j):
#                 sum_calorie += calorie[j]
#                 sum_score += score[j]
#         if sum_calorie <= L:
#             ans = max(ans, sum_score)
#
#     print("#{} {}".format(test_case, ans))

# 재귀

# def cook(idx):
#     global ans
#     if idx >= N:
#         sum_score = 0
#         sum_calorie = 0
#
#         for i in range(N):
#             if bits[i]:
#                 sum_score += score[i]
#                 sum_calorie += calorie[i]
#         if sum_calorie <= L:
#             ans = max(ans, sum_score)
#
#         return
#
#     bits[idx] = 1
#     cook(idx + 1)
#     bits[idx] = 0
#     cook(idx + 1)
#
#
# for test_case in range(1, int(input()) + 1):
#     N, L = map(int, input().split())
#
#     score, calorie = [], []
#
#     for _ in range(N):
#         s, c = map(int, input().split())
#         score.append(s)
#         calorie.append(c)
#
#     ans = 0
#     bits = [0] * N
#     cook(0)
#
#     print(test_case, ans)


# 백트래킹

def cook(idx, sum_score, sum_calorie):
    global ans
    if sum_calorie > L:
        return

    if idx == N:
        if sum_score > ans:
            ans = sum_score
        return

    # 재료 선택-비선택
    cook(idx + 1, sum_score + score[idx], sum_calorie + calorie[idx])
    cook(idx + 1, sum_score, sum_calorie)

for test_case in range(1, int(input()) + 1):
    N, L = map(int, input().split())

    score, calorie = [], []

    for _ in range(N):
        s, c = map(int, input().split())
        score.append(s)
        calorie.append(c)

    ans = 0
    cook(0, 0, 0)

    print("#{} {}".format(test_case, ans))
