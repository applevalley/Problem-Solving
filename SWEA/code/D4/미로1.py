dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def for_exit(x, y):
    global checked
    visited[x][y] = 1

    if x == exit_point[0][0] and y == exit_point[0][1]:
        checked = True
        return

    for i in range(4):
        tx, ty = x + dx[i], y + dy[i]
        if 0 <= tx < 16 and 0 < ty < 16 and arr[tx][ty] != '1' and not visited[tx][ty]:
            for_exit(tx, ty)
            if checked:
                return 1

    return 0


for test_case in range(1, 11):
    single_case = int(input())
    arr = [list(input()) for _ in range(16)]
    start_point = [[int(x), int(y)] for x in range(16) for y in range(16) if arr[x][y] == '2']
    exit_point = [[int(x), int(y)] for x in range(16) for y in range(16) if arr[x][y] == '3']
    visited = [[0] * 16 for _ in range(16)]
    checked = False

    print(f"#{single_case} {for_exit(start_point[0][0], start_point[0][1])}")