T = int(input())

for test_case in range(1, T+1):
    cnt, res = 0, 0
    arr = list(map(int, input().split()))

    cnt = sum(arr[1:]) / arr[0]

    for i in range(1, len(arr)):
        if arr[i] > cnt:
            res += 1

    print("{:.3f}%".format((res / arr[0]) * 100))