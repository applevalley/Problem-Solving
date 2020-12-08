import sys
sys.stdin = open('bus.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    bus_stop = [0] * 5001    # 전체 배열의 크기
    cnt = ''
    for i in range(N):
        a,b = map(int, input().split())
        for j in range(a, b+1):
            bus_stop[j] += 1          # 카운팅
    P = int(input())
    for i in range(P):
        cnt += str(bus_stop[int(input())]) + " "

    print("#{}".format(test_case), cnt)
