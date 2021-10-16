def move(k):
    global N, M, arr
    if k == 1:
        arr = arr[::-1]

    elif k == 2:
        for i in range(N):
            arr[i] = arr[i][::-1]

    elif k == 3:
        N, M = M, N

        new_arr = [list(i)[::-1] for i in zip(*arr)]
        arr = new_arr

    elif k == 4:
        N, M = M, N

        new_arr = [list(i) for i in list(zip(*arr))[::-1]]
        arr = new_arr

    elif k == 5:
        new_arr = [[0] * M for _ in range(N)]

        for i in range(N // 2):  # 1 -> 2
            for j in range(M // 2):
                new_arr[i][j + (M // 2)] = arr[i][j]
        for i in range(N // 2):  # 2 -> 3
            for j in range(M // 2, M):
                new_arr[i + (N // 2)][j] = arr[i][j]
        for i in range(N // 2, N):  # 3 -> 4
            for j in range(M // 2):
                new_arr[i - (N // 2)][j] = arr[i][j]
        for i in range(N // 2, N):  # 4 -> 1
            for j in range(M // 2, M):
                new_arr[i][j - (M // 2)] = arr[i][j]

        arr = new_arr[:]

    elif k == 6:
        new_arr = [[0] * M for _ in range(N)]

        for i in range(N // 2):  # 1 -> 4
            for j in range(M // 2):
                new_arr[i + (N // 2)][j] = arr[i][j]
        for i in range(N // 2, N):  # 4 -> 3
            for j in range(M // 2):
                new_arr[i][j + (M // 2)] = arr[i][j]
        for i in range(N // 2, N):  # 3 -> 2
            for j in range(M // 2, M):
                new_arr[i - (N // 2)][j] = arr[i][j]
        for i in range(N // 2):  # 2 -> 1
            for j in range(M // 2, M):
                new_arr[i][j - (M // 2)] = arr[i][j]

        arr = new_arr[:]


N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
order = list(map(int, input().split()))

for i in order:
    move(i)

for _ in arr:
    print(*_)