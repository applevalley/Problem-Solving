import sys
sys.stdin = open('1974.txt')

for test_case in range(1, int(input()) + 1):
    # T = int(input())
    arr = [list(map(int, input().split())) for _ in range(9)]
    true_number = [1,2,3,4,5,6,7,8,9]
    for i in range(9):
        row, col = [0] * 9, [0] * 9
        cnt = 0
        for j in range(9):
            if arr[i][j] in true_number:
                row[arr[i][j] - 1] = 1

        for k in range(9):
            if arr[k][i] in true_number:
                col[arr[k][i] - 1] = 1

        if 0 in row:
            print("#{} {}".format(test_case, 0))
            cnt += 1
            break
        if 0 in col:
            print("#{} {}".format(test_case, 0))
            cnt += 1
            break
    if cnt != 0: continue

    for i in range(9):
        diag = []
        width, height = i // 3, i % 3
        for j in range(3*width, 3*width + 3):
            for k in range(3*height, 3*height + 3):
                diag.append(arr[j][k])
        if len(set(diag)) % 9 != 0:
            print("#{} {}".format(test_case, 0))
            cnt += 1
            break
    if cnt != 0: continue
    print("#{} {}".format(test_case, 1))


# 4 5 7 1 6 3 8 2 9
# 6 3 9 8 2 7 5 4 1
# 7 9 3 4 8 5 1 6 2
# 1 8 2 5 4 9 6 3 7
# 8 6 1 7 9 2 3 5 4
# 5 2 4 6 3 1 7 9 8
# 3 7 6 9 1 4 2 8 5
# 2 4 5 3 7 8 9 1 6
# 9 1 8 2 5 6 4 7 3
#1 1
#2 0
#3 1
#4 0
#5 1
#6 1
#7 0
#8 1
#9 1
#10 0