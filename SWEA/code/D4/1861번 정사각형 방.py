import sys
sys.stdin = open('1861.txt')


dx = [1, -1, 0, 0]  # 상하좌우
dy = [0, 0, -1, 1]


def move(x, y):           # arr[x][y]에서 1 늘어난 숫자를 찾아 total_visit[tx][ty]에 입력
    for i in range(4):
        tx, ty = x + dx[i], y + dy[i]
        if 0 <= tx < N and 0 <= ty < N:
            if arr[tx][ty] == arr[x][y] + 1:
                total_visit[tx][ty] = total_visit[x][y] + 1
                move(tx, ty)


def back(x, y):          # 찾아낸 최댓값에서 1 줄어든 숫자를 찾아 최초의 숫자의 좌표를 찾아내는 함수
    global cnt
    if cnt == 0:
        start_list.extend([x, y])
    for i in range(4):
        tx, ty = x + dx[i], y + dy[i]
        if 0 <= tx < N and 0 <= ty < N:
            if arr[tx][ty] == arr[x][y] - 1:
                cnt -= 1
                back(tx, ty)
    else:
        return


for test_case in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    total_visit = [[0] * N for _ in range(N)]
    start_list = []
    max_list = []
    final_list = []
    for i in range(N):
        for j in range(N):
            move(i, j)

    top = total_visit[0][0]
    for i in range(N):
        for j in range(N):
            if top < total_visit[i][j]:
                top = total_visit[i][j]

    for i in range(N):
        for j in range(N):
            if total_visit[i][j] == top:
                max_list.extend([i, j])

    for i in range(len(max_list) // 2):
        cnt = top
        s, e = max_list[2 * i], max_list[2 * i + 1]
        back(s, e)

    for i in range(len(start_list) // 2):           # 찾아낸 시작점에서의 좌표 arr[sx][ex]를 따로 모음
        sx, ex = start_list[2 * i], start_list[2 * i + 1]
        final_list.append(arr[sx][ex])

    print("#{} {} {}".format(test_case, min(final_list), top + 1))