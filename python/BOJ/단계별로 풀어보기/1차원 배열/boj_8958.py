T = int(input())

for test_case in range(1, T+1):
    cnt, res = 0, 0
    arr = list(input())

    for i in range(len(arr)):
        if arr[i] == 'O':
            cnt += 1
            res += cnt
        else:
            cnt = 0
    print(res)