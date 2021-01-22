for test_case in range(1, int(input()) + 1):
    A, B, C = map(int, input().split())
    cnt = 0

    if (C // A) > (C // B):
        cnt += (C // A)
        if C % A >= B:
            cnt += (C // B)
        print('#{} {}'.format(test_case, cnt))
    else:
        cnt += (C // B)
        if C % B >= A:
            cnt += (C // A)
        print('#{} {}'.format(test_case, cnt))