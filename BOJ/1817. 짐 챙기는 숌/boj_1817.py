N, M = map(int, input().split())

if not N:
    print(0)
else:
    books = list(map(int, input().split()))
    cnt = 1
    temp = 0

    for i in books:
        temp += i
        if temp > M:
            temp = i
            cnt += 1

    print(cnt)