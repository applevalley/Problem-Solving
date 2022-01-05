for test_case in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    uni, twin = 0, 0
    while N != M:   # 뿔의 수와 동물의 수가 다르다면, 이 안에 뿔 2개짜리가 있다
        N -= 2
        M -= 1
        twin += 1
    uni = M
    print("#{} {} {}".format(test_case, uni, twin))