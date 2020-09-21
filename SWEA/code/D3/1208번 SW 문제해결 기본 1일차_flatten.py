import sys
sys.stdin = open('1208.txt')
for test_case in range(1, 11):
    number = int(input())
    arr = list(map(int, input().split()))

    for i in range(number):
        down, up = 0, 100
        for j in range(len(arr)):
            if arr[j] > down:
                down = arr[j]
                down_idx = j

            if arr[j] < up:
                up = arr[j]
                up_idx = j
        arr[down_idx] -= 1
        arr[up_idx] += 1

    print("#{} {}".format(test_case, max(arr) - min(arr)))

'''
#1 13
#2 32
#3 54
#4 25
#5 87
#6 14
#7 39
#8 26
#9 13
#10 29'''