for test_case in range(1, int(input()) + 1):
    N = int(input())
    numbers = list(map(int, input().split()))

    cnt = 0
    for i in numbers:
        if i / N <= sum(numbers) / N:
            cnt += 1

    print('#{} {}'.format(test_case, cnt))