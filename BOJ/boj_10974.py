import sys; sys.stdin = open('10974.txt')


def check_perm(numbers):
    for i in range(1, N):
        if numbers[i - 1] < numbers[i]:
            target_idx = i

    for j in range(N):
        if numbers[j] > numbers[target_idx - 1]:
            idx_for_swap = j

    numbers[target_idx - 1], numbers[idx_for_swap] = numbers[idx_for_swap], numbers[target_idx - 1]

    numbers[target_idx:] = numbers[target_idx:][::-1]

    for k in numbers:
        print(k, end=' ')
    print()


N = int(input())

numbers = [i for i in range(1, N + 1)]

reversed_numbers = numbers[::-1]

for i in numbers:
    print(i, end=' ')
print()

while True:
    if N == 1: break  # N = 1인 경우는 한 가지밖에 없다! 그 뒤 함수에서의 연산이 불가능
    check_perm(numbers)
    if numbers == reversed_numbers:
        break


# 이렇게도 구해지지만 사전순으로 안되는 문제가 생겼다!!

# def perm(n, k):
#     if k == n:
#         for _ in numbers:
#             print(_, end=' ')
#         print()
#     else:
#         for i in range(k, n):
#             numbers[k], numbers[i] = numbers[i], numbers[k]
#             perm(n, k + 1)
#             numbers[k], numbers[i] = numbers[i], numbers[k]
#
# N = int(input())
# numbers = [i for i in range(1, N + 1)]
# bits = [0] * N
# ans = []
#
#
# perm(N, 0)

# 사전순으로 바꾸려는 처절한 몸부림

# import copy
# def perm(n, k):
#     if k == n:
#         print(numbers)
#         new_numbers = copy.deepcopy(numbers)
#         ans.append(new_numbers)
#     else:
#         for i in range(k, n):
#             numbers[k], numbers[i] = numbers[i], numbers[k]
#             perm(n, k + 1)
#             numbers[k], numbers[i] = numbers[i], numbers[k]
#
# N = int(input())
# numbers = [i for i in range(1, N + 1)]
# bits = [0] * N
# ans = []
# temp = 1
#
# for i in range(N - 1, 0, -1):
#     temp *= i
#
# perm(N, 0)
#
# print(ans)
# for i in range(0, temp * N, temp): # 0 2 4
#     for j in range(i + 1, (i + temp)): # 1~2 / 3 ~
#         for k in range(1, N):
#             if ans[i][k] > ans[j][k]:
#                 ans[i], ans[j] = ans[j], ans[i]
#                 break
#             elif ans[i][k] == ans[j][k]:
#                 pass
#             else:
#                 break
#
# print(ans)