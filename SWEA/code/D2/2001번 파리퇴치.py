import sys
sys.stdin = open('fly_input.txt','r')

T = int(input())

for test_case in range(1,T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    sum_list = []

    def pari(a,b):
        cnt = 0
        for i in range(a, a+M):
            for j in range(b, b+M):
                cnt += arr[i][j]
        return cnt

    for i in range(N-M+1):
        for j in range(N-M+1):
            sum_list.append(pari(i,j))

    for i in range(len(sum_list)):
        for j in range(len(sum_list)-1):
            if sum_list[j] < sum_list[j+1]:
                sum_list[j], sum_list[j+1] = sum_list[j+1], sum_list[j]

    print("#{} {}".format(test_case, sum_list[0]))


# def fly(a,b):
#     count = 0
#     for i in range(a,a+M):
#         for j in range(b,b+M):
#             count += arr[i][j]
#     return count
#
# T = int(input())
#
#
# for test_case in range(1,T+1):
#     N,M = map(int, input().split())
#     arr = []
#     for k in range(N):
#         numbers = list(map(int, input().split()))
#         arr.append((numbers))
#
#     ans = 0
#     for i in range(N-M+1):
#         for j in range(N-M+1):
#             count1 = fly(i,j)
#             if ans < count1:
#                 ans = count1
#     print('#{} {}'.format(test_case, ans))

# 여기서부터 라이브 강의 복습

# MxM 범위의 합이 최대가 되는 경우를 구하자
# 최적화 문제
# 해답이 될 수 있는 모든 경우  -> 최적의 해를 찾아야 한다 -> 완전 검색
# 행, 열 -> 0 ~ N-M

# T = int(input())
#
# for test_case in range(1,T+1):
# # N, M
#     N,M = map(int, input().split())
# # N x N 입력 자료
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
# # 모든 사각영역의 좌상단 좌표
#
#     for x in range(0,N-M+1):
#         for y in range(0,N-M+1):
#             # (x,y)이고, 크기가 M인 사각영역을 처리.
#             s = 0
#             for i in range(x,x+M):
#                 for j in range(y,y+M):
#                     s += arr[i][j]
#     print(s)
