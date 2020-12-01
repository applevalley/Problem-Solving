import sys; sys.stdin = open('14500.txt')

block = [
    [[0, 1], [0, 2], [0, 3]],
    [[1, 0], [2, 0], [3, 0]],
    [[1, 0], [1, 1], [1, 2]],
    [[0, 1], [1, 0], [2, 0]],
    [[0, 1], [0, 2], [1, 2]],
    [[1, 0], [2, 0], [2, -1]],
    [[0, 1], [0, 2], [-1, 2]],
    [[1, 0], [2, 0], [2, 1]],
    [[0, 1], [0, 2], [1, 0]],
    [[0, 1], [1, 1], [2, 1]],
    [[0, 1], [1, 0], [1, 1]],
    [[0, 1], [-1, 1], [-1, 2]],
    [[1, 0], [1, 1], [2, 1]],
    [[0, 1], [1, 1], [1, 2]],
    [[1, 0], [1, -1], [2, -1]],
    [[0, 1], [0, 2], [-1, 1]],
    [[0, 1], [0, 2], [1, 1]],
    [[1, 0], [2, 0], [1, 1]],
    [[1, 0], [2, 0], [1, -1]]
]

N, M = map(int, input().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

cnt = 0

for i in range(N):
    for j in range(M):
        for k in range(len(block)):
            temp = 0
            temp += arr[i][j]
            chk = True
            for l in range(3):
                tx = i + block[k][l][0]
                ty = j + block[k][l][1]
                if 0 <= tx < N and 0 <= ty < M:
                    temp += arr[tx][ty]
                else:
                    chk = False
                    break

            if chk == True and cnt < temp:
                cnt = temp

print(cnt)


# cnt = temp = 0
# for i in range(N):
#     for j in range(M):
#         if i + 3 < N:
#             temp += (arr[i][j] + arr[i + 1][j] + arr[i + 2][j] + arr[i + 3][j])
#             cnt = max(cnt, temp)
#
#         if j + 3 < M:
#             temp += (arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i][j + 3])
#             cnt = max(cnt, temp)
#
#         if i + 1 < N and j + 2 < M:
#
