import sys
sys.stdin = open('1486.txt')

# 부분집합과 연관이 있다
# 점원의 수는 크게 중요하지 않다

def powerset(n, k):
    if n == k:
        cnt = 0
        for i in range(n):
            if A[i] == 1:
                cnt += height[i]
        if cnt >= B:
            sum_list.append(cnt)

    else:
        A[k] = 1
        powerset(n, k + 1)
        A[k] = 0
        powerset(n, k + 1)

for test_case in range(1, int(input())+1):
    N, B = map(int, input().split())  # 점원의 수, 선반의 높이
    A = [0] * N
    height = list(map(int, input().split()))  # 점원들의 키
    sum_list = []

    powerset(N, 0)

    min = sum_list[0] - B
    for i in range(1,len(sum_list)):
        if min > sum_list[i] - B:
            min = sum_list[i] - B

    print("#{} {}".format(test_case, min))